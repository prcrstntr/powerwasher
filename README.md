# powerwasher

Some scripts that find and ignore powerusers on a reddit account. A work in progress and didn't touch between April 2019 and May 2020. Original plan was to create a webapp that lets a user simply run the app, but was too lazy to actually learn web stuff. Detailed steps on how to run will be added later. 


# Files
**Python**

*Both python files need to be edited with reddit account info.* 
* userfinder.py - Finds users on the front page that have too much karma per year. Saves to powerusers.txt Currently runs really slow. 
* userIgnorer.py - Ignores user in powerusers.txt. Takes a few minutes to run. 

**Text Files**
* powerusers.txt - List of users found by userfinder.py
* regularuser.txt - List used to make running userfinder.py easier. Not needed. Will remove in future. 
