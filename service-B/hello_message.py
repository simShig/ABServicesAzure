from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_microsoft():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Hello Service</title>
        </head>
        <body>
            <h1>Hello Microsoft!</h1>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
