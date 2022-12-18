# Name:  Matthew Stasinowsky
# Student Number:  10471721

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of Programming Principles in Semester 1, 2021.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json

try:
    file = open('data.txt', 'r') # open the file in read mode
    data = json.load(file)  # read the json data into the 'data' variable
    file.close()

# If the file doesn't exist, set the 'data' variable to an empty list.
except:
    data = []
    


# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt):
    while True:

        try:
            user_input = int(input(prompt))
            return user_input

        # If it is NOT an integer then display error message.
        except ValueError:
            print('Invalid input - Please enter an integer.')
            
        


# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    while True:
        
        user_input = input(prompt).strip()
        
        # Check if the prompt is empty
        if user_input == '':
            print('Please enter something.')
        else:
            return user_input
        


# This function opens "data.txt" in write mode and writes data_list to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data_list):
    file = open('data.txt', 'w') # open the file in write mode
    json.dump(data_list, file, indent=4) # encode 'data_list' to json and write to file
    file.close()
    


# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.



# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the "Would You Rather" Admin Program.')

while True:
    
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower() # Convert input to lowercase to make choice selection case-insensitive.
        
    if choice == 'a':
        # Add a new question.
        question_dict = {}
        
        print('Both options should be phrased to follow "Would you rather..."')
        
        question_dict['option_1'] = input_something("Enter Option 1: ").strip('?')
        question_dict['option_2'] = input_something("Enter Option 2: ").strip('?')

        # Enter endless loop to make sure user inputs 'y' or 'n'
        # Not case sensitive 
        while True:
            
            mature_input = input_something('Is this question intended for mature audiences only? [Y/N]: ').upper()
        
            if mature_input == 'Y':
                question_dict['mature'] = True
                break
            elif mature_input == 'N':
                question_dict['mature'] = False
                break
            else:
                print("Invalid input - Please enter 'Y' or 'N'")
                

        # Adding keys for votes
        question_dict['votes_1'] = 0
        question_dict['votes_2'] = 0
            
        # Add question (dictionary) to data (list) 
        data.append(question_dict)

        # Write to file with 'save_data' function
        save_data(data)

        print('\n''Question added successfully')
        
        
        
    
    elif choice == 'l':
        # List the current questions.
        # If data is empty, display message
        if data == []:
            print('No questions saved.')

        else:     
            print('\n''List of questions:')
        
            # Loop through and print each item in the list
            for index, question in enumerate(data):
                print(index+1,') ', question['option_1'],'/',question['option_2'])




    elif choice == 's':
        # Search the current questions.
        no_match = True  

        # If data is empty, display message
        if data == []:
            print('No questions saved.')
        else:
            search_term = input_something("Enter search term: ").lower()

            print('Search results: ')

            # Loop through each option in all questions and
            # check for a match with the search_term
            for index, question in enumerate(data):
                if search_term in question['option_1'].lower() or search_term in question['option_2'].lower():
                    print(index+1,') ', question['option_1'],'/',question['option_2'])
                    no_match = False

            if no_match == True:
                print('\n''No matches found.')




    elif choice == 'v':
        # If data is empty, display message
        if data == []:
            print('No questions saved.')
            
        # Prompt user for their choice of question
        else:
            view_number = input_int('Question number to view: ') - 1
            
            # Check if it's a valid choice (an option on the list)
            if view_number >= len(data) or view_number < 0:
                print('Invalid question number.')
                
            # Display selected question details
            else:     
                print('\n''Would you rather...')
                print('Option 1) '+data[view_number]['option_1']+'?')
                print('Option 2) '+data[view_number]['option_2']+'?')

                # Display warning if question is for mature audiences
                if data[view_number]['mature'] == True:
                    print('\n''This question is intended for mature audiences only!')

                # Display no votes message if there are no votes
                if data[view_number]['votes_1'] == 0 and data[view_number]['votes_2'] == 0:
                    print('Nobody has answered this question yet.')
                # Otherwise, display votes
                else:
                    print('Option 1 has received',data[view_number]['votes_1'],'vote(s),',
                          'Option 2 has received',data[view_number]['votes_2'],'vote(s).')

                


        

    elif choice == 'd':
        # Delete a question.
        # If data is empty, display message
        if data == []:
            print('No questions saved.')
            
        # Prompt user for their choice of question
        else:
            question_to_delete = input_int('Question number to delete: ') - 1

            # Check if it's a valid choice (an option on the list)
            if question_to_delete >= len(data) or question_to_delete < 0:
                print('Invalid index number.')

            # Delete selected question
            else:
                del data[question_to_delete]
                # Write to file with 'save_data' function
                save_data(data)

                print('\n''Question deleted successfully.')
                

        

    elif choice == 'q':
        # Quit the program.
        print("Goodbye!")
        break




    else:
        # Print "invalid choice" message.
        print('\n''Invalid choice.')




# If you have been paid to write this program, please delete this comment.
