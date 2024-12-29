import os 
def show(f): 
    try :
        for i,o,u in os.walk(f): 
            print("directory:" + i)
            for a in o : 
                print("subfolders:"+a)
            for b in u : 

                print("file : "+b)
    except FileNotFoundError: 
        pass # include in the reason of complicated 
    else : 
        print(f"your system not incudes this{f} file")
a = "."  # replace this . with your desired file name or else it does for all system includes.
show(a)

    
