# User story (Cheater app)
# As a spouse I want to know if my significant other is looking at images on twitter that have adult content


#get twitter images from user liked tweets

from operator import attrgetter
from re import L, U
import sys, os
import tweepy
script_dir = r"C:\Users\bmahabir\Desktop\EC601\Project 2"
sys.path.append(os.path.abspath(script_dir))
import google_visions_tester as gc

def count_el(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

def backend(handle):

    ac_list = []

    with open(r"C:\Users\bmahabir\Desktop\twitter school login.txt", "r") as f:
        auth = f.readlines()
    bearer_token = auth[10]

    client = tweepy.Client(bearer_token)

    user = client.get_user(username=handle[1:])

    # Replace User ID
    id = user.data.id

    tweets = client.get_liked_tweets(id=id, tweet_fields=['context_annotations', 'created_at'],
                                        media_fields=['url','preview_image_url'], expansions='attachments.media_keys', max_results=50)

    media = {m["media_key"]: m for m in tweets.includes['media']}

    count = 0

    for tweet in tweets.data:
        if tweet.attachments != None:
            media_keys = tweet.attachments['media_keys']
            if media[media_keys[0]].url:
                ac_list.append(gc.detect_safe_search_uri(media[media_keys[0]].url))
                count += 1
            if media[media_keys[0]].preview_image_url:
                ac_list.append(gc.detect_safe_search_uri(media[media_keys[0]].preview_image_url))
                count += 1

    VL = count_el(ac_list, "VERY_LIKELY")
    L = count_el(ac_list, "VERY_LIKELY")
    P = count_el(ac_list, "POSSIBLE")


    if count == 0:
        return ("This person hasnt liked any tweets with images in awhile")
    elif VL:
        return ("This person has recently liked "+str(VL)+" pictures of erotic content")
    elif L:
        return ("This person has recently liked "+str(L)+" pictures of content that is likely erotic")
    elif P:
        return ("This person has recently liked "+str(P)+" pictures of content that is indecent")
    else:
        return ("Theres nothing to worry about")