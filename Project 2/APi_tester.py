import requests
import os
import json

# from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results

#Phase 1(a):   Twitter APIs
# Work Cited
#https://developer.twitter.com/en/docs/tutorials/step-by-step-guide-to-making-your-first-request-to-the-twitter-api-v2
#https://github.com/twitterdev/search-tweets-python/blob/master/examples/api_example.ipynb
#https://cloud.google.com/natural-language
"""Write test programs to exercise different twitter APIs.  For example, retrieving tweets, searching per time, hashtags, etc.
All your programs should be on GitHub including a README file explaining your tests and results.
Write test programs for the Botometer
All your programs should be on GitHub including a README file explaining your tests and results."""

#Testing Python library 

# premium_search_args  = load_credentials(filename = r"C:\Users\bmahabir\Desktop\twitter_keys.yaml",
#                                           yaml_key="search_tweets_api",
#                                           env_overwrite=False)
# rule = gen_rule_payload("beyonce", results_per_call=100)
# print(rule)
# tweets = collect_results(rule,
#                          max_results=10,
#                          result_stream_args=premium_search_args)

#[print(tweet.all_text) for tweet in tweets[0:10]]


# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

#Inital test with API

with open(r"C:\Users\bmahabir\Desktop\twitter school login.txt", "r") as f:
    auth = f.readlines()
bearer_token = auth[10]

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()



#Phase 1(b):   Google NLP
"""
Write test programs to exercise different Google NLP APIs.  Focus on Sentiment analysis.
All your programs should be on GitHub including a README file explaining your tests and results.
"""

from google.cloud import language_v1

def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))