import json

g=2
p=0x100000000
computed_values ={}

for i in range(p-1):
    v = pow(g,i,p)
    computed_values[v]=i

f = open("computed_values.json","w")
json.dump(computed_values,f)
f.close()
