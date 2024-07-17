import html
from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def hi() -> str:
 return "hi"    
  
@app.route('/convert',  methods=['GET', 'POST'])  
def convert(): 
    celsius = input()
    fahrenheit = 9/5 * int(celsius) + 32
    return fahrenheit

@app.route('/w')
def w_page() -> 'html':
    return render_template('w.html')

if __name__ == "__main__":
    app.run(debug=True)
