# Name:  Matthew Stasinowsky
# Student Number:  10471721

# This file is provided to you as a starting point for the "wyr.py" program of Assignment 2
# of Programming Principles in Semester 1, 2021.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
import tkinter
import tkinter.messagebox
import tkinter.font as tkFont
import json


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of wyr.py" section of the assignment brief.
        
        self.main = tkinter.Tk() # Create main window
        self.main.title('Would You Rather') # Give window title
        self.main.geometry('500x150')
        self.main.resizable(width=True, height=True)

        self.main.configure(bg='SkyBlue2')


        try:
            file = open('data.txt', 'r') # open the file in read mode
            self.data = json.load(file)  # read the json data into the 'self.data' variable
            file.close()
        except:
            tkinter.messagebox.showerror('Warning','Missing or invalid file!')
            self.main.destroy()
            return


        # Set fonts
        fontStyle = tkFont.Font(family="Lucida Grande", size=15, weight='bold')
        Question_fontStyle = tkFont.Font(family="Lucida Grande", size=10)
     
        # Would you rather message
        self.message = tkinter.Label(self.main, text = 'Would you rather...', bg='SkyBlue2', font=fontStyle)
        self.message.pack(padx=10, pady=10)

        # Buttons (Question options)
        self.button1 = tkinter.Button(self.main, command=lambda: self.record_vote('votes_1'), font=Question_fontStyle)
        self.button1.pack(padx=20, fill='x')
        self.button2 = tkinter.Button(self.main, command=lambda: self.record_vote('votes_2'), font=Question_fontStyle)
        self.button2.pack(padx=20, pady=10, fill='x')
        
        self.question_num = 0

        # View mature questions option
        self.mature = tkinter.messagebox.askyesno('Mature Content','Do you want to see questions intended for mature audiences?')
        if self.mature == True:
            self.show_mature = True
        else:
            self.show_mature = False


        self.show_question()
        
        tkinter.mainloop()
            




    def show_question(self):
        # This method is responsible for displaying the current question's options in the GUI and ending the program.
        # See Point 1 of the "Methods in the GUI class of wyr.py" section of the assignment brief.
        
        try:
            self.currentQuestion = self.data[self.question_num]
            
        except IndexError:
            tkinter.messagebox.showinfo('End of Questions','That was the final question.''\n''The program will now end.')
            self.main.destroy()
            return


        # Find correct question
        if self.currentQuestion['mature'] == True and self.show_mature == False:
            # Skip mature question
            self.question_num = self.question_num + 1
            self.show_question()
            
        else:
            # Display chosen question        
            self.button1.configure(text=self.currentQuestion['option_1']+'?')
            self.button2.configure(text=self.currentQuestion['option_2']+'?')


            
            
                




    def record_vote(self, vote):   
        # This method is responsible for recording the user's choice when they select an option of a question.
        # See Point 2 of the "Methods in the GUI class of wyr.py" section of the assignment brief.

        # Add vote
        self.data[self.question_num][vote] = self.data[self.question_num][vote] + 1

        # Save file
        file = open('data.txt', 'w') # open the file in write mode
        json.dump(self.data, file, indent=4) # encode 'data_list' to json and write to file
        file.close()

        # Show message
        tkinter.messagebox.showinfo('Vote Recorded','Your choice has been recorded')

        # Load next question
        self.question_num = self.question_num + 1
        self.show_question()






# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()


# If you have been paid to write this program, please delete this comment.
