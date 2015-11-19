import urllib2
import re

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
key = "#@!$%+{}[]_-&*()*^@/"
def main():
    page = urllib2.urlopen(url)
    data = page.read()
    result = ""
    for letter in data:
        if letter not in key:
            result += letter
    print result

if __name__ == "__main__":
    main()
