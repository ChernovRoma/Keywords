from functions import *
import pandas as pd

FILE = "US Terms.csv"


test = [
    "marketing",
]
marketing_filters = [
    "marketing",
    "event",
    "agenc",
    "advertis",
    "campaign",
    "campain",
    "lead",
    "roi",
    "customer",
    "perform",
    "seo",
    "ppc",
    "kpi",
    "conversion",
    "commer",
    "strateg",
    "brand",
    "remarket",
    "virtual",
    "affiliat",

]

creative_filters = [
    "design",
    "design",
    "approv",
    "creativ",
    "proofin",
    "graphic",
    "proof",
    "ux",
    "visual",
]

# df = pd.DataFrame()
#
# for marketing_filter in test:
#     result = main(FILE, marketing_filter)
#     result["Filter"] = marketing_filter
#     df = df.append(result)
#


negatives_df = pd.read_excel("/Users/roman.chernov/Downloads/NEW_WORDS.xlsx", sheet_name='Sheet1')
negatives_df = negatives_df["Word"].tolist()


df = pd.read_excel("/Users/roman.chernov/Downloads/RESULT FOR MARKETING ICP.xlsx", sheet_name='Sheet1')
result = clean_keywords(df, negatives_df)
result.to_excel(r'/Users/roman.chernov/Downloads/RESULT FOR MARKETING ICP CLEANED.xlsx', index = False)

# file_to_make_words = "/Users/roman.chernov/Downloads/RESULT FOR MARKETING ICP.xlsx"
# make_words = make_single_words_count(file_to_make_words)
# make_words.to_excel(r'/Users/roman.chernov/Downloads/NEW_WORDS.xlsx', index = False)

