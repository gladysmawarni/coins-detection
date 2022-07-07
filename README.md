# Computer Vision Project - Coins Detection 

#### This is my final project for [Ironhack](https://www.ironhack.com/en) Data Analytics Bootcamp that I did on October 2021 - December 2021.
#### [Presentation Link](https://www.canva.com/design/DAE58SXxRRM/5V8n55yDOmZtgkHl-HQJkA/view?utm_content=DAE58SXxRRM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

### Main Objective
The main goal why I decided to do this project is to gain more understanding about deep leaning, in particular the subject of computer vision as it is one that interest me the most.

I decided to build a model that detects coins(euros) in a picture with hope that it can be useful for people who are visually disabled, to help them identify how many coins that they have.

This project utilizes YOLOv5 object detection algorithm to detect coins in a picture, identify what each coin is, count the total of the values, and have a voiceover say out loud the total value.

### YOLOv5
[YOLOv5 repository](https://github.com/ultralytics/yolov5) developed by [Ultralytics](https://ultralytics.com/) and is built on top of Pytorch. 

After many exploration and reading about computer vision/ object detection I decided to use YOLOv5 for this project in favor of other libraries, mainly because I found it easier to implement for someone who does not have previous experience in the field. It is also quite precise and fast to train.

### How I build the project
To make my own model, I collected pictures of euro coins by myself and from [this repo](https://github.com/SuperDiodo/euro-coin-dataset). Then I annotate the coins that is in the picture by using [Roboflow](https://roboflow.com/), the total number of images I used to train and test the model is around 500 pictures.

Once I have my dataset, I train the model using batch of 16 and 200 epochs. The mean average precision of the model with 0.5 IoU is 0.96.

Finally, after I have my model I made a web application using Flask to be more user-friendly to use. The code to run it is in [app.py](https://github.com/gladysmawarni/coins-detection/blob/main/app.py)

![image](https://user-images.githubusercontent.com/78975611/177735425-9e94c14c-7bb1-41cf-8f37-233d0cdb3e13.png)

![image](https://user-images.githubusercontent.com/78975611/177735659-15c94f90-92eb-4967-80d9-f30d4c478e0e.png)
