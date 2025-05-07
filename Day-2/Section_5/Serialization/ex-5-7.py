import json
import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super().default(obj)

now = datetime.datetime.now()
print(json.dumps({'time': now}, cls=DateTimeEncoder))
