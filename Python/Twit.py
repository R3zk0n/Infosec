import requests
import argparse
from bs4 import BeautifulSoup
import sqlite3
import time






# Assumptions.
# Using known decent libs alot such as openssl is better then rolling your own crypto which is extremely easy to mess up.
# Output the 5 most recent and then new tweets and display them all? or...just the most recent 5?..
# Using sqlite3 might be a bad idea if the database gets large as it can be slow to load..
# Error logging could be done much better, there is no error logging.. \0/
# This is now quiet easy to write an API up say using flask if the post command is "dump"  == Select * from database; print, type of thing.
# Threading could be done too.



def Database():
    conn = sqlite3.connect('twitter.db')
    c = conn.cursor()
    try:
        c.execute("select * from twits")
    except sqlite3.OperationalError:
        c.execute("create table twits(id integer primary key UNIQUE, twit text NOT NULL UNIQUE, user text)")
        conn.commit()
        c.close()
        print("Database Started")

# this is super hacky away to ensure only new twits are printed out, however it does "Work"..
def Twit(user, idx):
    con = sqlite3.connect('twitter.db')
    c = con.cursor()
    ctr = int(idx)
    twitter_account = user
    res = requests.get("https://mobile.twitter.com/" + twitter_account)
    bs = BeautifulSoup(res.content, 'lxml')
    all_tweets = bs.find_all('div', {'class': 'tweet-text'})
    count = 0
    if all_tweets:
        for tweet in all_tweets[:ctr]:
            count += 1
            clean = tweet.text.strip()
            c.execute("SELECT twit FROM twits WHERE twit= ?", [clean])
            result = c.fetchall()
            if (len(result) == 0):
                c.execute("INSERT OR REPLACE INTO twits (twit, user) VALUES (?, ?)", [clean, user])
                print("ID: {0} | Twit: {1}".format(count, tweet.text.strip()))
                con.commit()
                # Theres 100% a better way to do this "check", however this functionally works..
            else:
                con.commit()
        con.close()
    print("Checking for new twits..")
    time.sleep(600)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Twitter Bot')
    parser.add_argument('--user', required=True, type=str, help='Twitter User to scrap')
    parser.add_argument('--scrap', required=False, type=int, help='Number of Twits to Scrap')
    args = parser.parse_args()
    if args.user and args.scrap:
        Database()
        while True:
            Twit(user=args.user, idx=args.scrap)
    else:
        Database()
        Twit(user=args.user, idx=5)
