# import libraries
import urllib.request as req
import sys
try:
    # create function
    def shorturl(url):
        # set the api of a url shortner to a var
        apiurl = "http://tinyurl.com/api-create.php?url="
        shorturl = req.urlopen(apiurl + url).read() #  append parameter to the api
        return shorturl.decode("utf-8")

    inurl = input("Enter or paste url to shorten here >>> ")
    BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

    sys.stdout.write(f"\nYour short-linked URL is\n>>> {RED} {shorturl(inurl)} {END}\n")

except KeyboardInterrupt:
    print("\n\nThank For using this app!!!!")
