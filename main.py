import cv2
import time
from ultralytics import YOLO

model = YOLO("runs/detect/train3/weights/best.pt")

cap = cv2.VideoCapture(0)

current_word = ""
last_letter = ""
last_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.30, device=0)
    annotated = results[0].plot()

    if results[0].boxes:
        letter = model.names[int(results[0].boxes.cls[0])]

        # Add letter only if different from last
        if letter != last_letter and time.time() - last_time > 1:
            current_word += letter
            last_letter = letter
            last_time = time.time()

    cv2.putText(annotated, current_word, (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    cv2.imshow("ASL Word Builder", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Final Word:", current_word)
