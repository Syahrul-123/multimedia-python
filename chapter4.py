import pygame
pygame.init()

# Memuat gambar
image = pygame.image.load('panda.jpg')

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Loop utama permainan
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 5
    if x > 800:
        x = 0

    # Menggambar gambar
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()

    # Memuat suara
    sound = pygame.mixer.Sound('cadangan.mp3')

    # Memutar suara
    sound.play()

pygame.quit()

#import tkinter as tk
#from tkinter import filedialog
#from pydub import AudioSegment
#from pydub.playback import play

# Membuat jendela utama
#root = tk.Tk()
#root.title("Music Player")

# Mendefinisikan fungsi untuk memutar musik
#def play_music():
   # file_path = filedialog.askopenfilename()
  #  if file_path:
   #     audio = AudioSegment.from_file(file_path)
   #     play(audio)

# Membuat tombol play
#play_button = tk.Button(root, text="Play", command=play_music)
#play_button.pack()

# Menjalankan loop acara Tkinter
#root.mainloop()