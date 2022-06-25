import cv2
import time
import datetime


def hit_key_to_stop(key: str):
    return cv2.waitKey(1) == ord(key)


def colect_face_layers(gray_scale_img):
    ACCURACY = 1.3
    MINIMAL_LAYERS_TO_BE_A_FACE = 5
    return face_cascade.detectMultiScale(
        gray_scale_img, ACCURACY, MINIMAL_LAYERS_TO_BE_A_FACE
    )


def draw_rectangle_around_face(face_layers):
    for x, y, width, height in face_layers:
        top_left = (x, y)
        bottom_right = (x + width, y + height)

        rectangle_color_bgr = (255, 100, 50)
        line_width = 3

        cv2.rectangle(
            frame, top_left, bottom_right, rectangle_color_bgr, line_width
        )


def there_are(face_layers):
    return len(face_layers) > 0


cap = cv2.VideoCapture(0)


four_carachter_code = cv2.VideoWriter_fourcc(*"mp4v")

video_capture_width = int(cap.get(3))
video_capture_height = int(cap.get(4))

frame_rate = 20.0
frame_size = (video_capture_width, video_capture_height)

output = cv2.VideoWriter(
    "video.mp4", four_carachter_code, frame_rate, frame_size
)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml"
)

while True:
    _, frame = cap.read()

    gray_scale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_layers = colect_face_layers(gray_scale_image)
    draw_rectangle_around_face(face_layers)

    if there_are(face_layers):
        recording = True

    output.write(frame)

    cv2.imshow("my-camera", frame)

    if hit_key_to_stop("q"):
        break

output.release()
cap.release()
cv2.destroyAllWindows()
