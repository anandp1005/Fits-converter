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
import matplotlib.pyplot as plt
import re
import pandas as pd
LOG_FORMAT = '%(asctime)s  %(message)s'
logging.basicConfig(filename = "C:\\Plato\\Data\\Image-STD.log",level = logging.DEBUG,format= LOG_FORMAT) 
logger =logging.getLogger()


for subdir, dirs, files in os.walk('C:\\Plato\\Data\\17_01_2020\\Image_data_txt\\Test2'):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".txt"):
            print (filepath)
            
            x=re.search('E_image',filepath)
            print(x)
            logger.info("\n\n---------------------------------------------------------\n\n")
            if(x!= None):
                    print ('E side')
                    logger.info("\n\n----------------E qaudrant-----------------------------------------\n\n")
                    arr_org=np.loadtxt(filepath ,dtype="uint16")
                    arr= np.delete(arr_org,0,axis=1)    # Deleting the first column as it all has zeros
                    arr= np.delete(arr,0,axis=0)    # Deleting the first row as CDS is not implemented for this yet. Will soon be!
                    maxim= np.amax(arr)
                    logger.info("std_dev_of the file: %s",filepath)

                    arr_box=arr[200:300,200:300] #100 pixel X 100 pixel box for STD
        
                    ##If processing data from E quadrant "arr" should be used or else arr_rev should be used.
                    #With raw data from FPGA
                    std_dev_raw= np.std(arr)
                    std_dev_box = np.std(arr_box)                   
                    std_dev_col= np.std(arr,axis=0)
                    std_dev_row= np.std(arr,axis=1)
                    #For displaying the plots while processing the data
                    plt.plot(std_dev_row)
                    plt.plot(std_dev_col)
                    plt.show()
                    # df = pd.DataFrame(std_dev_row,std_dev_col)
                    # df.to_excel(filepath+".xlsx",index =True)
                   #np.savetxt('test.out', (std_dev_row, std_dev_col))
                    os.path.split(filepath)
                    #For saving the files into log file for further review at a later stage
                    fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1, constrained_layout=False)
                    fig.subplots_adjust(hspace=1)
                    ax1.set_title('Row wise noise')
                    ax1.set_xlabel('Row No.')
                    ax1.set_ylabel('STD')
                    ax1.plot(std_dev_row)
                    fig.suptitle('Noise Analysis', fontsize=16)
                    
                    ax2.set_title('Column wise noise')
                    ax2.set_xlabel('Column No.')
                    ax2.set_ylabel('STD')
                    ax2.plot(std_dev_col)
                    fig.savefig(filepath + ".png")

                    plt.close(fig)    # close the figure window
                    
                    
                    std_dev_row_min= np.amin(std_dev_row)
                    std_dev_row_max= np.amax(std_dev_row)
                    std_dev_row_mean= np.mean(std_dev_row)
                    std_dev_col_min= np.amin(std_dev_col)
                    std_dev_col_max= np.amax(std_dev_col)
                    std_dev_col_mean= np.mean(std_dev_col)
                    
                    logger.info("std_dev_row: %f",std_dev_row)
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
                    hdu.header['Plato_BBV3_EM'] = 'With_either Simulator/CCD - E Quadrant'
                    hdu.writeto(os.path.splitext(filepath)[0]+'.fits', overwrite=True)
                    
            else: 
                    
                    print ('F side')
                    logger.info("\n\n----------------F qaudrant-----------------------------------------\n\n")
                    arr_org=np.loadtxt(filepath ,dtype="uint16")
                    arr1= np.delete(arr_org,-1,axis=1)    # Deleting the first column as it all has zeros
                    arr2 = np.delete(arr1, -1, axis=1)  # Deleting the first column as it all has zeros
                   # arr2= np.delete(arr1,1,axis=1)
                    arr= np.delete(arr2,0,axis=0)    # Deleting the first row as CDS is not implemented for this yet. Will soon be!
                    arr_rev= np.flip(arr,axis=0)
                    maxim= np.amax(arr_rev)
                    logger.info("std_dev_of the file: %s",filepath)
                    arr_box=arr_rev[200:300,200:300] #100 pixel X 100 pixel box for STD
        
                    ##If processing data from E quadrant "arr" should be used or else arr_rev should be used.
                    #With raw data from FPGA
                    std_dev_raw= np.std(arr_rev)
                    std_dev_box = np.std(arr_box)                   
                    std_dev_col= np.std(arr_rev,axis=0)
                    std_dev_row= np.std(arr_rev,axis=1)
                    plt.plot(std_dev_row)
                    plt.plot(std_dev_col)
                    plt.show()
                    #np.savetxt(filepath +".out" , (std_dev_row,))
                    # df1 = pd.DataFrame(std_dev_row)
                    # df2= pd.DataFrame(std_dev_col)
                    # df=pd.concat([df1,df2])
                    # df.to_excel(filepath + "_rowcolumn_wise.xlsx", index=False)
                    # # df.to_excel(filepath + "_col_wise.xlsx", index=False)

                    std_dev_row_min= np.amin(std_dev_row)
                    std_dev_row_max= np.amax(std_dev_row)
                    std_dev_row_mean= np.mean(std_dev_row)

                    
                    std_dev_col_min= np.amin(std_dev_col)
                    std_dev_col_max= np.amax(std_dev_col)
                    std_dev_col_mean= np.mean(std_dev_col)
                    
                    
                    fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1, constrained_layout=False)
                    fig.subplots_adjust(hspace=1)
                    ax1.set_title('Row wise noise')
                    ax1.set_xlabel('Row No.')
                    ax1.set_ylabel('STD')
                    ax1.plot(std_dev_row)
                    fig.suptitle('Noise Analysis', fontsize=16)
                    
                    ax2.set_title('Column wise noise')
                    ax2.set_xlabel('Column No.')
                    ax2.set_ylabel('STD')
                    ax2.plot(std_dev_col)
                    fig.savefig(filepath + ".png")
                    #ax.plot([0,1,2], [10,20,3])
                   # fig.savefig("C:\\Plato\\Data\\Image.jpg")   # save the figure to file
                    plt.close(fig)    # close the figure window
                    
                    
                    logger.info("std_dev_box_100X100 pixels: %f",std_dev_box)
                    
                    logger.info("std_dev_entire_image: %f",std_dev_raw)
                    logger.info("std_dev of image lines (row wise) - min value: %f",std_dev_row_min)
                    logger.info("std_dev of image lines (row wise)- max value: %f",std_dev_row_max)
                    logger.info("std_dev of image lines (row wise)- mean: %f",std_dev_row_mean)
                    
                    logger.info("std_dev of image lines (Col wise)- min value: %f",std_dev_col_min)
                    logger.info("std_dev of image lines (Col wise)- max value: %f",std_dev_col_max)
                    logger.info("std_dev of image lines (Col wise)- mean: %f",std_dev_col_mean)
                    
                       
                    hdu = fits.PrimaryHDU()
                    hdu.data=arr_rev
                    hdu.header
                    hdu.header['Plato_BBV3_EM'] = 'With_either Simulator/CCD - F Quadrant'
                    hdu.writeto(os.path.splitext(filepath)[0]+'.fits', overwrite=True)
                    
            
