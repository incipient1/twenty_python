from PIL import Image
img = Image.open('E:/Python_learning/learning_DC/google_img_crawler/imgs/50f5e6fefdc9f065f0006eb2.jpg')
img_copy = img.resize((500,375))
img_copy.save('E:/Python_learning/learning_everyday/img_resized/1111.jpg')
img_copy.show()