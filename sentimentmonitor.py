import tweepy, json, re;

from tweepy import OAuthHandler;

########################
# Function Definitions #
########################

def GetFollowers( oUserId ) :

    listFollowers = oApi.followers( user_id = oUserId )

    print( "Number of Followers: ", str( len( listFollowers ) ) );

def SearchTweet( strTweet, strSearchTerm ) :

    boolTermFound = re.search( strSearchTerm, strTweet )

    if boolTermFound :

        return True
    
    else :

        return False;

def GetTweets( oUserId, strTerm = "" ) :

    print( "*****************************" )
    print( "tweets for: ", str( oUserId ) )
    print( "*****************************" )

    listTweets = oApi.user_timeline( user_id = oUserId, count = 10 );

    # print( "Number of tweets: ", len( listTweets ) );

    for tweet in listTweets :

        # print( json.dumps( tweet._json, indent = 4 ) );

        objTweet = json.dumps( tweet._json, sort_keys = True, indent = 4 )

        try :

            # json.loads() loads a string parameter, while json.load takes a file parameter
            jsonTweet = json.loads( objTweet )
            
            print( "Name:", jsonTweet["user"]["name"] )
            print( "Screen Name:", jsonTweet["user"]["screen_name"] )
            print( "Posted at:", str( jsonTweet["created_at"] ) )
            print( "Number of Favorites:", str( jsonTweet["favorite_count"] ) )
            print( "Number of Retweets:", str( jsonTweet["retweet_count"] ) )
            print( "*************************************" );

            strTweetText = str( jsonTweet["text"] )

            if len( strTerm ) > 0 :

                boolFound = SearchTweet( strTweetText, strTerm  )

                if boolFound :

                    print( strTweetText, "contains search term: ", strTerm )

                else :
    
                    print( strTweetText, "does not contain search term: ", strTerm );

            else :

                print( "Tweet:", strTweetText );

        except :

            print( "Can't pull text" );
            print( "*************************************" )
            # print( strTweet );

########################################################################
########################################################################

################
# Main Runtime #
################

strCKey = "";
strCSecret = "";
strAToken = "";
strASecret = "";

strInputTerm = input( "Please enter a search term, otherwise press enter: " )

print( "Len of Term:", str( len( strInputTerm ) ) )

oAuth = OAuthHandler( strCKey, strCSecret );

oAuth.set_access_token( strAToken, strASecret );

oApi = tweepy.API( oAuth );

listFriends = oApi.friends_ids();

print( listFriends );

for oFriendId in range( len( listFriends ) ) :

    print( "FriendId:", str( listFriends[ oFriendId ] ) )

    iFriendId = int( listFriends[ oFriendId ] )

    GetTweets( iFriendId, strInputTerm );

    # pushes over rate limit
    # GetFollowers( iFriendId );
