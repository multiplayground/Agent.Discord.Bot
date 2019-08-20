import requests
import json
from collections import defaultdict
from my_tokens import git_token

def get_users_isues():
  url = 'https://api.github.com/graphql'
  json_ = { 'query' : '''
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
          createdAt
          closedAt
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
  ''' }
  api_token = git_token
  headers = {'Authorization': 'token %s' % api_token}
  r = json.loads(requests.post(url=url, json=json_, headers=headers).text)
  examples={'AlTheOne':{'isues':['one','two']}}
  users=defaultdict(list)
  
  [users[edge['node']['login']] for  edge in r['data']['repository']['assignableUsers']['edges']]

  [users[isue['node']['assignees']['edges'][0]['node']['login']].append(
    [isue['node']['title'],
    isue['node']['state'],
    isue['node']['createdAt'],
    isue['node']['closedAt']]) 
    for  isue in r['data']['repository']['issues']['edges'] if isue['node']['assignees']['edges'] ] 
  
  return users
if __name__ == '__main__':
  get_users_isues()

