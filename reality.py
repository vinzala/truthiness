class maintain:
    ''' A class which will do nothing to alter the interpretation of 'True' and 'False'. '''
    def __init__(self):
        pass


# If imported, the following assignments will invert the definition of 'True' and 'False'.
True = False
False = True
