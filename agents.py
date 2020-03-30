
from spade import agent


class MyAgent(agent.Agent):

    def __init__(self):
        self.id = 0

    def check_if_tender_is_over(tender_id):
        tender = register.find_tender(tender_id)
        if tender.is_tender_is_over:
            return True
        else:
            return False

class Organisator(MyAgent):

    def __init__(self):
        super(Organisator, self).__init__()

        self.offers = {}

        self.candidates_to_hire = 0
        self.candidates_hired = []
        self.candidate_valuations = []
        self.pending_offers = {}

    


    def request_for_registration(entity):

    def registration(list_criteria):

    def make_report():







class Company(MyAgent):

    def __init__(self):
        super(Company, self).__init__()
        self.candidates_to_hire = 0
        self.candidates_hired = []
        self.candidate_valuations = []
        self.pending_offers = {}


    def register_for_tender():


    def create_offer(salary, time_to_work, social_conditions):
        offer = Offer(salary, time_to_work, social_conditions)
        return offer

    def valuate_offer():

    def request_list_of_candidates():

    def send_offer():

    def get_offer():



    # def done(self):
    # def is_satisfied(self, offer):
    # def happiness(self):
    # def act(self, companies, candidates, compensation_data, time):
    # def decide_valuations(self, compensation_data, candidates):







class Candidate(MyAgent):

    def __init__(self):
        super(Candidate, self).__init__()
        self.job_type = ''


    def register_for_tender(id_tender):
        org

    def create_offer(salary, time_to_work, social_conditions):
        offer = Offer(salary, time_to_work, social_conditions)
        return offer

    def valuate_offer():

    def send_offer():

    def get_offer():





    # def done(self):
    # def is_satisfied(self, offer):
    # def happiness(self):
    # def act(self, companies, candidates, compensation_data, time):
    # def decide_valuation(self, avg_valuation):
