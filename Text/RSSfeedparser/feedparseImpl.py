"""
    Written By: Srinivas Avireddy
    Date : 11/28/2013
    This programs is used to for basic parsing of a RSS feed url
"""
import feedparser

# Feedparser is an python API to manipulate the RSS feed data into dictionary format with several key/value pairs


def printChannelInfo(feedInfo):
    # This method manipulates the general info about the RSS feed like its URL, Description, Version etc
    args = ["title","description","link"]
    
    if "url" in feedInfo:
        print ("\n The url for this feed is: \n %s \n") % feedInfo["url"]

    if "version" in feedInfo:
        print ("The version for this feed is: \n %s \n") % feedInfo["version"]

    if "channel" in feedInfo:
        for arg in args:
            if arg in feedInfo["channel"]:
                print ("The channel %s  : \n %s ") % (arg,feedInfo["channel"][arg])
        print "\n"

    

def printFeedItemInfo(feedInfo):
    # This method manipulates each item in the feed and displays each field(like title, summary, link)associated with the item
    items = feedInfo["items"]
    args = ["title","summary","link"]
    for item in items:
        print "########################################"
        for arg in args:
            if arg in item:
                print ("%s  : \n %s ") % (arg,item[arg])
        print "\n"
    

def main():
    url = raw_input("enter the RSS feed url to parse: ")
    feedInfo = feedparser.parse(url)
    # bozo is one of the key/value pair as result of parsing the RSS feed.
    # It is set to 1 if its not a valid RSS feed , else it is set to 0
    if feedInfo["bozo"] == 0:
        printChannelInfo(feedInfo)
        printFeedItemInfo(feedInfo)
    else:
        print "invalid RSS feed URL"

if __name__=="__main__":
    main()

