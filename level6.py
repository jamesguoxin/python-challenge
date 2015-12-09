import urllib2, re, zipfile

def main():
    url = "http://www.pythonchallenge.com/pc/def/channel.zip"
    # Download zip file as channel.zip
    f = zipfile.ZipFile("channel.zip")
    num = "90052"
    end = ".txt"
    key = ""
    while True:
        try:
            data = f.read(num + end)
        except:
            break
        key += f.getinfo(num + end).comment
        num = "".join(re.findall(r"Next nothing is (\d+)", data))
        print num
    print key

if __name__ == "__main__":
    main()
