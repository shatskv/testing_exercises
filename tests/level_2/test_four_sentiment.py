from functions.level_2.four_sentiment import check_tweet_sentiment


def get_words():
    return {'кот', 'собака'}, {'дурак', 'крыса', 'идиоты'}


def test__check_tweet_sentiment__bad_words_greater():
    text = 'Дурак кот собака стул стол идиоты Крыса'
    good_words, bad_words = get_words()

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == 'BAD'


def test__check_tweet_sentiment__good_words_greater():
    text = 'Дурак кот собака стул стол идиоты Крыса'
    bad_words, good_words = get_words()

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == 'GOOD'


def test__check_tweet_sentiment__num_words_but_word_repetition():
    text = 'Дурак кот собака стул Cобака стол идиоты Крыса'
    good_words, bad_words = get_words()

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == 'BAD'


def test__check_tweet_sentiment__words_set_empty():
    text = 'Дурак кот собака стул Cобака стол идиоты Крыса'
    good_words = {} 
    bad_words = {}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == None
