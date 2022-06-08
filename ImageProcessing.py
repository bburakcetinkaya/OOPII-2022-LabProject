# -*- coding: utf-8 -*-
"""
Created on Wed May 25 06:09:56 2022

@author: Burak Çetinkaya
        151220152110
"""
import numpy as np



# from skimage import data, img_as_float
from skimage.filters import threshold_multiotsu
from skimage.filters import roberts
from skimage.filters import sobel
from skimage.filters import scharr
from skimage.filters import prewitt

from skimage.segmentation import chan_vese
from skimage.segmentation import morphological_chan_vese
from skimage.segmentation import checkerboard_level_set

# from skimage.segmentation import store_evolution_in
from skimage import img_as_ubyte,img_as_float
from skimage.io import imread


from skimage.color import rgb2gray
from skimage.color import rgb2hsv
from skimage.color import label2rgb


class ImageProcessing(object):
    
    def RGBtoGreyscale(self,imgPath):
        print("RGBtoGreyscale image processing")
        self.rgb = np.array(imread(imgPath))
        self.grayscaleImg = rgb2gray(self.rgb)        
        self.uByteArr = img_as_ubyte(self.grayscaleImg)     
        
        return self.uByteArr
    
    def RGBtoHSV(self,imgPath):
        print("RGBtoHSV image processing")
        self.rgb = np.array(imread(imgPath))
        self.hsv = rgb2hsv(self.rgb)

        self.uByteArr = img_as_ubyte(self.hsv)
        
        return self.uByteArr
    
    def multiOtsuThresholding(self,imgPath):
        # self.rgb = self.RGBtoGreyscale(rgb)
        print("multiOtsuThresholding image processing")
        self.img = np.array(imread(imgPath,as_gray=True))
        print(self.img)
        # self.grayscaleImg = rgb2gray(self.rgb)        
        # self.uByteArr = img_as_ubyte(self.grayscaleImg) 
        # self.grayscaleImg = rgb2gray(self.rgb)
        # self.rgb = np.array(self.grayscaleImg)
        self.multiOtsuThresholding = np.array(self.img)
        self.thresholds = threshold_multiotsu(self.multiOtsuThresholding)
        self.regions = np.digitize(self.multiOtsuThresholding, bins=self.thresholds)
        self.regionsColorized = label2rgb(self.regions)       
        self.uByteArr = img_as_ubyte(self.regionsColorized)   

        return self.uByteArr          

        # image = data.camera()   
        # img = numpy.array(image)
        # thresholds = threshold_multiotsu(img)
        # regions = np.digitize(img, bins=thresholds)
        # regions_colorized = label2rgb(regions)
        
        # arr = img_as_ubyte(regions_colorized)
        # img = QImage(arr.data,arr.shape[1], arr.shape[1], arr.strides[0], QImage.Format_RGB888)

        # self.outputLabel.setPixmap(QtGui.QPixmap(img))
        
    def chanVeseSegmentation(self,imgPath):
        print("chanVeseSegmentation image processing")
        self.img = np.array(img_as_float(imread(imgPath,as_gray=True)))
        # Feel free to play around with the parameters to see how they impact the result
        self.cv = chan_vese(self.img, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
                        max_num_iter=200, dt=0.5, init_level_set="checkerboard",
                        extended_output=True)   
        self.uByteArr = img_as_ubyte(self.cv[1])        
      #  return index 1 for full segmentation 
      #  return index 0 for the segmentation given in the iter variable
        
        return self.uByteArr
        
    def morphologicalSnakes(self,imgPath):
        print("morphological snakes image processing")
        self.img = np.array(img_as_float(imread(imgPath,as_gray = True)))
        # Initial level set
        self.init_ls = checkerboard_level_set(self.img.shape, 6)
        # List with intermediate results for plotting the evolution
        self.evolution = []
        self.callback = store_evolution_in(self.evolution)
        self.ls = morphological_chan_vese(self.image, num_iter=35, init_level_set=self.init_ls,
                                          smoothing=3, iter_callback=self.callback)
        self.uByteArr = img_as_ubyte(self.ls)
        return self.uByteArr
            
    def Roberts(self,imgPath):
        print("Roberts image processing")
        self.img = np.array(img_as_float(imread(imgPath,as_gray=True)))
        self.filteredImg = roberts(self.img)
        self.result = img_as_ubyte(self.filteredImg)
        return self.result
        
    def Sobel(self,imgPath):
        print("Sobel image processing")
        self.img = np.array(img_as_float(imread(imgPath,as_gray=True)))
        self.filteredImg = sobel(self.img)
        self.result = img_as_ubyte(self.filteredImg)
        return self.result
        
    def Scharr(self,imgPath):
        print("Scharr image processing")
        self.img = np.array(img_as_float(imread(imgPath,as_gray=True)))
        self.filteredImg = scharr(self.img)
        self.result = img_as_ubyte(self.filteredImg)
        return self.result

    def Prewitt(self,imgPath):
        print("prewitt image processing")
        self.img = np.array(img_as_float(imread(imgPath,as_gray=True)))
        self.filteredImg = prewitt(self.img)
        self.result = img_as_ubyte(self.filteredImg)
        return self.result

        