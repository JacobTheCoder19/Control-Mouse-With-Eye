# Date Created: 03/29/2024
# Coded By: Jacob Graham
# Purpose: To have the ability to use your eye as a mouse and control the laptop

# Import necessary libraries
# OpenCV for image processing
import cv2   
# MediaPipe for face landmark detection
import mediapipe 
# PyAutoGUI for controlling the mouse
import pyautogui  

# Initialize the FaceMesh model from MediaPipe with refined landmarks
face_mesh_landmarks = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Start video capture from the default camera (index 0)
cam = cv2.VideoCapture(0)

# Get the screen width and height for mouse movement calculations
screen_w, screen_h = pyautogui.size()

# Start an infinite loop to continuously capture frames from the camera
while True:
    # Read a frame from the camera
    _, image = cam.read()
    
    # Flip the image horizontally to create a mirror effect
    image = cv2.flip(image, 1)
    
    # Get the dimensions of the captured image
    window_h, window_w, _ = image.shape
    
    # Convert the image from BGR to RGB color space for processing
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the RGB image to find face landmarks
    processed_image = face_mesh_landmarks.process(rgb_image)
    
    # Get all detected face landmark points
    all_face_landmark_points = processed_image.multi_face_landmarks
    
    # Check if any face landmarks were detected
    if all_face_landmark_points:
        # Get the landmark points for the first detected face
        one_face_landmark_points = all_face_landmark_points[0].landmark
        
        # Loop through specific landmark points (474 to 477) for eye tracking
        for id, landmark_point in enumerate(one_face_landmark_points[474:478]):
            # Calculate the x and y coordinates of the landmark point
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
            # print(x,y)  # Uncomment to see the coordinates
            
            # If the current landmark is the second one (id == 1), calculate mouse position
            if id == 1:
                # Scale the coordinates to the screen size
                mouse_x = int(screen_w / window_w * x)
                mouse_y = int(screen_h / window_h * y)
                # Move the mouse to the calculated position
                pyautogui.moveTo(mouse_x, mouse_y)

            # Draw a circle on the image at the landmark point for visualization
            cv2.circle(image, (x, y), 3, (0, 0, 255))
        
        # Define the left eye landmarks using specific indices
        left_eye = [one_face_landmark_points[145], one_face_landmark_points[159]]

        # Loop through the left eye landmarks to get their coordinates
        for landmark_point in left_eye:
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
            # print(x,y)  # Uncomment to see the coordinates
            # Draw a circle on the image at the left eye landmark points
            cv2.circle(image, (x, y), 3, (0, 255, 255))
        
        # Check if the vertical distance between the left eye landmarks is small enough to trigger a click
        if (left_eye[0].y - left_eye[1].y < 0.01):
            # Simulate a mouse click
            pyautogui.click()
            # Pause for 2 seconds after clicking
            pyautogui.sleep(2)
            # Print a message indicating a click occurred
            print("mouse clicked")  

    # Display the processed image in a window titled "Eye controlled mouse"
    cv2.imshow("Eye controlled mouse", image)
    
    # Wait for 100 milliseconds for a key press; if the 'Esc' key (key code 27) is pressed, exit the loop
    key = cv2.waitKey(100)
    if key == 27:
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
