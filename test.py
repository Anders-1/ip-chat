import pickle

try:
    # Getting back the objects:
    with open('testing.pkl', 'rb') as f:
      testing = pickle.load(f)
    print("Could retrieve the variables!")
except:
    testing = {'test': 'yes', 'bob': 'no'}
    print("Couldn't retrieve the variables!")

def save():
    # global testings
    # Saving the objects:
    with open('testing.pkl', 'wb') as f:
        pickle.dump(testing, f)

print("TESTING: " + str(testing))

save()
