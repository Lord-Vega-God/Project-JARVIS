from datetime import datetime
from voice.speak import speak


class Jarvis:

    def startup(self):
        self.greet()

    def greet(self):

        hour = datetime.now().hour

        if hour < 12:
            greeting = "Good Morning"

        elif hour < 18:
            greeting = "Good Afternoon"

        else:
            greeting = "Good Evening"

        speak(f"{greeting}, Sir.")

        print("JARVIS is online.")