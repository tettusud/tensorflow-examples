
import read_data as rd
import tensorflow as tf 
import numpy as np

BATCH_SIZE=10
EPOC=5

import os
dir_path = os.path.dirname(__file__) #<-- absolute dir the script is in 
file_path = os.path.join(dir_path, "data.csv")
data_cols=rd.extract_data(file_path)

#place holder for x 
X=tf.placeholder(tf.float32,[None,2])


W=tf.Variable(tf.zeros([2, 1], tf.float32))
B=tf.Variable(tf.zeros([1], tf.float32))

Y_pred=  tf.matmul(X,W)



train_x=[]

with tf.Session() as sess:
    
    sess.run(tf.global_variables_initializer())
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    
    for i in range(BATCH_SIZE):
    # Retrieve a single instance:
     features_result = sess.run(data_cols)
     train_x.append([features_result[0],features_result[1]])
    

    train_x=np.asarray(train_x)
  

    print(sess.run(Y_pred,feed_dict={X:train_x}))

    coord.request_stop()
    coord.join(threads)