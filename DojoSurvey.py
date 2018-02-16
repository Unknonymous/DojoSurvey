from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template('survey.html', methods=["POST"])

'''@app.route('/carry', methods=["POST"])
def carry():
    if request.method == "POST":
        name = request.form['name']
        where = request.form['where']
        language = request.form['what']
        comment = request.form['comments']
        redirect('/result.html')
    else:
        redirect('/')'''
@app.route('/result', methods=["POST"])
def result():
    name = request.form['name']
    where = request.form['where']
    language = request.form['what']
    comment = request.form['comments']
    return render_template('/result.html', name=name, where=where, language=language, comment=comment)
    '''return render_template('/result.html')'''

app.run(debug=True)