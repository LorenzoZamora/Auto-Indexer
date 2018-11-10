"""
Name: Lorenzo Zamora
Email: Lorenzo.Zamora@SLU.edu
Current Date: 5/3/2018 
Course Information: CSCI 1300
Instructor: Judy Etchison
"""

""" Driver for the AutoIndexer class. The appropriate input file is specified,
but feel free to add a different one, or put a garbage file in to test the file
checker program in the AutoIndexer class. """
from AutoIndexer import *

""" Creation of an AutoIndexer object. """
ProgrammingBook = AutoIndexer('editorsNotes.txt')

""" Loading the AutoIndexer program with the editor's notes for index editing. """
ProgrammingBook.loadEdNotes()

""" Alphabetize the topics in the editor's notes, and which will be in the
finished index. """
ProgrammingBook.alphabetizer()

""" Have the topics be matched with their corresponding page numbers, after
parsing and alphabetization. """
ProgrammingBook.pageWordMatcher()

""" Format the index so that it is clean, after which a file containing the
index is created. """
ProgrammingBook.indexFinalizer()
