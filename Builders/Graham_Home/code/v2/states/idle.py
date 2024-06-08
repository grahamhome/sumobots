from asyncio import sleep

from states import State


class Idle(State):
    async def start(self):
        await super().start()
        self.bot.pixels.fill(0xFF0000)
        while True:
            if self.bot.battery_low():
                from states import BatteryLow
                self.switch(BatteryLow)
                break
            else:
                await sleep(0)

    async def button_pressed(self, key_event):
        self.logger.debug("Button press detected")
        if key_event.key_number == 0 and key_event.pressed:
            from states import Armed
            self.switch(Armed)
