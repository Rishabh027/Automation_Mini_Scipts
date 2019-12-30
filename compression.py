import subprocess as sb
import os
path=input("Enter Path to perform compression: ")##Enter path in this format E:\Seasons\Silicon.Valley.2014
ls=os.listdir(path)
for i in ls:
    s=path+"\\"+i
    d=s+".zip"
    cmd="powershell Compress-Archive "+s+" "+d
    sb.call(cmd,shell=True)

