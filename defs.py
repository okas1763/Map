import requests
from params import main_config

def minus_spn():
    main_config["spn"] = main_config["spn"] - 0.05


def plus_spn():
    main_config["spn"] = main_config["spn"] + 0.05