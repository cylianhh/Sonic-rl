
from reward import SonicReward


reward = SonicReward()

# Initialisation : position 100, 0 anneau, 3 vies
reward.reset(x=100, rings=0, lives=3)


def test(description, x, rings, lives,
         level_finished=False, dead=False):

    result = reward.calculate(
        x, rings, lives,
        level_finished, dead
    )

    print(f"{description:<25} : {result:+.2f}")


# test("Avancer de 100", 200, 0, 3)
# test("Collecter 3 anneaux", 200, 3, 3)
# test("Perdre 2 anneaux", 200, 1, 3)
# test("Perdre une vie", 200, 1, 2)
# test("Avancer de 50", 250, 1, 2)
# test("Terminer le niveau", 250, 1, 2, level_finished=True)

# Nouveau scénario : Sonic perd tous ses anneaux
reward.reset(x=100, rings=5, lives=3)

test("Perdre 5 anneaux", 100, 0, 3)
test("Récupérer 2 anneaux", 100, 2, 3)
test("Perdre une vie sans anneaux", 100, 0, 2)

print("\nStatistiques finales :")

for key, value in reward.get_stats().items():
    print(f"{key:<20}: {value}")
