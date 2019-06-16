import json



class User:
    score=''
    name=''
    id=0
    def __init__ (self,score,name,id):
        self.score = score
        self.name = name
        self.id = id

    def score(self,user):
        return self.score