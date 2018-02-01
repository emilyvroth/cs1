from PIL import Image
im = Image.new('RGB', (512,512))
#im.show()

im1=Image.open('lab04files/ca.jpg')
im1_scaled=im1.resize((256,256))
im2=Image.open('lab04files/im.jpg')
im2_scaled=im2.resize((256,256))
im3=Image.open('lab04files/hk.jpg')
im3_scaled=im3.resize((256,256))
im4=Image.open('lab04files/bw.jpg')
im4_scaled=im4.resize((256,256))

im.paste(im1_scaled,(0,0))
im.paste(im2_scaled,(0,256))
im.paste(im3_scaled,(256,0))
im.paste(im4_scaled,(256,256))
im.show()
