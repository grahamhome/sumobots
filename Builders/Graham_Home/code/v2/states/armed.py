from states import State


class Armed(State):
    async def start(self):
        await super().start()
        self.bot.pixels.fill(0xFFFF00)

    async def button_pressed(self, key_event):
        self.logger.debug(f"Button {key_event.key_number} press (pressed={key_event.pressed}) detected from idle state")
        if key_event.key_number == 0 and not key_event.pressed:
            from states import Countdown
            await self.switch(Countdown)
