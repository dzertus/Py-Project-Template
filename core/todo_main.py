# Todo : Replace all the todo comments by your custom ones , remove the prefix
#  'todo' from the module name

import os
import sys

from data import env

from ytt_py_utils.config.yaml import parser as uc
from ytt_py_utils.log import logs as ul
from ytt_py_utils.web import request as ur


# Install Environment
installed = False


NAME = 'TMPLT' #Todo: replace NAME by yours
ENV = env.Env(NAME)

if env.Env.PATH is not None:
    if env.Env.PATH not in sys.path:
        sys.path.insert(0, env.Env.PATH)

    # Config
    conf_path = os.path.join(env.Env.DEFAULT_CONF_FILE)
    if not os.path.exists(conf_path):
        ur.download_file(default_config_url, env.Env.DEFAULT_CONF_FILE)

    config_parser = uc.YamlParser(env.Env.DEFAULT_CONF_FILE)
    config = config_parser.load()

    # Setup optional settings
    settings = config['settings']
    ENV.set_optional_settings(settings)


    # Setup main config
    # app_config = config['app']
    # parser = path.PathParser()

    # Setup logs config
    log_config = config['logs']
    logger_inst = ul.Log(__name__, log_config)

    logger = logger_inst.logger
    logger.debug('Parsing default_source data')

    installed = True

else:
    # Ask user to install PATH env variable
    print('Please install this environment variable : \n'
          'HINTERFACE as name \n'
          'Source code python path : '
          '..Helpers-Interface-initialize_python2/python as value\n'
          'For more informations on how to install an environment variable '
          'according to your OS , visit this page : \n'
          'https://github.com/dzertus/Helpers-Interface/blob/main/README.md#maya-helper-interface\n'
          )
    # Shut down process because PATH env variable not found
    # Todo Open dialog to set

def run():
    """
    :param scripts:
    :return:
    """
    logger.error()
    logger.info('...Init App')

    model = model_cls.CustomModel()

    # application
    logger.info(f'Running on : {sys.executable}')
    # app = QtWidgets.QApplication(sys.argv)

    # handler
    h = handler_cls.Handler(model)
    h.run()

    logger.info('Running...')
    sys.exit(app.exec_())


def main():
    """

    :return:
    """
    if installed is True:
        print('Processing')
    else:
        print('Shutting down..')
        sys.exit()

if __name__ == '__main__':
    main()