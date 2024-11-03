########################################
#Homework_15 Task_1
########################################
class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Person(name={self.name}, deposit={self.deposit}, loan={self.loan})"


class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "for sale"  # Default status when the house is created

    def sell_apartment(self, buyer, loan_amount=None):
        # Perform a sale without a loan
        if loan_amount is None:
            self.owner.deposit += self.price
            print(f"{self.owner.name}'s deposit after sale: {self.owner.deposit}")
            self.owner = buyer
            self.status = "sold"
            print(f"Apartment sold to {buyer.name}. Status: {self.status}")

        # Perform a sale with a loan
        else:
            self.owner.deposit += self.price
            print(f"{self.owner.name}'s deposit after sale: {self.owner.deposit}")
            self.owner = buyer
            self.status = "sold on loan"
            buyer.loan += loan_amount
            print(f"Apartment sold to {buyer.name} with a loan. Status: {self.status}")
            print(f"{buyer.name}'s loan after purchase: {buyer.loan}")

    def __str__(self):
        owner_name = self.owner.name if self.owner else "None"
        return f"House(ID={self.ID}, price={self.price}, owner={owner_name}, status={self.status})"

# --- Example Usage ---

# Create two Person objects (one as owner and another as buyer)
owner = Person(name="Zurab")
buyer = Person(name="Irakli")

# Create a House object with the owner
house = House(ID="123-456-789", price=150000, owner=owner)

# Display initial information
print(owner)
print(buyer)
print(house)

# Perform a sale without a loan
house.sell_apartment(buyer)

# Display updated information after sale
print(owner)
print(buyer)
print(house)

# Perform a sale with a loan (reset owner and status to simulate)
house.owner = owner
house.status = "for sale"
house.sell_apartment(buyer, loan_amount=50000)

# Display final information after sale with a loan
print(owner)
print(buyer)
print(house)

########################################
