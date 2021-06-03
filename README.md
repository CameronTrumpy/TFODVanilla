
# Tensorflow Object Detection Walkthrough

This Repository includes files from a [course](https://github.com/nicknochnack/TFODCourse) by Nicholas Renotte, plus my additional instructions and tips on how to set up a good work environment for TF. It also includes custom scripts and instructions that were not included in course material.

This set of Notebooks provides a complete set of code to be able to train and leverage your own custom object detection model using the Tensorflow Object Detection API. This accompanies the Tensorflow Object Detection course on my [YouTube channel](https://www.youtube.com/c/nicholasrenotte).

## Setup

**Step 0.1 - Environment**
I set up my project on an SSD with Ubuntu 20.04(LTS), and booted my pc from that SSD when I wanted to work on the project. I suggest a similar approach if you want to leverage the flexibility of Linux, along with the computing power of your CPU+GPU. It may be possible to set up the project in a Linux VM, but I haven't tried.s

If you don't know how to dual boot OSes on your machine, you can research it online, or you can attempt at working in Windows. I strongly reccomend against this as Windows is weird with package managment and PATH variables.

**Step 0.2 - Setup CUDA**
If you are planning to train your model with your GPU, which is much faster than CPU training, you need to set up CUDA on your machine.

As of writing, this [GPU support](https://www.tensorflow.org/install/gpu) article is a good install guide for CUDA. Take note that the guide(as of writing) is written for Ubuntu 18.04. for me it worked by just changing all of the 18.04s to 20.04s in all of the installation commands.

## TF Steps

<br  />

**Step 1.** Clone this repository. You may want to do this in a dedicated GIT repos directory(optional).

Optional repo directory setup
<pre>
cd ~
mkdir GITRepos
cd GITRepos
</pre>

Clone Repo
<pre>
git clone https://github.com/CameronTrumpy/TFODVanilla
cd  TFODVanilla
</pre>
<br/><br/>

**Step 2.** Create a new virtual environment

<pre>
python3 -m venv tfod
</pre>

<br/>

**Step 3.** Activate your virtual environment. Anytime you are working with this project your environment should be activated

<pre>
source tfod/bin/activate
</pre>

<br/>

**Step 4.** Install dependencies and add virtual environment to the Python Kernel, along with jupyter for jupyter notebooks

<pre>
python -m pip install --upgrade pip

pip install ipykernel

pip install jupyter

python -m ipykernel install --user --name=tfod
</pre>

<br/>

**Step 5.0.** Open The first notebook. [1. Image Collection.ipynb](https://github.com/CameronTrumpy/TFODVanilla/blob/master/1.%20Image%20Collection.ipynb)- ensure you start jupyter, and change the kernel to the virtual environment as shown below.

<pre>
jupyter notebook
</pre>

<img  src="https://i.imgur.com/8yac6Xl.png">

<br/>

**Step 5.1** Refer to the instructions file for how to successfully complete the first notebook. [Notebook Guide](https://github.com/CameronTrumpy/TFODVanilla/blob/master/NotebookGuide.md) 

**Step 6.** Manually divide collected images into two folders train and test. So now all folders and annotations should be split between the following two folders. <br/>

\TFODCourse\Tensorflow\workspace\images\train<br  />

\TFODCourse\Tensorflow\workspace\images\test

<br/><br/>

**Step 7.** Begin training process by opening  [2. Training and Detection.ipynb](https://github.com/CameronTrumpy/TFODVanilla/blob/master/2.%20Training%20and%20Detection.ipynb), this notebook will walk you through installing Tensorflow Object Detection, making detections, saving and exporting your model. Refer to the  [Notebook Guide](https://github.com/CameronTrumpy/TFODVanilla/blob/master/NotebookGuide.md) to successfully complete the notebook if issues arise.

<br  /><br/>

**Step 8.** During this process the Notebook will install Tensorflow Object Detection. You should ideally receive a notification indicating that the API has installed successfully at Step 8 with the last line stating OK.

<img  src="https://i.imgur.com/FSQFo16.png">

If not, resolve installation errors by referring to the <a  href="https://github.com/nicknochnack/TFODCourse/blob/main/README.md">Error Guide.md</a> in this folder.

<br  />  <br/>

**Step 9.** Once you get to step 6. Train the model, inside of the notebook, you may choose to train the model from within the notebook. I have noticed however that training inside of a separate terminal on a Windows machine you're able to display live loss metrics.

<img  src="https://i.imgur.com/K0wLO57.png">

<br  />

**Step 10.** You can optionally evaluate your model inside of Tensorboard. Once the model has been trained and you have run the evaluation command under Step 7. Navigate to the evaluation folder for your trained model e.g.

<pre> cd Tensorlfow/workspace/models/my_ssd_mobnet/eval</pre>

and open Tensorboard with the following command

<pre>tensorboard --logdir=. </pre>

Tensorboard will be accessible through your browser and you will be able to see metrics including mAP - mean Average Precision, and Recall.

<br  />