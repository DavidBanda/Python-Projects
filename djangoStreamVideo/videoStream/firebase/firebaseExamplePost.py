from firebase import firebase

FBConn = firebase.FirebaseApplication('https://ejemplo-b1ddf.firebaseio.com/', None)

while True:
    temperature = int(input("Ingrese temperatura"))
    data_to_upload = {
        'Temp': temperature
    }

    result = FBConn.post('/MyTestData/', data_to_upload)

    print(result)

