from flask import Flask, request
app = Flask(__name__)
app.debug = True   # need this for autoreload as and stack trace


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route('/hello')
def hello_form():
    if 'first' in request.args:
        return sendPage(request.args['first'], request.args['last'])
    else:
        return sendForm()

def sendForm():
    return '''
    <html>
      <body>
          <form method='get'>
              <label for="myname">Enter Your Name</label>
              <input id="myname" type="text" name="first" value="Foo" />
              <input id="myname' type="text" name="last" value="Bar" />
              <input type="submit">
          </form>
      </body>
    </html>
    '''

def sendPage(first, last):
    return '''
    <html>
      <body>
        <h1>Hello {0} {1}</h1>
      </body>
    </html>
    '''.format(first,last)

if __name__ == '__main__':
   app.run()
