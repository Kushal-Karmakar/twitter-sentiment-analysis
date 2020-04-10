import csv
import os
import tweepy
from flask import Blueprint, jsonify, request, abort
from flask_cors import cross_origin
from dotenv import load_dotenv
from textblob import TextBlob
import pandas as pd
from app.config import InitConfig
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
        twitter_clean_dataset_filepath = os.getenv("twitter_clean_dataset_filepath")

        tweet_created_at_list = []
        tweet_text_list = []
        tweet_geo_list = []
        tweet_favourites_count_list = []
        tweet_retweet_count_list = []
        tweet_screen_name_list = []
        tweet_user_location_list = []
        tweet_sentiment_analysis_list = []
        tweet_followers_count_list = []
        tweet_friends_count_list = []
        tweet_profile_image_url_https_list = []
        tweet_profile_background_image_url_https_list = []
        tweet_profile_banner_url_list = []
        tweet_user_description_list = []

        # with open(twitter_dataset_filepath,"w") as file:
        #     csv_writer = csv.writer(file, delimiter=',')
        no_of_tweets = 0
        for tweet in tweepy.Cursor(api.search,
                                   q=q,
                                   since=since,
                                   until=until,
                                   lang=lang).items():
            if (no_of_tweets == 30):
                break
            # analysis = TextBlob(tweet.text)
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
        df.to_csv(twitter_dataset_filepath, mode='w',
                  index=None, header=True)


        # df = pd.read_csv(twitter_dataset_filepath)
        # get_analysis = []
        # for i in df['sentiment']:
        #     try:
        #         if (str(i).isalpha() == False):
        #             if float(i) < 0:
        #                 get_analysis.append('negative')
        #             elif float(i) > 0:
        #                 get_analysis.append('positive')
        #             else:
        #                 get_analysis.append('neutral')
        #     except Exception as e:
        #         get_analysis.append('unknown')
        #         continue
        # df['analysis'] = get_analysis
        # df.to_csv(twitter_clean_dataset_filepath)

        response["status"] = True
        response["message"] = "Your file has been downloaded successfully"
        response["filepath"] = os.path.abspath(twitter_dataset_filepath)
        return  jsonify(response)
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
        user_model_obj.create_user(
                username=payload['username'],
                password=payload['password'],
                first_name=payload['first_name'],
                last_name=payload['last_name'],
                address=payload['address'],
                phone=payload['phone_no'],
                email=payload['email']
        )
        response["status"] = True
        response["message"] = "User is created!"
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
            response["message"] = "User is not exist"
            return jsonify(response), 400
        else:
            data = user_model_obj.login(username=payload["username"], password=payload["password"])
            if not data:
                response["status"] = False
                response["message"] = "Invalid Password! Please provide a valid password."
                response["data"] = data
                return jsonify(response), 400
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