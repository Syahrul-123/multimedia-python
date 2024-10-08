import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")


# from PIL import Image, ImageTk

# # Memuat gambar menggunakan Pillow
# image = Image.open('panda.jpg')
# photo = ImageTk.PhotoImage(image)

# # Membuat label untuk menampilkan gambar
# label = tk.Label(root, image=photo)
# label.pack()



# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()