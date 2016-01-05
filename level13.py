import xmlrpclib

def main():
    proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print proxy.system.listMethods()
    print proxy.system.methodHelp("phone")
    print proxy.phone("Bert")

if __name__ == "__main__":
    main()
