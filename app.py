from flask import Flask, render_template, request

app = Flask(__name__)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    global chat_history
    images = []
    response = ""

    if request.method == "POST":
        user_input = request.form["user_input"]
        chat_history.append({"role": "user", "text": user_input})

        lower_input = user_input.lower()

        if "credit card" in lower_input:
            response = "Pulled stored credit card information."
            images = ["Images/credit_card.png"]

        elif "customer" in lower_input:
            response = "Pulled customer-related files."
            images = ["Images/invoice1.png"]

        elif "picture" in lower_input or "photo" in lower_input or "family" in lower_input:
            response = "Found some personal photos."
            images = [
                "Images/family1.png",
                "Images/family2.png",
                "Images/image4.png",
                "Images/image5.png"
            ]

        else:
            response = f"Simulated bot response to: {user_input}"

        chat_history.append({"role": "bot", "text": response})

    return render_template("index.html", chat_history=chat_history, images=images)

if __name__ == "__main__":
    app.run(debug=True)
