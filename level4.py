import urllib2
import re

def main():
    ending = "25357"
    i = 0
    while i == 0:
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + ending
        print ending
        response = urllib2.urlopen(url)
        text = response.read()
        number = re.search(r'the next nothing is (\d+)', text).group(1)
        ending = "".join(number)
        if ending == "":
            print text
            i = 1
            print ending

if __name__ == "__main__":
    main()
