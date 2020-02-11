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
    RED, END = '\033[91m', '\033[0m' # adding colors to style answers

    sys.stdout.write(f"\nYour short-linked URL is\n>>> {RED} {shorturl(inurl)} {END}\n")

except KeyboardInterrupt:
    print("\n\nThank For using this app!!!!")
