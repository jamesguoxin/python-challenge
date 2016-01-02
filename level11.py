from PIL import Image
import numpy as np

def main():
    im = Image.open("cave.jpg")
    width, height = im.size
    imdata = np.array(im.getdata(),
                      np.uint8).reshape(height, width, 3)
    im1 = imdata[0:height:2, 0:width:2, :]
    im2 = imdata[0:height:2, 1:width:2, :]
    im3 = imdata[1:height:2, 0:width:2, :]
    im4 = imdata[1:height:2, 1:width:2, :]
    sub_im = Image.new(im.mode, (width/2, height/2))
    # print im4.reshape((-1, 3)).shape
    im4 = im4.reshape((-1, 3)).tolist()
    data = [tuple(pixel) for pixel in im4]
    sub_im.putdata(data)
    sub_im.show()

if __name__ == "__main__":
    main()
