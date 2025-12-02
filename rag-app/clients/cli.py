import  requests,  sys,  json, os
API  =  os.getenv("API","http://localhost:8080/rag")
query  =  "  ".join(sys.argv[1:]) or  "What  is  our retention  policy?"
resp  = requests.post(API,json={"query":query},timeout=30)
print(json.dumps(resp.json(),indent=2))
