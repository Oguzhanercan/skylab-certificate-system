from PIL import ImageFont

def user(data,i):
    return data.loc[i][0]+ " " + data.loc[i][1],data.loc[i][2]

def instructor():
    num = int(input("System supports maximum 2 instructor for a certificate. Please enter the number of instructor : "))
    instructors = []
    for i in range(num):
        instructors.append(input(f" Enter the name of instructor {i+1}"))

    return ' & '.join(instructors)


def start_pix_centered(img,text,font):
    text_size = font.getsize(text)[0]
    img_center = int(img.size[0]/2)
    return (img_center - int(text_size/2))


def start_pix_di(text,font,stp):
    text_size = font.getsize(text)[0]
    t_center = stp
    return (t_center - int(text_size/2))