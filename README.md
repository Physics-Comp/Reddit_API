# Reddit API Documentation

The following API pulls data from Reddit to expedite research for potential  guests. Users can specify Reddit Instances for a particular subreddit.

## Pip Install the Following Packages
```
(Reddit API)
$ pip install praw

(Rich API)
$ pip install rich
```

## Validation of Credentials
Upon running the script, the program will check the following.
* Read/Write privileges
* Are user credentials valid

No input is required from the user to perform the following credentials check. The credentials used for the API are my developer credentials, and validation is performed to ensure API can pull data from Reddit.

Below is an image of a successful validation

![image](https://user-images.githubusercontent.com/51255104/156967819-519dcf2e-af04-4366-8c6d-26660cd9ba20.png)

## Validation of Subreddit

Users will be prompted to enter the subreddit's name. Once the user hits enter, they will either receive a confirmation for a valid subreddit along with the title and description of the subreddit. 

![image](https://user-images.githubusercontent.com/51255104/156969236-96a01c2d-a359-4a6b-9926-166a088fe690.png)


If the user has entered an incorrect subreddit, the script will prompt the user to re-enter an existing subreddit.

![image](https://user-images.githubusercontent.com/51255104/156969449-da5eb2fb-1fc7-436b-b4cc-70c893dc1344.png)

## Choose a Reddit Submission Instance

Suppose the user has entered a valid subreddit. In that case, the script will generate a Submission Instance Key table. The script will prompt the user to choose a Reddit Submission Instance number (the table's number associated with its submission instance). 

![image](https://user-images.githubusercontent.com/51255104/156972789-b99f3265-11e5-47bf-b12c-ad705e278336.png)

Once a Reddit Instance number is entered, the script will prompt the user to enter the number of submissions (limit is 10). The API will process each request and output the following information.

![image](https://user-images.githubusercontent.com/51255104/156972865-9d911e19-0f20-4e9f-8050-4b208d16867c.png)

