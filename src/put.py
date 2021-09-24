from PIL import Image,ImageDraw,ImageFont
import qrcode
from src import get
from src import generate


def content(img,content):
    name = content
    font = ImageFont.truetype("arial.ttf", size = 100)
    d = ImageDraw.Draw(img)
    y_pix = 1150
    d.text((get.start_pix_centered(img,name,font),y_pix),name, fill=(0,0,0),font = font)



def qr(img):
    qr = generate.qr()
    qr = qr.resize((350,350), Image.ANTIALIAS)
    offset = (100,2025)
    img.paste(qr,offset)

def instructor(img):
    text = get.instructor()
    stp = 2630
    font = ImageFont.truetype("arial.ttf", size=65)
    d = ImageDraw.Draw(img)
    y_pix = 1930
    d.text((get.start_pix_di(text, font, stp), y_pix), text, fill=(0, 0, 0), font=font)

def date(img,date):
    text = date
    stp = 900
    font = ImageFont.truetype("arial.ttf", size=65)
    d = ImageDraw.Draw(img)
    y_pix = 1930
    d.text((get.start_pix_di(text, font, stp), y_pix), text, fill=(0, 0, 0), font=font)

def name(img,user):
    name = user
    font = ImageFont.truetype("arial.ttf", size = 150)
    d = ImageDraw.Draw(img)
    y_pix = 750
    d.text((get.start_pix_centered(img,name,font),y_pix),name, fill=(255,255,255),font = font)