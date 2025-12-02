param  location  string  = 'westeurope'
param  openAiAccountId  string
param  vnetPeSubnetId  string

resource  pe  'Microsoft.Network/privateEndpoints@2023-05-01'  = {
    name: 'openai-pe'
    location: location
    properties: {
       subnet:  {  id: vnetPeSubnetId  }
       privateLinkServiceConnections:  [
          {
              name: 'openai-conn'
              properties:  {
                 privateLinkServiceId:  openAiAccountId
                 groupIds:  [  'openai' ]
              }
          }
       ]
   }
}
