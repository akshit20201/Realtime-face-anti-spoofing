import cv2
import numpy as np

# Window name
WINDOW_NAME = "FAS Detector"

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Webcam
cap = cv2.VideoCapture(0)

def is_fake(face):
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    blur = cv2.Laplacian(gray, cv2.CV_64F).var()

    # threshold tuned for phone screens
    if blur < 120:
        return True
    return False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # UI text
    cv2.putText(frame, f"Faces: {len(faces)}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]

        fake = is_fake(face)

        if fake:
            label = "FAKE"
            color = (0, 0, 255)  # RED
            liveness = 0.0
        else:
            label = "REAL"
            color = (0, 255, 0)  # GREEN
            liveness = 1.0

        # BLUE face box
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (255, 0, 0), 2)

        # REAL / FAKE label
        cv2.putText(frame, label,
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, color, 2)

        # Liveness score
        cv2.putText(frame, f"Liveness: {liveness}",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

    cv2.imshow(WINDOW_NAME, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
