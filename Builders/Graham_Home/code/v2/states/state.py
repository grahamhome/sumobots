from asyncio import sleep

from base_bot import SumoBotBase
import adafruit_logging as logging


def get_logger():
    logger = logging.getLogger("SumoBot")
    logger.setLevel(logging.DEBUG)
    serial_handler = logging.StreamHandler()
    serial_handler.setLevel(logging.DEBUG)
    logger.addHandler(serial_handler)
    return logger


class State:
    """
    ABC for State subclasses.
    """

    logger = get_logger()

    def __init__(self, bot: SumoBotBase):
        self.bot = bot
        self.next = None
        self.logger.info(f"Creating state {self.__class__.__name__}")

    async def start(self):
        """
        Action performed on state activation.
        """
        self.logger.debug("Starting")

    async def run(self):
        """
        Action performed repeatedly while state is active.
        """
        self.logger.debug(f"Running in state {self.__class__.__name__}")
        await sleep(0.1)

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
