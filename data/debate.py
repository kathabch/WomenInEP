from datetime import datetime
from intervention import Intervention

class Debate(object):
    """Class for the debates of the European Parliament."""

    def __init__(self, 
                 debate_id: str,
                 date: datetime
                 ):
        
        self.debate_id = debate_id # "20220405.EN"
        self.date = date #"2014-10-23" 
        self.interventions = []
        
    def add_intervention(self, intervention: Intervention):
        self.interventions.append(intervention)

