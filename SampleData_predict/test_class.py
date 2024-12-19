
import pickle
import os

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import yticks
from tensorflow.keras.models import load_model
from Preprocessing.remove_background import singleRemoveBackground
from Preprocessing.util import getpred_Preprocess, saveConfig


curpath = os.path.dirname(os.path.abspath(__file__))
path_list =curpath.split("\\")[:-1]
rootpath = "\\".join(path_list)
# label_list = os.listdir(r"D:\imgs")
# print(label_list)
#saveConfig(label_list,rootpath)
# print(rootpath)
with open(f"{rootpath}\\config","rb") as fp:
    label_list = pickle.load(fp)
print("라벨리스트확인:",label_list)

sample_data = input("라벨리스트가 불러와 졌는지 확인 후 \n"
                    "샘플데이터의 파일 경로와 파일명을 지정해 주세요\n")
origin_img = cv.imread(sample_data,cv.COLOR_BGR2RGB)
origin_img= cv.resize(origin_img,(128,128))
rembg_img = singleRemoveBackground(r"{}".format(sample_data))
rembg_img = getpred_Preprocess(rembg_img)
rembg_img = np.array([rembg_img])
# D:\frog1.jpg
#모델 로딩
model = load_model(f"{rootpath}\\Trainning\\classification_image.keras")
y_pred = model.predict(rembg_img)
plt.imshow(sample_data)
plt.xlabel("pred:"+label_list[np.argmax(y_pred)])
plt.xticks([]);yticks([])
prlt.show()

