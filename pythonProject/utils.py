# utils functions
import re
import emoji
import datefinder


def get_tags(text):
    r = re.compile(r"@{1}[a-zA-Z0-9,!.-]*")
    return r.finditer(text)


def get_hashtags(text):
    r = re.compile(r"#{1}[^\s]*")
    return r.finditer(text)


def get_post_date(text):
    dates = datefinder.find_dates(text)
    return [str(date).split()[0] for date in dates if len(str(date).split()) !=0]


def get_emojis(s):
    return ''.join(c for c in s if c in emoji.UNICODE_EMOJI['en'])


def get_username(text):
    r = re.compile(r"(?<=by ).*?(?= in)")
    if len(r.findall(str(text))) != 0:
        return str(r.findall(str(text))).strip()
    else:
        r = re.compile(r"(?<=by ).*?(?= on)")
        if len(r.findall(str(text))) != 0:
            return str(r.findall(text)).strip()


# get text without hashtags and tags
def get_post_text(text):
    # delete tags
    text = re.sub(r"@{1}[a-zA-Z0-9,!.-]*", '', text)
    # delete hashtag
    text = re.sub(r"#{1}[a-zA-Z0-9,!.-]*", '', text)
    # cleaning
    text = " ".join(text.split())
    text = re.sub('[^A-Za-z0-9]+', ' ', text)
    return text

