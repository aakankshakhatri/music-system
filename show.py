import cv2
import label_image
import pygame as pg


def play_music(music_file, volume=0.8):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 2048  # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)
    
  





size = 4

# We load the xml file
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

webcam = cv2.VideoCapture(0)  # Using default WebCam connected to the PC.

while True:
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)  # Flip to act as a mirror

    # Resize the image to speed up detection
    mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))

    # detect MultiScale / faces
    faces = classifier.detectMultiScale(mini)

    # Draw rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 4)

        # Save just the rectangle faces in SubRecFaces
        sub_face = im[y:y + h, x:x + w]

        FaceFileName = "test.jpg"  # Saving the current image from the webcam for testing.
        cv2.imwrite(FaceFileName, sub_face)

        text = label_image.main(
            FaceFileName)  # Getting the Result from the label_image file, i.e., Classification Result.
        text = text.title()  # Title Case looks Stunning.
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(im, text, (x + w, y), font, 1, (0, 0, 255), 2)
        pred = text;
       
        if (pred == "angry"):

            tune = play_music("nick jonas - jealous.mp3")
            print("Angry song is playing.")
        elif(pred == "happy"):
            tune = play_music("nick jonas - jealous.mp3")
            print("Happy song is playing.")
        elif (pred == "Sad"):
            tune = play_music("nick jonas - jealous.mp3")
            print("Sad song is playing.")
        elif (pred == "neutral"):
            tune = play_music("nick jonas - jealous.mp3")
            print("Nuetral song is playing.")


    # Show the image
    cv2.imshow('Capture', im)
    key = cv2.waitKey(10)
    # if Esc key is press then break out of the loop
    if key == 27:  # The Esc key
        break




