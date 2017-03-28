import facebook

usr_token="EAAEnJsf9tAYBAFx1tuvtv2MHZAknNDJGm75a0XeAJi7bIESQScZBnckydeicE7amGq1BmVBTZBpZC9TvLW0yhjZCX4LBZAQ08cpJdL92KFJ7x4k0mzng47RIBavTpgsDSFsV0BVsBZC25d31xBkHsME4IA9SswGgo4ZD"

# https://developers.facebook.com/tools/accesstoken/
# https://developers.facebook.com/tools/explorer/145634995501895/

friends_access_token="EAACEdEose0cBAGnnac7j8zGBLLUR1SZCNBnTWcLZCViZCTI29rridivazZB95GWMoL73XRAq9F3Ay2MdINl910kBjuJg1iRpiuXO2sHZBGVVHShZArjh1as4bGvqsSHQbluNBsjBIyl5ZB7a5rOWGBMlox5RAn9UYqcm7NICJPqweRk9cmbZCIbjKT3JazJOjm4ZD"

graph = facebook.GraphAPI(friends_access_token)

# friends=graph.get_object("me/friends")
friends = graph.get_connections("me", "friends")
comments = graph.get_connections("me", "comments")

for friend in friends['data']:
    print friend['name'] , "->" , friend['id']

for comment in comments:
    print comment

# print friends

# profile = graph.get_object("me")
#
#
# friends = graph.get_connections("me", "friends")
# comments = graph.get_connections("me", "comments")
#
# print friends
#
# for friend in friends:
#     print friend


# friend_list = [friend['name'] for friend in friends['data']]
#
# print friend_list
