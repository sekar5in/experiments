# This is script is used to validate the youtube URL video.
# If error occurs it notification generates
# Author : Dhanasekara Pandian
# Email : sekar5in@quehive.com

import pafy
import youtubevalidator.dbconnector as yt

# Error video : "https://www.youtube.com/watch?v=8hYdV2Vi6Qs"
# 5RKI9_B7tOg
# ykmEajHcYkk - restricted video only to watch in youtube
# C7MAqIcM-Sg
# cyMHZVT91Dw
# Vidya Vox https://www.youtube.com/watch?v=tRLConvNTYg

# Connect with Database
c,conn = yt.lopConnection()

try:

    c.execute("SELECT FILM_NAME, SONG_NAME, YOUTUBE_URL FROM loptamil")
    ytData = c.fetchall()

    # Opening the File.
    saveWorkingUrl = open('WorkingUrl.txt', 'w')
    saveNotWorkingUrl = open('NotWorkingUrl.txt', 'w')

    for i in ytData:
        try:
            url = i[2]
            video = pafy.new(url)
            saveWorkingUrl.write("%s , %s , %s \n" %(i[0],i[1],i[2]))

        except Exception as e:
            saveNotWorkingUrl.write("%s , %s , %s \n" % (i[0], i[1], i[2]))


    saveWorkingUrl.close()
    saveNotWorkingUrl.close()
    c.close()
    conn.close()

except Exception as e:
    print(e)
