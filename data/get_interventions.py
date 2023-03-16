# %%
import os

from pathlib import Path
import pandas as pd
from bs4 import BeautifulSoup, Tag
from datetime import datetime

from debate import Debate
from intervention import Intervention


  
def get_debate(path_to_xml: str) -> Debate:
    """Returns debate object of a xml file of a European parliament debate day.

    Args:
        path_to_xml (str): path to xml file of debate

    Returns:
        Debate: Debate object 
    """

    # open file
    with open(path_to_xml, 'r', encoding="utf8") as f:
        data = f.read()
    
    soup = BeautifulSoup(data, "xml")
    
    # get debate infos
    debate_details = soup.find('text')
    debate_id = debate_details.get('id')
    debate_date = debate_details.get('date')

    debate_date = datetime.strptime(debate_date, "%Y-%m-%d") # convert string to datetime object
    
    debate = Debate(debate_id, debate_date) # Initiate a debate
    
    # get interventions
    interventions = soup.find_all('intervention')
    
    for intervention in interventions:
        int_id = intervention.get('id')
        speaker = intervention.get('name') #changed to name from speaker
        is_mep = intervention.get('is_mep')
        speaker_id = intervention.get('speaker_id')
        role = intervention.get('role')
        
        text = get_text(intervention)
        
        intervention = Intervention(int_id, debate_id, 
                                    speaker, is_mep, text, 
                                    speaker_id, role)
        
        debate.add_intervention(intervention)

    return debate

def get_text(intervention: Tag) -> str:  
    """Get raw text of paragraphs in intervention as concatenated string

    Args:
        intervention (Tag): A Tag object corresponds to an XML or HTML 
                            intervention tag in the original document

    Returns:
        str: Raw text of paragraphs in intervention as concatenated string
    """
    paragraphs = intervention.find_all('p')
    text = ""
    for paragraph in paragraphs:
        text += " " + paragraph.text.strip()
        
    return text

if __name__ == "__main__":
    filepath = 'C:/Users/Katharina/Documents/Uni/6_WS2223/Masterarbeit/code/WomenInEP/data/xml_1b2'
    #separately saved xml files as processing took too long (->"..._...)
    all_files = Path(filepath).glob('*.xml')

    ep_data = []
    for filename in all_files:
        print(filename)
        debate = get_debate(filename)
        df = pd.DataFrame([x.as_dict() for x in debate.interventions])
        ep_data.append(df)

    ep_data = pd.concat(ep_data, axis=0, ignore_index=True)
    ep_data.to_csv(r'C:/Users/Katharina/Documents/Uni/6_WS2223/Masterarbeit/code/WomenInEP/data/csv/ep_data_1b2.csv')


