import logging,sys

class Logger:
    def __init__(self):
        self.logger=logging.getLogger("logout")
        self.logger.setLevel(logging.DEBUG)
        self.sh=logging.StreamHandler(sys.stdout)
        self.sh.setLevel(logging.DEBUG)
        self.formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.sh.setFormatter(self.formatter)
        self.logger.addHandler(self.sh)
    def debug(self,debugs):
        self.logger.debug(debugs)
    def info(self,infos):
        self.logger.info(infos)
    def warning(self,warns):
        self.logger.warning(warns)
    def error(self,errors):
        self.logger.error(errors)