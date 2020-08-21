punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def strip_punctuation(s):
    for c in punctuation_chars:
        s = s.replace(c, '')
    return s
def get_pos(s):
    s.lower()
    words = strip_punctuation(s).split()
    positivity = 0
    for pos_w in positive_words:
        if pos_w in words:
            positivity += 1
    return positivity


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(s):
    words = strip_punctuation(s).split()
    negativity = 0
    for neg_w in negative_words:
        if neg_w in words:
            negativity += 1
    return negativity
def evaluate_tweet(tweet_data_input_line):
    tweet, retweets_count, replies_count = tweet_data_input_line.strip().split(",")
    neg_score = get_neg(tweet)
    pos_score = get_pos(tweet)
    net_score = pos_score - neg_score
    return '{},{},{},{},{}\n'.format(retweets_count, replies_count, pos_score, neg_score, net_score)
with open("project_twitter_data.csv") as twitter_f:
    with open("resulting_data.csv", "w") as results_f:
        result_header = "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n"
        results_f.write(result_header)
        reading_header = True
        for input_line in twitter_f:
            if reading_header:
                reading_header = False
                continue
            results_f.write(evaluate_tweet(input_line))
