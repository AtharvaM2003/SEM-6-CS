import random
class DHKE:
    def __init__(self, G, P):
        self.G_param = G
        self.P_param = P

    def generate_private_key(self):
        self.private_key = random.randrange(start=1, stop=10, step=1)

    def generate_public_key(self):
        self.public_key = pow(self.G_param, self.private_key) % self.P_param

    def exchange_key(self, other_public):
        self.shared_key = pow(other_public, self.private_key) % self.P_param

# Simulating the Key Exchange between two entities. Let Alice and Bob be the two entities.
Alice = DHKE(5, 22)
Bob = DHKE(5, 22)

Alice.generate_private_key()
Bob.generate_private_key()

print("------------Private Keys------------------\n")
print("Alice Private Key Generated is ", Alice.private_key, "\n")
print("Bob Private Key Generated is ", Bob.private_key, "\n")
print("------------End of Private Keys------------\n\n")
Alice.generate_public_key()
Bob.generate_public_key()

print("------------Public Keys------------------\n")
print("Alice Public Key Generated is ", Alice.public_key, '\n')
print("Bob Public Key Generated is ", Bob.public_key, '\n')
print("------------End of Public Keys-----------\n\n")
# Alice & Bob Exchange each other's keys now.
Alice.exchange_key(Bob.public_key)
Bob.exchange_key(Alice.public_key)
print("------------Shared Key Derived------------------\n")
print("Shared Key Generated now by Alice : ", Alice.shared_key, '\n')
print("Shared Key Generated now by Bob : ", Bob.shared_key, '\n')
print("------------End of Shared Key Derived-----------\n")
