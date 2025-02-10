from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Initialize the Flask application
app = Flask(__name__)

CORS(app)

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    try:
        # Get the message from the POST request
        message = request.json.get("message")

        # Load documents and create the index
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()
        
        response = query_engine.query(message)
        
        # Check if a valid response was received
        if  str(response):
            return jsonify({"response":  str(response)})
        else:
            return jsonify({"error": "Failed to generate a response."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)