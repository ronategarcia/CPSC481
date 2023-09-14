# Rodrigo Onate Garcia
# CPSC 481
# March 08, 2023l

from logic import *

colors = ["red", "blue", "green", "purple"]
symbols = []

for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))

knowledge = And()

# Each color has a position.
for color in colors:
    knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3")
    ))

# Only one position per color.
for color in colors:
    for p1 in range(4):
        for p2 in range(4):
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{color}{p1}"), Not(Symbol(f"{color}{p2}")))
                )

# Only one color per position.
for pos in range(4):
    for c1 in colors:
        for c2 in colors:
            if c1 != c2:
                knowledge.add(
                    Implication(Symbol(f"{c1}{pos}"),  Not(Symbol(f"{c2}{pos}")))
                )

# First Guess
knowledge.add(Or(
    And(Symbol("red0"), Symbol("blue1"), Not(Symbol("green2")), Not(Symbol("purple3"))),
    And(Not(Symbol("red0")), Not(Symbol("blue1")), Symbol("green2"), Symbol("purple3")),
    And(Symbol("red0"), Not(Symbol("blue1")), Not(Symbol("green2")), Symbol("purple3")),
    And(Not(Symbol("red0")), Symbol("blue1"), Symbol("green2"), Not(Symbol("purple3"))),
    And(Symbol("red0"), Not(Symbol("blue1")), Symbol("green2"), Not(Symbol("purple3"))),
    And(Not(Symbol("red0")), Symbol("blue1"), Not(Symbol("green2")), Symbol("purple3")))
)

# Second Guess
knowledge.add(
    And(Not(Symbol("blue0")), Not(Symbol("red1")), 
        Not(Symbol("green2")), Not(Symbol("purple3")))
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
