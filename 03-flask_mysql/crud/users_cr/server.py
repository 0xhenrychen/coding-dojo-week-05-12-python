from flask import Flask, render_template, request, redirect
# import the class from user.py
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)

@app.route("/create_user", methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    
    data = {
                "first_name": request.form["first_name"],
                "last_name": request.form["last_name"],
                "email": request.form["email"]
            }
    print("Here's the data: ", data)
    # We pass the data dictionary into the save method from the User class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect("/users")

@app.route("/users")
def show_users():
    users = User.get_all()
    print(users)
    return render_template("users.html", users = users)
            
if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5008)