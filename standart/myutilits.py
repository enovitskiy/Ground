from PIL import Image
import os

def resize_image(img,
                 output_image_path,
                 size):
    original_image = img

    width, height = original_image.size
    if (width - size[0]) >= (height - size[1]):
        size1 = [size[0], int(round(size[0] * height / width, 0))]
    else:
        size1 = [int(round(size[1] * width / height, 0)), size[1]]
    resized_image = original_image.resize(size1)
    # width, height = resized_image.size

    mask = resized_image.convert('RGBA')
    newimage = Image.new('RGB', size, '#ffffff')

    newimage.paste(resized_image.convert('RGBA'), ((size[0] - size1[0]) // 2, (size[1] - size1[1]) // 2), mask)
    newimage.save(output_image_path)


def Photoes(width,height,img,output_image_path,folder):
    try:
        os.makedirs(folder)
    except:
        pass
    exeption = {}
# try:
    resize_image(img=img,
                 output_image_path=output_image_path,
                 size=(width, height))
# except:
#         pass
    return exeption

if __name__ == '__main__':
    Photoes(photoes)