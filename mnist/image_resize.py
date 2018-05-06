
import glob
import os
import PIL
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from PIL import ImageFilter
import cv2
import numpy as np
from matplotlib import pyplot as plt
import random

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


def augment():
    datagen = ImageDataGenerator(
        rotation_range=20,       
        fill_mode='nearest')

    img = load_img('images/predict/0.jpg')  # this is a PIL image
    img=img.filter(ImageFilter.SHARPEN)
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

    datagen.fit(x)
    # the .flow() command below generates batches of randomly transformed images
    # and saves the results to the `preview/` directory
    i = 0
    for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='images/preview', save_prefix='ka', save_format='jpeg'):
        i += 1
        if i > 2:
          break  # otherwise the generator would loop indefinitely


data_directory="images/training"
files='**/*.jpg'
destination_directory="images/testing/"

def generate_test_images():   

    #filenames = glob.glob(os.path.join(data_directory, files))
    #random.shuffle(filenames)

    dirs = os.listdir(data_directory )


    filenames=filenames[:4]
    for name in filenames:
        #print(os.path.basename(os.path.dirname(name))) 
        filename=os.path.basename(name)
        basename=os.path.basename(os.path.dirname(name));
         
        img = cv2.imread(name)
        blur = cv2.GaussianBlur(img,(5,5),10)
        
        dest_basename=os.path.join(destination_directory, basename)
        if not os.path.exists(dest_basename):
            os.makedirs(dest_basename)
       
        cv2.imwrite(os.path.join(dest_basename,filename),blur)


    #for index in range(len(files)): 
       
       
       #img = cv2.imread(files[index])
       #blur = cv2.GaussianBlur(img,(5,5),10)
      
       #cv2.imwrite("images/preview/"+str(index)+".jpg",blur)

       #plt.subplot(121),plt.imshow(img),plt.title('Original')
       #plt.xticks([]), plt.yticks([])
       #plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
       #plt.xticks([]), plt.yticks([])
       #plt.show()

if __name__ == "__main__":
    generate_test_images()