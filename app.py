from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')


# 공통 완료 
@app.route('/payment_completed/')
def payment_completed():

    return render_template('payment_completed.html')


@app.route('/payment_inprogess/')
def payment_inprogess():
    # http://59.26.59.60:5000/payment_inprogess?productId=1&pg_token=b09338b8b5feea68a188
    productId = request.args.get('productId')
    pg_token  = request.args.get('pg_token')
    return render_template('payment_inprogess.html',productId=productId, data = pg_token)


@app.route('/payment/')
def payment_root():

    pg_token = request.args.get('pg_token', default = '', type = str)
    print(pg_token)

    return render_template('payment_completed.html', data = pg_token)

if __name__ == "__main__":
    app.run(host="192.168.0.106", port=5000)