# *************************************************
# Sumo Bot Firmware
# *************************************************
import simpleio
import time
import board
import busio
import digitalio
import neopixel
import pwmio
import adafruit_vl53l0x
from adafruit_motor import motor
from melodies import robot_startup_melody, note_values, note_frequencies, note_durations
from led_animations import (
    startup_animation,
    countdown_animation,
    countdown_start,
    countdown_end,
)
import keypad
# Pins connected to LEDs
LED_PINS = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP16,
    board.GP17,
    board.GP26,
    board.GP27,
    board.GP28,
]

# Pin connected to piezo buzzer
PIEZO_PIN = board.GP22

# Pins connected to DC motors (swap values if your motors are connected differently
RIGHT_MOTOR_PIN = board.GP8
LEFT_MOTOR_PIN = board.GP9

# Pin connected to NeoPixels
NEO_PIXEL_PIN = board.GP18

# Pins connected to buttons
BUTTON_1_PIN = board.GP20
BUTTON_2_PIN = board.GP21

# Robot states
STARTUP = 0  # Startup sequence
DISARMED = 1  # Waiting for button press
ARMED = 2  # Waiting for button release
COUNTDOWN = 3  # Counting down to fight
FIGHTING = 4  # Fight mode
LOST = 5  # Bot has lost the match
WON = 6  # Bot has won the match

class SumoBot:

    def __init__(self):
        """
        Sets up the sumo bot's hardware and internal state.
        """

        self.leds = []
        for pin in LED_PINS:
            # Set pins as digital output
            digout = digitalio.DigitalInOut(pin)
            digout.direction = digitalio.Direction.OUTPUT
            self.leds.append(digout)

        # Initialize Neopixel RGB LEDs
        self.pixels = neopixel.NeoPixel(NEO_PIXEL_PIN, 2, brightness=0.1)
        self.pixels.fill(0)

        # Initialize buttons
        self.keypad = keypad.Keys(
            (BUTTON_1_PIN, BUTTON_2_PIN), value_when_pressed=False, pull=True
        )

        # Initialize DC motors
        m1a = pwmio.PWMOut(RIGHT_MOTOR_PIN, frequency=50)
        m1b = pwmio.PWMOut(LEFT_MOTOR_PIN, frequency=50)
        self.motor1 = motor.DCMotor(m1a, m1b)
        m2a = pwmio.PWMOut(board.GP10, frequency=50)
        m2b = pwmio.PWMOut(board.GP11, frequency=50)
        self.motor2 = motor.DCMotor(m2a, m2b)

        # Initialize piezo
        self.piezo = PIEZO_PIN

        # Set initial state
        self.state = STARTUP

    def set_leds(self, settings):
        for led, setting in zip(self.leds, settings):
            led.value = bool(setting)

    def play_led_animation(self, animation):
        for settings_list, delay in animation:
            self.set_leds(settings_list)
            time.sleep(delay)

    def run(self):
        """
        Sumo bot main execution loop.
        """
        while True:
            if self.state == STARTUP:
                self.play_led_animation(startup_animation)
                self.state = DISARMED
            elif self.state == DISARMED:
                self.pixels.fill(0xFF0000)
                key_event = self.keypad.events.get()
                if key_event and key_event.key_number == 0 and key_event.pressed:
                    self.state = ARMED
            elif self.state == ARMED:
                self.pixels.fill(0xFFFF00)
                key_event = self.keypad.events.get()
                if key_event and key_event.key_number == 0 and not key_event.pressed:
                    self.state = COUNTDOWN
            elif self.state == COUNTDOWN:
                self.pixels.fill(0x00FF00)
                self.set_leds(countdown_start)
                simpleio.tone(
                    pin=self.piezo,
                    frequency=note_frequencies.get("C5"),
                    duration=0.3,
                )
                self.play_led_animation(countdown_animation)
                self.set_leds(countdown_end)
                self.state = FIGHTING
            elif self.state == FIGHTING:
                self.pixels.fill(0)
            elif self.state == LOST:
                pass
            elif self.state == WON:
                pass


if __name__ == "__main__":
    SumoBot().run()


