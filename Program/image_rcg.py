from PIL import Image
import numpy as np
i=Image.open("E:/img.jpg")
iarray=np.asarray(i)
print iarray
