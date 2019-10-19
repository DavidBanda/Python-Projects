import pickle

def putPickle():
    example_dict = {1: "A", 2: "B", 3: "C"}
    pickle_out = open("dict.pickle", "wb")
    pickle.dump(example_dict, pickle_out)
    pickle_out.close()

def getPickle():
    pickle_in = open('dict.pickle', 'rb')
    example_dict = pickle.load(pickle_in)
    print(example_dict)
    print(example_dict[3])

#putPickle()
getPickle()
