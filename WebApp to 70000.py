import flask
from array import array
from itertools import count
import random


#Generate list with random unique numbers
lst = random.sample(range(0, 70000), 70000)

new_a = []
##order numbers
def read_f1():
    a = lst
    a = str(a)[1:-1]
    a = a.split(',')
    a = [int(i) for i in a]
    while a:
        min = a[0]
        for x in a:
            if x < min:
                min = x
        new_a.append(min)
        a.remove(min)
    with open("/tmp/f1.txt", mode = "w") as f1:
        f1.write(str(new_a))
        f1.close()
    #return new_b == (new_a)[1:-1]

read_f1()

app = flask.Flask(__name__)

@app.get("/")

def hello():
    """Return a friendly HTTP greeting."""
    with open("/tmp/f1.txt", 'r+') as filefinal:
        f = str(filefinal.read())
        filefinal.close()
    return f


if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)