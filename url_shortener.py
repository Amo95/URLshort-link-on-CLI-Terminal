# import libraries
import urllib.request as req

# create function
def shorturl(url):
    # set the api of a url shortner to a var
    apiurl = ""
    shorturl = req.urlopen(apiurl + url).read() #  append parameter to the api
    return shorturl.decode("utf-8")

inurl = input("Enter or paste url to shorten here >>> ")
print(shorturl(inurl))
