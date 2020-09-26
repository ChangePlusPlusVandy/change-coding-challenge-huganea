import tweepy
import random

# Add your credentials here
twitter_keys = {
    'consumer_key': 'DSt3NyAqOGFEGyUWzLRYZcx1g',
    'consumer_secret': '581Fs2Q0hDctuMISQ83EkNp8xwc5JSu2wWB18hbYfjpR55dvO5',
    'access_token_key': '1143319962653560832-ggi4PS3OGStUcC5RLSPaV5YhwjJkE5',
    'access_token_secret': 'ZU48qIyslkpy6qVDRocKcXBDA7uS3ox7anwbtC5WJZHb7'
}

# Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)

screen_name_kanye = "kanyewest"
count = 3200
screen_name_elon = "elonmusk"

tweetListKanye = []
print("Welcome to the Kanye vs. Elon Twitter Showdown. In this high-stakes game, we will be " +
      "putting your deduction skills to the test. \n")

print("The objective of the game is simple. Given a random tweet from either of the two legendary individuals" +
      ", can you pick who is who?\n")
print("Loading......")

for status in tweepy.Cursor(api.user_timeline, screen_name='@kanyewest', tweet_mode="extended", exclude_replies=True,
                            include_rts=False).items():
    tweetListKanye.append(status)


tweetListElon = []
for status in tweepy.Cursor(api.user_timeline, screen_name='@elonmusk', tweet_mode="extended", exclude_replies=True,
                            include_rts=False).items():
    tweetListElon.append(status)

user_response = ""
while user_response != "NO":
    print("You'll have five chances to guess the Tweet author correctly. All you need to do is type in "
          + "the individuals full name (Kanye West OR Elon Musk) when prompted.\n")

    print("Once you have guessed all five Tweets, we'll add up your score!\n")
    print("Would you like to see the instructions again?\n")
    user_response = input("Yes | No ")
    user_response = user_response.upper()

user_answer = ""
user_score = 0
for i in range(5):
    kanye_knowledge = random.randint(1, 2)
    if kanye_knowledge == 1:
        print(tweetListElon[random.randint(0, len(tweetListElon))])
    else:
        print(tweetListKanye[random.randint(0, len(tweetListElon))])

    user_answer = input("Tell me, wise sage. Kanye? Or Elon?\n")
    if user_answer == kanye_knowledge:
        print("Wow! You are correct!")
        user_score += 1
    else:
        if kanye_knowledge == 2:
            print("Darn, you need to go back to Sunday School. It was Kanye!")
        else:
            print("X Æ A-Xii would be disappointed to hear you cannot identify his father. It was Kanye!")
print("------END GAME------\n")
print("Nice job completing the Kanye VS Elon Twitter Challenge! How well did you do?\n")
print("SCORE: " + str(user_score))