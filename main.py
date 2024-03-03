from flask import Flask, render_template, send_file, request, flash
from email.message import EmailMessage
import ssl
import os
import smtplib

app = Flask(__name__)

app.secret_key = "IDONTKNOW"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email_from = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        email_receiver = 'jhonanthonyjimenez568@gmail.com'
        email_password = 'gkip nqmh wkit agmb'

        contact_email = EmailMessage()
        contact_email["From"] = email_from
        contact_email["To"] = email_receiver
        contact_email["Subject"] = subject
        contact_email.set_content(f"Name: {name}\nPhone: {phone}\nMessage: {message}")

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_receiver, email_password)
            smtp.send_message(contact_email)
        flash(f"Thank so much for {name} contanct me I'll be more than glad to reach back a'")
        return "Email sent successfully!"

@app.route('/download_cv')
def download_cv():
    pdf_filename = "curriculum.pdf"
    pdf_path = os.path.join(app.root_path, 'static', pdf_filename)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

