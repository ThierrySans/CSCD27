#!/usr/local/bin/python3
import os, sys, getopt

from caesar26 import encrypt, decrypt

def run(mode, key, filename):
    with open(filename, "r") as inputFile:
        data = inputFile.read()
        print(mode(key, data))
    
def usage():
    print ('Usage:	' + os.path.basename(__file__) + ' option file ')
    print ('Options:')
    print ('\t -e, --encrypt')
    print ('\t -d, --decrypt')
    print ('\t -k n, --key=n')
    sys.exit(2)

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hedk:",["help", "encrypt", "decrypt", "key="])
   except getopt.GetoptError as err:
      print(err)
      usage()
   # extract arguments
   mode = None
   key = None
   filename = args[0] if len(args) > 0 else None
   for opt, arg in opts:
        if opt in ("-h", "--help"):
           usage()
        elif opt in ("-e", "--encrypt"):
           mode = encrypt
        elif opt in ("-d", "--decrypt"):
           mode = decrypt
        elif opt in ("-k", "--key"):
           key = arg
   # check arguments
   if (mode is None):
       print('encrypt/decrypt option is missing\n')
       usage()
   if (key is None):
       print('key option is missing\n')
       usage()
   if (filename is None):
       print('input file is missing\n')
       usage()
   # run command
   run(mode, key, filename)

if __name__ == "__main__":
   main(sys.argv[1:])