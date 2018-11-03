from flask import Flask, render_template, request, redirect, session
from random import randint

app = Flask(__name__)
app.secret_key = 'coolio'

def random_number_generator():
  random_number = randint(1, 100)
  return random_number

def clearGuess():
    if session.get('low'):
      session.pop('low')
    if session.get('high'):
      session.pop('high')
    if session.get('correct'):  
      session.pop('correct')




@app.route("/")
def index():
  lastGuess = request.args.get('lastGuess')

  if not lastGuess:
      clearGuess()    

  return render_template('index.html')

@app.route("/submit_guess", methods=['POST'])
def click_counter():
    clearGuess()

    session['user_guess'] = request.form['guess']
    
    if not 'actual_number' in session:
      session['actual_number'] = random_number_generator()

    if int(session['user_guess']) < session['actual_number']:
      session['low'] = "Your guess is low"
      
      

    elif int(session['user_guess']) > session['actual_number']:
      session['high'] = "Your guess is too high"
      
      

    else:
      session['correct'] = f"{session['user_guess']} is the right number!"
      
    lastGuess = session.pop('user_guess')

    return redirect("/?lastGuess={}".format(lastGuess))

@app.route("/play_again", methods=['POST'])
def reset_page():
  print('click')
  session.clear()
  return redirect('/')

if __name__ =='__main__':
    app.run(debug=True)