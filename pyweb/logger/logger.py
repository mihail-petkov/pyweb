import logging

class Logger():

    def set_debug(self, debug):
        logging.basicConfig()
        logging_app = self.get_logger()
        if debug:
            logging_app.setLevel(logging.DEBUG)
        else:
            logging_app.setLevel(logging.INFO)

    def error(self, msg):
        self.get_logger().error(msg)

    def warn(self, msg):
        self.get_logger().warn(msg)

    def debug(self, msg):
        self.get_logger().debug(msg)

    def info(self, msg):
        self.get_logger().info(msg)

    def get_logger(self):
        return logging.getLogger('pyweb')

logger = Logger()
