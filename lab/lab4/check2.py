import check2_helper
from PIL import Image
im = Image.new('RGB', (512,512))
#im.show()

im1=Image.open('lab04files/ca.jpg')
im1_scaled=check2_helper.make_square(im1)
im1_scaled=im1_scaled.resize((256,256))
im2=Image.open('lab04files/im.jpg')
im2_scaled=check2_helper.make_square(im2)
im2_scaled=im2_scaled.resize((256,256))
im3=Image.open('lab04files/hk.jpg')
im3_scaled=check2_helper.make_square(im3)
im3_scaled=im3_scaled.resize((256,256))
im4=Image.open('lab04files/bw.jpg')
im4_scaled=check2_helper.make_square(im4)
im4_scaled=im4_scaled.resize((256,256))

im.paste(im1_scaled,(0,0))
im.paste(im2_scaled,(0,256))
im.paste(im3_scaled,(256,0))
im.paste(im4_scaled,(256,256))
im.show()

