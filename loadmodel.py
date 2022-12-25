from keras.preprocessing import image

import numpy as np
from PIL import Image
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

anh = Image.open("ngua1.jpg")
model = load_model("AI_horse_or_human.h5")

for fn in anh :
    x = image.load_img(anh, target_size=(150,150))
    x = np.expand_dims(x, axis= 0)
    images = np.vstack([x])
classes = Model.predict(images , batch_size=10)

if classes[0] > 0.5:
    print(" Đây là người")
else :
    print(" Đây là ngựa")