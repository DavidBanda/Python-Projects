from firebase import firebase


class FirebaseConn:

    def __init__(self):
        self.FBConn = firebase.FirebaseApplication('https://ejemplo-b1ddf.firebaseio.com/', None)
        self.data = []
        self.result = self.FBConn.get('/MyTestData/', None)

    def getData(self):
        for keyID in self.result:
            # print(FirebaseConn.result[keyID]['Temp'])
            self.data.append(self.result[keyID]['Temp'])
        # print(FirebaseConn.data)
        return self.data
#
#
# fir = FirebaseConn()
# fir.getData()


