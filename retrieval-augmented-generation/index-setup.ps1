param(
    [string]$SearchServiceName,
   [string]$ResourceGroup,
   [string]$IndexName  =  "docs"
)

$apiKey  = az  search  admin-key  show -g  $ResourceGroup  --service-name  $SearchServiceName --query  primaryKey  -o  tsv

$body  =  @{
   name  = $IndexName
    fields =  @(
       @{  name="id"; type="Edm.String";  key=$true  },
       @{ name="content";  type="Edm.String";  searchable=$true  },
      @{  name="embedding";  type="Collection(Edm.Single)"  }
   )
} |  ConvertTo-Json  -Depth  4

Invoke-RestMethod  -Method  Put `
    -Uri "https://$SearchServiceName.search.windows.net/indexes/$IndexName?api-version=2023-11-01"  `
   -Headers  @{  "api-key"=$apiKey;  "Content-Type"="application/json" }  `
   -Body  $body
