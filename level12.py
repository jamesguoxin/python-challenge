# According to the picture in the http link, it seems to divide the .gfx file into 5 parts

def main():
    with open("evil2.gfx", "rb") as imdata:
        data = imdata.read()

    for i in range(5):
        with open("file"+str(i), "wb") as f:
            f.write(data[i::5])

if __name__ == "__main__":
    main()
