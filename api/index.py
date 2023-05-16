from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/email', methods=['POST'])
def send_email():
    data = request.get_json()
    
    # Extract data from the request
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')

    print(body)
    
    # Code to send the email using your preferred email service provider
    
    # Return a response
    response = {'message': 'Email sent successfully'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
