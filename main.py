import cv2
import mediapipe as mp
import pyautogui
import time

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

prev_left_click = False
prev_right_click = False
holding = False

def fingers_up(hand_landmarks):
    finger_tips = [8, 12, 16, 20]
    fingers = []

    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        hand = hands[0]
        drawing_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
        landmarks = hand.landmark
        fingers = fingers_up(hand)

        # Mouse movement
        index_finger = landmarks[8]
        x = int(index_finger.x * width)
        y = int(index_finger.y * height)
        screen_x = int(index_finger.x * screen_width)
        screen_y = int(index_finger.y * screen_height)
        pyautogui.moveTo(screen_x, screen_y)

        # Left Click: Thumb + Index
        if fingers == [1, 1, 0, 0, 0] and not prev_left_click:
            pyautogui.click()
            prev_left_click = True
            time.sleep(0.3)
        elif fingers != [1, 1, 0, 0, 0]:
            prev_left_click = False

        # Right Click: Index + Pinky
        if fingers == [0, 1, 0, 0, 1] and not prev_right_click:
            pyautogui.rightClick()
            prev_right_click = True
            time.sleep(0.3)
        elif fingers != [0, 1, 0, 0, 1]:
            prev_right_click = False

        # Scroll Down: Index + Middle
        if fingers == [0, 1, 1, 0, 0]:
            pyautogui.scroll(-80)
            time.sleep(0.1)

        # Scroll Up: Middle + Ring
        if fingers == [0, 0, 1, 1, 0]:
            pyautogui.scroll(80)
            time.sleep(0.1)

        # Mouse Hold: Index + Middle + Ring
        if fingers == [0, 1, 1, 1, 0] and not holding:
            pyautogui.mouseDown()
            holding = True
        elif fingers != [0, 1, 1, 1, 0] and holding:
            pyautogui.mouseUp()
            holding = False

        # Volume Up: All fingers
        if fingers == [1, 1, 1, 1, 1]:
            pyautogui.press('volumeup')
            time.sleep(0.3)

        # Volume Down: Thumb down
        if fingers == [0, 1, 1, 1, 1]:
            pyautogui.press('volumedown')
            time.sleep(0.3)

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
