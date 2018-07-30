from flask import Flask, request

app = Flask(__name__)

count = 0

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
       global count
       count += 1
    return "Hello World!!!"

@app.route("/counter")
def counter():
    return 'Post requests: %s' % str(count)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
