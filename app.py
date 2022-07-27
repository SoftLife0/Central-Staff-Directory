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
    image = db.Column(db.String() )
    identification = db.Column(db.String() )
    email =db.Column(db.String() )
    password = db.Column(db.String())
    department =  db.Column(db.String())
    phone = db.Column(db.String() )
    
    def __repr__(self):
        return f"Item('{self.name}', '{self.category}', )"


@app.route('/',methods=['GET','POST'])
def home():
    form = RegistrationForm()
    if request.method=='POST':
        # Handle POST Request here
        new_item = Contacts(name = form.name.data, phone=form.phone.data, password = form.password.data)
        db.session.add(new_item)
        db.session.commit()

        print(form.name.data)
        return render_template('index.html',form=form)
    return render_template('index.html', form = form)
@app.route('/alllcontacts')
def allcontacts():
    allcontacts= Contacts.query.all()
    print(allcontacts)
    return render_template('allcontacts',allcontacts=allcontacts)   


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
