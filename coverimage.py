from json import loads as json_loads
from urllib import urlopen, urlretrieve
import extra
from os.path import isfile
from tkFileDialog import askopenfile


def getcoverURL(search, resultCount=10):
    '''
    It will return the URL to coverart image
    '''
    extra.cls()
    # search = "drishyam"
    # resultCount = 10
    # This Custom Search Engine of google, search on www.saavn.com
    #  and itunes.apple.com for albums
    searchengineid = "014954134512375095903%3A1jlepwhgf1k"
    APIKey = str(raw_input("Please enter your Google API Key \n \
        Press 0 to browse image instead from your computer\n>> "))
    if APIKey == '0':
        return False
    print "Searching for " + search + "\n Do you wish to change album name (Y/N)?"
    ch = str(raw_input(">> ")).lower()
    if ch == 'y':
        search = str(raw_input("Enter Album name to search\n>> "))
    extra.log("Searching for " + search + "\n")
    url = "https://www.googleapis.com/customsearch/v1?" + \
        "q=" + search + \
        "&num=" + str(resultCount) + \
        "&cx=" + searchengineid + \
        "&key=" + APIKey
    extra.log("SearchURL = " + url)

    try:
        source = urlopen(url)
    except:
        extra.log("Can't connect to internet, unable to edit cover image")
        raw_input("Internet Issues, Press any key to browse cover image")
        return False
    # source = open('json.txt').read()

    parsedJSON = json_loads(source.read())

    if "error" in parsedJSON:
        extra.log("Please Update API Key")
        return False

    i = 1
    for each in parsedJSON["items"]:
        print i, each["title"], each["displayLink"]
        i += 1
    print "Enter your choice\n>> ",
    ch = int(input())
    # ch = 4
    url = parsedJSON["items"][ch - 1]["pagemap"]["cse_image"][0]["src"]
    if parsedJSON["items"][ch - 1]["displayLink"] == "www.saavn.com":
        pass
    else:
        url = url.replace("326x326", "600x600")

    return url


def getCoverImage(dirname, album):
    '''
    This function will return image as an object,
    if coverart.jpg exists in same folder,
    else getcoverURL method will be called on album
    '''
    if not isfile(dirname + "/coverart.jpg"):
        coverurl = getcoverURL(album, 10)
        if coverurl:
            urlretrieve(coverurl, dirname + "/coverart.jpg")
            imagedata = open(dirname + "/coverart.jpg", "rb").read()
            return imagedata
        else:
            try:
                imagepath
            except:
                imagepath = askopenfile(mode='rb')
                return imagepath.read()
            else:
                return imagepath.read()
    else:
        raw_input(
            "Using coverart.jpg as default, Press any key to continue ..... ")
        return open(dirname+'/coverart.jpg', 'rb').read()
