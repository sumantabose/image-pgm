from PIL import Image
img = Image.open('brick-house.png').convert('L')
#img.show()
img.save('brick-house-gs.png','png')

img.save('brick-house-gs.jpeg','jpeg')

size = img.size
half_size = (size[0]/2,size[1]/2)


half_img = img.resize(half_size)
half_img.save('brick-house-half_size.png','png')

img.rotate(45).show()