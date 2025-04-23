from flask import Flask, request
from flask_restful import Resource
from models.image import Image
from models.db import db
import logging
from utils.faiss_index import search_embedding
from utils.clip_model import get_image_embedding
import os
import uuid

app = Flask(__name__)

class SearchImage(Resource):
    @app.route('/search', methods=['POST'])
    def post(self):
        if 'search_image' not in request.files:
            return {"data": "No image uploaded"}, 400

        try:
            file = request.files['search_image']
            filename = f"temp_{uuid.uuid4().hex}.jpg"

            filepath = os.path.join("static", "temp", filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            file.save(filepath)

            embedding = get_image_embedding(filepath)
            distances, indices = search_embedding(embedding, top_k=3)

            images = Image.query.order_by(Image.id).all()

            results = []
            for i, idx in enumerate(indices):
                if 0 <= idx < len(images):
                    image = images[idx]
                    confidence = round(float(1 - distances[i]), 4)
                    results.append({
                        "id": image.id,
                        "filename": image.filename,
                        "confidence": confidence
                    })

            os.remove(filepath)
            return ({"data": results}), 200

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return {"data": "Failed to process"}, 400