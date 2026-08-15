from flask import Flask,jsonify,request,send_from_directory
import json

app = Flask(__name__,static_folder='.', static_url_path='')

#load the  mock data
with open('orders.json') as f:
    orders = json.load(f)
with open('returns.json') as f:
    returns = json.load(f)

# --Dashboard API EndPoints --

@app.route("/api/order/<order_id>")
def get_order(order_id):
    for order in orders:
        if order['id'] == order_id:
            # Attach refund data automatically if  the order has a return and exists
            refund_info = None
            for ret in returns:
                if ret['order_id'] == order_id:
                    refund_info = ret
            order['refund'] = refund_info
            return jsonify(order), 200
                    
    return jsonify({"error": "Order  ID not found"}), 404

@app.route("/api/return/<order_id>")
def get_return(order_id):
    for ret in returns:
        if ret['order_id'] == order_id:
            return jsonify(ret)
    return jsonify({"error": "No returns found for this order"}), 404

# SERVE THE  DASHBOARD
@app.route('/')
def dashboard():
    return send_from_directory('.', 'index.html')

# SERVE STATIC FILES (CSS/JS)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=True,port=5000)