import pickle
import hashlib

def test_pickle_stability(data1,protocol1,data2,protocol2):

    pickled1 = pickle.dumps(data1,protocol = protocol1)
    pickled2 = pickle.dumps(data2,protocol = protocol2)

    hash1 = hashlib.sha256(pickled1).hexdigest()
    hash2 = hashlib.sha256(pickled2).hexdigest()

    print(f"Pickle 1 Hash: {hash1}")
    print(f"Pickle 2 Hash: {hash2}")

    assert hash1 == hash2, "False"
    print("True")


if __name__ == "__main__":
    # case 1:dictionary of different history
    data1 = {}
    data2 = {}
    data1['city'] = 'hangzhou'
    del data1['city']
    test_pickle_stability(data1,4,data2,4)

    # case 2
