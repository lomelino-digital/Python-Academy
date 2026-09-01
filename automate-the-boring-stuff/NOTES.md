# Chapters 1, 2 and 3 did not get notes at the time of study and practice but comments in the programs, i decided to start this file to log my thought since i don't think i'll be opening the exercise programs to check the comments so this will be the first commit already starting with chapter 4, I'm hand copying the pratical exercises in the book and making edits I find interesting.

## Chapter 4 — Notes

This chapter is the first one I found fully unknown or unexpected concepts such as local and global scopes and how functions work with global variables. These rules are worth memorizing or making natural:

Use these four rules to tell whether a variable belongs to a local scope or the global scope:

1. A variable in the global scope (that is, outside all functions) is always a global variable.

2. A variable in a function with a `global` statement is always a global variable in that function.

3. Otherwise, if a function uses a variable in an assignment statement, it is a local variable.

4. However, if the function uses a variable but never in an assignment statement, it is a global variable.

`try` and `except` were constructs I have been hoping to find so that I can now check if `int(input())` succeeds and handle an error by asking the user to input a valid number.

staff-role-builder.py after chapter 3 had this:

 ## A different type of pain that i feel will be handled in Chapter 6 - Lists
    
    if type_of_class == '0':
        print('Please select numbers 1 to 7 from the following:\n\n 1. Prompt Engineer \n\n 2. Researcher \n\n 3. Auditor \n\n 4. Brainstorm Assistant \n\n 5. Teacher \n\n 6. Article Writer \n\n 7. Fiction Writer')
        continue
    elif type_of_class != '1' and type_of_class != '2' and type_of_class != '3' and type_of_class != '4' and type_of_class != '5' and type_of_class != '6' and type_of_class != '7':
        print('Please pick a number from 1 to 7 or pick 0 to see the choices again.')
        continue


Which it seems I'm able to mitigate my pain in chapter, sometimes it's good to be wrong

## Realizations in practicals: 

1. magic8Ball.py is that whenever there is a need for different written messages printed to depending on different results the wall of elifs will come and I'm not even sure when if ever this can be done differently

2. Variation in coinflip.py exercise I'm testing try/except as I intend to use this in my prompt assistant program, I made the program unecessarily complicated, using try int(intput()) is probably something that is recurrent at least at this level of programs where the user inputs a choice

3. Some of these problems feel pointless to copy by hand but it's a rule i defined and will not change it mid chapter because I feel bored, it may change later if i decide they are not a valuable use of my time but for now I keep forcing myself to do the boring reps

 and then the reps turned into gains -> in the callstack exercise I realized functions can be defined in any order as long as they are defined when called

## in the ch04 staff_role_builder.py version I will be attempting to use most of what is learned in the chapter 4 including time.sleep for a more pleasant UX

## After a bigger effort the staff_role_builder.py is no longer a blob of confusing code but split into functions that can be maintained, removed the time.sleep, it was there just to add some UX closer to what we expect a program to do but it was merely decorative. Now we have plenty of functions that can be easily maintained, copied into other projects...or turned into lists when chapter 6 arrives, conscious decision - push through chapter 05 debugging, not because it's not important but because the lack of arrays, lists, tuples etc is feeling like too much of constraint but it sure makes me value them more than i did whenever i tried learning coding in the past.
