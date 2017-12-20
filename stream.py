import tweepy, json, re;

from tweepy import *;

from tweepy.streaming import StreamListener;

strCKey = "";
strCSecret = "";
strAToken = "";
strASecret = "";

class clsStreamListener( tweepy.StreamListener ) :

    def on_status( self, status ) :

        print( status.text );

    def on_error( self, status ) :

        print ( status.text );

try :

    strInputTerm = input( "Please enter a search term, otherwise press enter: " )

    if len( strInputTerm ) <= 0 :

        strInputTerm = input( "Please enter a search term, otherwise press enter: " );

except :

    print( "Unable to capture input - defaulting to'#awesomesauce'" )

    strInputTerm = "#awesomesauce";

oAuth = OAuthHandler( strCKey, strCSecret );

oAuth.set_access_token( strAToken, strASecret );

oApi = tweepy.API( oAuth );

NewTweetListener = clsStreamListener();

TweetStream = tweepy.Stream( auth = oApi.auth, listener = NewTweetListener )

TweetStream.filter( track = [ strInputTerm ] );
