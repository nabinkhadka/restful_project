from flask import Flask

app = Flask(__name__)

@app.route("/records", methods=["GET"])
def get_task():
  records = {"record1":"record 1 data", "record2":"record 2 data", "record2":"record 3 data"}
  return {"records": records}, 200


app.run(debug=True)