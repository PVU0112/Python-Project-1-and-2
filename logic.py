import os
import csv



def button_clicked(gui, vote_id: str, vote_input: str) -> None:
    """
    Handles the click event for submitting a vote.

    This function validates the inputs, checks if the voter has already voted,
    and writes the vote to a CSV file if no errors are found.

    Raises:
        ValueError: If the ID is empty or the vote input is empty, or if the voter has already voted.
    """
    try:
        # Validate input
        if not vote_id.strip():
            raise ValueError("ID cannot be empty.")
        if not vote_input.strip():
            raise ValueError("You must select a candidate.")

        # Create file if it doesn't exist and write header if needed
        if not os.path.exists("data.csv"):
            with open("data.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["vote_id", "vote_input"])  # Writing the header

        # Open file for reading and writing
        with open("data.csv", mode="r+", newline="") as file:
            reader = csv.reader(file)
            # Check if the ID already exists in the CSV
            for row in reader:
                if row and vote_id == row[0]:
                    raise ValueError("You have already voted.")

            # If no duplicate, add the vote
            writer = csv.writer(file)
            writer.writerow([vote_id, vote_input])
            gui.logic_text_label.config(
                text=f"Vote submitted for {vote_input} with ID {vote_id}.", fg="green"
            )

    except ValueError as e:
        gui.logic_text_label.config(text=str(e), fg="red")
    except Exception as e:
        gui.logic_text_label.config(text=f"An unexpected error occurred: {str(e)}", fg="red")


def results_clicked(gui) -> None:
    """
    Processes the voting results and displays the total votes for each candidate.

    This function reads the votes from the CSV file and counts how many votes
    each candidate (Jack and John) has received, then updates the GUI with the results.


    """
    jack_points = 0
    john_points = 0

    # Read votes from the CSV file
    with open("data.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Skip empty rows
                # Count votes for Jack and John
                if "Jack" in row:
                    jack_points += 1
                if "John" in row:
                    john_points += 1

    # Update the GUI label with the results
    gui.logic_text_label.config(
        text=f"Votes for Jack: {jack_points} Votes for John: {john_points}.", fg="green")

