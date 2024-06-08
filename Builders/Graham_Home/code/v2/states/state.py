from base_bot import SumoBotBase
import adafruit_logging as logging


class State:
    """
    ABC for State subclasses.
    """

    def __init__(self, bot: SumoBotBase):
        self.bot = bot
        self.next = None
        self.logger = self.get_logger()


    def get_logger(self):
        logger = logging.getLogger("SumoBot")
        logger.setLevel(logging.DEBUG)
        serial_handler = logging.StreamHandler()
        serial_handler.setLevel(logging.DEBUG)
        logger.addHandler(serial_handler)
        return logger

    async def start(self):
        """
        Action performed on state activation.
        """
        self.logger.debug("Starting")

    def switch(self, next):
        self.logger.debug(f"Switching to {next.__name__}")
        self.stop()
        self.next = next


    async def stop(self):
        """
        Action performed on state deactivation.
        """
        self.logger.debug("Stopping")

    async def opponent_detected(self):
        """
        Defines behavior when an opponent is detected.
        """
        pass

    async def edge_detected(self):
        """
        Defines behavior when the edge is detected.
        """
        pass

    async def button_pressed(self, key_event):
        """
        Defines behavior when a button is pressed.
        """
        pass
