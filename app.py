from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy 
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), nullable=False)
    identification = db.Column(db.String(), nullable=False)
    email =db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    
    def __repr__(self):
        return f"Item('{self.name}', '{self.category}', )"


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
