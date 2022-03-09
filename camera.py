# import the opencv library


import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))  # depends on fourcc available camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 20)

cascade_faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# define a video capture object


while (True):

    # Capture the video frame
    # by frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade_faces.detectMultiScale(gray, 2, 4)

    for (x, y, w, h) in faces:
        print("Face Found")
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #     frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2RGB)

    #     cv2.normalize(frame, frame, 70, 255, cv2.NORM_MINMAX)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()



