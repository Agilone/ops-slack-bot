from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/slack/events', methods=['POST'])
def slack_events():
    data = request.get_json()
    # Handle Slack URL verification
    if data and data.get("type") == "url_verification":
        return make_response(data.get("challenge"), 200, {"content_type": "text/plain"})
    # Handle other Slack events here (expand this section as needed)
    return make_response("", 200)

if __name__ == '__main__':
    app.run(port=5000)