"""
Name: Lorenzo Zamora
Email: Lorenzo.Zamora@SLU.edu
Current Date: 5/3/2018 
Course Information: CSCI 1300
Instructor: Judy Etchison
"""

def isInList(iList,w):
    """ Function to see where the specified word is in the raw index list,
    so that it may be paired with its appropriate topic. Removes the word
    from the list of raw indeces, so as to prevent pages being counted again,
    in the case of duplicate topics and different page numbers. """
    found = False
    """ Iterate through the raw index list's lists. """
    for subList in range(len(iList)):
        """ In the case of the word being found, do not execute the rest.
        Otherwise, grab the number which corresponds to the passed in topic,
        and remove that topic from that sublist to avoid duplicates. """
        if (found == False):
            if w in iList[subList]:
                pageNum = iList[subList][0]
                (iList)[subList].remove(w)
                found = True
    """ Return the altered raw index list, and the topic's page number. """
    return iList,pageNum
