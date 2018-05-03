
import glob
import os
import PIL
from PIL import Image

def main():
   files=glob.glob("images/predict/*.jpg"); 
   
   for index in range(len(files)):    
        f=files[index]
        basewidth = 28
        img = Image.open(f)        
        #wpercent = (basewidth / float(img.size[0]))
        #hsize = int((float(img.size[1]) * float(wpercent)))
        baseHeight=28
        img = img.resize((basewidth, baseHeight), PIL.Image.ANTIALIAS)
        print(img.size)
        img.save(f)

def test():
   files=glob.glob("images/testing/**/*.jpg");  
   for index in range(len(files)):    
        f=files[index]
        basewidth = 28
        img = Image.open(f)        
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img.convert('L')
        img.save(f)

if __name__ == "__main__":
    main()