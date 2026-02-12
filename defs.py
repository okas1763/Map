import requests
from params import main_config

def minus_spn():
    main_config["zoom"] = main_config["zoom"] - 0.1


def plus_spn():
    main_config["zoom"] = main_config["zoom"] + 0.1