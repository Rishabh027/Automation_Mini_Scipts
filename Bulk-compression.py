import subprocess as sb
import os
path=input("Enter Path to perform compression(Use format E:\Seasons\Silicon.Valley.2014): ")##Enter path in this format E:\Seasons\Silicon.Valley.2014
ls=[name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]
for i in ls:
    s=path+"\\"+i
    d=s+".zip"
    cmd="powershell Compress-Archive "+s+" "+d
    sb.call(cmd,shell=True)

print("Compression Done!!")
    

