# 비디오 프래임 제거 cv2..apply()
import cv2
import numpy as np
import matplotlib.pyplot  as plt
from rembg import remove
#https://github.com/xuebinq/U-2-Net
#https://github.com/xuebinq/DIS
import os
def removeBackgroundFolder(rpath):

    rpath=r"D:\imgs"
    f_lists = os.listdir(rpath)

    print(f_lists)
    for folder in f_lists:
        f_names = os.listdir(rpath+"\\"+folder)
        print(folder,":")
        for f_name in f_names:
            ori_img = cv2.imread(rpath+"\\"+folder+"\\"+f_name)
            ori_img= cv2.resize(ori_img,(256,256))
            # cv2.imshow("ori "+f_name, ori_img)
            rmbg_img = remove(ori_img)
            cv2.imwrite(rpath+"\\"+folder+"\\"+f_name,rmbg_img)

            # cv2.imshow(f_name,rmbg_img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            print(".",end="")
        print()
def singleRemoveBackground(imagepathName):
    ori_img = cv2.imread(rpath + "\\" + folder + "\\" + f_name)
    ori_img = cv2.resize(ori_img, (256, 256))
    # cv2.imshow("ori "+f_name, ori_img)
    rmbg_img = remove(ori_img)
    cv2.imwrite(imagePathName)
    print("배경이미지 제거가 완료되었습니다.")
if __name__"__main__":
    pass #이 파일을 직접 실행했을때 작동 코드
else:
    pass #다른 파일에서 ,import 시 작동되는 코드


#grabCut

