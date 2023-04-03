from flask import Flask
from flask import *
import time
from interface import *

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    return 'This will be our home'

@app.route('/manufacturer', methods=['GET', 'POST'])
def manufacturer_page():
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
            history="sanskar is intelligent",
            par=-1,
            user_address=signer_account
        )

        return render_template('create_product.html', submitted=True)

    return render_template('create_product.html', submitted=False)


@app.route('/manufacturer/listProducts', methods=['GET', 'POST'])
def list_products():
    product_data = getAllProducts()
    print(product_data)
    return render_template('listof_products.html', product_data=product_data)


if __name__ == '__main__':
    app.run(debug=True)