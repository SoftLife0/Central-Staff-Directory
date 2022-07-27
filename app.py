import email
from email.policy import default
from multiprocessing import reduction
from traceback import format_stack
from flask import Flask,redirect,url_for,render_template,request
from forms import *
from flask_sqlalchemy import SQLAlchemy 
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY']= 'ADKADKFJ'
db = SQLAlchemy(app)

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String() )
    image = db.Column(db.String(), default="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80" )
    identification = db.Column(db.String())
    email =db.Column(db.String() )
    password = db.Column(db.String(),default = "Central@123")
    department =  db.Column(db.String())
    phone = db.Column(db.String() )
    
    def __repr__(self):
        return f"Item('{self.name}', '{self.phone}', )"


@app.route('/',methods=['GET','POST'])
def home():
    form = RegistrationForm()
    if request.method=='POST':
        # Handle POST Request here
        new_item = Contacts(name = form.name.data, phone=form.phone.data, email= form.email.data, identification  = form.identification.data , department = form.department.data)
        db.session.add(new_item)
        db.session.commit()

        print(form.name.data)
        return redirect(url_for('allcontacts'))
    return render_template('index.html', form = form)
@app.route('/allcontacts')
def allcontacts():
    allcontacts= Contacts.query.all()
    print(allcontacts)
    return render_template('allcontacts.html',allcontacts=allcontacts)   


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
