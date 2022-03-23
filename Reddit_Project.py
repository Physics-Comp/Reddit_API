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

#Submission ID List
submission_ID_List = []

#Extract all controversial submissions
def controversial():
    for submission in subreddit.controversial(limit = int(input("Number of submissions: "))):
        print("\n")
        progress()
        console.print("[underline]Submission Title:[/underline] ", submission.title, "\n")
        console.print("[underline]Context:[/underline] ", submission.selftext, "\n")
        console.print("[underline]Submission Score:[/underline] ", submission.score, "\n")
        console.print("[underline]Submission ID:[/underline] ", submission.id)
        console.print("[underline]Submission URL:[/underline] ", submission.url)

#Extract gilded submissions
def gilded():
    for submission in subreddit.gilded(limit = int(input("Number of submissions: "))):
        progress()
        console.print("[underline]Submission Score:[/underline] ", submission.score, "\n")
        console.print("[underline]Submission ID:[/underline] ", submission.id,"\n")

#Extract hot submissions
def hot():
    for submission in subreddit.hot(limit = int(input("Number of submissions: "))):
        progress()
        console.print("[underline]Submission Title:[/underline] ", submission.title, "\n")
        console.print("[underline]Context:[/underline] ", submission.selftext, "\n")
        console.print("[underline]Submission Score:[/underline] ", submission.score, "\n")
        console.print("[underline]Submission ID:[/underline] ", submission.id)
        console.print("[underline]Submission URL:[/underline] ", submission.url)

#Extract New Submissions
def new():
    for submission in subreddit.new(limit = int(input("Number of submissions: "))):
        progress()
        console.print("[underline]Submission Title:[/underline] ", submission.title, "\n")
        # console.printt("[underline]Context:[/underline] ", submission.selftext, "\n")
        console.print("[underline]Submission Score:[/underline] ", submission.score, "\n")
        console.print("[underline]Submission ID:[/underline] ", submission.id)
        console.print("[underline]Submission URL:[/underline] ", submission.url, "\n")

#Extract Rising Submissions
def rising():
    for submission in subreddit.rising(limit = int(input("Number of submissions: "))):
        progress()
        console.print("[underline]Submission Title:[/underline] ", submission.title, "\n")
        console.print("[underline]Context:[/underline] ", submission.selftext, "\n")
        console.print("[underline]Submission Score:[/underline] ", submission.score, "\n")
        console.print("[underline]Submission ID:[/underline] ", submission.id)
        console.print("[underline]Submission URL:[/underline] ", submission.url)

#Extract Top Submissions
def top():
    for submission in subreddit.top(limit = int(input("Number of submissions: "))):
        progress()
        console.print("[underline]Submission Title:[/underline] ", submission.title, "\n")
        console.print("[underline]Context:[/underline] ", submission.selftext, "\n")
        console.print("[underline]Submission Score:[/underline] ", submission.score, "\n")
        console.print("[underline]Submission ID:[/underline] ", submission.id)
        console.print("[underline]Submission URL:[/underline] ", submission.url)

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

#Table for mapping a number to the Reddit Submission Instance
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
        submissionChoice = redditSubmissionInstances[input("Choose a Reddit Submission Instance Number: ")]()
        break;
    except:
        console.log("Incorrect submission instace option, refer to the table!", style = "error")
        continue

#Pulling comments from a post
md_pulling_comments = """
## Pull Comments from Reddit Post

Given the posts above select the submission ID of the post that you want to pull comments from.

"""
md_pulling_comment_output = Markdown(md_pulling_comments)
console.print(md_pulling_comment_output,"\n")

#Table mapping for comment instances on Reddit
#Title for Table
table_comments = Table(title="Comment Attribute Key")

#Columns of Table
table_comments.add_column("Reddit Comment. No.", style="cyan", no_wrap=True)
table_comments.add_column("Comment Instance", style="magenta")
table_comments.add_column("Description")

#Rows of Table
table_comments.add_row("1", "Best", "Comments with a greater proportion of upvotes to downvotes in decending order. \n")
table_comments.add_row("2", "Top", "Comments with the most upvotes regardless of downvotes. \n")
table_comments.add_row("3", "New", "Most recent comments on Reddit post in acceding order. \n")
table_comments.add_row("4", "Controversial","Number of upvotes being roughly equal to the number of downvotes.\n")
table_comments.add_row("5", "Old","Oldest Reddit posts in decending order over time. \n")
table_comments.add_row("6", "Q&A","Shows all threads where OP responds to first level/parent comment. ")
console.print(table_comments)

"""
The following functions below 
"""
#Set of comment instances dictionary
#Pull best comments
def best_comments():
    comment_submission =  reddit.submission(input("Copy and past the submission ID: "))
    print("\n")
    comment_submission.comment_sort = "best"
    top_level_comments = list(comment_submission.comments)
    for i in range(len(top_level_comments)):
        print("Reddit submission ID: ",top_level_comments[i].id)
        print("Reddit comment: ",top_level_comments[i].body, "\n")

#Pull top comments
def top_comments():
    comment_submission =  reddit.submission(input("Copy and past the submission ID: "))
    print("\n")
    comment_submission.comment_sort = "top"
    top_level_comments = list(comment_submission.comments)
    for i in range(len(top_level_comments)):
        print("Reddit submission ID: ",top_level_comments[i].id)
        print("Reddit comment: ",top_level_comments[i].body, "\n")

# Pull new comments
def new_comments():
    comment_submission =  reddit.submission(input("Copy and past the submission ID: "))
    print("\n")
    comment_submission.comment_sort = "new"
    top_level_comments = list(comment_submission.comments)
    for i in range(len(top_level_comments)):
        print("Reddit submission ID: ",top_level_comments[i].id)
        print("Reddit comment: ",top_level_comments[i].body, "\n")

#Pull controversial comments
def controversial_comments():
    comment_submission =  reddit.submission(input("Copy and past the submission ID: "))
    print("\n")
    comment_submission.comment_sort = "controversial"
    top_level_comments = list(comment_submission.comments)
    for i in range(len(top_level_comments)):
        print("Reddit submission ID: ",top_level_comments[i].id)
        print("Reddit comment: ",top_level_comments[i].body, "\n")

#Pull old comments
def old_comments():
    comment_submission =  reddit.submission(input("Copy and past the submission ID: "))
    print("\n")
    comment_submission.comment_sort = "controversial"
    top_level_comments = list(comment_submission.comments)
    for i in range(len(top_level_comments)):
        print("Reddit submission ID: ",top_level_comments[i].id)
        print("Reddit comment: ",top_level_comments[i].body, "\n")

#Pull question and answers
def qa_comments():
    comment_submission =  reddit.submission(input("Copy and past the submission ID: "))
    print("\n")
    comment_submission.comment_sort = "Q&A"
    top_level_comments = list(comment_submission.comments)
    for i in range(len(top_level_comments)):
        print("Reddit submission ID: ",top_level_comments[i].id)
        print("Reddit comment: ",top_level_comments[i].body, "\n")

#Comment Instances Dictionary
redditCommentInstances = {
    "1":best_comments,
    "2":top_comments,
    "3":new_comments,
    "4":controversial_comments,
    "5":old_comments,
    "6":qa_comments
}

#User input to chose from Reddit comments instances