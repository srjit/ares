from textstat import textstat
#from readcalc import readcalc

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"



def get_readability_scores_from_readcalc(data, field="readable_text"):
    """

    Arguments:
    - `data`:
    - `field`:
    """
    data["gunning_fog"] = data['readable_text'].apply(lambda x:
                                                      readcalc.ReadCalc(x).get_gunning_fog_index())
    data["smog_index"] = data['readable_text'].apply(lambda x:
                                                          readcalc.ReadCalc(x).get_smog_index())
    data["dale_chall_score"] = data['readable_text'].apply(lambda x:
                                                          readcalc.ReadCalc(x).get_dale_chall_score())
    data["coleman_liau_index"] = data['readable_text'].apply(lambda x:
                                                          readcalc.ReadCalc(x).get_coleman_liau_index())
    data["flesch_reading_ease"] = data['readable_text'].apply(lambda x:
                                                          readcalc.ReadCalc(x).get_flesch_reading_ease())





def get_readability_scores_from_textstat(data, field="readable_text"):
    """
    """
    data['gunning_fog'] = data['readable_text'].apply(lambda x: 
                                textstat.textstat.gunning_fog(str(x)) if x is not '' else 0.0)
    data['reading_ease'] = data['readable_text'].apply(lambda x: 
                                textstat.textstat.flesch_reading_ease(str(x)) if x is not '' else 0.0)
    data['smog_index'] = data['readable_text'].apply(lambda x: 
                                textstat.textstat.smog_index(str(x)) if x is not '' else 0.0)
    data['automated_readability_index'] = data['readable_text'].apply(lambda x: 
                                textstat.textstat.automated_readability_index(str(x)) if x is not '' else 0.0)
    data['coleman_liau_index'] = data['readable_text'].apply(lambda x: 
                                textstat.textstat.coleman_liau_index(str(x)) if x is not '' else 0.0)
    data['linsear_write_formula'] = data['readable_text'].apply(lambda x: 
                                textstat.textstat.linsear_write_formula(str(x)) if x is not '' else 0.0)
    data['dale_chall_readability_score'] = data['readable_text'].apply(lambda x: 
                                textstat.textstat.dale_chall_readability_score(str(x)) if x is not '' else 0.0)
    data['syllable_count'] = data['readable_text'].apply(lambda x:
                                textstat.textstat.syllable_count(str(x)) if x is not '' else 0.0)
    data['lexicon_count'] = data['readable_text'].apply(lambda x:
                                textstat.textstat.lexicon_count(str(x)) if x is not '' else 0.0)
    data['sentence_count'] = data['readable_text'].apply(lambda x:
                                textstat.textstat.sentence_count(str(x)) if x is not '' else 0.0)						
    data['difficult_words'] = data['readable_text'].apply(lambda x:
                                textstat.textstat.difficult_words(str(x)) if x is not '' else 0.0)						
	

def get_readability_scores(data, type):
    """

    Arguments:
    - `data`:
    - `type`:
    """
    if type == "textstat":
        get_readability_scores_from_textstat(data)
    elif type == "readcalc":
        get_readability_scores_from_readcalc(data)
