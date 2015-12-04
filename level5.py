import urllib2
import pickle

def print_line(pair_list):
    print ''.join(pair[0] * pair[1] for pair in pair_list)

def main():
    unzipped = []
    myFile = pickle.load(urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))  
    for pair_list in myFile:
        print_line(pair_list)

if __name__ == "__main__":
    main()
