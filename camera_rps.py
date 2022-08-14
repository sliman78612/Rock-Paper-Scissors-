from tabnanny import verbose
import cv2
from keras.models import load_model
import numpy as np
import time


def get_prediction():

    model = load_model('keras_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    cap = cv2.VideoCapture(0)
    print('You have 5 seconds to choose')
    start_time = time.time()
    while True: 
       
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data, verbose = 0)
        cv2.imshow('frame', frame)
        time_passed = int(abs(round((start_time - time.time()),2)))
        #print(time_passed, end = '\r', flush=True)
        #print(abs(round((start_time - time.time()),1)) == 5)        
        # Press q to close the window
        if cv2.waitKey(1) & time_passed == 5:
            # After the loop release the cap object
            cap.release()
            # Destroy all the windows
            cv2.destroyAllWindows()
            result = np.where(prediction[0] == np.amax(prediction[0]))[0][0]
            options = ['Nothing','Rock', 'Paper','Scissors']
            return options[result]
                
print(get_prediction())