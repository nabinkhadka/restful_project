from flask import Flask

app = Flask(__name__)

@app.route("/records", methods=["GET"])
def get_task():
  records = {"record_1":"record 1 data", "record_2":"record 2 data", "record_3":"record 3 data"}
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

@app.route("/books", methods = ["GET"])
def get_book():
  books = {"book1":"book1 data", "book2":"book2 data", "book3":"book3 data"}
  return {"books": books}, 200

app.run(debug=True)
