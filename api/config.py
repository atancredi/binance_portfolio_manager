import os
from configparser import ConfigParser
from exceptions import ConfigurationError

def read_config() -> dict:
    config_data = {}
    try:
        config = ConfigParser()
        config.read("secret")
        config_data["API_KEY"] = config['SECRET']['API_KEY']
        config_data["API_SECRET"] = config['SECRET']['API_SECRET']

    except Exception:
        raise ConfigurationError('Error occured while reading config from file.')

    if not __API_KEY__ or not __API_SECRET__:
        try:
            __API_KEY__ = os.environ['API_KEY']
            __API_SECRET__ = os.environ['API_SECRET']
        except KeyError:
            raise ConfigurationError('Error occurred while reading config from environment variables')

    return config_data
