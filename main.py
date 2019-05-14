from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':

        name = request.args.get('Name')
        place = request.args.get('Place')

        return '''GET Method 
        Name = {}
        Place = {}'''.format(name,place)

    elif request.method == 'POST':

        name = request.form.get('Name')
        place = request.form.get('Place')

        return '''POST Method 
                Name = {}
                Place = {}'''.format(name, place)

@app.route('/form',methods =['GET'])
def form():
    return render_template('display.html')

if __name__ == '__main__':
    app.run(port=2000,debug=True)