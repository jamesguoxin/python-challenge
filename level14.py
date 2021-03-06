from PIL import Image

def main():
    im = Image.open("wire.png")
    new = Image.new("RGB", (100, 100), "black")

    count = 0
    flag = 0
    max = 99
    line = 1
    x = 0
    y = 0
    for i in xrange(10000):
        new.putpixel((x,y), im.getpixel((count, 0)))
        if (flag == 0):
            x += 1
        elif flag == 1:
            y += 1
        elif flag == 2:
            x -= 1
        else:
            y -= 1

        if (line == max):
            flag += 1
            line = 1
            if flag == 4:
                flag = 0
                max -= 2
                y += 1
                x += 1
        else:
            line += 1

        count += 1

    new.save("out14.png")

if __name__ == "__main__":
    main()
