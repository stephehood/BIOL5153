## The README for BIOL5153


#### More updates to parse_GFF.py
In class on 4/25/18 they went over the edits to add funtions to the Parse_GFF script. Updates have been made and pushed.
#### Updates to parse_gff
Added conditions to Parse_GFF to make it more flexible and compact

#### Homework 6
After realizing I was making life way harder than it needed to be on myself, I took a step back and realized, hey this ins't going to be all that bad. Homework 6 involved taking the filter_fasta_file_by_length.py and finishing it so that the user could set a min seq and use it to filter a FASTA file. Then I needed to take that code and make a filter_fasta_file_by_list.py where I used basically the same code but switched out the '-m' '--min_seq_length' to '-l' '--list', and removed any sequences just leaving headers.

#### Argparse
Attempted to use the filter_fasta_by_length.py code to apply to my parseGFF.py code but ran into some issues. Hopefully I can resolve some of these issues before class tomorrow. 041018
Update: 041118: backbone of code was ok, but I had added a bunch of things from the internet that were NOT needed. Tips for the future include trying to use the information provided to me from the class/book to solve my issues.
Code works well now!
#### Homework 5 -ParseGFF.py

This was a huge challenge for me as I had to learn a lot of new funtions on my own. I was able to pull out the start and stop locations but the I wasn't able to use that information to pull the data from watermelon.fsa
Hopefully tomorrow in class we will go over this more.
Update: 041018
Haley and Andy helped me get this code to work. Now need to use argparse so the code will be more versatile

Use BioPython
Stack Overflow.com has some helpful information
#### CV
Markdown version of my CV - March 2018

#### Python for Biologist in-text examples
##### Chapter 2 - Printing and manipulating text
##### Chapter 3 - Reading and writing files
##### Chapter 4 - Lists and Loops
##### Chapter 9 - Files, programs, and user input
##### Chapter 5- Functions
    This chapter was full of important information to make your code more flexible. Jupyter notebook wasn't returning correct values. Made everything zero
##### Chapter 6 - Conditional Tests
    This chapter reviewes if/ else, elif, etc. to help your code make decisions on the fly
##### Chapter 7 - Regular Expressions
    This chapter gave several examples on how to use regular expressions. This will be helpful for my final project. Reference the PowerPoint from class for more examples of Regular Expressions and how to use them.  
##### Chapter 8 - Dicitionaries
    This chapter was useful for learning how return more efficient output and make more concise code. Introduced a lot of new methods (keys, etc.)

    ```
