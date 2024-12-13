import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from opencv01 import removeBackgroundFolder, singLeRemoveBackground

from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import Dense, Conv2D, Dropout, maxPool2D
