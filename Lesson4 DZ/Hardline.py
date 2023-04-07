class Hardline:

    def __init__(self, hard_kerry, hard_support):
        self.hard_kerry = hard_kerry
        self.hard_support = hard_support

    def _showInfoHardline(self):
        print(f"Tank: {self.hard_kerry}\n"
              f"Semi Support: {self.hard_support}")