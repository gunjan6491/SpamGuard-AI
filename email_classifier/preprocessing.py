
import re
import string
import emoji
import pandas as pd
from bs4 import BeautifulSoup


def remove_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def replace_url(text):
    url_pattern = r'https?://\S+|www\.\S+'
    return re.sub(url_pattern, 'URL', text)


exclude = string.punctuation


def remove_punc(text):
    return text.translate(str.maketrans('', '', exclude))


def replace_emoji(text):
    return emoji.demojize(text)


def text_preprocessing(text):
    text = text.lower()
    text = remove_html(text)
    text = replace_url(text)
    text = remove_punc(text)
    text = replace_emoji(text)

    return text


def special_char(text):
    return sum(1 for char in text if char in string.punctuation)


def digit(text):
    return sum(1 for char in text if char.isdigit())


def capital(text):
    return sum(1 for char in text if char.isupper())


def feature_engineering(df):
    df["total_words"] = df["clean_message"].apply(
        lambda text: len(text.split())
    )
    df["char_count"] = df["v2"].apply(len)
    df["special_char"] = df["v2"].apply(special_char)
    df["digit_count"] = df["v2"].apply(digit)
    df["capital_letters"] = df["v2"].apply(capital)

    return df
