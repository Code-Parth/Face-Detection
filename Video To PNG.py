import cv2

video_file = 'output.avi'
cap = cv2.VideoCapture(video_file)
n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_idx = 0

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f'images/{frame_idx:03d}.png', frame)
        frame_idx += 1
    else:
        break

cap.release()
