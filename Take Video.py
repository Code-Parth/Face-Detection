import cv2

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 15.0, (640, 480))
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

for i in range(5):
    cap.read()

while True:
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow("Camera Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
