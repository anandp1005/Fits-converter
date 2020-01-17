import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data = pd.read_csv('C:\\Users\\PLATO\\PycharmProjects\\Fits_EMC\\F_image_18_17_16.txt', header = None)
from fits_converter_EMC import filepath

arr_org=np.loadtxt('C:\\Users\\PLATO\\PycharmProjects\\Fits_EMC\\E_imageCCD1_14_47_05.txt',dtype="uint16")
arr = np.delete(arr_org, 0, axis=1)  # Deleting the first column as it all has zeros
arr = np.delete(arr, 0, axis=1)  # Deleting the first row as CDS is not implemented for first column
sliced_array = arr[1,10:100]  # Multiple ramps
oneslice= arr[1,10:20]
plt.plot(sliced_array)
plt.plot(oneslice)
plt.show()

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, constrained_layout=False)
fig.subplots_adjust(hspace=1)
ax1.set_title('Multiple ramps')
ax1.set_xlabel('HRamps')
ax1.set_ylabel('ADU')
ax1.plot(sliced_array)
fig.suptitle('Non-Linearity', fontsize=16)

ax2.set_title('Single ramp')
ax2.set_xlabel('HRamp')
ax2.set_ylabel('ADU')
ax2.plot(oneslice)
fig.savefig("hramp.png")
plt.close(fig)  # close the figure window