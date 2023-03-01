import pandas as pd


def make_clean_kw_list(file):
    df = pd.read_csv(file, sep=',', skiprows=2)
    df["Search term"] = df["Search term"][
        df["Search term"].apply(lambda x: str(x).replace(" ", "").isalpha() and str(x).isascii())]

    # removed .isascii() to get DE keywords
    # df["Search term"] = df["Search term"][
    #     df["Search term"].apply(lambda x: str(x).replace(" ", "").isalpha())]
    df = df.dropna(subset=["Search term"]).drop_duplicates(subset='Search term')
    return df


def filter_kw_topic(df, filter_kw):
    df = df[df['Search term'].str.contains(filter_kw)].dropna()
    return df


def make_most_common_words(df):
    words = df['Search term'].str.split().explode().value_counts()
    good_words_list = words[(words.index.str.len() > 3) & (words > 2)].index.tolist()
    return good_words_list


def make_final_groups(df, good_words_list):
    df['Ad Groups'] = df["Search term"].str.split().apply(
        lambda x: " | ".join(sorted([w for w in x if w in good_words_list])))
    return df


def main(file, filter_kw):
    clean_list = make_clean_kw_list(file)
    filtered_list = filter_kw_topic(clean_list, filter_kw)
    common_words = make_most_common_words(filtered_list)
    final_groups = make_final_groups(filtered_list, common_words)
    return final_groups



def clean_keywords(df, negative_df):
    df = df.drop_duplicates(subset='Search term')
    remove_regex = r'\b' + r'\b|\b'.join(negative_df) + r'\b'
    df = df[~df['Search term'].str.contains(remove_regex, case=False)]
    return df


def make_single_words_count(file):
    df = pd.read_excel(file, sheet_name='Sheet1')
    all_words = df["Search term"].str.split().explode()
    word_counts = all_words.value_counts()
    result = pd.DataFrame({'Word': word_counts.index, 'Count': word_counts.values})
    return result

# negatives = pd.read_excel("negatives.xlsx", sheet_name='Sheet2')
# all_words = negatives['Search term'].str.split().explode().unique()
# all_words = pd.DataFrame(all_words)
# all_words.to_excel(r'/Users/roman.chernov/Downloads/Negative words.xlsx', index = False)

# negative_series = pd.read_excel("/Users/roman.chernov/Downloads/Negatives_Series.xlsx", sheet_name='Sheet1')
# all_words = negative_series['Negatives'].str.split().explode()
# word_counts = all_words.value_counts()
#
# result = pd.DataFrame({'Word': word_counts.index, 'Count': word_counts.values})
# result.to_excel('word_counts.xlsx', index=False)