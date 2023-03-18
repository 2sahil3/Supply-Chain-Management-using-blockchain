from flask import Flask
from flask import render_template, request
import time
from interface import create_product, get_product, last
app = Flask(__name__)


@app.route('/manufacturer', methods=['GET', 'POST'])
def manufacturer_page():
    if request.method == "POST":
        timeStamp = str(time.time())
        # itemName = request.form["item-name"]
        # mfgDate = request.form["manufacturer-date"]
        # expiryDate = request.form["expiry-date"]
        # batchNo = request.form["batch-number"]
        # numberUnits = int(request.form["number-units"])
        # print(ID)
        # ID += 1
        print(create_product(
            timeStamp=timeStamp,
            itemName="item",
            mfgDate=timeStamp,
            expiryDate=timeStamp,
            batchNo="256",
            numberUnits=123
        ))
        print(last())

        return render_template('manufacturer.html', submitted=True)

    return render_template('manufacturer.html', submitted=False)


if __name__ == '__main__':
    app.run(debug=True)
