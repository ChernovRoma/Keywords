import pandas as pd

words = []
df = pd.read_excel("MOFU keywords.xlsx")

for i in df['Search Query']:
    for word in i.split(" "):
        words.append(word)

words_count_dict = dict(pd.Series(words).value_counts())
good_words_list = []
for key, value in words_count_dict.items():
    if len(key) > 3 and value > 1:
        good_words_list.append(key)


def split_phrase(phrase, word_list):
    ad_group_words = []
    for a in phrase.split(" "):
        if a in word_list:
            ad_group_words.append(a)
    return ad_group_words


df['Ad Groups'] = df['Search Query'].apply(lambda x: split_phrase(x, good_words_list))

for _ in df['Ad Groups']:
    _.sort()


# df.to_excel(r'/Users/roman.chernov/Downloads/MOFU groups2.xlsx', index = False)