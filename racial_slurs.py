import re

def calculate_profanity_degree(tweet, racial_slurs):
    # Convert the tweet to lowercase for case-insensitive matching
    tweet_lower = tweet.lower()

    # Count the number of racial slurs found in the tweet
    num_slurs = len(re.findall("|".join(racial_slurs), tweet_lower))

    # Calculate the profanity degree as a percentage of racial slurs in the tweet
    profanity_degree = (num_slurs / len(tweet_lower.split())) * 100

    return profanity_degree

def main():
    # Assume the racial slurs are provided as a list of words
    racial_slurs = ["nigger", "reggin", "drug dealer","wetback","coolie","kike","chinky","japs"]

    # Assume the tweets are stored in a file called "tweets.txt" (one tweet per line)
    tweets_file = "tweets.txt"

    with open(tweets_file, 'r') as file:
        tweets = file.readlines()

    for tweet in tweets:
        tweet = tweet.strip()  # Remove leading/trailing whitespace
        profanity_degree = calculate_profanity_degree(tweet, racial_slurs)
        print(f"Tweet: {tweet}")
        print(f"Profanity Degree: {profanity_degree}%")
        print()

if __name__ == "__main__":
    main()
