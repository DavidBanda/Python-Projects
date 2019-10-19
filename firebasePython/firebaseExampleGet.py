from firebase import firebase

FBConn = firebase.FirebaseApplication('https://ejemplo-b1ddf.firebaseio.com/', None)

result = FBConn.get('/MyTestData/', None)

for keyID in result:
    print(result[keyID]['Temp'])

# print(result)
