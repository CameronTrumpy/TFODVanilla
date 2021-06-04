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

This step handles your image capture. It didn't work well for me, so I just captured my images outside of the notebook and copied them in to the correct directories. If you want to do it that way, this is how I went about it.
<pre>
sudo apt-get install cheese
cheese
</pre>
Cheese is a image capture tool for linux. In cheese, take whatever pictures you want for training. Once you're done, copy those images into the collectedimages directory created in the last step. Create a directory for each set of labeled images. For example, save all your thumbsup images in /collectedimages/thumbsup

**Step 5.**

This step installs labelImg into the directory Tensorflow/labelimg. LabelImg is used for placing labels on specific sections of your image. For me, it didn't properly run in the jupyter notebook, so I had to open it from a terminal window. You should open your terminal inside the repo directory, activate your virtual environment, and then run
<pre>
python labelImg.py
</pre>
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

This updates your config files based on what you had updated earlier.

**Step 6.**

TRAIN YOUR MODEL!! 

**Step 7.**

Evaluate your model. It should at the end return results on your test data if correct.

**Step 8.**
**Step 9.**
**Step 10.**
**Step 11.**
**Step 12.**
**Step 13.**
