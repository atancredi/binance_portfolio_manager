from os.path import exists
from os import environ as env
from configparser import ConfigParser
from exceptions import ConfigurationError

def read_config(config_path: str = "config") -> dict:
    config_data = {}
    config = ConfigParser()
    
    if not exists(config_path):
        raise ConfigurationError('Config file not found.')
    try:
        config.read(config_path)
    except Exception:
        raise ConfigurationError('Error reading Config file.')
    
    config_data["API_KEY"] = config['SECRET']['API_KEY']
    config_data["API_SECRET"] = config['SECRET']['API_SECRET']
    
    return config_data
