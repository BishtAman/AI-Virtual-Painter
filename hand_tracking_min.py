import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # for the width
cap.set(4, 480)  # for the height
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
while True:
    success, image = cap.read()
    image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(image_RGB)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                # print(id, lm)
                h, w, c = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
            # Decrease the size of landmarks and change line thickness and color
            mpDraw.draw_landmarks(image, hand_landmarks, mpHands.HAND_CONNECTIONS,
                                  landmark_drawing_spec=mpDraw.DrawingSpec(color=(255, 255, 0), thickness=2,
                                                                           circle_radius=2))

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 3)

    cv2.imshow("Image", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
