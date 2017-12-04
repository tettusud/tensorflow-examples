import tensorflow as tf 



 
def extract_data(file_path):    
    #string input producer to read file a line
    filename_queue = tf.train.string_input_producer([file_path])
    #skip the header skip_header_lines=1
    reader = tf.TextLineReader(skip_header_lines=1)
    key, value = reader.read(filename_queue)
    record_defaults = [[0.0], [0.0], [0.0]]
    col1, col2, col3 = tf.decode_csv(
    value, record_defaults=record_defaults)
    #tf.stack Stacks a list of rank-R tensors into one rank-(R+1) tensor.
    features = tf.stack([col1, col2, col3])
    return features
 