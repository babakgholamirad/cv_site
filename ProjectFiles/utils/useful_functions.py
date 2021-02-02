def get_accronym(str):
    
    if not str:
        return "UK" # as UnKnown

    acronym = ""
    return acronym.join(e[0] for e in str.split()).upper()