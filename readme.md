# Real-time Fruit Detection using YOLOv4

## Business Overview

In the rapid development of technology, significant concerns are given to the food we consume. In the agriculture industry, one of the most cost-demanding factors is skilled labor. The industry is moving towards automation to decrease the cost of work and to increase quality. Robotic harvesting can provide potential solutions to many such problems faced by the industry. There are numerous challenging tasks to be fulfilled by the upcoming technology, one of them being an accurate fruit detection system. Different technologies have been used in the past for fruit recognition using emerging computer vision technologies.

The particular project discusses building a robust model for fruit detections. There can be many advanced use cases for this. Some of them are:

1. You are working in a warehouse where lakhs of fruits come in daily, and if you try to separate and package each of the fruit boxes manually, it will require a lot of workforce. So, you can build an automated system that can detect fruits and separate them for packaging.

2. You are the owner of a vast orchid. If you want to harvest fruits from it manually, it will require a lot of workforces too. You can build a robot or a self-driving truck that can detect fruits on specific trees and harvest them for you.

---

## Aim

To build a robust fruit detection system using YOLOv4.

---

## Tech Stack

- **Language**: `Python`
- **Object Detection**: `YOLOv4`
- **Data Annotation**: `LabelImg`
- **Environment**: `Google Colab`

---

## Approach

### 1. Data Collection and Labeling with LabelImg

To create a custom object detector, we need an excellent dataset of images and labels so that the sensor can efficiently train to detect objects. We can do this in two ways:

- a. Using Google's Open Images Dataset
  - We can gather thousands of images and their auto-generated labels within minutes. Explore that dataset here!
- b. Creating your dataset and then labeling it manually
  - We will create a dataset manually by collecting images from google image scraper or manually clicking them and then marking them using an image annotation tool, LabelImg.

### 2. Building a YOLOv4 Object Detector with Darknet in the Cloud

- a. Enabling GPU within your notebook
- b. Cloning and Building Darknet
  - We are downloading AlexeyAB's famous repository and adjusting the Makefile to enable OPENCV and GPU for darknet and then build darknet.

### 3. Demo on Pretrained Model

YOLOv4 is trained on the coco dataset, which has 80 classes that it can predict. We will take these pre-trained weights to see how it gives results on some of the images.

### 4. Customize YOLOv4 with Different Command-Line Flags

- a. Threshold Flag
- b. Output Bounding Box Coordinates
- c. Don't Show Image
- d. Multiple Images at Once

### 5. Preparing Dataset for Training Yolo

- a. Labeled Custom Dataset
- b. Custom .cfg file
  - Edit the yolov4.cfg for your custom model training using the Colab editor
- c. obj.data and obj.names files
  - Create a new file within a code or text editor called obj.names where you will have one class name per line
- d. train.txt and test.txt files
  - The train.txt and test.txt files hold the relative paths to all our training images and validation images.

### 6. Train Your Custom Object Detector

### 7. Training Yolo Model from a Checkpoint

### 8. Model Evaluation using Mean Average Precision

### 9. Predictions on Images

### 10. Predictions on Video

---
