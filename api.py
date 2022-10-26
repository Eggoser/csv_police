from flask import Flask, request, jsonify
import datetime
import sqlite3


app = Flask(__name__)

sqlite_file = "db.sqlite3"


@app.route("/incidents", methods=["POST"])
def get_incident_data():
    per_page = 20
    page = request.json.get("page") or 1
    date_from = request.json.get("date_from")
    date_to = request.json.get("date_to")

    if not date_from or not date_to:
        return {"status": 1, "message": "need params 'date_from', 'date_to'"}

    try:
        date_from = datetime.date.fromisoformat(date_from)
        date_to = datetime.date.fromisoformat(date_to)
    except:
        return {"status": 1, "message": "dates must be in ISO format"}

    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    date_from = date_from.strftime("%Y-%m-%d")
    date_to = date_to.strftime("%Y-%m-%d")

    query = "select * from police_calls where DATE(`Report Date`) >= ? and DATE(`Report Date`) <= ? order by `Report Date` limit ? offset ? "
    cursor.execute(query, [date_from, date_to, per_page, per_page * (page - 1)])

    data = cursor.fetchall()
    data = [dict(row) for row in data]

    return jsonify(data)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
