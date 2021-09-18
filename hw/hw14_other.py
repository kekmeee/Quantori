from hw14 import Employee
import pickle

with open('../tmp/alice.pickle', 'rb') as a:
    alice = pickle.load(a)

print(alice.name, alice.department, alice.salary)
