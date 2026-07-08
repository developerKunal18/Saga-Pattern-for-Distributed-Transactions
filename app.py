from flask import Flask, jsonify
import random

app = Flask(__name__)

# ---------- Services ----------
def create_order():
    return True

def process_payment():
    return True

def reserve_inventory():
    return random.choice([True, False])

# ---------- Compensation ----------
def refund_payment():
    print("Payment Refunded")

def cancel_order():
    print("Order Cancelled")

# ---------- Saga ----------
@app.route("/checkout")
def checkout():

    if not create_order():
        return jsonify({
            "message": "Order Failed"
        })

    if not process_payment():
        cancel_order()

        return jsonify({
            "message": "Payment Failed"
        })

    if not reserve_inventory():

        refund_payment()
        cancel_order()

        return jsonify({
            "message": "Inventory Unavailable",
            "status": "Rollback Completed"
        })

    return jsonify({
        "message": "Order Completed Successfully"
    })

# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(debug=True)
