from asyncio import sleep

from base_bot import SumoBotBase
import adafruit_logging as logging

from code import StateManager


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

    def __init__(self, bot: SumoBotBase, state_manager: StateManager):
        self.bot = bot
        self.next = None
        self.manager = state_manager
        self.started = False

    async def start(self):
        """
        Action performed on state activation.
        """
        self.logger.debug(f"Starting {self.__class__.__name__}")
        await self.bot.stop()
        self.started = True

    async def run(self):
        """
        Action performed repeatedly while state is active.
        """
        if not self.started:
            await self.start()

    async def switch(self, next_state):
        self.logger.debug(f"Switching to {next_state.__name__}")
        self.manager.active = False
        await self.stop()
        self.manager.state = next_state(self.bot, self.manager)
        self.manager.active = True



    async def stop(self):
        """
        Action performed on state deactivation.
        """
        self.logger.debug(f"Stopping {self.__class__.__name__}")

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
