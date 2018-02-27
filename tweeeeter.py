import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "egJD9Rm8fVJaGJMdwQagWRmJh",
    "consumer_secret"     : "dvb4BTmNdcTcB2tXSqd666VAmrb213RgcMvmzOamFVIq7kkIvT",
    "access_token"        : "968399892988289024-doOI5KyMz0i35CfetApEWdVpUmYXn1U",
    "access_token_secret" : "a2PBKf7nB3h4BG5Vwdad1Rpai6oo96qHjirvFSQAz6pzk"

    }

  api = get_api(cfg)
  tweet = "Hello, i love you!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
