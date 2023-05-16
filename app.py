from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')


# 공통 페이지

@app.route('/selectlocker')
def selectlocker():
    usertype = request.args.get('usertype', default = '', type = str)
    print(usertype)
    if   usertype == "sell":
        return render_template('selectlocker.html', data = usertype)
    elif usertype ==  "buy":
        return render_template('selectlocker.html', data = usertype)
    else:
        return render_template('main.html', error = "잘못된 접근입니다(사용자 타입 누락)")

@app.route('/passwd')
def passwd():
    usertype = request.args.get('usertype', default = '', type = str)
    if   usertype == "sell":
        return render_template('passwd.html', data = usertype)
    elif usertype ==  "buy":
        return render_template('passwd.html', data = usertype)
    else:
        return render_template('main.html', error = "잘못된 접근입니다(사용자 타입 누락)")


# 구매자 페이지
@app.route('/preview/<product_id>')
def preview(product_id):
    productId = product_id
    return render_template('preview.html', productId = productId)

@app.route('/payment')
def payment():
    return render_template('payment.html')


# 판매자 페이지
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')




app.run(host='localhost', port = 80)