import json
data=json.load(open("data.json"))
def unos(w):
        w=w.lower()    
        if w in data:
            return data[w]
        else:
            return "The word does not exist"
a=input("Type some word: ")
output=unos(a)
if type(output)==list:
        for i in output:
                print(i)
else:
        print(output)
       
                
        
        






