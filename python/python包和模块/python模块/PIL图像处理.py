from PIL import Image,ImageDraw

def addTransparency(img, factor = 0.7 ):
    # 调整图片的透明程度
    img = img.convert('RGBA')
    img_blender = Image.new('RGBA', img.size, (0,0,0,0))
    img = Image.blend(img_blender, img, factor)
    return img

def circle_corner(img, radii):
    """
    圆角处理
    :param img: 源图象。
    :param radii: 半径，如：30。
    :return: 返回一个圆角处理后的图象。
    """

    # 画圆（用于分离4个角）
    circle = Image.new('L', (radii * 2, radii * 2), 0)  # 创建一个黑色背景的画布
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radii * 2, radii * 2), fill=255)  # 画白色圆形

    # 原图
    img = img.convert("RGBA")
    w, h = img.size

    # 画4个角（将整圆分离为4个部分）
    alpha = Image.new('L', img.size, 255)
    alpha.paste(circle.crop((0, 0, radii, radii)), (0, 0))  # 左上角
    alpha.paste(circle.crop((radii, 0, radii * 2, radii)), (w - radii, 0))  # 右上角
    alpha.paste(circle.crop((radii, radii, radii * 2, radii * 2)), (w - radii, h - radii))  # 右下角
    alpha.paste(circle.crop((0, radii, radii, radii * 2)), (0, h - radii))  # 左下角
    # alpha.show()

    img.putalpha(alpha)  # 白色区域透明可见，黑色区域不可见
    return img
# 打开图片
# imagesfile = "../../../html5+css3/images/16.jpg"
# imagesfile = "../../../../../bia/demo1.jpg"
# im = Image.open(imagesfile)
# box = (0,0,728,525)
# im2 = Image.new("RGB",())
# im = im.crop(box)
# im1.paste(im,(100,100))

# print(im.size)
# im1.show()
# 新建图片
# im1 = Image.new("RGBA",(800,300),(136,136,136))

# im1 = addTransparency(im1, factor = 0.1)

# print(im1.mode)

# 获取图片打印格式
# print(im1.format)

# im2 = Image.blend(im,im1,1)

# im1.show()

# 保存文件
# im.save("../../../../../bia/demo.jpg","JPEG")
# 
im1 = Image.open("../../../../../bia/demo.jpg")

# im1 = im1.crop((0,0,1920,1056))

# im2 = Image.new("RGB",(1488,572),"#A9A9A9")

# im2 = circle_corner(im2, radii=50)

# im2 = addTransparency(im2,0.4)

# im1.paste(im2,(218,243))

# im1 = im1.resize((1080,300))
# im1 = im1.draft("RGB", (200,200))
# 
fnt=ImageFont.truetype("c:/Windows/Fonts/Tahoma.ttf", 40)
print(im1.size)
im1.show()
exit()