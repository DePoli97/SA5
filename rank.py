import pyterrier as pt
import pandas as pd

index = None
df_all = pd.DataFrame()
df_esa = pd.DataFrame()
df_s_now = pd.DataFrame()

def prepare_df():
    global df_all, df_esa, df_s_now
    df_esa = pd.read_json("./space/results_esa.json")
    ids = []
    texts = []
    df_esa.rename(columns={'mission_name': 'title', 'mission_description': 'description', 'mission_page': 'link'},
                  inplace=True)
    for i in range(len(df_esa)):
        ids.append(f"d{i}")
        tmp = df_esa.iloc[i, :]
        texts.append(tmp['title'] + " " + tmp['description'] + " " + tmp['link'])

    df_s_now = pd.read_json("./space/results_spaceflight_no3.json")
    for i in range(len(df_esa), len(df_s_now) + len(df_esa)):
        ids.append(f"d{i}")
        tmp = df_s_now.iloc[i - len(df_esa)]
        texts.append((tmp['title'] + " " + tmp['description'] + " " + tmp['body'][:-34] + " " +
                       tmp['date'].strftime("%d-%B-%Y")).lower())

    df_wiki = pd.read_json("./space/results_wiki.json")
    for i in range(len(df_s_now) + len(df_esa), len(df_s_now) + len(df_esa) + len(df_wiki)):
        ids.append(f"d{i}")
        tmp = df_wiki.iloc[i - (len(df_s_now) + len(df_esa))]
        texts.append(tmp['Date'] + " " + tmp['Event'] + " " + tmp['Country'] + " " + tmp['Mission name'])

    # Verify lengths before creating the DataFrame

    df_all['docno'] = ids
    df_all['text'] = texts
    
def createIndex():
    global index
    if not pt.started():
        pt.init()
    indexer = pt.DFIndexer("./index_3docs", overwrite=True)
    index_ref = indexer.index(df_all["text"], df_all["docno"])
    index = pt.IndexFactory.of(index_ref)


def query(query: str):
    try:
        br = pt.BatchRetrieve(index, wmodel="BM25")
        queries = pd.DataFrame([["q1", str(query).lower()]], columns=["qid", "query"])
        results = br.transform(queries)
        docs_ids = []

        for i in range(results.shape[0]):
            tmp = results.iloc[i, :]
            docs_ids.append(tmp['docid'])

        print(f"docs_ids: {docs_ids}")

        docs_to_return = []
        for doc_id in docs_ids:
            if doc_id >= len(df_esa):
                if doc_id - len(df_esa) >= len(df_s_now):
                    print(f"Warning: Document ID {doc_id} is out-of-bounds for df_s_now.")
                    continue
                doc = df_s_now.iloc[doc_id - len(df_esa)]
            else:
                doc = df_esa.iloc[doc_id]
            docs_to_return.append({'title': doc['title'], 'description': doc['description'], 'link': doc['link']})

        return docs_to_return
    except Exception as e:
        print(f"Error in query processing: {e}")
        raise


def init():
    prepare_df()
    createIndex()
    print("Index Created")

