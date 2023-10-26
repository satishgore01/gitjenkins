from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    content = request.form.get('content')
    filename = request.form.get('filename')

    if content and filename:
        with open(f'{filename}.txt', 'w') as file:
            file.write(content)
        return redirect(url_for('success'))
    else:
        return "Please provide both content and filename."

@app.route('/success')
def success():
    return "File saved successfully!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
