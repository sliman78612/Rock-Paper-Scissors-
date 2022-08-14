#from tabnanny import verbose
import cv2
from keras.models import load_model
import numpy as np
import time
import manual_rps as mrps
#from manual_rps import get_computer_choice, get_winner, play
model = load_model('keras_model.h5')
print('')

def get_prediction():
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
            print(prediction[0])
            result = np.where(prediction[0] == np.amax(prediction[0]))[0][0]
            options = ['Nothing','Rock', 'Paper','Scissors']
            if result == 0:
                print('Choice unclear. Try again')
                return get_prediction()
            else:
                print(f'You chose {options[result]}')
                return options[result]
                
def play():
    print(mrps.get_winner(mrps.get_computer_choice(),get_prediction()))

while True:
    play()
    print(f'\nPlayer Score: {mrps.player_wins} | Computer Score: {mrps.computer_wins}')
    if mrps.player_wins == 5:
        print(f'You win! Final score {mrps.player_wins} - {mrps.computer_wins}')
        break
    elif mrps.computer_wins == 5:
        print(f'You lose! Final score {mrps.player_wins} - {mrps.computer_wins}')
        break