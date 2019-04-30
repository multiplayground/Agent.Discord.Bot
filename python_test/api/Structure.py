import json
def post(serv_structure):
    struck =json.loads(serv_structure)
    print (type (struck))
    return serv_structure

struct_obj= {"None" : [ "first" , "second" , "third" ] ,
         "first" :  [ "some one" , "some two" , "some three"] ,
         "second" :  [ "some one" , "some two" , "some three"] ,
         "third" :  [ "some one" , "some two" , "some three"] }
if __name__ == '__main__':
    jsonify =json.dumps(struct_obj) 
    post(jsonify)