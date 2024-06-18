from states import State


class Armed(State):
    async def start(self):
        await super().start()
        self.bot.pixels.fill(0xFFFF00)

    async def button_pressed(self, key_event):
        self.logger.debug("Button press detected")
        if key_event.key_number == 0 and not key_event.pressed:
            from states import Countdown
            self.switch(Countdown)
