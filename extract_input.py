from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    # do something with the data, like store it in a database or file
    print("name = ", name)
    print("email = ", email)
    return 'Form submitted successfully'
