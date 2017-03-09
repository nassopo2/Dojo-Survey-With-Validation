from flask import Flask , render_template, request, redirect,  flash, session

app=Flask(__name__)
app.secret_key="secret_key"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print"Got post info"

    return redirect('/')

@app.route ('/result', methods=['POST'])
def result():
    name=request.form['name']
    selected_language= request.form['FavoriteLanguage']
    location=request.form['Dojolocation']
    comment=request.form['description']
    print comment
    if len(request.form['name']) <1:
        flash('Name can not be empty')
        return redirect('/')
    elif len(request.form['description']) <1:
        flash('You need to add a comment')
        return redirect('/')
    elif len (request.form['description']) >=121:
        flash('Comment is larger than 120 characters')
        return redirect('/')
    return render_template("result.html", language=selected_language, location=location, name=name, comment=comment)
#@app.route('/reset, methods=['POST', 'get'])
#def reset():
    #sesion.pop('Your Name', None)
    #session.pop('Dojo Location',None)
    #session.pop('Favorite Language' None)
    #return render_template("/")



app.run(debug=True)
