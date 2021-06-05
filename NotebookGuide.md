# Jupyter Notebook Guide
This guide details how to properly step through notebook 1 and 2, and issues I have encountered.

## Notebook 1 - Image Collection

**Step 1.**

Importing your dependencies is fairly straightforward. I didn't encounter any issues at this step but if you do, the problem will likely be easy to look up online.

**Step 2.**

This step is also very straightforward. If your model is going to be trained for different labels, make sure to update the titles here. Also pay attention to their case. Later on you need to reference your labels, so a case mismatch would cause it to fail.

**Step 3.**

This step creates your training and test image directories if they do not already exist.

**Step 4.**

This step handles your image capture. This step will fail if you do not have a webcam on your device. if you want more control, you can capture your images outside of the notebook and copied them in to the correct directories. If you want to do it that way, this is how I went about it.

        sudo apt-get install cheese
        cheese

    
Cheese is a image capture tool for linux. In cheese, take whatever pictures you want for training. Once you're done, copy those images into the collectedimages directory created in the last step. Create a directory for each set of labeled images. For example, save all your thumbsup images in /collectedimages/thumbsup

**Step 5.**

This step installs labelImg into the directory Tensorflow/labelimg. LabelImg is used for placing labels on specific sections of your image. For me, it didn't properly run in the jupyter notebook, so I had to open it from a terminal window. You should open your terminal inside the repo directory, activate your virtual environment, and then run

        cd Tensorflow/labelimg
        python labelImg.py

Label your images. Be careful to draw your bounding boxes as tight to the object as possible. The more space included that isn't your object, the more chances there are for your model to become less precise.

**Step 6.**

Manually divide collected images into two folders train and test. Your images no longer have to be organized into their subcategories, as their label .xml files specify what images contain certain labels.
A good rule of thumb is to have about 80% of your collected images delegated to training, and 20% delegated to testing.

/TFODVanilla/Tensorflow/workspace/images/train

/TFODVanilla/Tensorflow/workspace/images/test

**Step 7.**

This step is just compressing your images into a tar.gz format. This isn't necessary, as we are training locally.

## Notebook 2 - Training and Detection

**Step 0.**

This step configures your paths for training your model. If you want to change which pretrained model you train with, you can change the PRETRAINED_MODEL_URL && NAME to match. Alternate models can be found at [TF2 Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md).

**Step 1.**

This step downloads your model, and installs TensorFlow Object Detection. 
Once installed, running the verification script should return an OK message. If it doesn't, try the next few lines and see if they help. If it says that a package is missing, make sure that you install it, or upgrade it to its correct version.

If you get the message, no module named 'object_detection', you may need to restart your kernel. you'll have to rerun the path setup cells, and your wget import. Then return to the import object_detection cell, and rerun.

**Step 2.**

This step creates your label map for your model. The labels should exactly match the labels that you previously assigned to your images in the first notebook, otherwise they will not work. Add as many labels as you need.

**Step 3.**

Create your TF records. These will be used later in the project for training your model.

**Step 4.**

This step copies the model into your training directory.

**Step 5.**

This updates your config files based on what you had updated earlier. This is necesssary for you to execute transfer learning and apply your data to the pretrained model.

**Step 6.**

TRAIN YOUR MODEL!! Training may take a while depending on if you're training on CPU or GPU. I trained on a GTX 1060TI, with a per-step time of around .15s. This per-step time indicates the average step speed in a batch, out of the total epoch of 2000 steps. 

Training on CPU is extremely slow compared to training on GPU, so even if you don't have a high powered GPU, it is still highly reccomended to train on one.

**Step 7.**

Evaluate your model. If your training correctly executed,the evaluation should return a results table on how your model performed with the test data.

**Step 8.**

Loading your model from a checkpoint should work fine if your previous two steps worked.

**Step 9.**

To detect from an image, make sure to update the image path to match a file you have taken.

**Step 10.**

I had issues with live detection, as openCV was having trouble displaying a GUI for live detection.

**Step 11.**

Freezing the graph allows to export your project to TFJS or TFLite for use on mobile devices.

**Step 12.**

Convert to TFJS for web application

**Step 13.**

Convert to TFLite to run on a device like a Raspberry Pi

**Step 14.**

Exporting models
