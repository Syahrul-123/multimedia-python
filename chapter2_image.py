from PIL import Image
from PIL import ImageFilter

# Memuat gambar
image = Image.open('images.jpg')

# Menyimpan gambar
image.save('images.jpg')

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_images.jpg')

resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_images.jpg')


filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_images.jpg')