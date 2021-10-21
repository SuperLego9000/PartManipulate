import sys
data={}
adding=True
stop=False
ScriptType=""
while ScriptType!="new" and ScriptType!="edit":
    ScriptType=input("new/edit: ")
    print(ScriptType)
data['ScriptName']=input("script object name: ")
if ScriptType=="edit":data['append']=input("location: ")
else:data['append']="Instance.new(\"Part\",game.Workspace)"
while adding:
    try:
        append=input("attribute=value: ")
        temp=append.split("=")
        data[temp[0]]=temp[1]
        stop=False
    except KeyboardInterrupt:
        if stop:
            print("\nBye!")
            print(f"\n\ndebug:\n{data}")
            sys.exit(0)
        else:
            stop=True
            print("^Compile\ndata=[\n")
            print(f"{data['ScriptName']}={data['append']}")
            for key in data.keys():
                if key!="ScriptName" and key!="append":
                    print(f"{data['ScriptName']}.{key}={data[key]}")
            print("\n]\n")
    except:pass