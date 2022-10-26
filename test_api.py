import requests
import datetime


from_date = datetime.date(day=3, month=4, year=2016)
to_date = datetime.date(day=4, month=4, year=2016)

data = {
    "date_from": from_date.isoformat(),
    'date_to': to_date.isoformat(),
    "page": 200
}

response = requests.post("http://localhost:5001/incidents", json=data)
print(response.json())
