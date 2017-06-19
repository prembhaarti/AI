from sklearn.preprocessing import MinMaxScaler


def minMaxScale(feature, feature_range=(0, 1)):
    return MinMaxScaler(feature_range).fit_transform(feature)



