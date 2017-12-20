import tweepy, json, re;

from tweepy import *;

from tweepy.streaming import StreamListener;

strCKey = "Ss0hd3ObqaVYo57akdHGR2fCx";
strCSecret = "AjfpjioH1UMTLdLGVPwF1zdeQNogB54zauyRFZjD0rKS00hFJE";
strAToken = "1548061171-Mx7Cspk1Ra0bv7YsYXLW1X4c2hy0iILStiPxaNW";
strASecret = "cbgsQmHK3vnk683S0ZZeEi3kpqlH99LBEChJYrSFwe5rC";

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