import tensorflow as tf
import sys, getopt
import argparse
import os

curr_dir = os.getcwd() + "/"
saved_model_dir = ''
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-i", "--Input", help = "Input Directory")
 
# Read arguments from command line
args = parser.parse_args()
 
if args.Input:
	saved_model_dir = args.Input
	print("Configured input as: % s" % args.Input)

print("MODEL DIR:" + saved_model_dir)
converter = tf.lite.TFLiteConverter.from_saved_model(curr_dir + saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quant_model = converter.convert()
open("quantized_model.tflite", "wb").write(tflite_quant_model)
