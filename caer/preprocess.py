# Author: Jason Dsouza
# Github: http://www.github.com/jasmcaus

# Importing the necessary packages
import numpy as np
from .utils import readToGray
from .utils import saveNumpy

def preprocess(DIR, categories, resized_size, size, name, isSave=True):
    """
    Reads Images in base directory DIR
    Returns
        train -> Image Pixel Values with corresponding labels
    Saves the above variables as .npy files if isSave = True
    """

    train = [] 
    try:
        # If train.npy already exists, load it in
        # if os.path.exists('train.npy')

        train = np.load(f'{name}.npy', allow_pickle=True)
        print('[INFO] Loading from Numpy Files')
    except:
        print(f'[INFO] Could not find {name}.npy. Generating the Image Files')
        for category in categories:
            category_path = os.path.join(DIR, category)
            classNum = categories.index(category)
            count = 0 
            for image in os.listdir(category_path):
                if count != size:
                    image_path = os.path.join(category_path, image)
                    # Returns image RESIZED and GRAY
                    gray = readToGray(image_path, resized_size)

                    train.append([gray, classNum])
                    count +=1 
                    _printTotal(count)
                else:
                    break
        # Shuffling the Training Set
        train = shuffle(train)

        # # Converting to Numpy handled by saveNumpy()
        # train = np.array(train)

        # Saves the Train set as a .npy file
        if isSave == True:
            #Converts to Numpy and saves
            saveNumpy(name, train)

    #Returns Training Set
    return train

def _printTotal(count):
    print(count)

def shuffle(train):
    """
    Shuffles the Array
    """
    import random
    random.shuffle(train)
    return train

def sepTrain(train, IMG_SIZE=224, channels=1):
    # x = []
    # y = []
    # for feature, label in train:
    #     x.append(feature)
    #     y.append(label)

    x = [i[0] for i in train]
    y = [i[1] for i in train]

    # Converting to Numpy + Reshaping X
    x = reshape(x, IMG_SIZE, channels)
    y = np.array(y)

    return x, y

def reshape(x, IMG_SIZE, channels):
    return np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE, channels)

def normalize(x):
    """
    Normalizes the data to mean 0 and standard deviation 1
    """
    x = x/255.0
    return x