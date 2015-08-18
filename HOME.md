Welcome to the mp3-tag-autoeditor wiki!

* Author - Ashwani Agarwal
* Language Used - Python 2(.7)
* Extra Lib - eyed3 (pip install eyed3)
* Tags Saved - Title, Album, Artist, Album-Artist, Genre, Year, Track Number, Total Track Number, Cover Art

#### Problem -
If, I've downloaded songs from DJMaza or any other site, Meta-tags of MP3 files are polluted with Websites name. Now I want to remove those unnecessary tags.

#### Approach -

1. Select the extracted folder, where all MP3s are located.
2. Ask User for pattern of tags. (Exp. <title> <extra-char> <website> = "Rabbe | DJMaza")
  1. Ask for Album, Genre, Year, Total Track No. since it will be same for all the tracks.
  2. Ask for Title, Track Number[1], Album-Artist, Artist Pattern
  3. Cover Art
    1. Whether to get from Internet (saavn.com or itunes.com can be used)
    2. Select file dialog
3. Start the Process 
  1. Save all the tags first (8 Tags; not cover art)
  2. Clears all the tags
  3. Update tag as per 2.1 and 2.2
  4. Update Cover Art
  5. Save Tags
4. Rename Coverart image to folder.jpg and make that system hidden (Windows Only; for thubnail preview)




[1] Downloadming also pollute track number with website name.