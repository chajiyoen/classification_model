import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from sympy import factor
import os

from test_cv2 import removeBackgroundFolder, singleRemoveBackground
from sympy.printing.tensorflow import tensorflow
from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import Dense, Conv2D, Dropout, MaxPool2D
#pre_model = Sequential()


def imageAugment_sub(orimg): #이미지 증강
    rn=np.random.randint(3,6)
    rn=round(rn/10,1)
    testimge1 = tf.image.random_brightness(orimg, rn)
    #testimge2 = tf.image.random_brightness(orimg, rn)

    #testimge1=tf.image.random_crop(testimge1, size=(150,150,3))
    # testimge1=tf.image.resize(
    # testimge1,size=(256,256,3),method="nearest",preserve_aspect_ratio=True)

    # testimge1=tf.image.random_flip_left_right(testimge1)
    # testimge1=tf.image.random_flip_up_down(testimge1)
    pre_model=tf.keras.layers.RandomRotation((-0.2,0.3)) #레이어 출력을 다시 정수로 변환
    testimge1= pre_model(testimge1)
    pre_model = tf.keras.layers.RandomFlip(mode="HORIZONTAL_AND_VERTICAL")
    testimge1 = pre_model(testimge1)
    tf.keras.layers.RandomZoom((-0.15,0.15),(-0.15,0.15))
    testimge1 = pre_model(testimge1)
    return  np.array(testimge1).astype(np.uint8)


def readIageDirect(rpath):
    cnt=0
    rpath = r"D:\imgs"
    f_lists = os.listdir(rpath)
    for folder in f_lists:
        f_names = os.listdir(rpath+"\\"+folder)
        print(folder,":",end="")
        for f_name in f_names:
            ori_img = cv.imread(rpath+"\\"+folder+"\\"+f_name)
            ori_img= cv.resize(ori_img,(256,256))
            for ix in range(5):
                arg_img=imageAugment_sub(ori_img)
                cv.imwrite(rpath+"\\"+folder+"\\" +str(cnt)+f_name,arg_img)
                cnt+=1
            print(".",end="")
        print()

readIageDirect(r"d\imgs")
np.random.seed=10
tf.random.set_seed(10)