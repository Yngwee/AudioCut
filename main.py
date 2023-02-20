import moviepy.editor
import tkinter.filedialog
import tkinter
from pathlib import Path


def choose_file():
    filetypes = (("Видеофайл", "*.mp4"),)

    filename = tkinter.filedialog.askopenfilename(title="Открыть файл", initialdir="/", filetypes=filetypes)
    if filename:
        return filename


try:
    video_file = Path(choose_file())
    video = moviepy.editor.VideoFileClip(f'{video_file}')
    audio = video.audio
    audio.write_audiofile(f'{video_file.stem}.mp3')
except:
    print('Файл не найден')
