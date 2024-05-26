from flask import Flask

app = Flask(__name__)

@app.route("/records", methods=["GET"])
def get_task():
  records = {"record1":"record 1 data", "record2":"record 2 data", "record2":"record 3 data"}
  return {"records": records}, 200

@app.route("/test", methods = ["GET"])
def test_Function():
  return "Test runs successful"

@app.route("/books", methods = ["GET"])
def get_book():
  books = {"book1":"book1 data", "book2":"book2 data", "book3":"book3 data"}
  return {"books": books}, 200

app.run(debug=True)
