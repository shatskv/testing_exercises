from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__bad_words_greater(words, short_text):
    good_words, bad_words = words

    assert check_tweet_sentiment(short_text, good_words, bad_words) == 'BAD'


def test__check_tweet_sentiment__good_words_greater(words, short_text):
    bad_words, good_words = words

    assert check_tweet_sentiment(short_text, good_words, bad_words) == 'GOOD'


def test__check_tweet_sentiment__num_words_but_word_repetition(words, long_text):
    good_words, bad_words = words

    assert check_tweet_sentiment(long_text, good_words, bad_words) == 'BAD'


def test__check_tweet_sentiment__words_set_empty(long_text):
    good_words = {} 
    bad_words = {}

    assert check_tweet_sentiment(long_text, good_words, bad_words) == None
