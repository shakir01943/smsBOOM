import bs4
import requests
import os

os.system("clear")
while(True):
    number = input("Input Number=> ")
    f = open("number.txt", "a")
    f.write(number)
    f.close()

    reg_url = "https://amrtube.com/reg.php"
    n = open("number.txt","r")
    num = n.readline()
    user_info = {
        'name': 'Shakir khan',
        'phone': num
    }
    requset = requests.post(reg_url, data=user_info)
    sup = bs4.BeautifulSoup(requset.text, "html.parser")
    find = sup.find("b")
    result = find.text
    final_result = result.lower()

    if final_result == "phone already registered":
        print("Okk...\nNow Start BooMBing")
        break

    elif final_result == "phone wrong!!!":
        print("Worng Phone Number!!!!")
        os.system("rm number.txt")
        continue