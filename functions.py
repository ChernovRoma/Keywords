import pandas as pd




def make_clean_kw_list(file):
    df = pd.read_csv(file, sep=',', skiprows=2)
    df["Query"] = df["Query"][
        df["Query"].apply(lambda x: str(x).replace(" ", "").isalpha() and str(x).isascii())]
    df = df.dropna(subset=["Query"])
    return df


def filter_kw_topic(df, topic):
    df["Query"] = df["Query"][df["Query"].str.contains(topic)]
    df = df.dropna()
    return df


def make_most_common_words(df):
    words = []
    for i in df["Query"]:
        for word in i.split(" "):
            words.append(word)

    words_count_dict = dict(pd.Series(words).value_counts())
    good_words_list = []
    for key, value in words_count_dict.items():
        if len(key) > 3 and value > 2:
            good_words_list.append(key)
    return good_words_list


def split_phrase(phrase, word_list):
    ad_group_words = []
    for a in phrase.split(" "):
        if a in word_list:
            ad_group_words.append(a)
    return ad_group_words


def make_final_groups(df, good_words_list):
    df['Ad Groups'] = df["Query"].apply(lambda x: split_phrase(x, good_words_list))

    for _ in df['Ad Groups']:
        _.sort()
    return df


def main(file, filter_kw):
    clean_list = make_clean_kw_list(file)
    filtered_list = filter_kw_topic(clean_list, filter_kw)
    common_words = make_most_common_words(filtered_list)
    final_groups = make_final_groups(filtered_list, common_words)
    return final_groups


