#use ~ sign if you want to add space at the start of the line
#like ~ my name is and add much space as you want after $
from PIL import Image
import string
import random
import numpy as np
import os
from fpdf import FPDF
l1 = []
l2 = []
k=1


text_file = "text_file.txt"
with open(text_file, "r",encoding="utf8") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    for char in stripped_line:
      l1.append(char)
    l2.append(l1)
    l1=[]
np.array(l2)
print(l2)
path = r"D:\\Projects\\Python\\Text to hanwrriting\\New folder (5)\\letters_"
sheet_path = r"D:\\Projects\\Python\\Text to hanwrriting\\New folder (5)\\final.jpg"
x = 170
z = 170
o = 11
y2 = 62
ycord = 245
img1 = Image.open(sheet_path).convert("RGBA")

for i in range(0,len(l2)): 
  if(len(l2[i])==0):
      ycord+=y2
      x = z
  for j in range(0,len(l2[i])):
    #yaha par changes kare h last time ke baad yaha par phle xcord ka bhi daal rkha tha if condition m (xcord>=1400 or ycord>=2075) to usse probelm ho raha tha to islie yaha se xcord hata dia h phir kabhi dikkat hui to vaapis daal denge
    if(ycord>=2150):
      rgb_im = img1.convert('RGB')
      rgb_im.save(r"D:\\Projects\\Python\\Text to hanwrriting\\Final Page\\"+"page"+str(k)+".jpg")
      k=k+1
      img1 = Image.open(sheet_path).convert("RGBA")
      x = 170
      ycord = 245
    else:
      # ye waali condition tab kaam karti h jab hum usi line m h par page ki width khatam ho gyi ho aur ab hume next line jana h
      # like a margin
      f = random.randrange(1476,1510,20)
      if(x>=f and l2[i][j-1] == " "):
        ycord +=y2
        x=z
      if(x>=f):
        ycord +=y2
        x=z
    if(l2[i][j] in string.ascii_lowercase or l2[i][j] in string.ascii_uppercase or l2[i][j] in string.punctuation or l2[i][j] in string.digits):
      try:
        if(l2[i][j]=='~' ):
          pass
        else:
          x += o
          if(l2[i][j]=='i' or l2[i][j]=='j' or l2[i][j]=='k' or l2[i][j]=='t' or l2[i][j]=='s' or l2[i][j]=='I' or l2[i][j]=='J' or l2[i][j]=='K' or l2[i][j]=='T' or l2[i][j]=='S'):
            x+=12
          else:
            x+=16
          # this if condition below checks if the current line is ended or not
          if(j==(len(l2[i]))-1):
            n = random.choice([1,2,3])
            img3 = Image.open(path+str(n)+"\\"+str(ord(l2[i][j]))+".png").convert("RGBA")
            img1.paste(img3, (x,ycord), mask = img3)
            # this line below here takes the code to next line after the first line is ended
            ycord +=y2
            x = z
          else:
            n = random.choice([1,2,3])
            # x += o
            img3 = Image.open(path+str(n)+"\\"+str(ord(l2[i][j]))+".png").convert("RGBA")
            img1.paste(img3, (x,ycord), mask = img3)
      except Exception as e:
        pass
    if(l2[i][j]==' ' or l2[i][j]== '~'):
      random_for_space = random.randrange(35,45)
      x+=random_for_space
him = img1.convert('RGB')
him.save((r"D:\\Projects\\Python\\Text to hanwrriting\\Final Page\\"+"page"+str(k)+".jpg"))
pdf = FPDF()
pdf.set_auto_page_break(0)
que = input("you wanna make a pdf?")
if(que=="yes"or que == "YES" or que == "y" or que == "Y"):
  for filename in os.listdir("D:/Projects/Python/Text to hanwrriting/Final Page"):
          if ".jpg" in filename:
            pdf.add_page()
            pdf.image("D:/Projects/Python/Text to hanwrriting/Final Page/"+filename,w=190,h=200)
  pdf.output("D:/Projects/Python/Text to hanwrriting/Final Page/"+'try.pdf',"F")

