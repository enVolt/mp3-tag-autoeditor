import tkFileDialog,urllib
import eyed3, os, json
import os
from Tkinter import *

root = Tk()
root.withdraw()

dirname = tkFileDialog.askdirectory(parent=root,  title='Please select a directory')
# dirname = os.getcwd()

# dirname = r'/home/ashwani/Music'

def cls():
    ''' clears the terminal '''
    os.system("clear")

def getcoverURL(search,resultCount=10):
    '''
    It will return the URL to coverart image
    '''
    # search = "drishyam"
    # resultCount = 10
    searchengineid = "014954134512375095903%3A1jlepwhgf1k"
    APIKey = "Google API Key"

    url = "https://www.googleapis.com/customsearch/v1?" + \
            "q="+search + \
            "&num="+str(resultCount) + \
            "&cx="+searchengineid + \
            "&key="+APIKey

    print url

    source = urllib.urlopen(url)

    # source = open('json.txt').read()

    parsedJSON = json.loads(source.read())

    i = 1
    for each in parsedJSON["items"]:
        print i,each["title"], each["displayLink"]
        i += 1
    print "Enter your choice\n>> " ,
    ch = int(input())
    # ch = 4

    if parsedJSON["items"][ch-1]["displayLink"] == "www.saavn.com":
        url =  parsedJSON["items"][ch-1]["pagemap"]["cse_image"][0]["src"]
    else:
        url = parsedJSON["items"][ch-1]["pagemap"]["cse_image"][0]["src"].replace("326x326","600x600")

    return url

def getlistofMP3s(dirname):
    '''
    Returns a list of MP3 file names
    '''
    l = []
    for i in os.listdir(dirname):
        if str(i[-3:]).lower() == "mp3":
            l += [i]
    return l

def getCoverImage(album):
    '''
    This function will return image as an object, if coverart.jpg exists in same folder,
    else getcoverURL method will be called on album
    '''
    if not os.path.isfile(dirname+"/coverart.jpg"):
        coverurl = getcoverURL(album,10)
        urllib.urlretrieve(coverurl,dirname+"/coverart.jpg")
    imagedata = open(dirname+"/coverart.jpg","rb").read()
    return imagedata

def getTag(mp3,type):
    '''
    Return tag from MP3 file
    allowed value of type 'album','artist','album_artist','title',
    'track_num','genre','year','total_track'
    '''
    if type == "album":
        if mp3.tag.album == None:
            return album
        else:
            return mp3.tag.album
    elif type == "artist":
        if mp3.tag.artist == None:
            return artist
        else:
            return mp3.tag.artist
    elif type == "album_artist":
        if mp3.tag.album_artist == None:
            return album_artist
        else:
            return mp3.tag.album_artist
    elif type == "title":
        if mp3.tag.title == None:
            return title
        else:
            return mp3.tag.title
    elif type == "track_num":
        if mp3.tag.track_num[0] == None:
            return track_num
        else:
            return str(mp3.tag.track_num[0])
    elif type == "genre":
        try:
            mp3.tag.genre.name
        except:
            return genre
        else:
            return mp3.tag.genre.name
    elif type == "year":
        if mp3.tag.best_release_date == None:
            return year
        else:
            return str(mp3.tag.best_release_date)
    elif type == "total_track":
        if mp3.tag.track_num[1] == None:
            return ""
        else:
            return str(mp3.tag.track_num[1])

def getFinalTag(mp3,type):
    '''
    Return tag from local execution scope
    allowed value of type 'album','artist','album_artist','title',
    'track_num','genre','year','total_track'
    '''
    if type == "album":
        try:
            album
        except:
            return getTag(mp3,'album')
        else:
            return album

    elif type == "artist":
        try:
            artistini
        except:
            return getTag(mp3,'artist')
        else:
            return getTag(mp3,'artist').split(" ",artistini)[artistini].rsplit(" ",artistfin)[0]

    elif type == "album_artist":
        try:
            album_artistini
        except:
            return getTag(mp3,'album_artist')
        else:
            return getTag(mp3,'album_artist').split(" ",album_artistini)[album_artistini].rsplit(" ",album_artistfin)[0]

    elif type == "title":
        try:
            titleini
        except:
            return getTag(mp3,'title')
        else:
            return getTag(mp3,'title').split(" ",titleini)[titleini].rsplit(" ",titlefin)[0]

    elif type == "track_num":
        try:
            track_numini,track_numfin
        except:
            return getTag(mp3,'track_num')
        else:
            return track_num.split(" ",track_numini)[track_numini].rsplit(" ",track_numfin)[0]
    elif type == "genre":
        try:
            genre
        except:
            return getTag(mp3,'genre')
        else:
            return genre

    elif type == "year":
        try:
            year
        except:
            return getTag(mp3,'year')
        else:
            return year

    elif type == "total_track":
        try:
            total_track
        except:
            return getTag(mp3,'total_track')
        else:
            return total_track

def setTag(mp3,type):
    '''
    Set tag from MP3 file (mp3 = eyed3.load("File.mp3"))
    allowed value of type 'album','artist','album_artist','title',
    'track_num','genre','year','total_track'
    '''
    if type == "album":
        mp3.tag.album = unicode(getTag(mp3,'album'))
    elif type == "artist":
        mp3.tag.artist = unicode(getTag(mp3,'artist'))
    elif type == "album_artist":
        mp3.tag.album_artist = unicode(getTag(mp3,'album_artist'))
    elif type == "title":
        mp3.tag.title = unicode(getTag(mp3,'title'))
    elif type == "track":
        mp3.tag.track_num = (getTag(mp3,'track_num'), getTag(mp3,'total_track'))
    elif type == "genre":
        mp3.tag.genre = unicode(getTag(mp3,'genre'))
    elif type == "year":
        mp3.tag.release_date = getTag(mp3,'year')

def printMenu(mp31):
    cls()
    print '''
        +-------------------------------+
        +                               +
        +      MP3 Tag Auto-editor      +
        +                               +
        +-------------------------------+

      1. Select Album ('''+getFinalTag(mp31,'album')+''')
      2. Edit Artist Pattern ('''+getFinalTag(mp31,'artist')+''')
      3. Edit Title Pattern ('''+getFinalTag(mp31,'title')+''')
      4. Select Genre ('''+getFinalTag(mp31,'genre')+''')
      5. Select Year ('''+getFinalTag(mp31,'year')+''')
      6. Edit Album-Artist Pattern ('''+getFinalTag(mp31,'album_artist')+''')
      7. Edit Track Number Pattern ('''+getFinalTag(mp31,'track_num')+''')
      8. Edit Total Track Number ('''+getFinalTag(mp31,'total_track')+''')
      9. ~~~ Do the Magic ~~~
      Enter Choice >> ''',

mp3files = getlistofMP3s(dirname)
mp31 = eyed3.load(dirname+"/"+mp3files[0])
ch = 0

while ch != 9:
    printMenu(mp31)
    ch = int(input())
    if ch == 1:
        ''' Abum Name '''
        album = raw_input("Enter Album Name >> ")
    elif ch == 2:
        ''' Artist Pattern '''
        while True:
            print "Enter Initial word count, End word count (0 if none) >> ",
            artistini,artistfin = [int(x) for x in raw_input().split()]
            print str(mp31.tag.artist).split(" ",artistini)[artistini].rsplit(" ",artistfin)[0]
            okprompt = raw_input("Is it OK ? (Y or N) >> ").lower()
            if okprompt == 'y':
                break
    elif ch == 3:
        ''' Title Pattern '''
        while True:
            print "Enter Initial word count, End word count (0 if none) >> ",
            titleini,titlefin = [int(x) for x in raw_input().split()]
            print str(mp31.tag.title).split(" ",titleini)[titleini].rsplit(" ",titlefin)[0]
            okprompt = raw_input("Is it OK ? (Y or N) >> ").lower()
            if okprompt == 'y':
                break
    elif ch == 4:
        ''' Genre '''
        genre = raw_input("Enter Genre >> ")
    elif ch == 5:
        ''' Release Year '''
        year = raw_input("Enter Release Year >> ")
    elif ch == 6:
        ''' Album-Artist Pattern '''
        while True:
            print "Enter Initial word count, End word count (0 if none) >> ",
            album_artistini,album_artistfin = [int(x) for x in raw_input().split()]
            print str(mp31.tag.album_artist).split(" ",album_artistini)[album_artistini].rsplit(" ",album_artistfin)[0]
            okprompt = raw_input("Is it OK ? (Y or N) >> ").lower()
            if okprompt == 'y':
                break
    elif ch == 7:
        ''' Track Number Pattern '''
        while True:
            print "Enter Initial word count, End word count (0 if none) >> ",
            track_numini,track_numfin = [int(x) for x in raw_input().split()]
            print str(mp31.tag.track_num[0]).split(" ",track_numini)[track_numini].rsplit(" ",track_numfin)[0]
            okprompt = raw_input("Is it OK ? (Y or N) >> ").lower()
            if okprompt == 'y':
                break
    elif ch == 8:
        ''' Total Track Number '''
        total_track = raw_input("Enter total track number >> ")
    else:
        pass


for i in mp3files:
    aud = eyed3.load(dirname+"/"+i)
    # Save the tags first
    title = getFinalTag(aud,'title')
    album = getFinalTag(aud,'album')
    album_artist = getFinalTag(aud,'album_artist')
    artist = getFinalTag(aud,'artist')
    genre = getFinalTag(aud,'genre')
    year = getFinalTag(aud,'year')
    track_num = getFinalTag(aud,'track_num')
    total_track = getFinalTag(aud,'total_track')
    # Remove all the tags (everything)
    aud.tag.clear()
    # # Update New Tags
    setTag(aud,'title')
    setTag(aud,'artist')
    setTag(aud,'album')
    setTag(aud,'album_artist')
    setTag(aud,'track')
    setTag(aud,'genre')
    setTag(aud,'year')
    aud.tag.images.set(3,getCoverImage(album),"image/jpeg",u"")
    # Save the tags to file,
    # After using tag.clear() method, need to supply file name to save tag
    aud.tag.save(dirname+"/"+i,version=(1,None,None))
    aud.tag.save(dirname+"/"+i,version=(2,4,0))

    # Finally, Rename file as format '%tn %title'
    new_name = dirname+"/"+str(aud.tag.track_num[0])+" "+aud.tag.title+".mp3"
    os.rename(dirname+"/"+i, new_name)
