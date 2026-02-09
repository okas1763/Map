from api import API_KEY_GEOCODE, API_KEY_STATIC

class Params:
    def __init__(self, params: dict):
        self.params = dict()
        self.default_geocode_params = {
            "size": "600,450",
            "ll": "52.043386, 39.736096",
            "z": "6",
            "api_key": API_KEY_GEOCODE, 
        }
        # self.default_static_params = {
        #     "1": "1"
        # }
        self.add_params(params)
    
    def add_params(self, params: dict):
        for key, val in params.items():
            self.params[key] = val
    
    def del_key(self, key):
        try:
            del self.params[key]
        except KeyError:
            pass
    
    def clear(self):
        self.params.clear()
    
    def get_params(self):
        return self.params