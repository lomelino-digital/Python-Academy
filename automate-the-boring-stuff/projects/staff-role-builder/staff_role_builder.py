import sys

# initially i had the funcitons all as type_of_class argument
# Then i changed it beause i thought that even though we were working
# In local scope that it was still better to have different variable names
# But now i see it was more work than necessary creating variable names that
# Didn't make things simpler

def classSelector():
    print("What is the class of the new staff member?\n\n")
    print('Please select numbers 1 to 7 from the following:\n\n 1. Prompt Engineer \n\n 2. Researcher \n\n 3. Auditor \n\n 4. Brainstorm Assistant \n\n 5. Teacher \n\n 6. Article Writer \n\n 7. Fiction Writer')
    while True:              
        role_type = input('Select a class type (1-7): ')
        try:
            role_type = int(role_type)       
            if 0 < role_type <= 7:
                return role_type 
            print(str(role_type) + ' is an Invalid Selection, please select an integer from 1 to 7')
            continue
        except ValueError:
            print(role_type + ' is an Invalid Selection, please select an integer from 1 to 7')
            continue



def get_role(type_of_class):         

        # Now we feel the pain of having 7 categories and having to write 
        # a block for each, the user has defined what class type of prompt he 
        # wishes to build but we are reducing the pain using function already
        # Hopefully this operation, thinking this function could just be part of
        # classSelector() but this way i have an int value and a string class
        # name value for the roles, not sure if it will be useful but it's
        # simple to merge the functions if i decide to, or maybe turn this function
        # into some sort of list

        if type_of_class == 1:            
            # print('The new staff member is a Prompt Engineer type.')
            return "Prompt Engineer"
        elif type_of_class == 2:
            # print('The new staff member is a Researcher type.')
            return "Researcher"
        elif type_of_class == 3:
            # print('The new staff member is an Auditor type.')
            return "Auditor"
        elif type_of_class == 4:
            # print('The new staff member is a Brainstorm Assistant type.')
            return "Brainstorm Assistant"
        elif type_of_class == 5:
            # print('The new staff member is a Teacher type.')
            return "Teacher"
        elif type_of_class == 6:
            # print('The new staff member is a Article Writer type.')
            return "Article Writer"
        elif type_of_class == 7:
            # print('The new staff member is a Fiction Writer type.')
            return "Fiction Writer"

    # I was wanting just one more function for the whole prompt
    # But having 2 choices i want to still guardrail the possible
    # options as i don't the user causing errors with typos
    # and other user issues
        
def architectureType(arch_role):
    print('How do you imagine this ' + arch_role + ' working as a monolith or a modular execution?\n')
    while True:
        architecture_type = input('(1) Monolith\n\n(2) Modular Execution\n\n>')
        try:
            architecture_type = int(architecture_type)
            if architecture_type == 1:
                return "Monolith"
            elif architecture_type == 2: 
                return "Modular Execution"
            else:
                print(str(architecture_type) + ' is not a valid number, Please select a valid number, will this ' + arch_role + 'work as a:\n')
                continue
        except ValueError:
            print(architecture_type + ' is not a valid choice, Please select a valid number, will this ' + arch_role + 'work as a:\n')
            continue

    # Probably suboptimal do declare the global variables
    # But since this is chapter 4 or less i don't see a 
    # Way to return multiple values from a function which
    # Probably you can if you can just return a list or a
    # Tuple
            
def promptContext():            
    print('What do you intend this new prompt member to assist you with, what problems it should tackle or how it can be useful')
    global architecture_context
    architecture_context = input('>')
    print('What data, information, examples or analogies better contribute for this staff members execution to be as intended?')
    global architecture_data
    architecture_data = input('>')
    print('What special instructions you would like to add to the prompt before we start building?')
    global architecture_instructions
    architecture_instructions = input('>')
    # For a fun little moment
    if architecture_instructions == 'make no mistakes':
        print('------------------------------')
        print('I see you are good at this!')
        print('------------------------------')


def classSpecs(spec_role):
    if spec_role == 3:
        print('What will you needed audited? (example: Text, Code, A spreadsheet')
        why_audit = input('>')
        return 'This auditor specializes in:\n' + why_audit
    elif spec_role == 2:
        print('Building a Researcher type.\n')
        print('Please be explicit, will you be using a regular search, deep research feature or other type (which?) with this prompt?\n')
        optimize_research = input('>')
        print("\n\n Do you have a specific type of usage for this research? Which, if no type general?")
        why_research = input('>')             
   
       
        return 'We are building a research specialist type, this research specialist should be optimized for:\n\n' + optimize_research + '\n\n The users specific goal with this research assistant is ' + why_research + ' Provide structure data and ask questions that help find the best desired output for the user.'

    else:
        return 'Ask if more specificity is required.'
    
# Probably unecessary as a function and can be written in type_of_prompt selection
# But still i can build it better later in the single function and transport it
# More easily like this:       
        
def singlePrompt():
    operation_type = input('Please describe what you would like this prompt to do:\n')
    return 'the user is trying to create a prompt to do: ' + operation_type + ' ask 5 to 10 clarifying questions achieve more specificity in the result, these questions should guide the user to explore his intent in the request as well provide clarification on what the output should be, after the user replies ask 5 more questions and keep asking if further clarification is deemed necessary'       
    

# The program starts running here:

print('Hello Mister Operator, are we building a new meta prompt?')
print()


while True:
    print('What would you like to build?\n')
    type_of_prompt = input('(1) Single operation prompt\n(2) A new member of AI Staff\n(3) Exit\n')
    try:
        type_of_prompt = int(type_of_prompt)
        if type_of_prompt == 3:
            print('Thank you for your hard word Mister Operator, come back anytime.')
            sys.exit()
        elif type_of_prompt == 2:
            classID = classSelector()
            role = get_role(classID)
            architecture_type = architectureType(role)
            promptContext()
            class_specs = classSpecs(classID)
            magic_prompt = 'We are working on a new ' +  '**' + architecture_type + '**' + ' execution \n\n' + '## Role: \n' + role + '\n\n' + '## More role specific intructions:\n\n' + class_specs + '## Context: \n' + architecture_context + '\n\n' + '## Data: \n' + architecture_data + '\n\n' + '## Special Instructions: \n' + architecture_instructions + '\n\n' + ' Ask exactly 5 high-value clarifying questions per round. After each round, evaluate whether the objective, responsibilities, constraints, inputs, outputs, architecture, and success criteria are sufficiently clear to construct the staff role. If not, ask another round of 5 questions. Do not begin constructing the final role until the specification is sufficiently unambiguous.'
            print('Please copy and paste the following prompt into the llm and take it from there:\n')
            print('----------------------------------------------')
            print(magic_prompt)
            print('----------------------------------------------')
           
        elif type_of_prompt == 1:
            magic_prompt = singlePrompt()
            print('Please copy and paste the following prompt into the llm and take it from there:\n')
            print('----------------------------------------------------')
            print(magic_prompt)
            print('----------------------------------------------------')

        else:            
            print('Error detected')
            print(str(type_of_prompt) + ' is not one of the available options, please select 1, 2 or 3')
            continue
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
        print('Error detected')
        print(type_of_prompt + 'is not one of the available options, please select 1, 2 or 3')
        continue