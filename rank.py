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
    df_esa.rename(columns={'mission_name' : 'title', 'mission_description' : 'description', 'mission_page' : 'link'},inplace=True)
    for i in range(len(df_esa)):
        ids.append(f"d{i}")
    for i in range(df_esa.shape[0]):
        tmp = df_esa.iloc[i, :]
        texts.append(tmp['title'] + " " + tmp['description']  + " " + tmp['link'])

    df_s_now = pd.read_json("./space/results_spaceflight_no3.json")
    for i in range(len(df_esa),len(df_s_now)+len(df_esa)):
        ids.append(f"d{i}")


    for i in range(df_s_now.shape[0]):
        tmp = df_s_now.iloc[i, :]
        texts.append((tmp['title'] + " " + tmp['description'] + " " + tmp['body'][:-34] + " " + tmp['date'].strftime("%d-%B-%Y")).lower())

    # df_wiki = pd.read_json("./space/result_wiki.json")
    # for i in range(df_s_now.shape[0]):
    #     print(df_s_now.iloc[i, :])
    #     # texts.append((tmp['title'] + " " + tmp['description'] + " " + tmp['body'][:-34] + " " + tmp['date'].strftime("%d-%B-%Y")).lower())


    df_all['docno'] = ids
    df_all['text'] = texts
    
def createIndex():
    global index
    if not pt.started():
        pt.init()
    indexer = pt.DFIndexer("./index_3docs", overwrite=True)
    index_ref = indexer.index(df_all["text"], df_all["docno"])
    index = pt.IndexFactory.of(index_ref)


def query(query :str):
    br = pt.BatchRetrieve(index, wmodel="BM25") #Query with a single word
    queries = pd.DataFrame([["q1", str(query)]], columns=["qid", "query"])
    results = br.transform(queries)
    docs_ids = []
    print(results.shape[0])
    for i in range(results.shape[0]):
        tmp = results.iloc[i, :]
        docs_ids.append(tmp['docid'])
        if i >= 100:
            break
    docs_to_return = []
    for id in docs_ids:
        print("id",id)
        if (id > len(df_esa)):
            doc = df_s_now.iloc[id-len(df_esa)]
        else:
            doc = df_esa.iloc[id]
        docs_to_return.append({'title' : doc['title'], 'description' : doc['description'], 'link' : doc['link'] })
    return docs_to_return

def init():
    prepare_df()
    createIndex()
    print("Index Created")

