import json
from datetime import datetime


def json_encode(data):
    if isinstance(data, datetime):
        return data.isoformat()
    if isinstance(data, (dict, list)):
        return json.dumps(data)


def json_serializer(data):
    return json.dumps(data, default=str).encode("utf-8")


def json_deserializer(data):
    return json.loads(data.decode("utf-8"))


def get_month(month: int):
    print(month)
    month_map = {
        1: "JAN", 2: 'FEB', 3: "MAR",
        4: "APR", 5: "MAY", 6: "JUN",
        7: "JUL", 8: "AUG", 9: "SEP",
        10: "OCT", 11: "NOV", 12: "DEC"
    }
    return [month_map[mon] for mon in month]


def date_key(date: str):
    dt = date.split('-')

    return ''.join(dt)
