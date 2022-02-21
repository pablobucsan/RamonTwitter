import tweepy
import time
import schedule

APPid='23384240'

APIkey='VMvaSKbGK0X6vFK8jT3Bg4eqT'
APIkeysecret='ZUSzrmvv6KcHzz32kMxdvhfHIkdcI9Eu2Rjhu1bJmaBIahKvi1'
Bearertoken='AAAAAAAAAAAAAAAAAAAAAMHSZAEAAAAAETN7hsfBl9AgNXLKl7j13SaW0oQ%3DGfLIMJSE3OQX1oYBC234yQQrhXB2STKUoWDXgTclBZFJufikR4'
AccessToken='1492979818299809799-DE22DijAOpzTpMT8lH7T1nxItmNCsC'
AccessTokenSecret='5ty8X02GTyNrampGqb8kI6FuvVaK2WYM1czSnRHAfSLaN'


auth=tweepy.OAuthHandler(APIkey,APIkeysecret)
auth.set_access_token(AccessToken,AccessTokenSecret)
api=tweepy.API(auth,wait_on_rate_limit=True)

nftlist=['nft','NFT','nfts','NFTS','NFTs','Nft','Nfts','golem','@rudegolems','@RudeGolems','golem','Golem', 'willycoin','Willycoin','golems','Golems']
testlist=['test']

username='WillyrexYT'
user_id1=api.get_user(screen_name=username)


username2='cryptoramonbot'
user_id2=api.get_user(screen_name=username2)

username3='pablitobuz'
user_id3=api.get_user(screen_name=username3)






def contador(a,b):
    file=open('contador.txt','r')
    read=file.read()
    nonft=int(read.split(' ')[0])+a
    sinft=int(read.split(' ')[1])+b
    file.close()
    file=open('contador.txt','w')
    file.write(f'{nonft}'+' ' + f'{sinft}')

def show():
    file=open('contador.txt','r')
    read=file.read()
    nonft=int(read.split(' ')[0])
    sinft=int(read.split(' ')[1])
    porcentaje=(sinft/nonft)*100
    return(sinft,porcentaje)

def checkear(new_tweet):
    file=open('tweets.txt','r')
    last_tweet=file.read()
    file.close()
    if last_tweet==new_tweet:
        return(False)
    else:
        file2=open('tweets.txt','w')
        file2.write(f'{new_tweet}')
        return(True)


def on_status(status):
    name=status.user.screen_name
    id_str=status.id_str

    message=f'El porcentaje es {round(show(),2)}'
    reply_tweet='@'+str(name)+' '+ message

    api.update_status(reply_tweet,in_reply_to_status_id=id_str)

def pablo():
    tweet_list=api.user_timeline(user_id=user_id3.id_str,count=1)
    tweet=tweet_list[0].text
    check=checkear(tweet)
    if check==True:
        if any (word in tweet for word in testlist):
            api.update_status('working')
        else:
            pass
    else:
        pass   


def tweetear():
    tweet_list=api.user_timeline(user_id=user_id1.id_str,count=1)
    tweet=tweet_list[0].text
    check=checkear(tweet)
    if check==True:
        if any (word in tweet for word in nftlist):
            contador(1,1)
            api.update_status('Willy por favor' + '\n' + '\n' +f'Willy por favor deja de hablar de NFTs, aviso numero: {show()[0]}')
        else:
            contador(1,0)
    else:
        pass

def main():
    schedule.every(120).seconds.do(pablo)
    schedule.every(100).seconds.do(tweetear)
    while True:
        try:
            schedule.run_pending()
            time.sleep(100)
        except:
            pass

if __name__=='__main__':
    main()
