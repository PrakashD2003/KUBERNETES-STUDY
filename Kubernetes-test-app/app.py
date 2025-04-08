# Importing required modules from Flask
from flask import Flask, render_template, request

# Creating an instance of the Flask class.
# This will be our WSGI application.
app = Flask(__name__)

# Defining the route for the root URL ("/").
# The route supports both GET and POST HTTP methods.
@app.route("/", methods=["GET", "POST"])
def home():
    # Initializing an empty message variable
    message = ""

    # If the request method is POST (i.e., form is submitted)
    if request.method == "POST":
        # Get the value from the HTML form input with name="name"
        name = request.form.get("name")

        # Construct a welcome message using the entered name
        message = f"Hello {name}, Welcome to the Kubernetes test application!!!"

        # Render the 'index.html' template and pass the message variable
        return render_template("index.html", message=message)

    # If method is GET, or in case of an unhandled scenario,
    # render the page with an empty or default message
    return render_template("index.html", message=message)

# This block ensures that the Flask app runs only when the script is executed directly
if __name__ == "__main__":
    # Run the Flask development server
    # host="0.0.0.0" makes the app accessible externally (e.g., from EC2/public IP)
    # port=5000 sets the port number
    # debug=True enables debug mode for automatic reload on code changes and detailed error messages
    app.run(host="0.0.0.0", port=5000)
