from api import API_KEY_GEOCODE, API_KEY_STATIC

class Params:
    def __init__(self, params: dict):
        self.params = dict()
        self.default_geocode_params = dict()
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
    
    def dict2str(self):
        return "&".join([f"{key}={value}" for key, value in self.params.items()])
    
    
class GeocodeParams(Params):
    def __init__(self, params):
        super().__init__(params)
        self.add_params({"apikey": API_KEY_GEOCODE})


class StaticParams(Params):
    def __init__(self, params):
        super().__init__(params)
        self.add_params({"apikey": API_KEY_STATIC})
        
