from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder='.')

# Load data
def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return {}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    if os.path.isfile(filename):
        return send_from_directory('.', filename)
    return {'error': 'Not found'}, 404

@app.route('/api/order/<order_id>', methods=['GET'])
def get_order(order_id):
    orders = load_json('orders.json')
    if order_id in orders:
        return jsonify(orders[order_id])
    return jsonify({'error': 'Order not found'}), 404

@app.route('/api/return/<return_id>', methods=['GET'])
def get_return(return_id):
    returns = load_json('returns.json')
    if return_id in returns:
        return jsonify(returns[return_id])
    return jsonify({'error': 'Return not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
