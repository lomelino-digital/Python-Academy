import sys, time

def aistaff():

    print("What is the class of the new staff member?\n\n")
    print('Please select numbers 1 to 7 from the following:\n\n 1. Prompt Engineer \n\n 2. Researcher \n\n 3. Auditor \n\n 4. Brainstorm Assistant \n\n 5. Teacher \n\n 6. Article Writer \n\n 7. Fiction Writer')
    while True:
        

        type_of_class = input('Select a class type (1-7): ')
        # A different type of pain that i feel will be handled in Chapter 6 - Lists
        
        if type_of_class == '0':
            print('Please select numbers 1 to 7 from the following:\n\n 1. Prompt Engineer \n\n 2. Researcher \n\n 3. Auditor \n\n 4. Brainstorm Assistant \n\n 5. Teacher \n\n 6. Article Writer \n\n 7. Fiction Writer')
            continue
        elif type_of_class != '1' and type_of_class != '2' and type_of_class != '3' and type_of_class != '4' and type_of_class != '5' and type_of_class != '6' and type_of_class != '7':
            print('Please pick a number from 1 to 7 or pick 0 to see the choices again.')
            continue

            

        # Now we feel the pain of having 7 categories and having to write a block for each, the user has defined what class type of prompt he wishes to build
        if type_of_class == "1":
            
            print('The new staff member is a Prompt Engineer type.')
            role = "Prompt Engineer"
        elif type_of_class == "2":
            print('The new staff member is a Researcher type.')
            role = "Researcher"
        elif type_of_class == "3":
            print('The new staff member is an Auditor type.')
            role = "Auditor"
        elif type_of_class == "4":
            print('The new staff member is a Brainstorm Assistant type.')
            role = "Brainstorm Assistant"
        elif type_of_class == "5":
            print('The new staff member is a Teacher type.')
            role = "Teacher"
        elif type_of_class == "6":
            print('The new staff member is a Article Writer type.')
            role = "Article Writer"
        elif type_of_class == "7":
            print('The new staff member is a Fiction Writer type.')
            role = "Fiction Writer"
        

        print('How do you imagine this role working as a monolith or a modular execution?')
        architecture_type = input('>')


        print('What exactly do you intend this new staff member to solve, what problems it should tackle or how it can be useful')
        architecture_context = input('>')
        print('What data, information, examples or analogies better contribute for this staff members execution to be as intended?')
        architecture_data = input('>')
        print('What special instructions you would like to add to our prompt engineer before we start building?')
        architecture_instructions = input('>')
        print('Very well, thank you for your input Operator we will be building a ' + role  + ' ' + architecture_type + ' execution with the expressed specifications, we have enough for a pseudo magic prompt formula, let me just ask you this to hone in on your request...')

        magic_prompt = 'We are working on a new ' +  '**' + architecture_type + '**' + ' execution \n\n' + '## Role: \n' + role + '\n\n' + '## Context: \n' + architecture_context + '\n\n' + '## Data: \n' + architecture_data + '\n\n' + '## Special Instructions: \n' + architecture_instructions + '\n\n' + '>Ask exactly 5 high-value clarifying questions per round. After each round, evaluate whether the objective, responsibilities, constraints, inputs, outputs, architecture, and success criteria are sufficiently clear to construct the staff role. If not, ask another round of 5 questions. Do not begin constructing the final role until the specification is sufficiently unambiguous.'


        if type_of_class == "1":
            print('Why is this prompt engineer type needed over the one we are using already?')
            why_prompt_engineer = input('>')
            print("\n\n Thank you for your input, post this output into the prompt engineer:\n\n")
            print(magic_prompt)
            print('We are building a prompt engineer specialist type, the why of modifying, upgrading or rebuild the current execution is:\n\n' + why_prompt_engineer)
        elif type_of_class == "2":
            print(role + ' is a Researcher type.')
            print('Please be explicit, will you be using a regular search, deep research feature or other type (which?) with this prompt?')
            optimize_research = input('>')
            print("\n\n Do you have a specific type of usage for this research? Which, if no type general?")
            why_research = input('>')
            print("\n\n Are you running this research on a limitless token plan?")
            token_gobler = input('>')
            if token_gobler == 'yes' or token_gobler == 'Yes' or token_gobler == 'YES' or token_gobler == 'YARR' or token_gobler == 'sure':
                token_behaviour = " Maximize useful, non redundant source gathering and output tokens, direct your questions from precision in order to assist with this maximization "
            else:
                token_behaviour = ' Provide structure data and ask questions that help find the best desired output for the user '
            print("\n\n Thank you for your input, post this output into the prompt engineer:\n\n")
            
            print(magic_prompt)
            print('We are building a research specialist type, this research specialist should be optimized for:\n\n' + optimize_research + '\n\n The users specific goal with this research assistant is ' + why_research + token_behaviour)

        elif type_of_class != "1" and type_of_class != "2":
            print(magic_prompt)
        break
       
        
def singlePrompt():
    operation_type = input('Please describe what you would like this prompt to do:\n')
    magic_prompt = 'the user is trying to create a prompt to:' + operation_type +'ask 5 to 10 clarifying questions achieve more specificity in the result, these questions should guide the user to explore his intent in the request as well provide clarification on what the output should be, after the user replies ask 5 more questions and keep asking if further clarification is deemed necessary'       
    return(magic_prompt)   

print('Hello Mister Operator, are we building a new meta prompt?')
print()


while True:
    print('Would you like to build?\n')
    type_of_prompt = input('(1) Single operation prompt\n(2) A new member of AI Staff\n(3) Exit\n')
    try:
        type_of_prompt = int(type_of_prompt)
        if type_of_prompt == 3:
            print('Thank you for your hard word Mister Operator, come back anytime.')
            sys.exit()
        elif type_of_prompt == 2:

            aistaff()
            print('----------------------------------------------')
            print('Please copy and paste the output into your llm prompt engineer. \n Would you like to build another?')
           
        elif type_of_prompt == 1:
            
            print(singlePrompt())
            print('----------------------------------------------')
            print('Please copy and paste the prompt into the llm and take it from there.')

        else:
            time.sleep(0.5)
            print('Error detected')
            time.sleep(0.5)
            print(type_of_prompt + 'is not one of the available options, please select 1, 2 or 3')
        while True:
            keep_building = input('Build another? (y/n):')
            if keep_building != 'y' and keep_building != 'n':
                print('Invalid answer, please pick [y] or [n]')
                continue
            elif keep_building == 'n':
                print('Goodbye, come back soon!')
                sys.exit()
            elif keep_building == 'y':                
                break
            continue
    except ValueError:
        time.sleep(0.5)
        print('Error detected')
        time.sleep(0.5)
        print(type_of_prompt + 'is not one of the available options, please select 1, 2 or 3')
        continue


    
    

