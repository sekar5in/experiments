#! /usr/local/bin/python3

# This is the sample program to show the pickle module to dump the strings data into file as binary/bytes write and read it.

import pickle

#example_Dict = {'2': '4', '4': '5', '9': '20'}

# Dumping the string as binary.

#pickle_out = open('pickle.dump', 'wb')
#pickle.dump(example_Dict, pickle_out)
#pickle_out.close()

# Retreiving the data backup from binary file.

pickle_in = open('pickle.dump', 'rb')
example_Dict = pickle.load(pickle_in)

print(example_Dict)
print(example_Dict['9'])

pickle_in.close()
