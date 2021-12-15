from flask import Flask, request
from caesar import rotate_string
app = Flask('app')
app.config['DEBUG'] = True

#Creating a form with a post method
form = """
<!doctype html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/" method="POST">
        <label for="rot">Rotate by:
        <input type="text" name="rot" value="0" />
        <p class="error"></p>
        </label>
        <textarea name="text">{0}</textarea>
        <input type="submit" value="Encrypt Text" />
      </form>
    </body>
</html>
"""
#Rendering the form on this path/route
@app.route('/')
def hello_world():
  return form.format("")

#Adding new variables for requests and a method
@app.route('/', methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    res = rotate_string(text, rot)
    return form.format(res)

app.run()