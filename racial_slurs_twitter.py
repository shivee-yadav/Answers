import re

def calculate_profanity_degree(tweet, racial_slurs):
    # Remove non-alphanumeric characters and convert to lowercase
    tweet = re.sub(r'[^a-zA-Z0-9\s]', '', tweet.lower())
    
    # Split the tweet into words
    words = tweet.split()
    
    # Count the number of racial slurs present in the tweet
    num_slurs = sum(1 for word in words if word in racial_slurs)
    
    # Calculate the profanity degree as a percentage of racial slurs to total words
    profanity_degree = (num_slurs / len(words)) * 100
    
    return profanity_degree

def analyze_tweets(file_path, racial_slurs):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = line.strip()
            profanity_degree = calculate_profanity_degree(tweet, racial_slurs)
            print(f'Tweet: {tweet}')
            print(f'Profanity Degree: {profanity_degree}%\n')

# Set of racial slurs
racial_slurs = {'slur1', 'slur2', 'slur3', ...}  # Add racial slurs as required

# File containing Twitter tweets
file_path = 'tweets.txt'  # Replace with the actual file path

# Analyze the tweets
analyze_tweets(file_path, racial_slurs)
