###add a sample dataset ingestion script so your RAG app can demo with real content. This script will take local text files (or PDFs converted to text) and push them into Azure Cognitive Search securely.


import  os,  requests, json,  uuid
 
 SEARCH_ENDPOINT =  os.getenv("SEARCH_ENDPOINT")    # e.g.  https://<service>.search.windows.net
 SEARCH_API_KEY  = os.getenv("SEARCH_API_KEY")
 INDEX_NAME  =  os.getenv("INDEX_NAME", "docs")
 
 def  upload_docs(docs):
       url  =  f"{SEARCH_ENDPOINT}/indexes/{INDEX_NAME}/docs/index?api-version=2023-11-01"
        headers =  {"api-key":  SEARCH_API_KEY,  "Content-Type": "application/json"}
        actions  =  []
       for  content  in  docs:
              actions.append({
                      "@search.action":  "upload",
                      "id": str(uuid.uuid4()),
                      "content":  content
               })
       body  =  {"value":  actions}
       r  =  requests.post(url,  headers=headers, json=body)
        r.raise_for_status()
        print("Uploaded",  len(docs), "documents")
 
 if  __name__ ==  "__main__":
        #  Load sample  text  files  from ./data  folder
        docs  = []
        data_dir  =  "./data"
       for  fname  in  os.listdir(data_dir):
              if  fname.endswith(".txt"):
                      with  open(os.path.join(data_dir, fname),  encoding="utf-8")  as  f:
                            docs.append(f.read())
        upload_docs(docs)
