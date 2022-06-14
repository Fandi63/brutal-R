import os
os.system("apt install figlet") 
os.system("clear")
os.system("figlet brutal-R")
print("1 install figlet")
print("2 Start pinging Russia websites")
x=input("brutal-R>")
if x == 1:
    os.system("apt install figlet")
if x == 2:
    os.system("timeout 7 ping russia.com")
    os.system("timeout 3 ping www.news.ru")
    os.system("timeout 2 ping www.tvrain.ru") 
    x=input("brutal-R>")
