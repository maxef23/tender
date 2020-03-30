from enum import Enum

JOB_TYPES = ['1', '2', '3']

class Strategy(Enum):
    accept_first = 1
    reject_first_accept_second = 2
    randomly_accept = 3
    negotiate_until_satisfied = 4
    negotiate_once = 5


class Action(Enum):
    propose = 1
    nothing = 2
    accept = 3
