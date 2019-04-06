from sklearn.preprocessing import OneHotEncoder
from numpy import nan

X = [['Male', 1], ['Female', 2], [nan, nan]]
good_enc = OneHotEncoder(handle_missing="mode")
good_enc.fit(X)


print("Hello")
# Y = [['Male', 1], ['Female', 2], [None, 3]]
# bad_enc = OneHotEncoder()
# bad_enc.fit(Y)