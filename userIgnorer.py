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

poweruser = set()

try:
    print('Importing powerusers')
    with open("powerusers.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content] 
    for user in content:
        poweruser.add(user)
    f.close()
    print('Users imported')
    
except Exception as e:
    print(e)

for user in poweruser:
    print(user)
    redditor = reddit.redditor(user)
    redditor.block()

print('Done')
