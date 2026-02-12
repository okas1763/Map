import requests
from params import main_config

def minus_spn():
    main_config["spn"] = main_config["spn"] - 0.1


def plus_spn():
    main_config["spn"] = main_config["spn"] + 0.1


def minus_x():
    main_config["x"] = main_config["x"] - 0.1


def plus_x():
    main_config["x"] = main_config["x"] + 0.1
