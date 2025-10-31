# Image Analyzer 

This is a Flask based Image analyzer built using Google Cloud Vision API. It analyzes
uploaded image and returns Labels, Likelihood, Text, and properties of the image.
If the there's text on the image then it will be translated into the targeted language. 

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

* body_translation: 
              
                "q" : for the text to be translated

                "target": language in which extracted text will be translated

                "format": format of the source text

## Technologies used:

1. Flask
2. Google cloud vision API
3. Translation API

### Translation

![alt text](images/Translation(image11).png)

### Face detection
        
![alt text](images/Face_detection(image9).png)

### Label Detection and Image properties

![alt text](images/Label_detection(image3).png)

### Text and Label Detection

![alt text](<images/Label and Text_detection(image4).png>)