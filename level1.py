import string

encrypted = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

url = "http://www.pythonchallenge.com/pc/def/map.html"
url = "map"

def main():
    str_to_print = ""
    for letter in url:
        if letter.isalpha():
            index = string.lowercase.index(letter)
            index = (index + 2) % 26
            letter = string.lowercase[index]
            str_to_print += letter
        else:
            str_to_print += letter
    print str_to_print

if __name__ == "__main__":
    main()
