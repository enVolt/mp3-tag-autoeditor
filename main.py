from tkFileDialog import askdirectory
from eyed3 import load as eyed3load
import coverimage
import extra
from os import name as os_name, system as os_system,\
    chdir as os_chdir, listdir as os_listdir, rename as os_rename
from Tkinter import Tk

extra.cls()

# Initial Welcome Message
print '''

    This program can be used to quickly edit tags.
    Works great with MP3 folder

    NOT TO BE USED WITH FOLDER, CONTAINING MP3 FROM DIFF ALBUMs

    Press any key to continue, and select the folder to start the process

>> ''',

raw_input()

root = Tk()
root.withdraw()

dirname = askdirectory(parent=root, title='Please select a directory')
extra.log("Dirname = "+dirname)
extra.cls()
# dirname = r'/home/ashwani/Music'


def getlistofMP3s(dirname):
    '''
    Returns a list of MP3 file names
    '''
    l = []
    for i in os_listdir(dirname):
        if str(i[-3:]).lower() == "mp3":
            l += [i]
    return l


def getTag(mp3, type):
    '''
    Return tag from MP3 file
    allowed value of type 'album','artist','album_artist','title',
    'track_num','genre','year','total_track'
    '''
    if type == "album":
        if mp3.tag.album is None:
            return ""
        else:
            return mp3.tag.album
    elif type == "artist":
        if mp3.tag.artist is None:
            return ""
        else:
            return mp3.tag.artist
    elif type == "album_artist":
        if mp3.tag.album_artist is None:
            return ""
        else:
            return mp3.tag.album_artist
    elif type == "title":
        if mp3.tag.title is None:
            return ""
        else:
            return mp3.tag.title
    elif type == "track_num":
        if mp3.tag.track_num[0] is None:
            return ""
        else:
            return str(mp3.tag.track_num[0])
    elif type == "genre":
        try:
            mp3.tag.genre.name
        except:
            return ""
        else:
            return mp3.tag.genre.name
    elif type == "year":
        if mp3.tag.best_release_date is None:
            return ""
        else:
            return str(mp3.tag.best_release_date)
    elif type == "total_track":
        if mp3.tag.track_num[1] is None:
            return ""
        else:
            return str(mp3.tag.track_num[1])


def getFinalTag(mp3, type):
    '''
    Return tag from local execution scope
    allowed value of type 'album','artist','album_artist','title',
    'track_num','genre','year','total_track'
    '''
    if type == "album":
        try:
            final_album
        except:
            return getTag(mp3, 'album')
        else:
            return final_album

    elif type == "artist":
        try:
            final_artist
        except:
            try:
                artistini
            except:
                return getTag(mp3, 'artist')
            else:
                return getTag(mp3, 'artist'). \
                    split(" ", artistini)[artistini]. \
                    rsplit(" ", artistfin)[0]
        else:
            return final_artist

    elif type == "album_artist":
        try:
            final_album_artist
        except:
            try:
                album_artistini
            except:
                return getTag(mp3, 'album_artist')
            else:
                return getTag(mp3, 'album_artist'). \
                    split(" ", album_artistini)[album_artistini]. \
                    rsplit(" ", album_artistfin)[0]
        else:
            return final_album_artist
    elif type == "title":
        try:
            titleini
        except:
            return getTag(mp3, 'title')
        else:
            return getTag(mp3, 'title'). \
                split(" ", titleini)[titleini]. \
                rsplit(" ", titlefin)[0]

    elif type == "track_num":
        try:
            track_numini, track_numfin
        except:
            return getTag(mp3, 'track_num')
        else:
            return track_num. \
                split(" ", track_numini)[track_numini]. \
                rsplit(" ", track_numfin)[0]
    elif type == "genre":
        try:
            final_genre
        except:
            return getTag(mp3, 'genre')
        else:
            return genre

    elif type == "year":
        try:
            final_year
        except:
            return getTag(mp3, 'year')
        else:
            return year

    elif type == "total_track":
        try:
            final_total_track
        except:
            return getTag(mp3, 'total_track')
        else:
            return total_track


def setTag(mp3, type_value, type):
    '''
    Set tag from MP3 file (mp3 = eyed3.load("File.mp3"))
    allowed value of type 'album','artist','album_artist','title',
    'track_num','genre','year','total_track'
    '''
    if type == "album":
        mp3.tag.album = unicode(getFinalTag(mp3, 'album'))
    elif type == "artist":
        mp3.tag.artist = unicode(getFinalTag(mp3, 'artist'))
    elif type == "album_artist":
        mp3.tag.album_artist = unicode(getFinalTag(mp3, 'album_artist'))
    elif type == "title":
        mp3.tag.title = unicode(getFinalTag(mp3, 'title'))
    elif type == "track":
        # Track_num = (TrackNumber, Total Track) //Tuple
        track_num = (getFinalTag(mp3, 'track_num'))
        total_track = (getFinalTag(mp3, 'total_track'))
        mp3.tag.track_num = (track_num, total_track)
    elif type == "genre":
        mp3.tag.genre = unicode(getFinalTag(mp3, 'genre'))
    elif type == "year":
        mp3.tag.release_date = getFinalTag(mp3, 'year')


def printMenu(mp31):
    extra.cls()
    print '''
        +-------------------------------+
        +                               +
        +      MP3 Tag Auto-editor      +
        +                               +
        +-------------------------------+
      1. Select Album ('''+getFinalTag(mp31, 'album')+''')
      2. Edit Artist Pattern ('''+getFinalTag(mp31, 'artist')+''')
      3. Edit Title Pattern ('''+getFinalTag(mp31, 'title')+''')
      4. Select Genre ('''+getFinalTag(mp31, 'genre')+''')
      5. Select Year ('''+getFinalTag(mp31, 'year')+''')
      6. Edit Album-Artist Pattern ('''+getFinalTag(mp31, 'album_artist')+''')
      7. Edit Track Number Pattern ('''+getFinalTag(mp31, 'track_num')+''')
      8. Select Total Track Number ('''+getFinalTag(mp31, 'total_track')+''')
      9. Select Artist ('''+getFinalTag(mp31, 'artist')+''') (Change for all MP3s)
     10. Select Album-Artist ('''+getFinalTag(mp31, 'album_artist')+''') (Change for all MP3s)
     11. Select Cover-Art ('coverart.jpg' will be used by default in selected folder)
      0. ~~~ Do the Magic ~~~
      Enter Choice >> ''',

mp3files = getlistofMP3s(dirname)
extra.log(str(mp3files))
mp31 = eyed3load(dirname+"/"+mp3files[0])
ch = 10

while ch != 0:
    extra.log("Entered in loop")
    printMenu(mp31)
    ch = int(input())
    if ch == 1:
        ''' Abum Name '''
        final_album = raw_input("Enter Album Name >> ")
    elif ch == 2:
        ''' Artist Pattern '''
        while True:
            print "Enter Initial word count, End word count (0 if none) >> ",
            artistini, artistfin = [int(x) for x in raw_input().split()]
            print str(mp31.tag.artist). \
                split(" ", artistini)[artistini]. \
                rsplit(" ", artistfin)[0]
            okprompt = raw_input("Is it OK ? (Y or N) >> ").lower()
            if okprompt == 'y':
                break
    elif ch == 3:
        ''' Title Pattern '''
        while True:
            print "Enter Initial word count, End word count (0 if none) >> ",
            titleini, titlefin = [int(x) for x in raw_input().split()]
            print str(mp31.tag.title). \
                split(" ", titleini)[titleini]. \
                rsplit(" ", titlefin)[0]
            okprompt = raw_input("Is it OK ? (Y or N) >> ").lower()
            if okprompt == 'y':
                break
    elif ch == 4:
        ''' Genre '''
        final_genre = raw_input("Enter Genre >> ")
    elif ch == 5:
        ''' Release Year '''
        final_year = raw_input("Enter Release Year >> ")
    elif ch == 6:
        ''' Album-Artist Pattern '''
        while True:
            print "Enter Initial word count, End word count (0 if none) >> ",
            album_artistini, album_artistfin = [int(
                x) for x in raw_input().split()]
            print str(mp31.tag.album_artist). \
                split(" ", album_artistini)[album_artistini]. \
                rsplit(" ", album_artistfin)[0]
            okprompt = raw_input("Is it OK ? (Y or N) >> ").lower()
            if okprompt == 'y':
                break
    elif ch == 7:
        ''' Track Number Pattern '''
        while True:
            print "Enter Initial word count, End word count (0 if none) >> ",
            track_numini, track_numfin = [int(x) for x in raw_input().split()]
            print str(mp31.tag.track_num[0]). \
                split(" ", track_numini)[track_numini]. \
                rsplit(" ", track_numfin)[0]
            okprompt = raw_input("Is it OK ? (Y or N) >> ").lower()
            if okprompt == 'y':
                break
    elif ch == 8:
        ''' Total Track Number '''
        final_total_track = raw_input("Enter total track number >> ")
    elif ch == 9:
        ''' Artist for all MP3s '''
        final_artist = raw_input("Enter Artist >> ")
    elif ch == 10:
        ''' Album-Artist for all MP3s '''
        final_album_artist = raw_input("Enter Album-Artist >> ")
    elif ch == 11:
        final_image = coverimage.getCoverImage(
            dirname, getFinalTag(mp31, 'album'))
    else:
        pass


for i in mp3files:
    aud = eyed3load(dirname+"/"+i)
    # Save the tags first
    title = getFinalTag(aud, 'title')
    album = getFinalTag(aud, 'album')
    album_artist = getFinalTag(aud, 'album_artist')
    artist = getFinalTag(aud, 'artist')
    genre = getFinalTag(aud, 'genre')
    year = getFinalTag(aud, 'year')
    track_num = getFinalTag(aud, 'track_num')
    total_track = getFinalTag(aud, 'total_track')
    # Remove all the tags (everything)
    extra.log("File = "+i)
    extra.log(title+album+album_artist+artist)
    aud.tag.clear()
    # Update New Tags
    setTag(aud, title, 'title')
    setTag(aud, artist, 'artist')
    setTag(aud, album, 'album')
    setTag(aud, album_artist, 'album_artist')
    setTag(aud, (track_num, total_track), 'track')
    setTag(aud, genre, 'genre')
    setTag(aud, year, 'year')
    try:
        final_image
    except:
        final_image = coverimage.getCoverImage(dirname, album)
    if final_image:
        extra.log("saving cover")
        aud.tag.images.set(3, final_image, "image/jpeg", u"")
    # Save the tags to file,
    # After using tag.clear() method, need to supply file name to save tag
    aud.tag.save(dirname+"/"+i, version=(1, None, None))
    aud.tag.save(dirname+"/"+i, version=(2, 4, 0))
    # Finally, Rename file as format '%tn %title'
    extra.log(str(aud.tag.track_num[0])+aud.tag.title)

extra.cls()
ch = raw_input("Do you wish to rename files? >> (Y/N) ").lower()
if ch == 'y':
    print '''\n
    Select Pattern
    1. <Track Number> <Title> (default)
    2. <Artist> - <Title>\n
    >> ''',
    ch = raw_input()
    for i in mp3files:
        aud = eyed3load(dirname+"/"+i)
        if ch == '2':
            ren_pattern = str(aud.tag.artist)+" - "+aud.tag.title
        else:
            ren_pattern = str(aud.tag.track_num[0])+" "+aud.tag.title
        new_name = dirname+"/"+ren_pattern+".mp3"
        os_rename(dirname+"/"+i, new_name)

extra.cls()
print '''
    All Set, Exiting the program, 
    If you've faced any problem, please send log.txt file to author
    Else delete that file

    Press Any Key to Exit.......
    ''',
raw_input()
