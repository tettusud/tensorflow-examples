import tensorflow as tf
from PIL import Image
import glob

def train_data():
    filenames=tf.constant (["images/1.jpg","images/3.jpg","images/2.jpg","images/4.jpg","images/5.jpg"]);
    labels = tf. constant ([1, 1, 1,2, 2])

    #. Step 2: create a dataset returning slices of 'filenames
    dataset=tf.data.Dataset.from_tensor_slices ((filenames, labels))
    # step 3: parse every image in the dataset using map
    def _parse_function (filename, label) :
        image_string =tf.read_file (filename)
        image_decoded =tf. image.decode_jpeg (image_string, channels=1)
        image=tf.cast (image_decoded, tf.float32)
        resize_image= tf.image.resize_images (image, [28,28])
        return tf.reshape (resize_image, [-1]), label

    dataset = dataset.map (_parse_function)
    dataset = dataset.batch (5)
    #make one shot iterator
    iterator = dataset.make_one_shot_iterator()
    images, labels= iterator.get_next()
    return images, labels

def test_data():
    filenames=tf.constant (["images/5.jpg"]);
    return _parse_function(filenames[0])


def _parse_function (filename) :
    image_string =tf.read_file (filename)
    image_decoded =tf. image.decode_jpeg (image_string, channels=1)
    image=tf.cast (image_decoded, tf.float32)
    resize_image= tf.image.resize_images (image, [28,28])
    return tf.reshape (resize_image, [-1])


import PIL
from PIL import Image

def resize_img():
   files=glob.glob("images/1/*.jpg");
  
   for index in range(len(files)):    
        f=files[index]
        basewidth = 28
        img = Image.open(f)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img.save(f)

  


if __name__ == "__main__":
    #tf.app.run()
    resize_img();