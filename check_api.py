import json
from datetime import datetime,timedelta
from dateutil.parser import parse
import time

local=datetime.now()

tweets_data_path = 'data.txt'

class User(object):
    name=""
    urls=[]

    def display(self):
        print self.name
        print self.link


while(True):
    tweets_file = open(tweets_data_path, "r")
    users=[]
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            user=User()
            created_at=parse(tweet["created_at"])
            created_at=created_at.strftime("%Y-%m-%d %H:%M:%S")
            created_at=parse(created_at)
            created_at=created_at +timedelta(hours=5,minutes=30)
            if((abs(local-created_at).total_seconds())/60 > 5):
                local=datetime.now()

            else:

                user.name=tweet["user"]["name"]
                for url in tweet["entities"]['urls']:
                    user.urls.append( url['expanded_url'])
                users.append(user)
        except:
            continue

    for user in users:
        print "User Name :" + user.name
        for url in user.urls:
            print url
        print "Total Urls Related :%d" %(len(user.urls))
        print "****************"

    print "------------------------------------------------------------"
    tweets_file.close()
    time.sleep(60)


