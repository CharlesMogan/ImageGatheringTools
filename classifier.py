from keras.models import load_model
from keras.applications import mobilenet_v2 as my_model
from keras.applications.mobilenet_v2 import MobileNetV2 as MyModel
from keras.preprocessing import image
import numpy as np

model_size = (224, 224)  # 224 for moblenet 299 for inceptionv3


def prepare_image(file):
    img_path = ''
    img = image.load_img(img_path + file, target_size=model_size)
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return my_model.preprocess_input(img_array_expanded_dims)


def prepare_image2(preloaded_image):    # FIXME perhaps this is where I am going wrong do comparison
    img_array = image.img_to_array(preloaded_image)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return my_model.preprocess_input(img_array_expanded_dims)


def predict_image(preped_image):
    modelFileName = 'rodmoblenet12c.h5'
    model = load_model(modelFileName)
    class_names = ["beaver", "capybara", "chinchilla", "chipmunk", "degu", "hamster", "mouse", "rat", "gerbil",
                   "groundhog",  # FIXME get from folder names then save in correct format
                   "guinea_pig", "rabbit"]
    prediction = model.predict(preped_image)

    # The prediction for each image is the probability for each class, e.g. [0.8, 0.1, 0.2]
    # So get the index of the highest probability
    class_idx = np.argmax(prediction)

    print(class_names[int(class_idx)])
    return class_names[int(class_idx)]
