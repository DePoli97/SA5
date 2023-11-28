from fastapi import FastAPI
import uvicorn
import pyterrier as pt
import pandas as pd

app = FastAPI()

df_all = pd.DataFrame()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/query/")
async def query(query: str = ""):
    global df_all
    return {"message" : query}
    # print(df_all.shape)
    # return {"message" : df_all.shape}



if __name__ == "__main__":
    if not pt.started():
        pt.init()

    df_esa = pd.read_json("./results_esa.json")
    ids = []
    texts = []
    for i in range(len(df_esa)):
        ids.append(f"d{i}")
    for i in range(df_esa.shape[0]):
        tmp = df_esa.iloc[i, :]
        texts.append(df_esa['mission_name'] + " " + df_esa['mission_descrition']  + " " + df_esa['mission_page'])

    # df_s_now = pd.read_json("./results_spaceflight_no3.json")
    # for i in range(len(df_esa),len(df_s_now)+len(df_esa)):
    #     ids.append(f"d{i}")

    # for i in range(df_s_now.shape[0]):
    #     tmp = df_s_now.iloc[i, :]
    #     texts.append((tmp['title'] + " " + tmp['description'] + " " + tmp['body'][:-34] + " " + tmp['date'].strftime("%d-%B-%Y")).lower())
    df_all['docno'] = ids
    df_all['text'] = texts
    print(df_all.shape)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)