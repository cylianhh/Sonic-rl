
class SonicReward:

    def __init__(self):
        self.reset(0, 0, 0)

    def reset(self, x, rings, lives):
        """Initialise les valeurs pour un nouvel épisode."""

        self.initial_x = x
        self.previous_x = x
        self.previous_rings = rings
        self.previous_lives = lives

        # Statistiques
        self.steps = 0
        self.total_reward = 0

        self.rings_collected = 0
        self.rings_lost = 0
        self.hits_received = 0
        self.lives_lost = 0

        self.max_x = x

        self.level_finished = False
        self.dead = False

    def calculate(self, x, rings, lives,
                  hit_received=False,
                  level_finished=False,
                  dead=False):

        reward = 0

        # 1. Progression horizontale
        delta_x = x - self.previous_x

        if delta_x >= 0:
            reward += 0.1 * delta_x
        else:
            reward += 0.02 * delta_x

        # 2. Anneaux collectés ou perdus
        delta_rings = rings - self.previous_rings

        if delta_rings > 0:
            reward += 10 * delta_rings
            self.rings_collected += delta_rings

        elif delta_rings < 0:
            lost = -delta_rings
            reward -= 2 * lost
            self.rings_lost += lost

        # 3. Coup reçu
        if hit_received:
            reward -= 2
            self.hits_received += 1

        # 4. Vies réellement perdues
        delta_lives = self.previous_lives - lives

        if delta_lives > 0:
            reward -= 100 * delta_lives
            self.lives_lost += delta_lives

        # 5. Fin du niveau
        if level_finished and not self.level_finished:
            reward += 500
            self.level_finished = True

        # 6. Game over
        if dead and not self.dead:
            reward -= 200
            self.dead = True

        # Mise à jour des statistiques
        self.steps += 1
        self.total_reward += reward

        self.max_x = max(self.max_x, x)

        self.previous_x = x
        self.previous_rings = rings
        self.previous_lives = lives

        return reward

    def get_stats(self):
        """Retourne les statistiques de l'épisode."""

        return {
            "progression": self.previous_x - self.initial_x,
            "progression_max": self.max_x - self.initial_x,
            "anneaux_collectes": self.rings_collected,
            "anneaux_perdus": self.rings_lost,
            "coups_recus": self.hits_received,
            "vies_perdues": self.lives_lost,
            "steps": self.steps,
            "duree_secondes": round(self.steps / 60, 2),
            "reward_total": round(self.total_reward, 2),
            "niveau_termine": self.level_finished,
            "game_over": self.dead
        }
