from moviepy.editor import VideoFileClip
from moviepy.editor import vfx
from moviepy.editor import concatenate_videoclips

# Memuat file video
video = VideoFileClip('videoo.mp4')

# Menyimpan file video
video.write_videofile('videoo.mp4')

short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
short_video.write_videofile('short_videoo.mp4')


combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_videoo.mp4')


reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
reversed_video.write_videofile('reversed_videoo.mp4')

sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
sped_up_video.write_videofile('sped_up_videoo.mp4')