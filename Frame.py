import cv2
import os

# Function to extract frames
def extract_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    frame_count = 0

    while True:
        # Read a frame
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Save frame as JPEG file
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:05d}.jpg")
        cv2.imwrite(frame_filename, frame)
        
        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Extracted {frame_count} frames.")

# Example usage
video_path = 'male-Barbell-barbell-romanian-deadlift-side.mp4'
output_folder = 'Frames'
extract_frames(video_path, output_folder)
