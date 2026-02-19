from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # libera requisições do frontend

posts = []

@app.route('/api/posts', methods=['GET', 'POST'])
def handle_posts():
    global posts
    if request.method == 'GET':
        return jsonify(posts)

    if request.method == 'POST':
        data = request.get_json()
        text = data.get("text", "")
        if text:
            post = {"id": len(posts)+1, "text": text}
            posts.append(post)
            return jsonify(post)
        return jsonify({"error": "Texto vazio"}), 400

    return jsonify({"error": "Método não permitido"}), 405

