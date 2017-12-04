import tensorflow as tf 

x = tf.constant([[1, 1, 1], [1, 1, 1]])

#reduce sum
with tf.Session() as sess:
   print(sess.run(tf.reduce_sum(x)))