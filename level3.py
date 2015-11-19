import urllib2
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"

def main():
    page = urllib2.urlopen(url)
    data = page.read()
    print "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', data))

if __name__ == "__main__":
    main()
