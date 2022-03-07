# Reddit API Documentation

The following API pulls data from Reddit to expedite research for potential  guests. Users can specify Reddit Instances for a particular subreddit. Refer  to the following documentation.

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

Users will be prompted to enter the subreddit's name, and once the user hits enter, they will either receive a confirmation for a valid subreddit or an error. If the user has entered an incorrect subreddit, the script will prompt the user to re-enter an existing subreddit.

