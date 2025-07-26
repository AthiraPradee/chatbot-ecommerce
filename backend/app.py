from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# 🔹 Load all Excel files
orders = pd.read_excel("orders.xlsx")      # file with Order ID
products = pd.read_excel("products.xlsx")  # file with Product
quantities = pd.read_excel("quantities.xlsx")  # file with Quantity

# 🔹 Combine columns side by side
df = pd.concat([orders, products, quantities], axis=1)

@app.route("/")
def home():
    return jsonify({"message": "E-commerce Chatbot API is running!"})

@app.route("/top-products", methods=["GET"])
def top_products():
    top = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)
    return jsonify({"top_products": top.to_dict()})

@app.route("/order-status/<order_id>", methods=["GET"])
def order_status(order_id):
    order = df[df["Order ID"].astype(str) == order_id]
    if order.empty:
        return jsonify({"status": "Order not found"})
    return jsonify({"order_id": order_id, "status": "Delivered"})

@app.route("/stock/<item>", methods=["GET"])
def stock(item):
    stock_count = df[df["Product"].str.lower() == item.lower()]["Quantity"].sum()
    return jsonify({"item": item, "stock_left": int(stock_count)})

if __name__ == "__main__":
    app.run(debug=True)

