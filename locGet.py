import authGet

api = authGet.authentigate()

def locFind(user):
    userInfo = api.get_user(user)
    userLocation = userInfo.location
    return userLocation