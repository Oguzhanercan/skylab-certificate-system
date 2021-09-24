from PIL import Image,ImageDraw,ImageFont
import numpy as np
import qrcode
import pandas as pd
from src import get
from src import put
from src import mailling
from tqdm import tqdm
xls_file = input("Enter the name of the file. Example : c_programming_list\nbut be careful about that the file must be in the same directory with this system")
date = input("Enter the date that participant graduated : ")
content = input("Enter the name of course : ")
sender = ""#the mail adress of sender
password = ""#mail password
data = pd.read_excel(xls_file,header = None)
data = data.iloc[:, :3]
img = Image.open("img_flow/template.png")
put.qr(img)
put.date(img,date)
put.instructor(img)
put.content(img,content)
put.qr(img)
subject = "SKY LAB Academy" #mail subject
img = img.save("img_flow/getready.png")

for i in tqdm(range(len(data))):
    img = Image.open("img_flow/getready.png")
    user,mail_adress = get.user(data,i)


    #mail content
    body = (f"Hi {user}, congrats for completing {content} course.")
    put.name(img,user)
    img.save("img_flow/ready2send.png")
    attachment = "img_flow/ready2send.png"
    mailling.mail(user,subject, body, sender, mail_adress, password, attachment = attachment)
print("succesfly end")
