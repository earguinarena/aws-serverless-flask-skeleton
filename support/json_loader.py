from decimal import Decimal
import json


def load_json(o):
    return json.loads(o, parse_float=Decimal)
