# YOLOv5_Vietnamese_Card_Game

## Introduction

I introduce YOLOv5s model with [PlayingCards](https://universe.roboflow.com/autoproject/betercarddetector/dataset/9) dataset. This model could be used to detect different hand in Vietnamese card game such as Thirteen, Baccarat and Blackjack

<p align="center">
  <img src="demo/card.gif" width=600><br/>
  <i>Thirteen Demo (Tien Len)</i>
</p>

## The training result on the validation set at the 50th epoch.

| Model     | Size (pixels) | mAP<sup>val 50-95 | mAP<sup>val 50 | Parameters (M) |
| --------- | ------------- | ------------------ | --------------- | -------------- | 
| YOLOv5s   | **640**       | **0.78**           | **0.995**       | **1.9**               |


## Step to try model on local device (can be used by CPU/GPU)

Firstly, you need to clone this repository

- Open terminal
- Creat new folder: `mkdir cards_yolov5`
- Move to folder: `cd cards_yolov5`
- Clone repository: `git clone ...`

Secondly, you need to creat Python virtual environment to try this model

- Open terminal in cards_yolov5 folder

**Ubuntu**

- Create venv: `python3 -m venv cards_yolov5`
- Activate venv: `source cards_yolov5/bin/activate`

**Window**

- Create venv: `python -m venv cards_yolov5`
- Activate venv: `cards_yolov5\Scripts\activate`

**Mac**

- Create venv: `python3 -m venv cards_yolov5`
- Activate venv: `source cards_yolov5/bin/activate`

Thirthly, you need to install requirement packages
- `pip/pip3 install -r requirements.txt`

Finally, run detect.py in terminal and enjoy! (source 0: camera)
```bash
python/python3 detect.py --weights small_best.pt --kind "Tien Len" --source 0      
                                                                                           "Ba Cao"              
                                                                                           "Xi Dach"                     
```
**THANK YOU SO MUCH** 
