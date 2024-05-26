from flask import Flask

app = Flask(__name__)

@app.route("/records", methods=["GET"])
def get_task():
  records = {"record1":"record 1 data", "record2":"record 2 data", "record2":"record 3 data"}
  return {"records": records}, 200

@app.route("/test", methods = ["GET"])
def test_Function():
  return "Test runs successful"
app.run(debug=True)

@app.route('/books', methods=['GET'])
def get_books():
    books = [
        {'title': 'Harry Potter', 'volume': "The Philosopher's Stone"},
        {'title': 'Harry Potter', 'volume': "Chamber of Secrets"},
        {'title': 'Harry Potter', 'volume': "Prisoner of Azkaban"},
    ]
    return {'books': books}, 200

app.run(debug=True, port=5000)