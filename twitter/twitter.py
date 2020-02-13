import config_twitter
import tweepy
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime

class MyStreamListener(tweepy.StreamListener):
    def from_creator(self, status):
        if hasattr(status, 'retweeted_status'):
            return False
        elif status.in_reply_to_status_id != None:
            return False
        elif status.in_reply_to_screen_name != None:
            return False
        elif status.in_reply_to_user_id != None:
            return False
        else:
            return True
    
    def on_status(self, status):
        if self.from_creator(status):
            try:
                db.collection(u'tweetarray').add({'tweetid': status.id_str, "createdAt": datetime.now(), 'tweetcontents': status.text})
                return status.id_str
            except BaseException as e:
                print("Error on_data %s" % str(e))
            return True
        return True

    def on_error(self, status_code):
        print("Error: ", status_code)
        pass # on error, recognize error but continue

if __name__ == '__main__':
    # Authenticate firebase db
    cred = credentials.Certificate('twitter/serviceAccountCredentials.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    # Authenticate through twitter
    auth = tweepy.OAuthHandler(config_twitter.consumer_key, config_twitter.consumer_secret)
    auth.set_access_token(config_twitter.access_token, config_twitter.access_token_secret)
    api = tweepy.API(auth)
    # Create stream listener
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    # twitter ids of following accounts in order: LP, JT, NDP, JS, CG, EM, CPC, AS, PPC, MB, CBCPolitics
    myStream.filter(follow=["16397147", "14260960", "188007231", "253340075", "28370071", "16220555", 
            "190817371", "256360738", "1035238562042716160", "2791988124", "74186967"], is_async=True)
    #myStream.filter(follow=["556176455"], is_async=True) # MY TWITTER ID FOR TESTING.