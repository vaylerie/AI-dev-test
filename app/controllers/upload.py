from flask import Flask, request
from flask_restful import Resource
from models.image import Image
from models.db import db
import os
import logging
from utils.clip_model import get_image_embedding
from utils.faiss_index import add_embedding

app = Flask(__name__)
class UploadImage(Resource):
    @app.route('/upload', methods=['POST'])
    def post(self):
        if 'image' not in request.files:
            return {"data": "Failed to upload image"}, 400

        file = request.files['image']
        if file.filename == '':
            return {"data": "Failed to upload image"}, 400

        if file.filename.lower().endswith(('.png', '.jpg')):
            try:
                filepath = os.path.join('static/image/', file.filename)
                file.save(filepath)

                embedding = get_image_embedding(filepath)
                add_embedding(embedding)

                upload_image = Image(filename = file.filename,
                                     filepath = filepath)
                db.session.add(upload_image)
                db.session.commit()

                return {"data":
                            {"filepath": str(filepath)}
                        }, 200

            except Exception as e:
                logging.error(f"Error occurred: {e}")
                return {"data": "Failed to upload image"}, 400
        else:
            return {"data": "Failed to upload image. Please upload image with .png or .jpg extensions"}, 400