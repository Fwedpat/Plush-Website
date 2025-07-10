import mysql.connector
import cgi, math, cgitb
from flask import *

cgitb.enable()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Fudge100",
  database="pokemon",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM mons")

myresult = mycursor.fetchall()

app = Flask(__name__)
app.secret_key = "HailLordArceus"

@app.route("/")
def home():
    return render_template("Main.html", content=myresult)


@app.route('/add', methods=['POST'])
def add_to_cart():
  id = request.form['code']
  findmon = "SELECT * FROM mons WHERE idmons= " + str(id)
  mycursor.execute(findmon)
  cart = AddCart(prefix="cart")
  row = mycursor.fetchone()
  session.modified = True
  if 'cart_item' in session:
    if not any(row[1] in d for d in session['cart_item']):
      session['cart_item'].append({row[1]: 1})
    elif any(row[1] in d for d in session['cart_item']):
      for d in session['cart_item']:
        d.update((k, cart))


  return redirect(url_for('.home'))



def array_merge(arr1, arr2):
  return arr1 + arr2;

if __name__ == "__main__":
    app.run(debug=True)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pokemon",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM mons")

myresult = mycursor.fetchall()
