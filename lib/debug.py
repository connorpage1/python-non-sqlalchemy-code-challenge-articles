#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    connor = Author("Connor")
    mag = Magazine("The Examiner", "CBT")
    test_art = Article(connor, mag, "Test Article")
    art_2 = Article(connor, mag, "Test article")
    
    # don't remove this line, it's for debugging!
    ipdb.set_trace()
