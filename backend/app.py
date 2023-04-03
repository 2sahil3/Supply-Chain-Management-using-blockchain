import time
from flask import *
import sqlalchemy
from flask_login import LoginManager
from interface import *
from models import db, Users, PendingRequests
from index import index
from login import login
from logout import logout
from register import register
from home import home

#initialize variables required in interface file...comment the function call while testing only flask and web2 interface things
interfaceInit()

app = Flask(__name__, template_folder='../frontend')

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'

login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)

app.app_context().push()

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(home)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/show')
def products():
    allTodo = Users.query.all()
    print(allTodo)
    return 'this is products page'

@app.route('/manufacturer', methods=['GET', 'POST'])
def manufacturer_page():

    manufacturer_id = request.args.get('id')
    # print(type(manufacturer_id))
    # print('id = ' + str(manufacturer_id))
    # id type = <class 'builtin_function_or_method'>
    manufacturer_details = Users.query.filter_by(id = manufacturer_id).first()
    print(manufacturer_details)

    return render_template('manufacturer.html')

@app.route('/manufacturer/createProduct', methods=['GET', 'POST'])
def create_product_page():
    if request.method == "POST":
        timeStamp = str(time.time())
        itemName = request.form["item-name"]
        mfgDate = request.form["manufacturer-date"]
        expiryDate = request.form["expiry-date"]
        batchNo = request.form["batch-number"]
        numberUnits = int(request.form["number-units"])

        create_product(
            timeStamp=timeStamp,
            itemName=itemName,
            mfgDate=mfgDate,
            expiryDate=expiryDate,
            batchNo=batchNo,
            numberUnits=numberUnits,
            history="Sanskar is built different",
            par=-1,
            user_address=signer_account
        )

        return render_template('create_product.html', submitted=True)

    return render_template('create_product.html', submitted=False)


@app.route('/manufacturer/requests',methods=['GET', 'POST'])
def requests():
    if 'id' in session:
        manufacturer_id = session['id']
        pending_req = PendingRequests.query.filter_by(to_id=manufacturer_id).all()
        print("____________")
        print(pending_req)
        print("_______________")
        return render_template('showRequests.html',requests=pending_req)

    else:
        return "Id not found "
@app.route('/distributor',methods=['GET', 'POST'])
def makeRequest():
    if request.method == "POST":
        
        itemName = request.form["item-name"]
        manufacturer_id = request.form["manufacturer_id"]
        additional_message = request.form["additional_message"]
        numOfUnits = request.form["number-units"]

        try:
                    user = Users.query.filter_by(id=session['id']).first()
                    new_request = PendingRequests(
                        req_from  = user.username,
                        productName = itemName ,
                        numOfItem = numOfUnits,
                        to_id = manufacturer_id,
                        web3Address_from = user.web3Address,
                        message = additional_message
                    )
                    db.session.add(new_request)
                    db.session.commit()
        except sqlalchemy.exc.IntegrityError:
             print("error")
    print(PendingRequests.query.all())
    return render_template('make_request.html')


@app.route('/manufacturer/listProducts', methods=['GET', 'POST'])
def list_products():
    product_data = getAllProducts()
    print(product_data)
    return render_template('listof_products.html', product_data=product_data)



if __name__ == '__main__':
    app.run( port=3000, debug=True)
