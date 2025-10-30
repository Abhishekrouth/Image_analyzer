# Image Analyzer 

This is a Flask based Image analyzer built using Google Cloud Vision API. It analyzes
uploaded image and returns Labels, Likelihood, Text, and properties of the image.

## Features:

* @app.route("/image_analyzer"): To analyze the uploaded image
* body:
       requests: to read image
       features: 
                type (LABEL_DETECTION):To return the details of the image like description, score etc.
                type (TEXT_DETECTION): To return the text content on the image.
                type (IMAGE_PROPERTIES): To return the dominantColors, pixelFraction etc.
                type (FACE_DETECTION): To retun the likelyhood of the image, example: joyLikelihood etc.
        
        maxResults: To set the maximum number of output.

## Technologies used:

1. Flask
2. Google cloud vision 


### Face detection
        
![alt text](images/Face_detection(image9).png)

### Label Detection

![alt text](images/Label_detection(image3).png)

### Text and Label Detection

![alt text](<images/Label and Text_detection(image4).png>)