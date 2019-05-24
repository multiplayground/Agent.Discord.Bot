import requests

url = 'https://api.github.com/graphql'
json = { 'query' : '{  repository(owner:"multiplayground", name:"mlp_api") {    issues(last:30, states:CLOSED) {      edges {        node { title     url      labels(first:5) { edges { node {  name   }   }   }   }   }  } }}' }
api_token = "e9acd99b8d29542c37ae8c233006bdaae9578d8f"
headers = {'Authorization': 'token %s' % api_token}

r = requests.post(url=url, json=json, headers=headers)
print (r.text)




query {
  repository(owner: "multiplayground", name: "mlp_api") {
    assignableUsers(first: 100) {
      edges {
        node {
          login
        }
      }
    }
    issues(first: 100) {
      edges {
        node {
          title
          state
          assignees(first: 100){
            edges{
              node{
                login
              }
            }
          }
        }
      }
    }
  }
}