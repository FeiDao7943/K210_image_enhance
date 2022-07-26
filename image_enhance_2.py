import tensorflow as tf
import os
import random
source_file = './enhance1/'
target_file = './enhance2/'
num = 300
if not os.path.exists(target_file):
    os.makedirs(target_file)
file_list = os.listdir(source_file)
with tf.Session() as sess:
    for i in range(num):
        max_random = len(file_list)-1
        a = random.randint(0, max_random)
        image_raw_data = tf.gfile.FastGFile(source_file + file_list[a], "rb").read()
        print("Processing: ", file_list[a])
        image_data = tf.image.decode_jpeg(image_raw_data)
        filpped_le_re = tf.image.random_flip_left_right(image_data)
        filpped_up_down = tf.image.random_flip_up_down(image_data)
        adjust = tf.image.random_brightness(filpped_up_down, 0.4)
        image_data = tf.image.convert_image_dtype(adjust, dtype=tf.uint8)
        encode_data = tf.image.encode_jpeg(image_data)
        with tf.gfile.GFile(target_file + str(i) + "_enhance" + ".jpg", "wb") as f:
            f.write(encode_data.eval())
print("Image enhanced done!")
