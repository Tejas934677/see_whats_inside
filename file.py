import shelve 
with shelve.open('t') as me : 
    me["a"] = "apple"
    me["b"] = "ball"
#me.close() , not needed because we used with , as 
with shelve.open("t") as d : 
    print(d["a"])