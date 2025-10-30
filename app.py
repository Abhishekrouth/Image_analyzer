from flask import Flask, jsonify, request, abort
import requests
import base64
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

@app.errorhandler(400)
def bad_request(e):
    return jsonify({
        "status": "error",
        "code": 400,
        "message": "Bad Request. Image file is missing."
    }), 400

@app.route("/image_analyzer", methods=["POST"])
def image_analyzer():
    if "image_file" not in request.files:
        abort(400)

    image_file = request.files["image_file"]
    image_content = base64.b64encode(image_file.read())
    img= image_content.decode("utf-8")

    url = f"https://vision.googleapis.com/v1/images:annotate?key={google_api_key}"

    body = {
        "requests": [
            {
                "image": {
                    "content": img
                    },
                "features": [
                    {
                        "type": "LABEL_DETECTION",
                        "maxResults": 1
                    },
                    {
                        "type": "TEXT_DETECTION",
                        "maxResults": 1
                    },
                    {
                        "type": "IMAGE_PROPERTIES",
                        "maxResults": 1
                    },
                    {
                        "type": "FACE_DETECTION",
                        "maxResults": 2
                    }
                    
                        ]
            }
        ]
    }
    response = requests.post(url, json=body)
    result = response.json()
    face = result["responses"][0].get("faceAnnotations",[])
    if face:
        exp1 = face[0]["joyLikelihood"]
        exp2 = face[0]["sorrowLikelihood"]
        exp3= face[0]["angerLikelihood"]
        exp4= face[0]["surpriseLikelihood"]
        return jsonify ({"Likelihoods:"  : {
                        "joyLikelihood": exp1,
                        "sorrowLikelihood": exp2,
                        "angerLikelihood": exp3,
                        "supriseLikelihood": exp4
                        }})
    else:
        labels = result["responses"][0].get("labelAnnotations",[])
        text = result["responses"][0].get("textAnnotations",[])
        img_prop= result["responses"][0].get("imagePropertiesAnnotation",[])
        if text:
            des = text[0]["description"]
        else:
            des = "No text detected"
        
        return jsonify({
            "Labels": labels,
            "text": des,
            "image_properties": img_prop
    })

if __name__ == "__main__":
    app.run(debug=True)
