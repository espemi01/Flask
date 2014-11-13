from flask import Flask, request
import random, string
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_form():
    if 'max' in request.args:
        return send(request.args['small'], request.args['large'], request.args['max'])
    else:
        return select()

def select():
    return '''
        <html>
          <body>
              <h1>Passoword Generator</h1>
              <form method='get'>
                  <hr>
                  <h4><label for="size">Select the size of your password</label></h4>
                  <p>Smallest: (1-5)</p><input id="size" type="range" name="small" min=1 max=5 value=4 />
                  <p>Largest: (5-10)</p><input id="size" type="range" name="large" min=5 max=10 value=8 />
                  <p>Total Length: (20 - 40)</p><input id="size" type="range" name="max" min=20 max=40 value=30 />
                  <hr>
                  <h4><label for="params">Select the parameters for your passwords</label></h4>
                  <p>Capitalize a random word: </p><input id="params" type="checkbox" name="cap" />
                  <p>Substitute: (3 == E...$ == S...etc)</p>First<input id="params" type="checkbox" name="first" />Second<input id="params" type="checkbox" name="second" />Third<input id="params" type="checkbox" name="third" />Fourth<input id="params" type="checkbox" name="fourth" />
                  <hr>
                  <input type="submit">
              </form>
          </body>
        </html>
        '''
def getDB():
    myFile = open('wordLST.txt', 'r')
    
    #Build an array of words to chose from
    words = []
    pw = []
    for i in myFile:
        line = i.strip()
        words.append(line)
        
    return words

def output(w1,w2,w3,w4):
    pw = w1 + ' ' + w2 + ' ' + w3 + ' ' + w4
        
    return '''
    <html>
      <body>
        <h1>Password Generator</h1>
        <p>1st Word: {0}</p>
        <p>2nd Word: {1}</p>
        <p>3rd Word: {2}</p>
        <p>4th Word: {3}</p>
        <p>Your Full Password: {4}</p>
      </body>
    </html>
    '''.format(w1,w2,w3,w4,pw)

def send(Low, High, Max):
    Low = int(Low)
    High = int(High)
    Max = int(Max)
    words = getDB()
    pw = []
    
    tLen = 0
    
    w1 = getWord(Low, High, Max, tLen, words)
    w2 = getWord(Low, High, Max, tLen, words)
    w3 = getWord(Low, High, Max, tLen, words)
    w4 = getWord(Low, High, Max, tLen, words)
    
    if 'first' in request.args:
        c1 = request.args['first']
        if c1 == 'on':
            w1 = swap(w1)
    if 'second' in request.args:
        c2 = request.args['second']
        if c2 == 'on':
            w2 = swap(w2)
    if 'third' in request.args:
        c3 = request.args['third']
        if c3 == 'on':
            w3 = swap(w3)
    if 'fourth' in request.args:
        c4 = request.args['fourth']
        if c4 == 'on':
            w4 = swap(w4)
    
    wl = [w1,w2,w3,w4]
    
    if 'cap' in request.args:
        s = request.args['cap']
        if s == 'on':
            word = random.choice(wl)
            Word = caps(word)
            if word == w1:
                w1 = Word
            elif word == w2:
                w2 = Word
            elif word == w3:
                w3 = Word
            elif word == w4:
                w4 = Word
            
            
            
    return output(w1,w2,w3,w4)

def getWord(Low, High, Max, tLen, words):
    go = False
    
    while go is False:
        index = random.randint(0,5012)
        word = words[index]
        
        if len(word) < High:
            if len(word) > Low:
                aLen = tLen + len(word)
                if aLen < Max:
                    tLen += len(word)
                    go = True
    return word

def caps(word):
    return word.upper()

def swap(word):
    lst = ['A','I','E','O','L']
    slst = ['@','!','3','0','1']
    
    result = ''
    
    for letter in word:
        LETTER = letter.upper()
        
        if LETTER in lst:
                for n in range(0,len(lst)-1):
                    if LETTER == lst[n]:
                        LETTER = slst[n]
                        result += LETTER
        else:
            result += letter
                
    return result

def sendPW(a,b,c,d,e,f,g,h,i,j):
    
    return '''
    <html>
    <head>
    </head>
        <body>
            <h1>Password Generator</h1>
            <p>1: {a} </p>
            <p>2: {b} </p>
            <p>3: {c} </p>
            <p>4: {d} </p>
            <p>5: {e} </p>
            <p>6: {f} </p>
            <p>7: {g} </p>
            <p>8: {h} </p>
            <p>9: {i} </p>
            <p>10: {j} </p>
    '''

if __name__ == '__main__':
   app.run()
