from base_model import BaseModel
from flask.json import JSONEncoder


class ModelJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, BaseModel):
                return obj.__str__()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)

        return JSONEncoder.default(self, obj)
