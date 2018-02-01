from PIL import Image
def make_square(im):
	s=im.size
	if s[0]>s[1]:
		return im.crop((0,0,s[1],s[1]))
	elif s[0]<s[1]:
		return im.crop((0,0,s[0],s[0]))

#im=Image.open('lab04files/1.jpg')
#imsquare=make_square(im)
#imsquare.show()