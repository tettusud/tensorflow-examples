import tensorflow as tf 

import os
dir_path = os.path.dirname(__file__) #<-- absolute dir the script is in
 
file_path = os.path.join(dir_path, "data.csv")
print(file_path)
#string input producer to read file a line
filename_queue = tf.train.string_input_producer([file_path])
 
def extract_data():
    #skip the header skip_header_lines=1
    reader = tf.TextLineReader(skip_header_lines=1)
    key, value = reader.read(filename_queue)
    record_defaults = [[1], [1], [1]]
    col1, col2, col3 = tf.decode_csv(
    value, record_defaults=record_defaults)
    #tf.stack Stacks a list of rank-R tensors into one rank-(R+1) tensor.
    features = tf.stack([col1, col2, col3])
    return features

csv_data=    extract_data()

#reduce sum
with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    for i in range(7):
    # Retrieve a single instance:
     features_result = sess.run(csv_data)
     print(" features from csv %s" % features_result)

    coord.request_stop()
    coord.join(threads)