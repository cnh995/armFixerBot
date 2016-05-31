#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#Above lines are added for Linux compatibility

#import
import praw
import time
import os
import pdb
import re
from armFixer import *

if not os.path.isfile("commentsRepliedTo.txt"):
    commentsRepliedTo = []
else:
    with open("commentsRepliedTo.txt", "r") as f:
        commentsRepliedTo = f.read()
        commentsRepliedTo = commentsRepliedTo.split("\n")

#logging in to reddit
r = praw.Reddit(user_agent = "ArmFixerBot")
r.login("username", "password") #No, these aren't the actual username and password

def run_bot():
    try:
        subreddit = r.get_subreddit("all") #insert subreddit in double quotes
        comments = subreddit.get_comments(limit = 100)  #searches comments
        keywords = ["¯\_(ツ)_/¯","¯\\\_(ツ)_/¯","¯\\\_(ツ)_/¯","¯\\\_(ツ)_/¯","¯\\\\_(ツ)_/¯","¯_(ツ)_/¯\ ","¯_(ツ)_/¯\\"] #sets up keywords to look for
        dskeywords = ["\[T]/","[T]/"] #Looks for the Dark Souls emote
        for comment in comments:
            comment_text = comment.body
            commentMatch = any(string in comment_text for string in keywords) #searches for matches between comment body and keywords list
            print(commentMatch)
            if commentMatch and comment.id not in commentsRepliedTo:
                comment.reply('I think you were trying to make this ¯\\\\\\_(ツ)\_/¯!  \n  Type it like this ¯\\\\\\\\\\\\\_(ツ)\_/¯  \n  ^^I ^^am ^^a ^^bot, ^^visit ^^/r/ArmFixerBot ^^for ^^more ^^info!') #enter comment reply in quotes
                commentsRepliedTo.append(comment.id)
                with open("commentsRepliedTo.txt", "w") as f: #adds comment id to a list, so it will never be replied to again
                    for comment_id in commentsRepliedTo:
                        f.write(comment_id + "\n")

            #Don't look for certain items, prevents issues with infinite comment loops
            dontFind = ["\\\\\\[T]/", "\\\\[T]/", "\\\\\\\[T]/", "\\\\\[T]/", "\\\\\\\\[T]/", "\\\\\\\\\[T]/", "\\\\\\\\\\[T]/", "\\\[T]/", "\\\\\\\\\\\[T]/", "\\\\\\\\\\\[T]/", "\\\\\\\\\\\\[T]/", "\\\[T]/"]
            repeatMatch = any(string in comment_text for string in dontFind)
            dsCommentMatch = any(string in comment_text for string in dskeywords) #searches for the dark souls arm mistakes
            print(dsCommentMatch) #Notify me if comment is found
            if dsCommentMatch and comment.id not in commentsRepliedTo and repeatMatch == False:
                comment.reply('I think you were trying to make this  \\\\\\[T]/!  \n  Type it like this  \\\\\\\[T]/  \n  ^^I ^^am ^^a ^^bot, ^^visit ^^/r/ArmFixerBot ^^for ^^more ^^info!') #enter comment reply in quotes
                commentsRepliedTo.append(comment.id)
                with open("commentsRepliedTo.txt", "w") as f: #adds comment id to a list, so it will never be replied to again
                    for comment_id in commentsRepliedTo:
                        f.write(comment_id + "\n")

    #Error handling
    except Exception as e:
        print(type(e))
    
#puts bot to sleep after running out of posts or comments to look for
while True:
    run_bot()
    time.sleep(10)
