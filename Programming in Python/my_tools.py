def lettergrade(score):
    """ This function returns the letter grade for a given score.

    Parameters
    score : float
            The score to be converted.

    Returns
    grade : String
            The calculated letter grade.
    """
    if score<0 or score>100:
        raise ValueError('Score cannot be less than 0, or above 100.')
    
    if 90<=score<=100:
        return 'A'
    elif 80<=score<90:
        return 'B'
    elif 70<=score<80:
        return 'C'
    elif 60<=score<70:
        return 'D'
    else:
        return 'F'