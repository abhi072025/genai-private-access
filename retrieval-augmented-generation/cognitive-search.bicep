param  location  string  = 'westeurope'
param  searchServiceName  string =  'search-private'

resource search  'Microsoft.Search/searchServices@2023-11-01'  =  {
   name:  searchServiceName
   location:  location
   sku:  { name:  'standard'  }
   properties:  {
       hostingMode: 'default'
       networkRuleSet:  {
          publicNetworkAccess:  'Disabled'
       }
   }
}
