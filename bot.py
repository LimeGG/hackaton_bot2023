import asyncio
import logging
from aiogram import Bot, Dispatcher, types
# from aiogram.filters.command import Command

import speech_recognition as speech_r
import pyaudio
import wave

# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)
# # Объект бота
# bot = Bot(token="6215651953:AAHT_4kNGCbn4FYjWvdfuoaIoYED7JH4IgY")
# # Диспетчер
# dp = Dispatcher()


# # Хэндлер на команду /start
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Hello!")
#
#
# async def main():
#     await dp.start_polling(bot)
#

#
# if __name__ == "__main__":
#     asyncio.run(main())


def voice():
    CHUNK = 1024  # определяет форму ауди сигнала
    FRT = pyaudio.paInt16  # шестнадцатибитный формат задает значение амплитуды
    CHAN = 1  # канал записи звука
    RT = 44100  # частота
    REC_SEC = 5  # длина записи
    OUTPUT = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FRT, channels=CHAN, rate=RT, input=True,
                    frames_per_buffer=CHUNK)  # открываем поток для записи
    print("rec")
    frames = []  # формируем выборку данных фреймов
    for i in range(0, int(RT / CHUNK * REC_SEC)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("done")

    stream.stop_stream()  # останавливаем и закрываем поток
    stream.close()
    p.terminate()

    w = wave.open(OUTPUT, 'wb')
    w.setnchannels(CHAN)
    w.setsampwidth(p.get_sample_size(FRT))
    w.setframerate(RT)
    w.writeframes(b''.join(frames))
    w.close()

    sample = speech_r.WavFile('C:\Users\Александр\Desktop\Myproject\Hackaton2023output.wav')

    r = speech_r.Recognizer

    with sample as audio:
        content = r.record(audio)

    with sample as audio:
        content = r.record(audio)
        r.adjust_for_ambient_noise(audio)

    g = r.recognize_google(audio, language="ru-RU"
    return g