import decimal
import json
from datetime import datetime, date 
import base64
from boto3.dynamodb.types import BINARY_TYPES


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, BINARY_TYPES):
            return base64.b85encode(obj).decode('utf-8')
        return super(CustomJsonEncoder, self).default(obj)
