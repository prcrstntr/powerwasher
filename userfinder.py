#Powerwasher
#A way to easily ignore powerusers and reposters. 

#This script finds them.
#A later one will ignore them and possibly ban them. 

#TODO:Use less requests

import praw
import pickle
import config
import time

print("Authenticating...")
reddit = praw.Reddit(
    client_id=config.CLIENT_ID,
    client_secret=config.CLIENT_SECRET,
    password=config.PASSWORD,
    user_agent=config.USER_AGENT,
    username=config.USERNAME)
print("Authenticaed as {}".format(reddit.user.me()))



'''
So who do I want to ban?
People with too much karma (eg over 200k/year)
People with a lot of karma and post more than they comment (spam)

Maybe People who only repost. Actually if they are successful, then they'll have enough karma
We are just making a text list here,
and then the list will be used in the main script

Sort the potential offenders into a list, so that way we can selectively ignore some
Add various thresholds, like karma/year, post:comment ratio, comment karma, etc.
Only track people who make the front page, because that's easier. 

'''
checkedUsers = set()
poweruser = set()
regularuser = set()
watchlist = set()

powerusers = dict()

YEAR = 60*60*24*365
MONTH = 60*60*24*30

try:
    print('Importing powerusers')
    with open("powerusers.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content] 
    for user in content:
        poweruser.add(user)
    f.close()
except Exception as e:
    print(e)    
try:
    print('Importing regular users')

    with open("regularuser.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content] 
    for user in content:
        regularuser.add(user)
    f.close()
except Exception as e:
    print(e)

for user in poweruser:
    checkedUsers.add(user)
for user in regularuser:
    checkedUsers.add(user)

NOW = time.time()    
    


YEARLY_KARMA_LIMIT = 300000 #300,000
MIN_KARMA = 50000
sub_count = 1
kw = 0 #current karmawhore count
total_kw = 0
SUBMISSIONS_PER_SUB = 25
NUMBER_OF_SUBS = 10

worst_sub = ""
worst_sub_karmawhores = 0

for subreddit in reddit.subreddits.popular(limit = NUMBER_OF_SUBS):
    kw = 0
    print()
    print(str(sub_count) +' out of '+str(NUMBER_OF_SUBS))
    sub_count+=1
    print(subreddit)
    for submission in subreddit.hot(limit = SUBMISSIONS_PER_SUB):
        try:
            author = submission.author
            name = author.name
            if name not in checkedUsers:
                checkedUsers.add(name)
                account_age = time.time() - author.created_utc
                account_karma = author.link_karma
                if account_karma / (account_age / YEAR) > YEARLY_KARMA_LIMIT and account_karma > MIN_KARMA: #more than n karma a year, but less than 50k incase they got lucky
                    print(name + " is a karmawhore with "+str("{:,}".format((account_karma)))+" karma and "+
                          str("{:,}".format(int(account_karma / (account_age / YEAR)))) +" karma/year")
                    poweruser.add(name)
                    #powerusers[name] = (account_karma, author.comment_karma, account_age)
                    kw +=1
                    if account_age < MONTH:
                        watchlist.add(name) #Maybe not one. 
                else:
                    regularuser.add(name)
            elif name in poweruser:
                kw+=1
        except Exception as e:
            print(e)
    if kw == 0:
        print('Free from powerusers')
    else:
        if kw > worst_sub_karmawhores:
            worst_sub_karmawhores = kw
            worst_sub = str(subreddit)
        elif kw == worst_sub_karmawhores:
            worst_sub+= " ,"+str(subreddit)
            
        print(str(kw)+' powerusers out of '+str(SUBMISSIONS_PER_SUB) +', '+str((kw/SUBMISSIONS_PER_SUB)*100)+'%')
    total_kw += kw



open("regularuser.txt", "w").close()

with open("regularuser.txt", "a") as myfile:
    for user in regularuser:
        myfile.write(user+"\n")

poweruser = sorted(poweruser)
open("powerusers.txt", "w").close()

with open("powerusers.txt", "a") as myfile:
    for user in poweruser:
        #print(user)        
        myfile.write(user+"\n")

print('Time elapsed')
print(str(int(int(time.time() - NOW)/60))+' minutes')
print('Worst subreddit(s)')
print(worst_sub)
print(str(worst_sub_karmawhores)+' powerusers out of '+str(SUBMISSIONS_PER_SUB) +', '+str((worst_sub_karmawhores/SUBMISSIONS_PER_SUB)*100)+'%')
print("Total posts by kw: "+str(total_kw)+" out of about "+ str("{:,}".format((SUBMISSIONS_PER_SUB*NUMBER_OF_SUBS))))
