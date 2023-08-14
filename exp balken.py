class Knight:
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.exp_to_next_level = 1

    def gain_exp(self, amount):
        self.exp += amount
        while self.exp >= self.exp_to_next_level:
            self.level_up()

    def level_up(self):
        self.exp -= self.exp_to_next_level
        self.level += 1
        self.exp_to_next_level = round(self.exp_to_next_level * 1.1)

class Bandit:
    def __init__(self):
        self.exp_reward = 1.5

def print_exp_bar(knight):
    exp_percentage = (knight.exp / knight.exp_to_next_level) * 100
    bar_length = 20
    filled_length = int(bar_length * exp_percentage / 100)
    bar = "=" * filled_length + "-" * (bar_length - filled_length)
    print(f"Knight Level: {knight.level}, Exp: {knight.exp}/{knight.exp_to_next_level}")
    print(f"[{bar}] {exp_percentage:.2f}%\n")

def main():
    knight = Knight()
    bandit1 = Bandit()

    # Simuliere einige Kämpfe
    for i in range(10):
        knight.gain_exp(bandit1.exp_reward)
        print_exp_bar(knight)

if __name__ == "__main__":
    main()
