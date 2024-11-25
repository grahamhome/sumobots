from asyncio import sleep

from base_bot import SumoBotBase

from code import StateManager

class State:
    """
    ABC for State subclasses.
    """
    color = 0xFF0000
    def __init__(self, bot: SumoBotBase, state_manager: StateManager):
        self.bot = bot
        self.next = None
        self.manager = state_manager
        self.started = False

    async def start(self):
        """
        Action performed on state activation.
        """
        print(f"Starting {self.__class__.__name__}")
        await self.bot.stop()
        self.bot.pixels.fill(self.color)
        self.started = True

    async def run(self):
        """
        Action performed repeatedly while state is active.
        """
        if not self.started:
            await self.start()

    async def switch(self, next_state):
        self.manager.active = False
        await self.stop()
        self.manager.state = next_state(self.bot, self.manager)
        self.manager.active = True



    async def stop(self):
        """
        Action performed on state deactivation.
        """
        self.bot.pixels.fill(0xFF0000)

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
