from datetime import datetime

class Tender():

	def __init__(self, id_tender, name, subject, organisator, time_start, time_end):
		self.id = id_tender
        self.name = name
        self.subject = subject
        self.organisator = organisator
        self.time_start = time_start
        self.time_end = time_end
        self.list_criteria_of_all_participants = {}
        self.protocol = {}
        self.is_tender_is_over = False
        self.introduction = {}


    def start_tender():


    def stop_tender():



class Register():

	def __init__(self):
        self.count = 0
        self.tenders = {} # {id_tender (int) : tender (class Tender)}
        self.last_id = 0

    def find_tender(id_tender):
    	return self.tenders.get(id_tender)

    def get_protocol(id_tender):
    	current_tender = self.tenders.get(id_tender)
    	return current_tender.protocol

    def get_past_tenders():
    	now = datetime.now()
    	current_tenders = []
    	for key in self.tenders:
    		tender = self.tenders.get(key)
    		if now > tender.time_start:
    			current_tenders.append(tender)
    	return current_tenders

    def get_future_tenders():
    	now = datetime.now()
    	current_tenders = []
    	for key in self.tenders:
    		tender = self.tenders.get(key)
    		if now <= tender.time_start:
    			current_tenders.append(tender)
    	return current_tenders

    def create_tender(name, subject, organisator, time_start):
    	tender = Tender(last_id, name, subject, organisator, time_start)
    	self.tenders[last_id] = tender
    	self.last_id++
    	self.count++


   	def delete_tender(id_tender):
   		self.tenders.pop(id_tender)
   		self.count--


    # def change_tender(id_tender):




# глобальная (единственная) переменная реестра
register = Register()





