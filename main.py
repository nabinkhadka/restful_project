from flask import Flask

app = Flask(__name__)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = {"first": "open laptop", "second": "open IDE", "third": "start coding"}
    return {"tasks": tasks}, 200


app.run(debug=True)
