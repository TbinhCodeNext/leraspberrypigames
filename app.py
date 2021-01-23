from flask import Flask, render_template
import raspimoneats
#import catchem

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/raspieats')

def raspieatsgame():
    my_game = raspimoneats.Game()
    my_game.run()
    return "You chose the raspieats path."

# @app.route('/catchem')

# def catchemgame():
#     return "You chose the catchem path."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')