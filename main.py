import os 

for i,o,u in os.walk("C:/Users/nn194/Desktop"): 
    print("directory:" + i)
    for a in o : 
        print("subfolders:"+a)
    for b in u : 

        print("file : "+b)
