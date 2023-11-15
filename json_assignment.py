import json
s1= open("interns.json", "r") 
s2= s1.read()
intern_data = json.loads(s2)
diction={}
for inter in intern_data['interns']:
    if inter [ "middle_name"] == None:
           email=(f"{inter['first_name']}.{inter['last_name']}@pvpsit.com") 
           name=(f"{ inter['first_name']}{ inter['last_name']}") 
    else : 
        email=(f"{inter['first_name']}-{inter['middle_name']}.{inter['last_name']}@pvpsit.com")
        name=(f"{inter['first_name']}{inter['middle_name']}{inter['last_name']}")
    diction[email]={"id":inter["id"], "fullname":name} 
print(diction)
