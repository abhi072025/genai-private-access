import  os, requests
from  flask  import Flask,  request,  jsonify

SEARCH_ENDPOINT  =  os.getenv("SEARCH_ENDPOINT")
SEARCH_API_KEY =  os.getenv("SEARCH_API_KEY")
OPENAI_ENDPOINT  = os.getenv("OPENAI_ENDPOINT")
OPENAI_API_KEY  =  os.getenv("OPENAI_API_KEY")
INDEX_NAME  =  os.getenv("INDEX_NAME",  "docs")

app  =  Flask(__name__)

def  search_docs(query,  top_k=5):
      url  =  f"{SEARCH_ENDPOINT}/indexes/{INDEX_NAME}/docs/search?api-version=2023-11-01"
       headers =  {"api-key":  SEARCH_API_KEY,  "Content-Type": "application/json"}
       payload  =  {"search": query,  "top":  top_k}
       r =  requests.post(url,  headers=headers,  json=payload)
      r.raise_for_status()
       return  [hit.get("content","")  for hit  in  r.json().get("value",[])]

def  call_openai(prompt):
       url  = f"{OPENAI_ENDPOINT}/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"
       headers  =  {"api-key": OPENAI_API_KEY,  "Content-Type":  "application/json"}
       body =  {"messages":[{"role":"user","content":prompt}],"temperature":0.2}
       r  = requests.post(url,  headers=headers,  json=body)
       r.raise_for_status()
      return  r.json()["choices"][0]["message"]["content"]

@app.post("/rag")
def  rag():
       data  = request.get_json()
       query  =  data.get("query")
      contexts  =  search_docs(query)
       prompt =  f"Answer  using  only the  context:\n\n"  +  "\n---\n".join(contexts) +  f"\n\nQuestion:  {query}"
       answer =  call_openai(prompt)
       return  jsonify({"answer": answer,  "contexts":  contexts})

@app.get("/health")
def  health():
       return jsonify({"status":"ok"})

if  __name__ ==  "__main__":
       app.run(host="0.0.0.0",  port=8080)
