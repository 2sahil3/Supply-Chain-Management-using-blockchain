import base64
import time
from flask import *
import sqlalchemy
from flask_login import LoginManager
from interface import *
# from interface import signer_account
from models import db, Users, PendingRequests
from index import index
from login import login
from logout import logout
from register import register
from home import home
import io
import qrcode


# initialize variables required in interface file...comment the function call while testing only flask and web2 interface things
# interfaceInit()

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


# manufacturer interface starts
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
    manufacturer_details = Users.query.filter_by(id=manufacturer_id).first()
    print(manufacturer_details)

    return render_template('manufacturer.html')


@app.route('/manufacturer/createProduct', methods=['GET', 'POST'])
def create_product_page():
    if request.method == "POST":
        timeStamp = str(time.time())
        requestId = request.args.get('req_id')
        requestData = PendingRequests.query.filter_by(req_id=requestId).first()
        itemName = requestData.productName
        mfgDate = request.form["manufacturer-date"]
        expiryDate = request.form["expiry-date"]
        batchNo = request.form["batch-number"]
        numberUnits = requestData.numOfItem
        userId = session['id']
        user = Users.query.filter_by(id=userId).first()

        create_product(
            timeStamp=timeStamp,
            itemName=itemName,
            mfgDate=mfgDate,
            expiryDate=expiryDate,
            batchNo=batchNo,
            numberUnits=numberUnits,
            history="atharva apni servicing karva chuka hai",
            par=-1,
            user_address=user.web3Address
        )

        pid = getLastProductID(user.web3Address)
        db.session.delete(requestData)
        db.session.commit()
        return render_template('success.html', submitted=True, p_id=pid)

    return render_template('create_product.html', submitted=False)


@app.route('/manufacturer/qrViewer/<id>', methods=['GET', 'POST'])
def showQR(id):
    print("showQrCalled")
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(id)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    img_html_base64 = base64.b64encode(img_bytes.getvalue()).decode()

    return f'<html><body><img src="data:image/png;base64,{img_html_base64}" alt="QR Code"></body></html>'


@app.route('/manufacturer/requests', methods=['GET', 'POST'])
def requests():
    if 'id' in session:
        manufacturer_id = session['id']
        pending_req = PendingRequests.query.filter_by(
            to_id=manufacturer_id).all()
        return render_template('showRequests.html', requests=pending_req)

    else:
        return "Id not found "


@app.route('/manufacturer/listProducts', methods=['GET', 'POST'])
def list_products():
    product_data = getAllProducts()
    print(product_data)
    return render_template('listof_products.html', product_data=product_data)

# manufacturer interface ends

# Distributor interface starts


@app.route('/distributor')
def distributorMainPage():
    return render_template('distributor.html')


@app.route('/distributor/makerequest', methods=['GET', 'POST'])
def makeRequest():
    manufacturers = Users.query.filter_by(userType='manufacturer').all()
    if request.method == "POST":

        itemName = request.form["item-name"]
        manufacturer_id = int(request.form.get('manufacturer_id'))
        additional_message = request.form["additional_message"]
        numOfUnits = request.form["number-units"]

        try:
            user = Users.query.filter_by(id=session['id']).first()
            new_request = PendingRequests(
                req_from=user.username,
                productName=itemName,
                numOfItem=numOfUnits,
                to_id=manufacturer_id,
                web3Address_from=user.web3Address,
                message=additional_message
            )
            db.session.add(new_request)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            print("error")

    return render_template('make_request.html', manufacturers=manufacturers)


@app.route('/distributor/pendingRequests')
def pendingRequest():
    dist_id = session['id']
    pending_req = PendingRequests.query.filter_by(to_id=dist_id).all()
    return render_template('showRequests.html', requests=pending_req)


@app.route('/distributor/inventory', methods=['GET', 'POST'])
def showInventory():
    print("distributor inventory page called")


if __name__ == '__main__':
    app.run(port=3000, debug=True)
