import time

import keyboard
import speech_recognition as sr


def get_audio_from_mic(recognizer: sr.Recognizer) -> sr.AudioData:
    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source)

        print("Diga alguma coisa: ")  # TODO: tocar audio nessa parte

        audio = recognizer.listen(source)

        return audio


def mic_speech_to_text() -> None:
    recognizer = sr.Recognizer()

    audio = get_audio_from_mic(recognizer)

    print("Reconhecendo audio...")  # TODO: tocar audio nessa parte
    phrase = recognizer.recognize_google(audio, language="pt-BR")

    return phrase


def try_mic_speech_to_text():

    try:
        speech_text = mic_speech_to_text()
    except sr.UnkownValueError:
        print("Não entendi")  # TODO: tocar audio nessa parte
    except sr.RequestError:
        print(
            "Não consegui me comunicar com o servidor do Google...\nA internet está funcionando?"
        )  # TODO: tocar audio nessa parte
    else:
        print("Audio recebido:\n" + speech_text)  # TODO: tocar audio nessa parte
        # TODO: manipular o texto para realizar substituições
        # keyboard.write(speech_text)
        print(speech_text)


def main():

    # keyboard.add_hotkey("ctrl+shift+0", try_mic_speech_to_text)

    while True:
        time.sleep(0.01)
        if keyboard.is_pressed("ctrl+shift+0"):
            try_mic_speech_to_text()

    # keyboard.wait()


if __name__ == "__main__":
    main()
