from flask import Flask, request, make_response, redirect, session

app = Flask(__name__)
counter = 1


@app.route('/api', methods=['GET', 'POST'])
def Count():
    global counter
    if request.method == 'POST':
        counter = counter + 1
    return str(counter)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
