# powerwasher

Some very basic scripts that find and ignore powerusers on a reddit account. A current work in progress and didn't touch between April 2019 and May 2020. Original plan was to create a webapp that lets a user simply run the app, but was too lazy to actually learn web stuff. Do need to update my banlist because there are a lot of karmafarming accounts made in the past while. Detailed steps on how to run will be added later. 

The basic steps are:

1. Get python   
2. Install reddit's api PRAW     
3. Don't make a dumb spambot after installing PRAW. 
4. Find the magic numbers that let you run bots on your account
5. Download userfinder.py and powerusers.txt
6. Edit userIgnorer.py so the username, password, ids and stuff are for your account
7. Run userIgnorer.py
8. Enjoy reddit for a little while longer.




# Files
**Python**

*Both python files need to be edited with reddit account info.* 
* userfinder.py - Finds users on the front page that have too much karma per year. Saves to powerusers.txt Currently runs really slow. 
* userIgnorer.py - Ignores user in powerusers.txt. Takes a few minutes to run. 

**Text Files**
* powerusers.txt - List of users found by userfinder.py
* regularuser.txt - List used to make running userfinder.py easier. Not needed. Will remove in future. A blank regularuser.txt is needed to run userfinder.py and helps make repeated queries a bit faster. 


# FAQ

*i havnt shared this with anybody so these werent actually asked*
##

**Q:** How do you determine "karmawhore"?   

**A:** Anybody who gets over 300k link karma in a year and has over 50k.
##

**Q:** Can you remove a user from this list?

**A:** It depends. 
##

**Q:** Is link karma counted? 

**A:** No. Only post karma. Comments are the lifeblood of reddit. 
##

**Q:** Why?

**A:** Spent too much time on this site and am disapointed to see it decay the way it has. 
