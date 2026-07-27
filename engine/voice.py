# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Voice Manager
Text-to-Speech and Speech-to-Text
"""

import threading

try:
    import pyttsx3
except Exception:
    pyttsx3 = None

try:
    import speech_recognition as sr
except Exception:
    sr = None


class VoiceManager:

    def __init__(self):
        self.engine = None
        self.recognizer = None
        self.speaking = False

        if pyttsx3:
            try:
                self.engine = pyttsx3.init()
                self.engine.setProperty("rate", 170)
            except Exception:
                self.engine = None

        if sr:
            self.recognizer = sr.Recognizer()

    def available_tts(self):
        """
        Check if Text-to-Speech is available.
        """
        return self.engine is not None

    def available_stt(self):
        """
        Check if Speech-to-Text is available.
        """
        return self.recognizer is not None

    def speak(self, text):
        """
        Speak text in a background thread.
        """

        if not self.available_tts():
            return False

        if self.speaking:
            return False

        def worker():
            self.speaking = True

            try:
                self.engine.say(str(text))
                self.engine.runAndWait()
            finally:
                self.speaking = False

        threading.Thread(
            target=worker,
            daemon=True
        ).start()

        return True

    def stop(self):
        """
        Stop speaking.
        """

        if self.engine:
            try:
                self.engine.stop()
            except Exception:
                pass

        self.speaking = False

    def listen(self, language="hi-IN"):
        """
        Listen from microphone.
        """

        if not self.available_stt():
            return {
                "success": False,
                "text": "",
                "error": "Speech Recognition unavailable."
            }

        try:
            with sr.Microphone() as source:

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = self.recognizer.listen(source)

            text = self.recognizer.recognize_google(
                audio,
                language=language
            )

            return {
                "success": True,
                "text": text,
                "error": ""
            }

        except Exception as error:
            return {
                "success": False,
                "text": "",
                "error": str(error)
            }


voice = VoiceManager()
