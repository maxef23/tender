# self.salary = 0.0
# self.retirement = 0.0
# self.benefits = 0.0
# self.pto = 0.0
# self.stock_options = 0.0
# self.signing_bonus = 0.0
# self.other = 0.0


class Offer():

    def __init__(self, salary, time_to_work, social_conditions):
        # self.id = offer_id
        self.salary = salary
        self.time_to_work = time_to_work
        self.social_conditions = social_conditions

    # @staticmethod
    # def action(offer, new_action):
        
