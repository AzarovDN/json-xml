import json

def find_word():
    with open('files/newsafr.json') as datafile:
        json_data = json.load(datafile)

    news_list = json_data['rss']['channel']['items']

    words_dict = {}
    for news in news_list:
        news_word = news['description'].split()
        for word in news_word:
            if len(word) > 6:
                if word in words_dict.keys():
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1

    words_len_list = []
    for key, value in words_dict.items():
        word_tuple = (value, key)
        words_len_list.append(word_tuple)

    words_len_list_sorted = sorted(words_len_list)

    print('Топ 10 встречаюшихся слов: ')
    n = 10
    for key, value in words_len_list_sorted[-10:]:
        print('{} место. Слово "{}" встречается {} раз'.format(n, value, key))
        n -= 1

find_word()