from logic import *

ATruthoraptor = Symbol("A is a Truthoraptor")
ALieosaurus = Symbol("A is a Lieosaurus")

BTruthoraptor = Symbol("B is a Truthoraptor")
BLieosaurus = Symbol("B is a Lieosaurus")

CTruthoraptor = Symbol("C is a Truthoraptor")
CLieosaurus = Symbol("C is a Lieosaurus")

# Puzzle 0
# A says "I am both a Truthoraptor and a Lieosaurus."
knowledge0 = And(
    # A is a Truthoraptor or Lieosaurus not both
    And(Or(ALieosaurus, ATruthoraptor), Not(And(ALieosaurus, ATruthoraptor))),
    # If A is a Lieosaurus his sentence is false
    Implication(ALieosaurus, Not(And(ATruthoraptor, ALieosaurus))),
    # If A is Truthoraptor his sentence is True
    Implication(ATruthoraptor, (And(ATruthoraptor, ALieosaurus)))
)

# Puzzle 1
# A says "We are both Lieosaurus."
# B says nothing.
knowledge1 = And(
    # A and B are Lieosaurus or Truthoraptor but not both
    And(Or(ALieosaurus, ATruthoraptor), Not(And(ALieosaurus, ATruthoraptor))),
    And(Or(BLieosaurus,BTruthoraptor), Not(And(BLieosaurus,BTruthoraptor))),
    # if A is a Truthorator,A nd B are both Lieosaurus
    Implication(ATruthoraptor,(And(ALieosaurus,BLieosaurus))),
    # If A is a Lieosaurus , his statement is false
    Implication(ALieosaurus, Not(And(ALieosaurus, BLieosaurus)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A and B are Lieosaurus or Truthraptor but not both
    And(Or(ALieosaurus, ATruthoraptor), Not(And(ALieosaurus, ATruthoraptor))),
    And(Or(BLieosaurus,BTruthoraptor), Not(And(BLieosaurus,BTruthoraptor))),
    # if A is a Truthraptor, B is a Truthraptor
    Implication(ATruthoraptor, Or(And(ALieosaurus, BLieosaurus), 
        And(ATruthoraptor, BTruthoraptor))),
    # if A is a Lieosaurus, his statement is false (different kind)
    Implication(ALieosaurus, Not(Or(And(ALieosaurus, BLieosaurus), 
        And(ATruthoraptor, BTruthoraptor)))),
    # if B is a Truthraptor, A is a Lieosaurus
    Implication(BTruthoraptor, Or(And(ALieosaurus, BTruthoraptor), 
        And(BLieosaurus, ATruthoraptor))),
    # if B is a Lieosaurus, his statement is false (same kind)
    Implication(BLieosaurus, Not(Or(And(ALieosaurus, BTruthoraptor), 
        And(BLieosaurus, ATruthoraptor))))
)

# Puzzle 3
# A says either "I am a Truthoraptor." or "I am a Lieosaurus.", but you don't know which.
# B says "A said 'I am a Lieosaurus'."
# B says "C is a Lieosaurus."
# C says "A is a Truthoraptor."
knowledge3 = And(
    # A, B and C are a Truthoraptor or a Lieosaurus, but not both
    And(Or(ALieosaurus, ATruthoraptor), Not(And(ALieosaurus, ATruthoraptor))),
    And(Or(BLieosaurus, BTruthoraptor), Not(And(BLieosaurus,BTruthoraptor))),
    And(Or(CLieosaurus, CTruthoraptor), Not(And(CLieosaurus, CTruthoraptor))),
    # if A is a Truthoraptor, it is a Truthraptor or a Lieosaurus, but don't know
    Implication(ATruthoraptor, Or(ATruthoraptor, ALieosaurus)),
    # if A is a Lieosaurus, it is a Truthoraptor or a Lieosarus, but don't know
    Implication(ALieosaurus, Not(Or(ATruthoraptor, ALieosaurus))),
    # if B is a Truthoraptor, C is a Lieosaurus
    Implication(BTruthoraptor, CLieosaurus),
    # if B is a Lieosaurus, C is a Truthoraptor
    Implication(BLieosaurus, Not(CLieosaurus)),
    # if C is a Truthoraptor, A is a Truthoraptor
    Implication(CTruthoraptor, ATruthoraptor),
    # if C is a Lieosaurus, A is a Lieosaurus
    Implication(CLieosaurus, Not(ATruthoraptor))
)


def main():
    symbols = [ATruthoraptor, ALieosaurus, BTruthoraptor, BLieosaurus, CTruthoraptor, CLieosaurus]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
