import os
import cv2
from ultralytics import YOLO

# Load the YOLOv8 model from Ultralytics
model = YOLO('yolov8n-pose.pt')  # Make sure to use the correct path to the model

# Directory paths
image_dir_path = 'Frames'
annotate_dir_path = 'annotations'

# Create directory for annotations if it doesn't exist
os.makedirs(annotate_dir_path, exist_ok=True)

# Process each image in the frames_extracted folder
for filename in os.listdir(image_dir_path):
    if filename.endswith('.jpg'):
        # Path to the image
        image_path = os.path.join(image_dir_path, filename)

        # Load the image
        image = cv2.imread(image_path)

        # Perform inference
        results = model(image)

        # Extract keypoints from the results
        if results and hasattr(results[0], 'keypoints'):
            keypoints = results[0].keypoints.cpu().numpy()[0]  # Extracting keypoints for the first detected person

            # File path for the annotation file
            annotate_file_path = os.path.join(annotate_dir_path, f'{os.path.splitext(filename)[0]}.txt')

            # Save keypoints to a text file
            with open(annotate_file_path, 'w') as f:
                if len(keypoints) > 0:
                    f.write("Keypoints:\n")
                    for keypoint in keypoints:
                        f.write(f"{keypoint}\n")
                else:
                    f.write("No keypoints found")
        else:
            print(f"No keypoints found for {filename}")
