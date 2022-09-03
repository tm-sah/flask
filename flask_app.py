import mysql.connector
import flask
from flask import request,Flask

mydb = mysql.connector.connect(
  host="sql8.freesqldatabase.com",
  user="sql8516940",
  password="FwfwBKp3LR",
  database = "sql8516940"
)
app = Flask(__name__)
mycursor = mydb.cursor()
@app.route("/")
def main():

    mycursor.execute("SELECT * FROM users ")
    mycursor.exe
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
try:
    if __name__ == "__main__":
      app.run(host="localhost",port=8080)
except:
  pass
