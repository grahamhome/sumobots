from ..base_bot import SumoBotBase
import logging


class State:
    """
    ABC for State subclasses.
    """

    def __init__(self, bot: SumoBotBase):
        self.bot = bot
        self.next = None
        self.setup_logger()


    def setup_logger(self):
        self.logger = logging.getLogger("SumoBot")
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler("sumobot.log")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(f"{self.__class__.__name__}: %(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        self.logger.addHandler(file_handler)

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
