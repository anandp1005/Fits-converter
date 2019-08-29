# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:40:03 2019

@author: Pendem
"""

import os
import numpy as np
from astropy.table import Table
from astropy.io import fits
import logging

LOG_FORMAT = '%(asctime)s  %(message)s'
logging.basicConfig(filename = "C:\\Users\\fits\\test\\test1.log",level = logging.DEBUG,format= LOG_FORMAT) 
logger =logging.getLogger()


for subdir, dirs, files in os.walk('C:\\Users\\fits\\test'):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".txt"):
            print (filepath)
            logger.info("\n\n---------------------------------------------------------\n\n")
            arr=np.loadtxt(filepath,dtype="uint16")
            logger.info("std_dev_of the file: %s",filepath)
            arr.shape
            arr_box=arr[200:300,200:300] #100 pixel X 100 pixel box for STD

            #With raw data from FPGA
            std_dev_raw= np.std(arr)
            std_dev_box = np.std(arr_box)              
            std_dev_col= np.std(arr,axis=0)
            std_dev_row= np.std(arr,axis=1)
            
            std_dev_row_min= np.amin(std_dev_row)
            std_dev_row_max= np.amax(std_dev_row)
            std_dev_row_mean= np.mean(std_dev_row)
            
            
            std_dev_col_min= np.amin(std_dev_col)
            std_dev_col_max= np.amax(std_dev_col)
            std_dev_col_mean= np.mean(std_dev_col)
            
            logger.info("std_dev_box_100X100 pixels: %f",std_dev_box)
            logger.info("std_dev_entire_image: %f",std_dev_raw)
            logger.info("std_dev of image lines (row wise) - min value: %f",std_dev_row_min)
            logger.info("std_dev of image lines (row wise)- max value: %f",std_dev_row_max)
            logger.info("std_dev of image lines (row wise)- mean: %f",std_dev_row_mean)
            
            logger.info("std_dev of image lines (Col wise)- min value: %f",std_dev_col_min)
            logger.info("std_dev of image lines (Col wise)- max value: %f",std_dev_col_max)
            logger.info("std_dev of image lines (Col wise)- mean: %f",std_dev_col_mean)
            
               
            hdu = fits.PrimaryHDU()
            hdu.data=arr
            hdu.header
            hdu.header['Plato_BBV3'] = 'With_CCD/Simulator'
            hdu.writeto(os.path.splitext(filepath)[0]+'.fits')
            
            