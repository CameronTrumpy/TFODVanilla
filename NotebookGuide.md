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
Cheese is a image capture tool for linux. In cheese, take whatever pictures you want for training. Once you're done, copy those images into the collectedimages directory created in the last step.

**Step 5.**
This step installs labelImg into the directory Tensorflow/labelimg. LabelImg is used for placing labels on specific sections of your image. For me, it didn't properly run in the jupyter notebook, so I had to open it from a terminal window. You should open your terminal inside the repo directory, activate your virtual environment, and then run
<pre>
python labelImg.py
</pre>

**Step 6.**

**Step 7.**

## Notebook 2 - Training and Detection

**Step 1.**
**Step 2.**
**Step 3.**
**Step 4.**
**Step 5.**
**Step 6.**
**Step 7.**
**Step 8.**
**Step 9.**
**Step 10.**
**Step 11.**
**Step 12.**
**Step 13.**
