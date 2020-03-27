from flask import Flask
from flask_cors import CORS
from email_utils import send_msg
from database import get_user_info, get_photo_from_db
from verifier import recognize_face

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def root():
    return 'The App works';

@app.route('/<email>/<transaction_id>')
def temp(email, transaction_id):
    get_photo_from_db()
    user_id, phone_number = get_user_info(email)

    if get_photo_from_db:
        confidence, label = recognize_face()
        print(f"Match: {confidence}, DB OwnerMatched Label:{label}")
        if user_id == label and confidence > 70:
            send_msg(email, phone_number, transaction_id)
            return "Message Sent"
        if confidence == 1000 and label == 0:
            return "no face detected"





if __name__ == '__main__':
    context = ('server.crt', 'server.key')
    app.run(host="0.0.0.0",debug=True, use_reloader=True, ssl_context=context)

