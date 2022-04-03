import warnings
warnings.filterwarnings("ignore")
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from flask import Flask, jsonify, request, make_response
import argparse
import uuid
import json
import time
from tqdm import tqdm
from deepface import DeepFace
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Please use /analyze api route for analyzing your image</h1>'

@app.route('/analyze', methods=['POST'])
def analyze():

	tic = time.time()
	req = request.get_json()
	# trx_id = uuid.uuid4()
	resp_obj = analyzeWrapper(req) 
	toc = time.time()
	resp_obj["seconds"] = toc-tic
	return resp_obj, 200

def analyzeWrapper(req):
	resp_obj = jsonify({'success': False})
	instances = []
	if "img" in list(req.keys()):
		raw_content = req["img"] #list
		for item in raw_content: #item is in type of dict
			instances.append(item)
	if len(instances) == 0:
		return jsonify({'success': False, 'error': 'you must pass at least one img object in your request'}), 205
	print("Analyzing ", len(instances)," instances")

	detector_backend = 'mediapipe'
	actions= ['age', 'gender']

	if "actions" in list(req.keys()):
		actions = req["actions"]
	if "detector_backend" in list(req.keys()):
		detector_backend = req["detector_backend"]

	try:
		resp_obj = DeepFace.analyze(instances, actions = actions, detector_backend=detector_backend)
	except Exception as err:
		print("Exception: ", str(err))
		return jsonify({'success': False, 'error': str(err)}), 205
	return resp_obj

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'-p', '--port',
		type=int,
		default=5100,
		help='Port of serving api')
	args = parser.parse_args()
	app.run(host='0.0.0.0',debug=True,  port=args.port)
