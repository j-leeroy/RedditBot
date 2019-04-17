import praw


reddit = praw.Reddit('CREDENTIALS')


subreddit = reddit.subreddit('HEB')

keywords = ['work policy', 'time and attendance', 'occurance', 'policy', 'drug']
for submission in subreddit.hot():
    lowerCase_title = submission.title.lower()
    for questions in keywords:
        if questions in lowerCase_title:
            print(lowerCase_title)
            print(
                'You asked a policy question, I encourage you to visit https://partnernet.heb.com/HR/Policies/Forms/AllItems.aspx: I am a bot')
            break

