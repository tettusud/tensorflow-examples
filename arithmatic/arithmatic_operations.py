import tensorflow as tf 



a= tf.constant(3)
b= tf.constant(5)

mul= tf.multiply(a,b)
add=tf.add(a,b)
sub=tf.subtract(a,b)
pow=tf.pow(a,b) 

with tf.Session() as sess:  
  print(sess.run(mul))
  print(sess.run(add))
  print(sess.run(sub))
  print(sess.run(pow))

  