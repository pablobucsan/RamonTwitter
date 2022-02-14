from cgitb import text
from tkinter import E
import tweepy
import time

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
username='WillyrexYT'
user_id=api.get_user(screen_name=username)


username2='cryptoramonbot'
user_id2=api.get_user(screen_name=username2)

username3='pablitobuz'
user_id3=api.get_user(screen_name=username3)

tweet_list=api.user_timeline(user_id=user_id.id_str,count=1)
tweet=tweet_list[0].text




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


def on_status(status):
    name=status.user.screen_name
    id_str=status.id_str

    message=f'El porcentaje es {round(show(),2)}'
    reply_tweet='@'+str(name)+' '+ message

    api.update_status(reply_tweet,in_reply_to_status_id=id_str)


while True:
    tweet_list=api.user_timeline(user_id=user_id.id_str,count=1)
    new_tweet=tweet_list[0].text
    if new_tweet==tweet:
        pass
    else:
        tweet=new_tweet
        if any(word in tweet for word in nftlist):
            contador(1,1)
            api.update_status('Willy por favor' + '\n' + '\n' +f'Willy por favor deja de hablar de NFTs, aviso numero: {show()[0]}')
        else:
            contador(1,0)
    time.sleep(10)
