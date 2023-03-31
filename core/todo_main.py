# Todo : Replace all the todo comments by your custom ones , remove the prefix
#  'todo' from the module name

import os
import sys

from models import models
from handlers import handlers

from ytt_py_utils.env import envs
from ytt_py_utils.config.yaml import parser as uc
from ytt_py_utils.log import logs as ul
from ytt_py_utils.web import request as ur
from ytt_py_utils.ui.Pyside2 import core as uic

def run_application(logger=None):
    """
    :param scripts:
    :return:
    """
    logger.info('...Init App')

    model = models.CustomModel()

    # application
    logger.info(f'Running on : {sys.executable}')
    app = uic.get_app()

    # handler
    h = handlers.CustomHandler(model)
    h.run()

    logger.info('Running...')
    sys.exit(app.exec_())

def main():
    """

    :return:
    """
    # Install Environment

    NAME = 'YTT_TMPLT'  # Todo: replace NAME by yours
    envs.Env(NAME)

    if envs.Env.PATH not in sys.path:
        sys.path.insert(0, envs.Env.PATH)

    # Config
    if not os.path.exists(envs.Env.DEFAULT_CONF_FILE):
        ur.download_file(default_config_url, envs.Env.DEFAULT_CONF_FILE)

    config_parser = uc.YamlParser(envs.Env.DEFAULT_CONF_FILE)
    config = config_parser.load()

    # Setup main config
    # app_config = config['app']
    # parser = path.PathParser()

    # Setup logs config
    log_config = config['logs']
    logger_inst = ul.Log(__name__, log_config)

    logger = logger_inst.logger
    logger.debug('Parsing default_source data')

    run_application(logger=logger)


if __name__ == '__main__':
    main()