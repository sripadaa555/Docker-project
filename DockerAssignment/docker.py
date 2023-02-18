import os
import socket
from collections import Counter

Counter = Counter()

def getIPAddress():
    hostname = socket.gethostname()
    IPAddress = socket.gethostbyname(hostname)
    return IPAddress

def countWords(file):
    totalwordcount = 0
    with open(file, 'r') as file:
        for line in file:
            if (line != '\n'):
                if (file.name.endswith("IF.txt")):
                    Counter.update(line.replace("Â", "").split())
                totalwordcount = totalwordcount + len(line.replace("Â", "").split())
    return totalwordcount

TextFiles_WordCounts = {}
path ="/home/data"
if os.path.exists(path + "/" +"result.txt"):
  os.remove(path + "/" +"result.txt")
outputStr="====|| Text File at Location: /home/data ||====\n"
for eachFile in os.listdir(path):
    if eachFile.endswith(".txt"):
        outputStr=outputStr+eachFile+"\n"
        TextFiles_WordCounts[eachFile] = countWords(path + "/" + eachFile)
        
outputStr=outputStr+"\n"
outputStr=outputStr+"====|| b.Read the two text files and count total number of words in each text files ||====\n"
AllFiles_WordCount = 0
AllFiles_Names = ""
for i in TextFiles_WordCounts.keys():
    AllFiles_Names = AllFiles_Names + i + ","
    AllFiles_WordCount = AllFiles_WordCount + TextFiles_WordCounts.get(i)
    outputStr = outputStr +"Total number of words in [" + i + "] is : " + str(TextFiles_WordCounts.get(i))+"\n"

outputStr = outputStr +"\n"
outputStr = outputStr +"====|| Grand total (total number of words in both files) ||====\n"
outputStr = outputStr +"Total number of words in both files [" + AllFiles_Names[0:len(AllFiles_Names) - 1] + "] is: " + str(AllFiles_WordCount)+"\n"

outputStr = outputStr +"\n"
outputStr = outputStr +"====|| Top 3 words with maximum number of counts in IF.txt ||====\n"
outputStr = outputStr +str(Counter.most_common(3))+"\n"

outputStr = outputStr +"\n"
outputStr = outputStr +"====|| IP address ||====\n"
outputStr = outputStr +"Your Computer's IP Address is:" + getIPAddress()

results_TextFile = open(path + "/" +"result.txt","w")
results_TextFile.write(outputStr)
results_TextFile.close()
for eachline in open(path + "/" +"result.txt","r").readlines():
    print(eachline.replace("\n",""))
