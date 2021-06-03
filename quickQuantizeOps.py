import tensorflow as tf
import sys, getopt
import argparse
import os

curr_dir = os.getcwd() + "/"
saved_model_dir = ''
 
parser = argparse.ArgumentParser() # Initialize parser
parser.add_argument("-i", "--Input", help = "Input Directory") # Adding optional argument
args = parser.parse_args() # Read arguments from command line
 
if args.Input:
	saved_model_dir = args.Input
	print("Configured input as: % s" % args.Input)

print("MODEL DIR:" + saved_model_dir)


#def representative_dataset():
#  for data in tf.data.Dataset.from_tensor_slices((images)).batch(1).take(100):
#    yield [tf.dtypes.cast(data, tf.float32)]


converter = tf.lite.TFLiteConverter.from_saved_model(curr_dir + saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

#Integer only quantization https://www.tensorflow.org/lite/performance/post_training_quantization
#converter.representative_dataset = representative_dataset
#converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
#converter.inference_input_type = tf.int8  # or tf.uint8
#converter.inference_output_type = tf.int8  # or tf.uint8

#https://www.tensorflow.org/lite/guide/ops_select why ops file is needed
converter.target_spec.supported_ops = [
  tf.lite.OpsSet.TFLITE_BUILTINS, # enable TensorFlow Lite ops.
  tf.lite.OpsSet.SELECT_TF_OPS # enable TensorFlow ops.
]

tflite_quant_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_quant_model)
