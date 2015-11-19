import urllib2

url = "http://www.pythonchallenge.com/pc/def/ocr.html"

def main():
    page = urllib2.urlopen(url)
    data = page.read()
    print data

if __name__ == "__main__":
    main()
