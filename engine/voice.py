# Created by : Amarchand Meghwal
# AP AI Android v41.2

from engine.info import VOICE_INPUT, VOICE_OUTPUT


class VoiceSystem:

    def __init__(self):
        self.input_enabled = VOICE_INPUT
        self.output_enabled = VOICE_OUTPUT

    def status(self):
        print("\n========== Voice System ==========")
        print(f"Voice Input  : {'ON' if self.input_enabled else 'OFF'}")
        print(f"Voice Output : {'ON' if self.output_enabled else 'OFF'}")
        print("==================================\n")

    def listen(self):
        if not self.input_enabled:
            return None

        print("🎤 Voice Input is not available yet.")
        return None

    def speak(self, text):
        if not self.output_enabled:
            return

        print(f"🔊 {text}")


voice = VoiceSystem()
