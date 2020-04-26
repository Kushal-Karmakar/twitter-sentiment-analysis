import json
import os
import tweepy
import datetime as dt
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from dotenv import load_dotenv
from textblob import TextBlob
import pandas as pd
import numpy as np
from app.config import InitConfig
from app.models.HashtagModel import HashtagModel
from app.models.TwitterSentimentAnalysisModel import TwitterSentimentAnalysisModel
from app.models.UserModel import UserModel

version1 = Blueprint("version", __name__)

@version1.route('/home', methods=['GET'])
@cross_origin()
def home():
    return jsonify({"status" : 200,
                    "msg" : "I am in Home..."})

@version1.route('/get-twitter-dataset', methods=['GET'])
@cross_origin()
def get_twitter_dataset():
    response = {}
    try:
        q = request.args.get('q')  # cororna or covid-19 or pandemic 2020
        since = request.args.get('since')
        until = request.args.get('until') #2020-04-05
        lang = request.args.get('lang')
        init_config = InitConfig()
        config_file = init_config.config_file
        load_dotenv(dotenv_path=config_file)
        auth = tweepy.auth.OAuthHandler(os.getenv("consumer_key"), os.getenv("consumer_secret"))
        auth.set_access_token(os.getenv("access_token_key"), os.getenv("access_token_secret"))
        api = tweepy.API(auth)
        twitter_dataset_filepath = os.getenv("twitter_dataset_filepath")

        tweet_created_at_list = []
        tweet_text_list = []
        tweet_geo_list = []
        tweet_favourites_count_list = []
        tweet_retweet_count_list = []
        tweet_screen_name_list = []
        tweet_user_location_list = []
        tweet_followers_count_list = []
        tweet_friends_count_list = []
        tweet_profile_image_url_https_list = []
        tweet_profile_background_image_url_https_list = []
        tweet_profile_banner_url_list = []
        tweet_user_description_list = []

        no_of_tweets = 0
        for tweet in tweepy.Cursor(api.search,
                                   q=q,
                                   since=since,
                                   until=until,
                                   lang=lang).items():
            if (no_of_tweets == 10):
                break

            try:
                tweet_screen_name_list.append(tweet.user.screen_name)
                tweet_user_description_list.append(tweet.user.description)
                tweet_friends_count_list.append(tweet.user.friends_count)
                tweet_followers_count_list.append(tweet.user.followers_count)
                tweet_user_location_list.append(tweet.user.location)
                tweet_geo_list.append(tweet.geo)
                tweet_profile_image_url_https_list.append(tweet.user.profile_image_url_https)
                tweet_profile_background_image_url_https_list.append(tweet.user.profile_background_image_url_https)
                tweet_profile_banner_url_list.append(tweet.user.profile_banner_url)
                tweet_favourites_count_list.append(tweet.user.favourites_count)
                tweet_created_at_list.append(tweet.created_at)
                tweet_text_list.append(tweet.text)
                tweet_retweet_count_list.append(tweet.retweet_count)
            except Exception:
                pass
            finally:
                no_of_tweets += 1

        dataset = {
            "screen_name": tweet_screen_name_list,
            "user_description": tweet_user_description_list,
            "no_of_friends": tweet_friends_count_list,
            "no_of_followers": tweet_followers_count_list,
            "location": tweet_user_location_list,
            "geo": tweet_geo_list,
            "profile_image": tweet_profile_image_url_https_list,
            "profile_background_image": tweet_profile_background_image_url_https_list,
            "profile_banner": tweet_profile_banner_url_list,
            "no_of_favourites": tweet_favourites_count_list,
            "tweet_creation_time": tweet_created_at_list,
            "tweet_text": tweet_text_list,
            "no_of_retweet": tweet_retweet_count_list
        }
        df = pd.DataFrame(dataset, columns=['screen_name',
                                            'user_description',
                                            'no_of_friends',
                                            'no_of_followers',
                                            'location',
                                            'geo',
                                            'profile_image',
                                            'profile_background_image',
                                            'profile_banner',
                                            'no_of_favourites',
                                            'tweet_creation_time',
                                            'tweet_creation_time',
                                            'tweet_text',
                                            'no_of_retweet'
                                            ])
        df.to_csv(twitter_dataset_filepath, mode='a',
                  index=None, header=False)

        response["status"] = True
        response["message"] = "Your file has been downloaded successfully"
        response["filepath"] = os.path.abspath(twitter_dataset_filepath)
        return  jsonify(response)
    except Exception as ex:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = ex
        return jsonify(response)

@version1.route('/get-twitter-dataset-from-specifed-hashtag', methods=['GET'])
@cross_origin()
def get_twitter_dataset_from_specifed_hashtag():
    response = {}
    activated_hashtags = []
    try:
        hashtag_model_obj = HashtagModel()
        hashtag_data = hashtag_model_obj.get_all_hastags_data()

        for each_hashtag in hashtag_data:
            if (each_hashtag["is_activated"] == 1):
                activated_hashtags.append(each_hashtag["hashtag"])

        twitter_sentiment_analysis_model_obj = TwitterSentimentAnalysisModel()
        operation_data = twitter_sentiment_analysis_model_obj.get_twitter_sentiment_analysis_operation_data()

        q = ""
        if (operation_data[0]["operation"] == "AND"):
            for each_hashtag in activated_hashtags:
                q = q + each_hashtag + " AND "
            q = q[:-5]
        else:
            for each_hashtag in activated_hashtags:
                q = q + each_hashtag + " OR "
            q = q[:-4]

        print(q)
        since = request.args.get('since')
        until = request.args.get('until') #2020-04-05
        lang = request.args.get('lang')
        print(since)
        print(until)
        init_config = InitConfig()
        config_file = init_config.config_file
        load_dotenv(dotenv_path=config_file)
        auth = tweepy.auth.OAuthHandler(os.getenv("consumer_key"), os.getenv("consumer_secret"))
        auth.set_access_token(os.getenv("access_token_key"), os.getenv("access_token_secret"))
        api = tweepy.API(auth)
        twitter_dataset_filepath = os.getenv("twitter_dataset_filepath")

        tweet_created_at_list = []
        tweet_text_list = []
        tweet_geo_list = []
        tweet_favourites_count_list = []
        tweet_retweet_count_list = []
        tweet_screen_name_list = []
        tweet_user_location_list = []
        tweet_followers_count_list = []
        tweet_friends_count_list = []
        tweet_profile_image_url_https_list = []
        tweet_profile_background_image_url_https_list = []
        tweet_profile_banner_url_list = []
        tweet_user_description_list = []

        no_of_tweets = 0
        for tweet in tweepy.Cursor(api.search,
                                   q=q,
                                   since=since,
                                   until=until,
                                   lang=lang).items():
            if (no_of_tweets == 10):
                break
            print(tweet)
            try:
                tweet_screen_name_list.append(tweet.user.screen_name)
                tweet_user_description_list.append(tweet.user.description)
                tweet_friends_count_list.append(tweet.user.friends_count)
                tweet_followers_count_list.append(tweet.user.followers_count)
                tweet_user_location_list.append(tweet.user.location)
                tweet_geo_list.append(tweet.geo)
                tweet_profile_image_url_https_list.append(tweet.user.profile_image_url_https)
                tweet_profile_background_image_url_https_list.append(tweet.user.profile_background_image_url_https)
                tweet_profile_banner_url_list.append(tweet.user.profile_banner_url)
                tweet_favourites_count_list.append(tweet.user.favourites_count)
                tweet_created_at_list.append(tweet.created_at)
                tweet_text_list.append(tweet.text)
                tweet_retweet_count_list.append(tweet.retweet_count)
            except Exception:
                pass
            finally:
                no_of_tweets += 1

        dataset = {
            "screen_name": tweet_screen_name_list,
            "user_description": tweet_user_description_list,
            "no_of_friends": tweet_friends_count_list,
            "no_of_followers": tweet_followers_count_list,
            "location": tweet_user_location_list,
            "geo": tweet_geo_list,
            "profile_image": tweet_profile_image_url_https_list,
            "profile_background_image": tweet_profile_background_image_url_https_list,
            "profile_banner": tweet_profile_banner_url_list,
            "no_of_favourites": tweet_favourites_count_list,
            "tweet_creation_time": tweet_created_at_list,
            "tweet_text": tweet_text_list,
            "no_of_retweet": tweet_retweet_count_list
        }
        df = pd.DataFrame(dataset, columns=['screen_name',
                                            'user_description',
                                            'no_of_friends',
                                            'no_of_followers',
                                            'location',
                                            'geo',
                                            'profile_image',
                                            'profile_background_image',
                                            'profile_banner',
                                            'no_of_favourites',
                                            'tweet_creation_time',
                                            'tweet_creation_time',
                                            'tweet_text',
                                            'no_of_retweet'
                                            ])
        df.to_csv(twitter_dataset_filepath, mode='a',
                  index=None, header=False)

        response["status"] = True
        response["message"] = "Your file has been downloaded successfully"
        response["filepath"] = os.path.abspath(twitter_dataset_filepath)
        return  jsonify(response)
    except Exception as ex:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = ex
        return jsonify(response)

@version1.route('/analysis', methods=['POST'])
@cross_origin()
def analysis():
    response = {}
    try:
        init_config = InitConfig()
        config_file = init_config.config_file
        load_dotenv(dotenv_path=config_file)
        twitter_dataset_filepath = os.getenv("twitter_dataset_filepath")
        twitter_clean_dataset_filepath = os.getenv("twitter_clean_dataset_filepath")
        df = pd.read_csv(twitter_dataset_filepath)
        polarity = []
        sentiment = []
        df_tweet_text = df['tweet_text'].astype(str)
        for row in df_tweet_text:
            blob = TextBlob(row)
            polarity.append(blob.sentiment.polarity)
            if blob.sentiment.polarity > 0:
                val = "Positive"
            elif blob.sentiment.polarity == 0:
                val = "Neutral"
            elif blob.sentiment.polarity < 0:
                val = "Negative"
            else:
                val = "unknown"

            sentiment.append(val)
        df["polarity"] = np.array(polarity)
        df["sentiment"] = np.array(sentiment)

        df.to_csv(twitter_clean_dataset_filepath, mode='a',
                  index=None, header=False)

        response["status"] = True
        response["message"] = "Your file has been analyzed successfully"
        response["filepath"] = os.path.abspath(twitter_clean_dataset_filepath)
        return jsonify(response)
    except Exception as ex:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = ex
        return jsonify(response)

@version1.route('/register', methods=['POST'])
@cross_origin()
def create_user():
    response = {}
    try:
        payload = request.get_json()
        user_model_obj = UserModel()
        is_user_exists = user_model_obj.check_existing_user(username=payload["username"])

        if (is_user_exists):
            response["status"] = False
            response["message"] = "Username is already exist."
            return jsonify(response), 200

        else:
            user_model_obj.create_user(
                username=payload['username'],
                password=payload['password'],
                first_name=payload['first_name'],
                last_name=payload['last_name'],
                address=payload['address'],
                phone=payload['phone_no'],
                email=payload['email'],
                registration_no=payload['registration_no'],
                speciality=payload['speciality']
            )
            data = user_model_obj.login(username=payload["username"], password=payload["password"])
            response["status"] = True
            response["message"] = "Your account has been created successfully."
            response["data"] = data
            return jsonify(response), 200

    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong."
        response["error"] = e
        return jsonify(response), 405

@version1.route('/users', methods=['GET'])
@cross_origin()
def get_all_users():
    response = {}
    try:
        user_model_obj = UserModel()
        data = user_model_obj.get_all_users_data()
        response["status"] = True
        response["data"] = data
        return jsonify(response), 200
    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400

@version1.route('/promote-user/<username>', methods=['PUT'])
@cross_origin()
def promote_user(username):
    response = {}
    try:
        user_model_obj = UserModel()
        user_model_obj.promote_user(username=username)
        response["status"] = True
        response["message"] = "User has been promoted to Admin"
        return jsonify(response), 200
    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400

@version1.route('/demote-user/<username>', methods=['PUT'])
@cross_origin()
def demote_user(username):
    response = {}
    try:
        user_model_obj = UserModel()
        user_model_obj.demote_user(username=username)
        response["status"] = True
        response["message"] = "User has been demoted to normal user"
        return jsonify(response), 200
    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400

@version1.route('/login', methods=['POST'])
@cross_origin()
def login():
    response = {}
    try:
        payload = request.get_json()
        user_model_obj = UserModel()
        is_user_exists = user_model_obj.check_existing_user(username=payload["username"])

        if (is_user_exists == False):
            response["status"] = False
            response["message"] = "Invalid Username! Please provide a valid Username."
            return jsonify(response), 200
        else:
            data = user_model_obj.login(username=payload["username"], password=payload["password"])
            if not data:
                response["status"] = False
                response["message"] = "Invalid Password! Please provide a valid password."
                response["data"] = data
                return jsonify(response), 200
            else:
                response["status"] = True
                response["message"] = "You're successfully logged in."
                response["data"] = data
                return jsonify(response), 200

    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400

@version1.route('/get-twitter-users-data', methods=['GET'])
@cross_origin()
def get_twitter_users_data():
    response = {}
    try:
        init_config = InitConfig()
        config_file = init_config.config_file
        load_dotenv(dotenv_path=config_file)
        twitter_clean_dataset_filepath = os.getenv("twitter_clean_dataset_filepath")
        df = pd.read_csv(twitter_clean_dataset_filepath)

        response["status"] = True
        response["message"] = "Successfully fetched users data"
        response["data"] = json.loads(df.to_json(orient='records'))
        return jsonify(response), 200

    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400

@version1.route('/get-pie-chart-data', methods=['GET'])
@cross_origin()
def get_pie_chart_data():
    response = {}
    try:
        init_config = InitConfig()
        config_file = init_config.config_file
        load_dotenv(dotenv_path=config_file)
        twitter_clean_dataset_filepath = os.getenv("twitter_clean_dataset_filepath")
        df = pd.read_csv(twitter_clean_dataset_filepath)
        records = dict(df['sentiment'].value_counts(normalize=True) * 100)
        data = []
        for i in range(0,len(records)):
            data.append({ "name" : list(records.keys())[i], "y": list(records.values())[i]})

        response["status"] = True
        response["message"] = "Successfully fetched pie charts data"
        response["data"] = data
        return jsonify(response), 200

    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400

@version1.route('/get-column-chart-data', methods=['GET'])
@cross_origin()
def get_column_chart_data():
    response = {}
    try:
        init_config = InitConfig()
        config_file = init_config.config_file
        load_dotenv(dotenv_path=config_file)
        twitter_clean_dataset_filepath = os.getenv("twitter_clean_dataset_filepath")
        df = pd.read_csv(twitter_clean_dataset_filepath)
        records = dict(df['sentiment'].value_counts())
        data = []
        for i in range(0,len(records)):
            data.append({ "name" : list(records.keys())[i], "y": float(list(records.values())[i])})

        response["status"] = True
        response["message"] = "Successfully fetched column charts data"
        response["data"] = data
        return jsonify(response)

    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400

@version1.route('/create-hashtag', methods=['POST'])
@cross_origin()
def create_hashtag():
    response = {}
    try:
        payload = request.get_json()
        hashtag_model_obj = HashtagModel()
        is_user_exists = hashtag_model_obj.check_existing_hashtag(hashtag=payload["hashtag"])

        if (is_user_exists):
            response["status"] = False
            response["message"] = "Hashtag is already exist."
            return jsonify(response), 200

        else:
            hashtag_model_obj.create_hashtag(
                hashtag=payload["hashtag"]
            )
            response["status"] = True
            response["message"] = "Your hashtag has been added successfully."
            return jsonify(response), 200

    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong."
        response["error"] = e
        return jsonify(response), 405

@version1.route('/hashtags', methods=['GET'])
@cross_origin()
def get_all_hashtags():
    response = {}
    try:
        hashtag_model_obj = HashtagModel()
        data = hashtag_model_obj.get_all_hastags_data()
        response["status"] = True
        response["data"] = data
        return jsonify(response), 200

    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400

@version1.route('/activate-hashtag/<hashtag>', methods=['PUT'])
@cross_origin()
def activate_hashtag(hashtag):
    response = {}
    try:
        hashtag_model_obj = HashtagModel()
        hashtag_model_obj.activate_hashtag(hashtag=hashtag)
        response["status"] = True
        response["message"] = "Hashtag is activated"
        return jsonify(response), 200
    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400

@version1.route('/deactivate-hashtag/<hashtag>', methods=['PUT'])
@cross_origin()
def deactivate_hashtag(hashtag):
    response = {}
    try:
        hashtag_model_obj = HashtagModel()
        hashtag_model_obj.deactivate_hashtag(hashtag=hashtag)
        response["status"] = True
        response["message"] = "Hashtag is deactivated"
        return jsonify(response), 200
    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400


@version1.route('/operations', methods=['GET'])
@cross_origin()
def get_all_twitter_sentiment_analysis_operation():
    response = {}
    try:
        twitter_sentiment_analysis_model_obj = TwitterSentimentAnalysisModel()
        data = twitter_sentiment_analysis_model_obj.get_twitter_sentiment_analysis_operation_data()
        response["status"] = True
        response["data"] = data
        return jsonify(response), 200

    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400

@version1.route('/update-operation/<operation>', methods=['PUT'])
@cross_origin()
def update_operation(operation):
    response = {}
    try:
        twitter_sentiment_analysis_model_obj = TwitterSentimentAnalysisModel()
        twitter_sentiment_analysis_model_obj.update_twitter_sentiment_analysis_model(operation=operation)
        response["status"] = True
        response["message"] = "Operation is updated"
        return jsonify(response), 200

    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400

@version1.route('/get-wordcloud-data', methods=['GET'])
@cross_origin()
def get_wordcloud_data():
    response = {}
    data = ""
    sentence = ""
    try:
        init_config = InitConfig()
        config_file = init_config.config_file
        load_dotenv(dotenv_path=config_file)
        twitter_clean_dataset_filepath = os.getenv("twitter_clean_dataset_filepath")

        stopwords = [" i ", " me ", " my ", " myself ", " we ", " our ", " ours ", " ourselves ", " you ", " your ", " yours ", " yourself ", " yourselves ", " he ", " him ", " his ", " himself ", " she ", " her ", " hers ", " herself ", " it ", " its ", " itself ", " they ", " them ", " their ", " theirs ", " themselves ", " what ", " which ", " who ", " whom ", " this ", " that ", " these ", " those ", " am ", " is ", " are ", " was ", " were ", " be ", " been ", " being ", " have ", " has ", " had ", " having ", " do ", " does ", " did ", " doing ", " a ", " an ", " the ", " and ", " but ", " if ", " or ", " because ", " as ", " until ", " while ", " of ", " at ", " by ", " for ", " with ", " about ", " against ", " between ", " into ", " through ", " during ", " before ", " after ", " above ", " below ", " to ", " from ", " up ", " down ", " in ", " out ", " on ", " off ", " over ", " under ", " again ", " further ", " then ", " once ", " here ", " there ", " when ", " where ", " why ", " how ", " all ", " any ", " both ", " each ", " few ", " more ", " most ", " other ", " some ", " such ", " no ", " nor ", " not ", " only ", " own ", " same ", " so ", " than ", " too ", " very ", " s ", " t ", " can ", " will ", " just ", " don ", " should ", " now ", "https://t "," that "]

        df = pd.read_csv(twitter_clean_dataset_filepath)
        tweet_text = df["tweet_text"].to_list()
        for each_text in tweet_text:
            for each_stop_word in stopwords:
                each_text = each_text.replace(each_stop_word, '')
            data = data + " " + each_text

        response["status"] = True
        response["message"] = "Success"
        response["data"] = data
        return jsonify(response), 200
    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400

@version1.route('/get-timeseries-data', methods=['GET'])
@cross_origin()
def get_timeseries_data():
    response = {}
    try:
        init_config = InitConfig()
        config_file = init_config.config_file
        load_dotenv(dotenv_path=config_file)
        twitter_clean_dataset_filepath = os.getenv("twitter_clean_dataset_filepath")

        df = pd.read_csv(twitter_clean_dataset_filepath)
        df["tweet_creation_time"] = pd.to_datetime(df["tweet_creation_time"])
        df["tweet_creation_time"] = (df['tweet_creation_time'] - dt.datetime(1970,1,1)).dt.total_seconds()
        df = df.groupby(['tweet_creation_time']).size().reset_index(name='count')

        response["status"] = True
        response["message"] = "Success"
        response["data"] = df.values.tolist()
        return jsonify(response), 200
    except Exception as e:
        response["status"] = False
        response["message"] = "Oops! Something went wrong"
        response["error"] = e
        return jsonify(response), 400