# importing necessary libraries i.e... opencv, mediapipe
import cv2  # open cv
import mediapipe as mp  # pose estimation

mp_drawing = mp.solutions.drawing_utils  # pose landmarks
mp_pose = mp.solutions.pose  # performing pose estimation

# Function to detect push-ups
def detect_pushups(image):
    # Convert the image to RGB format
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect the pose landmarks in the image
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        results = pose.process(image_rgb)

        # Draw the pose landmarks on the image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2))

        # Check if the left and right wrists are above the corresponding shoulders
        if results.pose_landmarks:
            left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y
            left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y

            right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y
            right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y

            if left_wrist < left_shoulder and right_wrist < right_shoulder:
                # If wrists are above the shoulders, it's a push-up
                cv2.putText(image, "Push-up", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    return image

# Start push-up detection
cap = cv2.VideoCapture(0)  # Change the parameter to the desired camera index if needed

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip the frame horizontally for mirror effect

    # Detect and track push-ups
    frame = detect_pushups(frame)

    # Display the resulting frame
    cv2.imshow('Push-up Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
