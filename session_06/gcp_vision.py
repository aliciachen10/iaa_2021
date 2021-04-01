import io
import os
import argparse

from google.cloud import vision

# Instantiate a client
client = vision.ImageAnnotatorClient()

def gcp_vision_labels(image_filepath):
    
    # Loads the image into memory
    with io.open(image_filepath, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    
    print('Labels:')
    for label in labels:
        print(label.description)


if __name__ == "__main__":
    
    ap = argparse.ArgumentParser()
    ap.add_argument("--image_filepath", required=True, help="Filename and path for image")
    args = vars(ap.parse_args())
    
    gcp_vision_labels(args['image_filepath'])


#ZEND
