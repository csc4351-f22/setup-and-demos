# Lecture 5 Activity
You're going to be splitting your team into two groups (2 and 2, or 1 and 2) and adding logging to two different parts of your project.  

We will be adding logging for the login part of the project, and for the API call part of the project.

## 1) Prepare
1. Sit with your team.  Discuss what your logging file should be called.  For this exercise, you will be splitting the work into two teams, but if you were to both log to the same file with your individual code, there would likely be conflicts.  If later you want to actually push this code and consolidate, you can.  For now, any code you make in your new branches will not be merged into master, so don't worry about the conflicts.
2. Decide who will work on the login logging and who will work on the API logging.

## 2) Setup (for both login and api)
1. Add `import logging` to your app.py file.
2. Setup the basic config for your logger: `logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))`
3. Create your logger, logging file, and the format you want your logs to be in.  An example is here, but look at the attached link for other ways to format your logs.
```
log = logging.getLogger("writing-logger")
fh = logging.FileHandler("./mylog2.log")
formatting = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatting)
log.addHandler(fh)
```
https://docs.python.org/3/library/logging.html#logging.Formatter
4. In your main function, add a line `log.info("Hello, world!")` and verfiy that when you run your app, you see the log added to your logging file.

## 3) Login Logging
We're going to be adding info logging when someone logs in incorrectly.  I am assuming you have a check in place to know whether the login should work or not based on if the user  exists.  If that is not the case, use some case to log when an error will occur
1. Find your login code.  
2. In the case that a login did not work, because of username or password errors, add the following log: `log.info("Username or Password Incorrect")`
3. Verify that this works in your project.
4. Think about what else we could log here, and what we definitely should not log here (password information).  Add other logs that would be helpful in your login form and database access.


## 4) API Logging
Here, we're going to add error logging when the API doesn't work.  In some cases, API calls might be within a try-catch statement if there are instances where the API would fail, perhaps with an invalid input type for example.
1. Find your API call code
2. In the case of an error, you decide what type of error, add an error log `log.error("Error Message")` in your code
3. Verify that this works in your project when an incorrect API call is made
4. Think about what other API logs we could add.  These could be info logs of what information is called, other types of error or critical logs, or anything else.  Add other logs that will be helpful to you in the use of your API.