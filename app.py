from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/where-am-i')
def where_am_i():
    return render_template('where_am_i.html')

@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(os.path.join(app.root_path, 'media'), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

