from flask import Flask, request, jsonify, render_template
import replicate
import os

app = Flask(__name__)

# Set your Replicate API key
os.environ["REPLICATE_API_TOKEN"] = 'r8_U73XchgXHaxTZrh5jrdGqnV4WZEKiqW2z2Nyx'  # Replace with your actual API key

MODEL_ID = 'bingbangboom-lab/flux-dreamscape'
MODEL_VERSION = 'b761fa16918356ee07f31fad9b0d41d8919b9ff08f999e2d298a5a35b672f47e'

# Serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-model', methods=['POST'])
def run_model():
    input_data = request.json

    try:
        # Run the model using the replicate library
        output = replicate.run(
            f"{MODEL_ID}:{MODEL_VERSION}",
            input=input_data
        )
        return jsonify({'output': output})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
