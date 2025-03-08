
def get_options_ratio (option, total):

    ratio = option / total
    return ratio

def get_faculty_rating (ratio):
    if 0.9 <= ratio < 1:
        return "Excellent" 
    
    elif 0.8 < ratio < 0.9:
        return "Very Good"
    
    elif 0.7 < ratio < 0.8:
        return "Good"
    
    elif 0.6 < ratio < 0.7:
        return "Needs Improvement"
    
    elif 0 < ratio <= 0.6:
        return "Unacceptable"
    

