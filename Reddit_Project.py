#Import libraries
import praw #Reddit API
import time
import pprint
from time import sleep
from rich.console import Console
from rich.theme import Theme
from rich.markdown import Markdown
from rich.table import Table
from rich.progress import Progress

#Custome theme of console
custom_theme = Theme({"success":"green4", "error":"bold red","description":" bold orange3"})
console = Console(theme=custom_theme)

#Authoried Reddit instance; ability to read and write to Reddit.
reddit = praw.Reddit(
    client_id = "xkDH9z2z5pzh5V2dEPoA0w",
    client_secret = "9ivOeSBle5z9AQ3k8u4g-lOaBiRAmw",
    user_agent = "python:myredditappproject:v1.0.0 by u/Conscious-Sky-838",
    username = "Conscious-Sky-838",
    password = "Physnewt1224#",
    check_for_async = False)


#Description of API
heading_of_API = """
# Reddit Guest Research API
The following API pulls data from Reddit to expedite research for potential  guests. 
Users can specify Reddit Instances for a particular subreddit. Refer  to the following documentation.

Reddit API Doc. ==> (https://github.com/Physics-Comp/Reddit_API/blob/main/README.md).
"""
#Output for API Heading
md_heading = Markdown(heading_of_API)
console.print(md_heading,'\n')

#Subheading Check Credentials
check_credentials_API = """
## Check Credentials and Read/Write Priviledges
"""
#Subheading Output for Check Credentials
md_check_cred = Markdown(check_credentials_API)
console.print(md_check_cred,"\n")

#Check Credentials Logic
with console.status("[success]Checking Credentials ...."):
    
    #Check If User has Read/Write Priviledges Reddit
    assert not reddit.read_only
    sleep(2)
    console.print("- Read/Write Priviledges :white_check_mark:", style = "success")
    
    #Check User Credentials
    try:
        assert reddit.user.me() != "Conscious-Sky-838"
        sleep(2)
        console.log("- User credentials invalid, you cannot make requests to Reddit API", style = "error")
    except:
        assert reddit.user.me() == "Conscious-Sky-838"
        sleep(2)
        console.print("- User Credentials Valid :white_check_mark:", style = "success")
        
console.log('[bold][red] You can make requests to the Reddit API, enjoy!!',"\n")

# Validating Subreddit Subheading
md_subreddit_input = """
## Validating Subreddit 
"""

#Validating Subreddit Subheading Output
md_check_subreddit_valid = Markdown(md_subreddit_input)
console.print(md_check_subreddit_valid)


#Validates If Subreddit is Valid 
while True:
    try:
        user_subreddit_input = input("Enter name of subreddit: ")
        subreddit = reddit.subreddit(user_subreddit_input)
        console.print('[green4]Valid Subreddit![/green4]\n \n[underline]Title:[/underline]', subreddit.title, "\n")
        console.print('[underline]Description:[/underline]',subreddit.description)
        break;
    except:
        console.print("Not a valid subreddit, please check spelling", style = "error")
        continue

#Progress Bar
def progress():
    with Progress() as progress:
        task1 = progress.add_task("[green]Processing...", total=100)
        while not progress.finished:
            progress.update(task1, advance=1.0)
            time.sleep(0.02)

"""
Below we have series of functions for specific Reddit instance submissions. Below are the most
popular Reddit instance submissions.
"""    
#Extract all controversial submissions
def controversial():
    for submission in subreddit.controversial(limit = int(input("Number of submissions: "))):
        progress()
        print("Submission Title: ", submission.title, "\n")
        print("Context:", submission.selftext, "\n")
        print("Submission Score: ", submission.score, "\n")
        print("Submission ID: ", submission.id, "\n")
        print("Submission URL: ", submission.url,"\n")

#Extract gilded submissions
def gilded():
    for submission in subreddit.gilded(limit = int(input("Number of submissions: "))):
        progress()
        print("Submission Score: ", submission.score, "\n")
        print("Submission ID: ", submission.id,"\n")

#Extract hot submissions
def hot():
    for submission in subreddit.hot(limit = int(input("Number of submissions: "))):
        progress()
        print("Submission Title: ", submission.title, "\n")
        print("Context:", submission.selftext, "\n")
        print("Submission Score: ", submission.score, "\n")
        print("Submission ID: ", submission.id, "\n")
        print("Submission URL: ", submission.url,"\n")

#Extract New Submissions
def new():
    for submission in subreddit.new(limit = int(input("Number of submissions: "))):
        progress()
        print("Submission Title: ", submission.title, "\n")
        print("Context:", submission.selftext, "\n")
        print("Submission Score: ", submission.score, "\n")
        print("Submission ID: ", submission.id, "\n")
        print("Submission URL: ", submission.url,"\n")

#Extract Rising Submissions
def rising():
    for submission in subreddit.rising(limit = int(input("Number of submissions: "))):
        progress()
        print("Submission Title: ", submission.title, "\n")
        print("Context:", submission.selftext, "\n")
        print("Submission Score: ", submission.score, "\n")
        print("Submission ID: ", submission.id, "\n")
        print("Submission URL: ", submission.url,"\n")

#Extract Top Submissions
def top():
    for submission in subreddit.top(limit = int(input("Number of submissions: "))):
        progress()
        print("Submission Title: ", submission.title, "\n")
        print("Context:", submission.selftext, "\n")
        print("Submission Score: ", submission.score, "\n")
        print("Submission ID: ", submission.id, "\n")
        print("Submission URL: ", submission.url,"\n")

"""
Dictionary mapping numbers to subbmission instances.
"""
#Reddit Submission Instances Dictionary
redditSubmissionInstances = {
    "1":controversial,
    "2":gilded,
    "3":hot,
    "4":new,
    "5":rising,
    "6":top   
}

"""
Markdown table illistrating the dictionary mapping convention along with a description of each
submission instace. 
"""
md_subreddit_submission = """
## Submission Instance 
"""
md_reddit_subinstance = Markdown(md_subreddit_submission)
console.print(md_reddit_subinstance,"\n")

#Title for Table
table = Table(title="Submission Instance Key")

#Columns of Table
table.add_column("Reddit Instance. No.", style="cyan", no_wrap=True)
table.add_column("Submission Instance", style="magenta")
table.add_column("Description")

#Rows of Table
table.add_row("1", "Controversial", "Number of upvotes being roughly equal to the number of downvotes.\n")
table.add_row("2", "Gilded", "Posts given awards by other users. \n")
table.add_row("3", "Hot", "The number of upvotes/comments recently.\n")
table.add_row("4", "New","Latest Reddit posts.\n")
table.add_row("5", "Rising","Posts with lots of upvotes and comments at the current moment.\n")
table.add_row("6", "Top","Most upvotes over a set period of time.")
console.print(table)

#Determine if you have a correct reddit submission opiton
while True:
    try:
        submissionChoice = redditSubmissionInstances[input("Choose a Reddit Submission Instace Number: ")]()
        break;
    except:
        console.log("Incorrect submission instace option, refer to the table!", style = "error")
        continue

#Obtain the Redditor and the 
comment_id = input("Copy and past submission ID to pull comment: ")
comment = reddit.comment(comment_id)
body = comment.body
console.print(body)