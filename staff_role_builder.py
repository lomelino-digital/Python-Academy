print('Hello Mister Operator, are we adding a new member of staff?')
#Some ifs that will come later in case the answer is no , for example, no upgrade existing staff member
#lets be more ambitions and create an entire interface with the ai staff somehow
print("What is the role of the new staff member?")
role = input('>')
print('We will be building a ' + role + ' then.')
print('How do you imagine this role working as a monolith or a modular execution?')
architecture_type = input('>')
print('What exactly do you intend this new staff member to solve, what problems it should tackle or how it can be useful')
architecture_context = input('>')
print('What data, information, examples or analogies better contribute for this staff members execution to be as intended?')
architecture_data = input('>')
print('What special instructions you would like to add to our prompt engineer before we start building?')
architecture_instructions = input('>')
print('Very well, thank you for your input Operator we will be building a ' + role  + ' ' + architecture_type + ' execution with the expressed specifications, we have enough for a pseudo magic prompt formula')

magic_prompt = 'We are working on a new ' +  '**' + architecture_type + '**' + ' execution \n\n' + '## Role: \n' + role + '\n\n' + '## Context: \n' + architecture_context + '\n\n' + '## Data: \n' + architecture_data + '\n\n' + '## Special Instructions: \n' + architecture_instructions + '\n\n' + '>Ask exactly 5 high-value clarifying questions per round. After each round, evaluate whether the objective, responsibilities, constraints, inputs, outputs, architecture, and success criteria are sufficiently clear to construct the staff role. If not, ask another round of 5 questions. Do not begin constructing the final role until the specification is sufficiently unambiguous.'
print(magic_prompt)