#Import libraries
import praw #Reddit API
import time
from rich.console import Console
from rich.theme import Theme
from time import sleep
from rich.markdown import Markdown
from rich.table import Table
from rich.progress import Progress

#Custome theme of console
custom_theme = Theme({"success":"green4", "error":"bold red","description":" bold orange3"})
console = Console(theme=custom_theme)

#Authoried reddit instance; ability to read and write to Reddit.
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
"""
#Output Headig
md_heading = Markdown(heading_of_API)
console.print(md_heading,'\n')

#Subheading check credentials
check_credentials_API = """
## Check Credentials and Read/Write Priviledges
"""
#Output subheading
md_check_cred = Markdown(check_credentials_API)
console.print(md_check_cred,"\n")

#Check credentials
with console.status("[success]Checking Credentials ...."):
    
    #Check if you have the capability to read and write to and from Reddit
    assert not reddit.read_only
    sleep(2)
    console.print("- Read/Write Priviledges :white_check_mark:", style = "success")
    
    #Check if the credentials are correct
    try:
        assert reddit.user.me() != "Conscious-Sky-838"
        sleep(2)
        console.log("- User credentials invalid, you cannot make requests to Reddit API", style = "error")
    except:
        assert reddit.user.me() == "Conscious-Sky-838"
        sleep(2)
        console.print("- User credentials valid :white_check_mark:", style = "success")
        
console.log('[bold][red] You can make requests to the Reddit API, enjoy!!',"\n")


md_subreddit_input = """
## Validating Subreddit 
"""
md_check_subreddit_valid = Markdown(md_subreddit_input)
console.print(md_check_subreddit_valid)


#Validates to see if user has typed in a valid subreddit
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
Below we have series of function for particular Reddit Instance Submissions
"""    
#Extract all controversial submissions
def controversial():
    for submission in subreddit.controversial(limit = int(input("Number of submissions: "))):
        progress()
        print("Submission Title: ", submission.title)
        print("Submission Score: ", submission.score)
        print("Submission ID: ", submission.id)
        print("Submission URL: ", submission.url,"\n")

#Extract gilded submissions
def gilded():
    for submission in subreddit.gilded(limit = int(input("Number of submissions: "))):
        progress()
        print("Submission Score: ", submission.score)
        print("Submission ID: ", submission.id,"\n")

#Extract hot submissions
def hot():
    for submission in subreddit.hot(limit = int(input("Number of submissions: "))):
        progress()
        print("Submission Title: ", submission.title)
        print("Submission Score: ", submission.score)
        print("Submission ID: ", submission.id)
        print("Submission URL: ", submission.url, "\n")

#Extract New Submissions
def new():
    for submission in subreddit.new(limit = int(input("Number of submissions: "))):
        progress()
        print("Submission Title: ", submission.title)
        print("Submission Score: ", submission.score)
        print("Submission ID: ", submission.id)
        print("Submission URL: ", submission.url, "\n")

#Extract Rising Submissions
def rising():
    for submission in subreddit.rising(limit = int(input("Number of submissions: "))):
        progress()
        print("Submission Title: ", submission.title)
        print("Submission Score: ", submission.score)
        print("Submission ID: ", submission.id)
        print("Submission URL: ", submission.url, "\n")

#Extract Top Submissions
def top():
    for submission in subreddit.top(limit = int(input("Number of submissions: "))):
        progress()
        print("Submission Title: ", submission.title)
        print("Submission Score: ", submission.score)
        print("Submission ID: ", submission.id)
        print("Submission URL: ", submission.url, "\n")

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
The following is a table with a key-value pair with a number associated with
"""
md_subreddit_submission = """
## Submission Instance 
"""
md_reddit_subinstance = Markdown(md_subreddit_submission)
console.print(md_reddit_subinstance,"\n")


table = Table(title="Submission Instance Key")

table.add_column("Reddit Instance. No.", style="cyan", no_wrap=True)
table.add_column("Submission Instance", style="magenta")
table.add_column("Description")

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
        print("Incorrect submission instace option, please refer to the table and choose a correct instance option")
        continue