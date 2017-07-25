import logging

class logger:
    logging.basicConfig(level=logging.DEBUG,filename='log/modulelog',filemode='a',
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
                        ,datefmt='%H:%M:%S')
    log = logging.getLogger("modulelog")
