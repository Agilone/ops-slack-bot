from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/slack/events', methods=['POST'])
def slack_events():
    data = request.get_json()
    if data and data.get("type") == "url_verification":
        return make_response(data.get("challenge"), 200, {"content_type": "text/plain"})
    return make_response("", 200)

if __name__ == '__main__':
    app.run(port=5000)