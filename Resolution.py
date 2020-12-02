from PIL import Image 
import os

im = Image.open(r"Hulk.png")  
width, height = im.size

a = list(im.getdata())


t = []
m = []
o = 1

for x in range(len(a)):
    try:
        k = (a[x]+a[x+1])/2
        t.append(k)
    except:
        continue

for x in range(len(a)):
    try:
        k = (a[x]+a[x+width])/2
        m.append(k)
    except:
        continue
    
for x in t:
    a.insert(o, x)
    o += 2

for x in m:
    a. insert(width, x)
    width += 2



im.putdata(a)


im.save("gevgev.png")

os.startfile("gevgev.png")

