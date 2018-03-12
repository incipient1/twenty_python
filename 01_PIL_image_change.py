from PIL import Image,ImageDraw,ImageFont
im = Image.open('E:/Python_learning/learning_BL/image_pycodes_beijing/fcity.jpg')
dr = ImageDraw.Draw(im)
font1 = ImageFont.truetype('C:/Windows/Fonts/arial.ttf',50)

text1 = 'Bei jing'
dr.text((im.size[0]*0.7,im.size[1]*0.08),text=text1,outline=(124,124,124),font=font1)

im.show()
im.save('E:/Python_learning/learning_BL/image_pycodes_beijing/fcity3.jpg')