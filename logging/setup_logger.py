# -- define logger
import logging.config
import yaml

def setup_logger(log_conf_path, store_log_path):
    """
        Function for setting up the logger
    """
    now = datetime.now()
    log_file_name = os.path.join(store_log_path,
                                 '{}{:02d}{:02d}_{:02d}{:02d}.log'.format(now.year, now.month, now.day, now.hour, now.minute)
                                )
    with open(log_conf_path) as f:
        config = yaml.safe_load(f.read())

    config['handlers']['file']['filename'] = config['handlers']['file']['filename'].format(path_filename =log_file_name)
    #print(config['handlers']['file']['filename'])
    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
    logger.info(f"logger setup done. Saving logs at {config['handlers']['file']['filename']}")
    
## Use logger in other modules
    # log_conf_path = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),'src','log_conf.yaml')
    # setup_logger(log_conf_path,logdir )
    # logger = logging.getLogger(__name__)
