import os, json

import pytest
from appium import webdriver


DEFAULT_WAIT_TIME = 10
APK_PATH = os.path.abspath('src/resources/apps/me.wolszon.fastshopping_23.apk')
COMMAND_EXECUTOR = 'http://127.0.0.1:4723/wd/hub'

# Json files
CONFIG_PATH = 'src/config.json'

@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH, encoding='utf-8') as config_file:
        data = json.load(config_file)

        return data

@pytest.fixture(scope='session')
def config_wait_time(config):
    if 'wait_time' not in config:
        return DEFAULT_WAIT_TIME

    return config['wait_time']

@pytest.fixture(scope='session')
def config_device_name(config):
    if 'device_name' not in config:
        Exception('The config file does not contain "device_name".')
    else:
        return config['device_name']

@pytest.fixture(scope='session')
def config_platform_version(config):
    if 'platform_version' not in config:
        Exception('The config file does not contain "platform_version".')
    else:
        return config['platform_version']

@pytest.fixture(scope='session')
def config_desired_capabilities(config_platform_version, config_device_name):
    desired_capabilities = {
        'platformName': 'Android',
        'platformVersion': config_platform_version,
        'deviceName': config_device_name,
        'app': APK_PATH
    }

    return desired_capabilities

@pytest.fixture(scope='function')
def driver(config_wait_time, config_desired_capabilities):
    driver = webdriver.Remote(command_executor=COMMAND_EXECUTOR, desired_capabilities=config_desired_capabilities)

    driver.implicitly_wait(config_wait_time)

    yield driver

    driver.quit()