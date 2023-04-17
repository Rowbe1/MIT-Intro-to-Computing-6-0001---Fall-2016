# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory():
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate
        


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    
    def is_phrase_in(self, text):
        self.text = text.lower()
        text_listed = []
        phrase_listed = []
        punc = string.punctuation
        space = ' '
        for item in punc:
            self.text = self.text.replace(item,' ')
        for item in self.text.split():
            text_listed.append(item)
        for item in self.phrase.split():
            phrase_listed.append(item)
        flag = False
        for item in phrase_listed:
            flag = item in text_listed
        if flag:
            single_space_text = space.join(text_listed)
            return self.phrase in single_space_text
        else:
            return flag

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        self.title = story.get_title()
        return PhraseTrigger.is_phrase_in(self, self.title)
        
# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        self.description = story.get_description()
        return PhraseTrigger.is_phrase_in(self, self.description)

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, time):
        time = datetime.strptime(time, "%d %b %Y %X")
        self.time = time.replace(tzinfo=pytz.timezone('EST'))

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
    
    def evaluate(self, story):
        story_time = story.get_pubdate()
        self.story_time = story_time.replace(tzinfo=pytz.timezone('EST'))
        return self.story_time < self.time
    
class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
        
    def evaluate(self, story):
        story_time = story.get_pubdate()
        self.story_time = story_time.replace(tzinfo=pytz.timezone('EST'))
        return self.story_time > self.time

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
        
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)
    

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)
    


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            print(trigger)
            if trigger.evaluate(story) == True:
                if story not in filtered_stories:
                    filtered_stories.append(story)
    return filtered_stories
    #return stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    
    all_items = []
    trigger_dict = {}
    triggerlist = []
    
    #transform lines into nested list
    for item in lines:
        all_items.append([part for part in item.split(',')]) 
    
    #convert nested list into dictionary with trigger names or 'ADD' as keys
    for item in all_items:
        trigger_dict[item[0]] = item[1:]
    
    #convert trigger specifications into trigger objects assigned to keys in dictionary
    #for 'ADD' put the relevant triggers into the triggerlist - objects specified by dictionary keys already defined
    for item in trigger_dict:
        if trigger_dict[item][0] == 'TITLE':
            trigger_dict[item] = TitleTrigger(trigger_dict[item][1])
        elif trigger_dict[item][0] == 'DESCRIPTION':
            trigger_dict[item] = DescriptionTrigger(trigger_dict[item][1])
        elif trigger_dict[item][0] == 'BEFORE':
            trigger_dict[item] = BeforeTrigger(trigger_dict[item][1]) 
        elif trigger_dict[item][0] == 'AFTER':
            trigger_dict[item] = AfterTrigger(trigger_dict[item][1])
        elif trigger_dict[item][0] == 'NOT':
            not_trig = trigger_dict[item][1]
            trigger_dict[item] = NotTrigger(trigger_dict[not_trig])
        elif trigger_dict[item][0] == 'AND':
            and_trig1 = trigger_dict[item][1]
            and_trig2 = trigger_dict[item][2]
            trigger_dict[item] = AndTrigger(trigger_dict[and_trig1],trigger_dict[and_trig2]) 
        elif trigger_dict[item][0] == 'OR':
            or_trig1 = trigger_dict[item][1]
            or_trig2 = trigger_dict[item][2]
            trigger_dict[item] = OrTrigger(trigger_dict[or_trig1],trigger_dict[or_trig2])
        elif item == 'ADD':
            for trig in trigger_dict[item]:
                triggerlist.append(trigger_dict[trig])
        
    print(triggerlist)    
    return triggerlist




SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        #t1 = TitleTrigger("Boris")
        #t2 = DescriptionTrigger("Covid")
        #t3 = DescriptionTrigger("Strike")
        #t4 = AndTrigger(t2, t3)
        #triggerlist = [t1, t2, t3, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            #stories = process("http://news.google.com/news/rss") #?output=rss
            stories = process("https://news.google.com/rss?hl=en-GB&gl=GB&ceid=GB:en")

            # Get stories from Yahoo's Top Stories RSS news feed
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

