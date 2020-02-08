import os

import numpy as np
from PIL import Image
import requests
import json

with open("coco_label_map.json", "r") as f:
	label_map = json.load(f)

# print(label_map)

od_url = "http://coco_model:8501/v1/models/coco_model:predict"


def predict_image(img):
	# img = Image.open(io.BytesIO(image_data))
	if img.mode in ('RGBA', 'LA') or (img.mode == 'P' or 'transparency' in img.info):
		img = img.convert('RGB')

	image_array = np.array(img).astype(np.uint8)
	payload = {"instances": [image_array.tolist()]}
	res = requests.post(od_url, json=payload)
	response = res.json()["predictions"][0]
	detection_scores = response["detection_scores"]
	detection_classes = response["detection_classes"]

	results = []
	for score, c in zip(detection_scores, detection_classes):
		if score > 0.50:
			print(score, c)
			results.append((label_map[str(int(c))]["display_name"], score))

	return results
