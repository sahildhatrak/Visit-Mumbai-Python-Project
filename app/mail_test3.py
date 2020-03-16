from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from forms import LoginForm
import os


app =Flask(__name__,static_url_path='/static')
mail=Mail(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'visit.mumbaii@gmail.com'
app.config['MAIL_PASSWORD'] = 'gjkldkktaljegkdp'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	msg = Message('Reservation Confirmation', sender = 'Visit Mumbai', recipients = [form.email.data])
        
    	msg.html = "<h2>Dear {},</h2><br><h2>Thank you for visiting our website, VisitMumbai. We are pleased to inform you that we have reserved a booking in your desired place of stay. We hope you have a good time.</h2><br><h2>Please feel free to contact us incase of any queries.</h2><br><h2>Mail us at : visitmumbai@gmail.com</h2><br><h2>Call us at : 1800-702-1224 </h2><br><br><h3>Regards<br>Visit Mumbai</h3>".format(form.name.data)
    	mail.send(msg)
    	flash('Email successfully sent to {} '.format(form.email.data))
    	return redirect(url_for('login'))

    return render_template('reservation.html', title='Sign In', form=form)



@app.route("/")
def home():
	return render_template('mumbai.html')

@app.route('/mumbai', methods=['GET','POST'])
def mumbai():
    if request.method=='POST':
        return redirect(url_for('mumbai'))
    return render_template('mumbai.html')

@app.route('/bandra', methods=['GET','POST'])
def bandra():
    if request.method=='POST':
        return redirect(url_for('mumbai'))
    return render_template('bandra.html')

@app.route('/colaba', methods=['GET','POST'])
def colaba():
    if request.method=='POST':
        return redirect(url_for('mumbai'))
    return render_template('colaba.html')

@app.route('/navi', methods=['GET','POST'])
def navi():
    if request.method=='POST':
        return redirect(url_for('mumbai'))
    return render_template('navi.html')

@app.route('/thane', methods=['GET','POST'])
def thane():
    if request.method=='POST':
        return redirect(url_for('mumbai'))
    return render_template('thane.html')

@app.route('/powai', methods=['GET','POST'])
def powai():
    if request.method=='POST':
        return redirect(url_for('mumbai'))
    return render_template('powai.html')

@app.route('/food', methods=['GET','POST'])
def food():
    if request.method=='POST':
        return redirect(url_for('mumbai'))
    return render_template('food.html')

@app.route('/picnic', methods=['GET','POST'])
def picnic():
    if request.method=='POST':
        return redirect(url_for('mumbai'))
    return render_template('picnic.html')

@app.route('/shopping', methods=['GET','POST'])
def shopping():
    if request.method=='POST':
        return redirect(url_for('mumbai'))
    return render_template('shopping.html')

@app.route('/about_mumbai', methods=['GET','POST'])
def about_mumbai():
    if request.method=='POST':
        return redirect(url_for('mumbai'))
    return render_template('about_mumbai.html')

@app.route('/history', methods=['GET','POST'])
def history():
    if request.method=='POST':
        return redirect(url_for('mumbai'))
    return render_template('history.html')

@app.route('/reservation', methods=['GET','POST'])
def reservation():
    if request.method=='POST':
        return redirect(url_for('mumbai'))
    return render_template('reservation.html')


if __name__ == '__main__':
   app.run(debug = True)
