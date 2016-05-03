from PIL import Image
import csv
import numpy as np
from numpy import float32
from numpy import uint8
import random
import scipy.misc

class mdata:
    def __init__(self, data, labels, n, b, m):
        self.data      = data
        self.labels    = labels
        self.normal    = n
        self.benign    = b
        self.malignant = m

def readData():
    f=open("data/reduced_labels.csv")
    labels = []
    mgrams = []
    fname = "data/combined_set_52/"
    n = 0
    b = 0
    m = 0
    for row in csv.reader(f, delimiter=' '):
        if row[3] == "N":
            labels.append(0)
            n += 1
        elif row[3] == "B":
            labels.append(1)
            b += 1
        else:
            labels.append(2)
            m += 1
        #read image pixel vals in
        name = row[0]
        name = fname + name + ".png" #.../mdbXYZ.png
        # print("Reading in: ", name)
        # for i in range(1,num_images):
        #     if i < 33 or i > 57 or i < 291 or i > 311: #ignored
        #         if i < 100:
        #             if i < 10:
        #                 name = fname + "00" + str(i) + ".png"
        #             else:
        #                 name = fname + "0" + str(i) + ".png"
        #         else:
        #             name = fname + str(i) + ".png"
        im = Image.open(name).load() #Can be many different formats.
                # pixels = []
                # for k in range(1024):
                #     for j in range(1024):
                #         pixels.append(im[k,j])
        # center = random.randrange(482,542)
        pixels = [im[k,j]/256.0 for k in range(0, 48) for j in range(0, 48)]
        mgrams.append(pixels)
    print("Total images: ", len(mgrams))
    # print("Total pixels: ", len(mgrams[0]))
    print("Total labels: ", len(labels))
    print("Normals: ", n, "Benign: ", b, "Malignant: ", m)
    return mdata(mgrams, labels, n, b, m)



    # mgrams = np.ndarray(shape=(num_images - 1,48*48), buffer=np.array(mgrams), dtype=float32)

    #read label data
    #https://www.tensorflow.org/versions/r0.7/tutorials/mnist/beginners/index.html#mnist-for-ml-beginners

    # del labels[num_images:]