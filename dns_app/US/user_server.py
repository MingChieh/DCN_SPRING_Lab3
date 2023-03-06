from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def page_request():
    hostname = request.args["hostname"]
    fs_port = request.args["fs_port"]
    number = request.args["number"]
    as_ip = request.args["as_ip"]
    as_port = request.args["as_port"]
    return HELLO_HTML.format(hostname, fs_port, fib(number), as_ip, as_port)

HELLO_HTML = """
    <html><body>
        <h1> {0} {2} </h1>
        fib={2}.
        exist = {1}
    </body></html>"""

def fib(x):
    x = int(x)
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

