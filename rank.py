import pyterrier as pt
from typing import List
import pandas as pd

index = None
df_all = pd.DataFrame()
df_esa = pd.DataFrame()
df_s_now = pd.DataFrame()

last_query = ""
last_result = pd.DataFrame()

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


def query(query :str, feedback : List[int]):
    global last_query, last_result
    docs_ids = []
    results = pd.DataFrame()
    if (query != last_query):
        last_query = query
        bm25 = pt.BatchRetrieve(index, num_results = 100, wmodel="BM25")
        queries = pd.DataFrame([["q1", str(query).lower()]], columns=["qid", "query"])
        results = bm25.transform(queries)
        last_result = results
    else:
        for i, row in last_result.iterrows():
            if feedback[i] > 0:
                last_result.at[i, 'score'] = row['score'] * 1.25
            elif feedback[i] < 0:
                last_result.at[i, 'score'] = row['score'] * 0.75
        last_result.sort_values(by='score',inplace=True,ascending=False)
        results = last_result
        
    docs_to_return = []
    for i in range(results.shape[0]):
            tmp = results.iloc[i]
            docs_ids.append(tmp['docid'])
    for id in docs_ids:
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

