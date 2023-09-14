from logic import *

people = ["Tom", "Susan", "Sam", "Lily"]
houses = ["Red", "Green", "Blue", "Yellow"]
symbols = []
knowledge = And()

for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}"))

# Each person belongs to a house.
for person in people:
    knowledge.add(Or(
        Symbol(f"{person}Red"),
        Symbol(f"{person}Green"),
        Symbol(f"{person}Blue"),
        Symbol(f"{person}Yellow")
    ))
print(symbols)
# # Only one house per person.
# for person in people:
#     for h1 in houses:
#         for h2 in houses:
#             if h1 != h2:
#                 knowledge.add(
#                     Implication(Symbol(f"{person}{h1}"), Not(Symbol(f"{person}{h2}")))
#                 )

# # Only one person per house.
# for house in houses:
#     for p1 in people:
#         for p2 in people:
#             if p1 != p2:
#                 knowledge.add(
#                     Implication(Symbol(f"{p1}{house}"), Not(Symbol(f"{p2}{house}")))
#                 )

# knowledge.add(
#     Or(Symbol("TomRed"), Symbol("TomBlue"))
# )

# knowledge.add(
#     Not(Symbol("SamYellow"))
# )

# knowledge.add(
#     Symbol("SusanRed")
# )

# for symbol in symbols:
#     if model_check(knowledge, symbol):
#         print(symbol)