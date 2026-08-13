# Northstar Retail Order Center

A self-service order tracking and management system for Northstar Retail customers.

## Features

- **Order Lookup**: Search for orders by Order ID and email address
- **Order Status Tracking**: View real-time order status and delivery information
- **Return Management**: Track return requests and refund status
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Customer Support**: Easy access to support team contact information

## Project Structure

```
├── app.py              # Flask backend application
├── index.html          # Main HTML interface
├── style.css           # Styling and layout
├── script.js           # Frontend JavaScript functionality
├── orders.json         # Sample order data
├── returns.json        # Sample return data
└── README.md           # This file
```

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Data**: JSON

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
```bash
git clone https://github.com/debbieruss-hub/northstar-dashboard.git
cd northstar-dashboard
```

2. Install dependencies:
```bash
pip install flask
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## API Endpoints

### Get Order Information
```
GET /api/order/<order_id>
```

### Get Return Information
```
GET /api/return/<return_id>
```

## Usage

1. Enter your Order ID and email address in the search form
2. Click "Check Order Status" to retrieve order information
3. View your order details, delivery status, and return options
4. Contact support if you need additional assistance

## File Descriptions

- **app.py**: Flask server that serves the static files and provides API endpoints for order and return data
- **index.html**: Main HTML structure with header, hero section, search form, and results display
- **style.css**: Complete styling for a professional retail interface
- **script.js**: JavaScript logic for form handling and API requests
- **orders.json**: Sample order data for testing
- **returns.json**: Sample return data for testing

## License

© 2026 Northstar Retail Co. All rights reserved.

## Support

For customer support, please visit the application and click "Contact Support" in the help section.
