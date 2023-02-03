import pandas as pd


def make_clean_kw_list(file):
    df = pd.read_csv(file, sep=',', skiprows=2)
    df["Query"] = df["Query"][
        df["Query"].apply(lambda x: str(x).replace(" ", "").isalpha() and str(x).isascii())]
    df = df.dropna(subset=["Query"])
    return df


def filter_kw_topic(df, filter_kw):
    df = df[df['Query'].str.contains(filter_kw)].dropna()
    return df


def make_most_common_words(df):
    words = df['Query'].str.split().explode().value_counts()
    good_words_list = words[(words.index.str.len() > 3) & (words > 2)].index.tolist()
    return good_words_list


def make_final_groups(df, good_words_list):
    df['Ad Groups'] = df["Query"].str.split().apply(
        lambda x: " | ".join(sorted([w for w in x if w in good_words_list])))
    return df


def main(file, filter_kw):
    clean_list = make_clean_kw_list(file)
    filtered_list = filter_kw_topic(clean_list, filter_kw)
    common_words = make_most_common_words(filtered_list)
    final_groups = make_final_groups(filtered_list, common_words)
    return final_groups
