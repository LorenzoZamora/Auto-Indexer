"""
Name: Lorenzo Zamora
Email: Lorenzo.Zamora@SLU.edu
Current Date: 5/3/2018 
Course Information: CSCI 1300
Instructor: Judy Etchison
"""

class AutoIndexer():
    """ AutoIndexer class that takes the page numebr and its associated topics following it,
    and indexes the topics in alphabetical order, with their appropriate page numbers as well. """
    def __init__(self,fiNa):
        self._fileName = fiNa
        self._fileObj = None
        self._fileObj2 = None
        
        """ Determine if the provided file name is readable, and if not, asks for another until
        a readable one is provided. """
        while not self._fileObj:
            try:
                self._fileObj = file(self._fileName)
                self._fileObj2 = file(self._fileName)
            except IOError:
                print 'Sorry. Unable to open the specified file.'
                self._fileName = raw_input('Please re-enter the file name: ')

    def loadEdNotes(self):
        """ Function that takes the editor's notes, which were the input file, and splits those notes
        into: (1) page numbers, and (2) its following topics, in the form of sublists of a raw index list.
        The first element in each sublist is the page number, followed by its corresponding topics. """
        self._indexList = []
        firstRun = True
        
        """ Iterate line by line through the input file. """
        for fileLine in self._fileObj:
            """ Strips the new line char off the current line in the file, and makes it all lowercase. """
            line = (fileLine.strip('\n')).lower()
            """ Determines if the line is a number or not. True for number, False for word. """
            self._numOrWord = any(char.isdigit() for char in line) 
            """ Creates a new sublist beginning with the page number, and appends the topics relevant to that
            page number, until it reaches another number, and appends the old number's sublist to the raw index
            list. After that, it goes back and does the steps that were aforementioned again. """
            if (self._numOrWord == True):
                if (firstRun == True):
                    self._topicSubList = []
                    (self._topicSubList).append(line)
                    firstRun = False
                else:
                    (self._indexList).append(self._topicSubList)
                    self._topicSubList = []
                    (self._topicSubList).append(line)
                """ Part that appends the topics relevant to that page number, until a new number is reached. """
            else:
                (self._topicSubList).append(line)
        """ Append the last of the sublists of the page numbers and its topics to be sublists in the raw index. """
        (self._indexList).append(self._topicSubList)
        (self._fileObj).close()

    def alphabetizer(self):
        """ Function to create a list of all the topics that will be in the finished index, and alphabetize them. """
        self._wordList = []
        
        """ Iterate line by line through the input file again. """
        for fLine in self._fileObj2:
            """ Strips the new line char off the current line in the file, and makes it all lowercase. """
            aLine = (fLine.strip('\n')).lower()
            """ Determines if the line is a number or not. True for number, False for word. """ 
            self._numOrWord2 = any(char.isdigit() for char in aLine)
            """ If the line was determined to be a word, it is appended to a list of index topics. """
            if (self._numOrWord2 == False):
                (self._wordList).append(aLine)
        (self._fileObj2).close()
        """ Alphabetize the list of index topics. """
        (self._wordList).sort()

    def pageWordMatcher(self):
        """ Function that pairs the topics in the alphabetized list, to the appropriate page number on which it can
        be found. This is all done with the use of a dictionary, with the topics acting as keys, and the page numbers
        as the content at that key. """
        from isInList import isInList
        self._finalFormat = []
        self._indexDict = dict()
        firstRun = True
        
        """ Iterate through the words in the alphabetized list of topics. """
        for word in self._wordList:
            searching = True
            if firstRun == True:
                self._indexList,pageNum = isInList((self._indexList),word)
                (self._finalFormat).append(word)
                (self._indexDict)[word] = [pageNum]
                firstRun = False
            elif firstRun == False:
                placement = -1
                """ Checks the words in the final index format list to detmermine if there are duplicates. """
                for subFin in self._finalFormat:
                    placement += 1
                    if (searching == True):
                        """ Execute in the case that a duplicate was found. A key is added to the pre-existing topic,
                        and the page number page of the duplicate topic is found with the isInList function, and
                        assigned to that topic key, in addition to whatever other page numbers are in that topic key. """
                        if word == subFin:
                            self._indexList,pageNum = isInList((self._indexList),word)
                            (self._finalFormat)[placement] = ((self._finalFormat)[placement])
                            """ Turns the already present page numbers at a topic key, and makes them into a list. Appends
                            the new page number found for the duplicate topic to that list, and sorts it in ascending order.
                            After which, the new page number as well as the old ones are assigned back to the topic key. """
                            interimList = []
                            for curPage in range(len(((self._indexDict)[word]))):
                                interimList.append(((self._indexDict)[word])[curPage])
                            interimList.append(pageNum.strip())
                            interimList.sort()
                            ((self._indexDict)[word]) = interimList
                            searching = False
                """ Execute in the case that a duplicate was not found. A key is created for the topic, and the page
                number page of the unique topic is found with the isInList function, and assigned to that topic key.
                Also, that topic is appended to a list of the properly edited index topics. """
                if (searching == True):
                    self._indexList,pageNum = isInList((self._indexList),word)
                    (self._finalFormat).append(word.strip())
                    (self._indexDict)[word] = [pageNum.strip()]
                    searching = False

    def indexFinalizer(self):
        """ Function that finalizes the editing process for the index. Mostly just adds the appropriate page numbers in a
        nice format to the topic that it corresponds to, and write those all to a file, as a beautiful and alphabetized index. """
        self._formattedIndex = file('Index.txt','w')

        (self._formattedIndex).write('====   Index   ====\n')
        """ Iterates through all the topics in alphabetical order. """
        for topic in self._finalFormat:
            display = topic
            """ Appends the topic's corresponding page numbers to the topic, adding commas after multiple page nummbers if needed. """
            for pages in range(len((self._indexDict)[topic])):
                if pages < (len(((self._indexDict)[topic]))-1):
                    display += ' '+((self._indexDict)[topic])[pages]+','
                else:
                    display += ' '+((self._indexDict)[topic])[pages]+'\n'
            """ Writes the topic and its page numbers to the finished index file. """
            (self._formattedIndex).write(display)

