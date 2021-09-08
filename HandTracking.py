import cv2
import mediapipe
import pyttsx3

camera = cv2.VideoCapture(0)

engine = pyttsx3.init()

mpHands = mediapipe.solutions.hands

hands = mpHands.Hands()

mpDraw = mediapipe.solutions.drawing_utils

checkThumbsUp = False

while True:

    success, img = camera.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    hlms = hands.process(imgRGB)

    height, width, channel = img.shape

    if hlms.multi_hand_landmarks:
        for handlandmarks in hlms.multi_hand_landmarks:

            for fingerNum, landmark in enumerate(handlandmarks.landmark):
                positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                if fingerNum > 4 and landmark.y < handlandmarks.landmark[2].y:
                    break

                if fingerNum == 20 and landmark.y > handlandmarks.landmark[2].y:
                    checkThumbsUp = True

            mpDraw.draw_landmarks(img, handlandmarks, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Camera", img)

    # if checkThumbsUp:
    #     engine.say("Thumbs Up!")
    #     engine.runAndWait()
    #     break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break