from googletrans import Translator

translator = Translator()

class Intervention(object):
    """Class for the interventions of the European Parliament."""

    def __init__(self, 
                 int_id: str, 
                 debate_id: str,
                 speaker: str,
                 is_mep: bool,
                 text: str,
                 speaker_id: int = None,
                 role: str = None,
                 party: str = None):
        
        self.int_id = int_id # "4-008-000"
        self.debate_id = debate_id #"20141023.EN"
        self.speaker = speaker #"Ivan Štefanec" #changed in get_intervention, wsnt working before
        self.is_mep = is_mep #True/False
        self.text = text
        
        self.speaker_id = speaker_id #"96952"
        self.role = role #President
        self.party = party
            
        self.text_translated = None
        self.language = None
        
        self.translate() 

    def translate(self):
        """Translates text to English with Google-API and adds language of original"""
        try:
            translation = translator.translate(self.text, dest='en')
            self.text_translated = translation.text
            self.language = translation.src
        except:
            pass
        
    def as_dict(self):
        return {'int_id': self.int_id, 
                'debate_id': self.debate_id, 
                'speaker': self.speaker,
                'is_mep': self.is_mep, 
                'text': self.text, 
                'speaker_id': self.speaker_id,
                'role': self.role, 
                'party': self.party, 
                'text_translated': self.text_translated,
                'language': self.language
                }



