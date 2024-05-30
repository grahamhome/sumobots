from .countdown import Countdown
from .state import State


class Armed(State):
    def start(self):
        super().start()
        self.bot.pixels.fill(0xFFFF00)

    def button_pressed(self, key_event):
        self.logger.debug("Button press detected")
        if key_event.key_number == 0 and not key_event.pressed:
            self.switch(Countdown)
