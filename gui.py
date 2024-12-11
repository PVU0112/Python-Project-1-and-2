from tkinter import *
from logic import button_clicked, results_clicked


class Gui:
    def __init__(self:object, window):

        ''' Creates the Graphics for the Vote Application
        Voting_app_name frames the name of the application
        Id input frames the ID text and an input text
        Candidates_text just shows text
        Candidate choices has two radio buttons with a vote_input variable with the values of the respective candidate
        Logic text is a text that is used whenever an error occur, confirms an action, or show texts after voting
        Vote and Results have buttons with commands that are in logic.py


        '''
        self.window = window
        # Voting app name
        self.voting_app_name = Frame(self.window, width=460, height=40,)
        self.vote_title = Label(self.voting_app_name, text='Voting Application')
        self.vote_title.pack(side='left', padx=10, pady=5)
        self.voting_app_name.pack(anchor='w', padx=10, pady=10)

        # ID input
        self.id_name = Frame(self.window, width=460, height=40)
        self.vote_id_label = Label(self.id_name, text='ID:')
        self.vote_id_input = Entry(self.id_name)
        self.vote_id_label.pack(side='left', padx=5)
        self.vote_id_input.pack(padx=5, side='left')
        self.id_name.pack(anchor='w', padx=10, pady=10)

        # Candidate text
        self.candidate_text = Frame(self.window, width=460, height=30)
        self.candidate_text_title = Label(self.candidate_text, text='CANDIDATES')
        self.candidate_text_title.pack(side='left', padx=10, pady=5)
        self.candidate_text.pack(anchor='w', padx=10, pady=5)

        # Candidates
        self.candidate_choices = Frame(self.window, width=460, height=50)
        self.vote_input = StringVar(value="")  # Use StringVar for Radiobutton variables
        self.candidate_1 = Radiobutton(self.candidate_choices, text="Jack", variable=self.vote_input, value="Jack")
        self.candidate_2 = Radiobutton(self.candidate_choices, text="John", variable=self.vote_input, value="John")
        self.candidate_1.pack(side='left', padx=20)
        self.candidate_2.pack(side='left', padx=20)
        self.candidate_choices.pack(anchor='w', padx=10, pady=10)

        # Logic text label (for feedback messages)
        self.logic_text_label = Label(self.window, text="", fg="red")
        self.logic_text_label.pack(anchor='w', padx=10, pady=10)

        # Submit Button
        self.vote_button = Frame(self.window, width=460, height=40)
        self.vote_submit_button = Button(
            self.vote_button,
            text="SUBMIT",
            command=lambda: button_clicked(self, self.vote_id_input.get(), self.vote_input.get()),
        )
        self.vote_submit_button.pack(side='left', padx=5, pady=5)
        self.vote_button.pack(anchor='w', padx=10, pady=10)

        # Results
        self.vote_results = Frame(self.window, width=460, height=40)
        self.vote_results_button = Button(
            self.vote_results,
            text="Check Results",
            command=lambda: results_clicked(self)

        )
        self.vote_results_button.pack(side='left', padx=5, pady=5)
        self.vote_results.pack(anchor='w', padx=10, pady=10)
