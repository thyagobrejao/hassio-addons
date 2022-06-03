from flask import Flask, render_template
import os

path = '/config/djtec'

# Check whether the specified path exists or not
isExist = os.path.exists(path)

if not isExist:

  # Create a new directory because it does not exist
  os.makedirs(path)

app = Flask(__name__)


@app.route("/")
def hello_world():
    file = open(path + '/cacilda.txt', 'a+')
    file.write("Woops! I have deleted the content!")
    file.close()
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
