image = 'ch_4_image.jpg'
with open(image, 'rb') as image_file:
	content = image_file.read()
print(len(content))