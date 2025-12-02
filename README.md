 #  Private-Access  Generative AI  with  RAG
 
This  project  deploys  Azure OpenAI  behind  Private  Link and  integrates  it  with Azure  Cognitive  Search  to build  a  secure  Retrieval Augmented  Generation  (RAG)  application.

 ##  Steps
 1. Deploy  `openai/private-endpoint.bicep`  to  secure Azure  OpenAI.
 2.  Deploy `retrieval-augmented-generation/cognitive-search.bicep`  for  private  Cognitive Search.
 3.  Run  `index-setup.ps1` to  create  a  secure index.
 4.  Start  the RAG  app  (`server.py`)  and query  with  `cli.py`.
 
##  Security
 -  Azure OpenAI  accessible  only  via Private  Endpoint.
 -  Role assignments  enforce  least  privilege.
-  No  public  network access  for  Cognitive  Search.
