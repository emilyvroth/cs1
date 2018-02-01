import check2_helper
from PIL import Image
im = Image.new('RGB', (1000,360))

im1=Image.open('lab04files/1.jpg')
ratio1=im1.size[0]/im1.size[1]
im1_scaled=im1.resize((round(256*ratio1),256))

im2=Image.open('lab04files/2.jpg')
ratio2=im2.size[0]/im2.size[1]
im2_scaled=im2.resize((round(256*ratio2),256))

im3=Image.open('lab04files/3.jpg')
ratio3=im3.size[0]/im3.size[1]
im3_scaled=im3.resize((round(256*ratio3),256))

im4=Image.open('lab04files/4.jpg')
ratio4=im4.size[0]/im4.size[1]
im4_scaled=im4.resize((round(256*ratio4),256))

im5=Image.open('lab04files/5.jpg')
ratio5=im5.size[0]/im5.size[1]
im5_scaled=im5.resize((round(256*ratio5),256))

im6=Image.open('lab04files/6.jpg')
ratio6=im6.size[0]/im6.size[1]
im6_scaled=im6.resize((round(256*ratio6),256))

im.paste(im1_scaled,(31,20))
im.paste(im2_scaled,(190,60))
im.paste(im3_scaled,(349,20))
im.paste(im4_scaled,(508,60))
im.paste(im5_scaled,(667,20))
im.paste(im6_scaled,(826,60))

im.show()
#149x256