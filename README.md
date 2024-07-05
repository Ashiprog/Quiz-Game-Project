# Quiz-Game-Project
This script initializes a quiz using data from question_data imported from data. It utilizes QuizBrain from quiz_brain to manage quiz questions. The quiz continues until all questions are answered. Finally, it outputs the user's final score.

The quiz_brain module houses the QuizBrain class, designed to orchestrate the entire quiz process:

Initialization and Setup:
Loads question data from an external source (e.g., question_data) upon initialization.
Initializes variables to track the quiz's progress, including the current question index, user score, and total number of questions.

Quiz Flow Management:
next_question() method: Displays the current question to the user and prompts for a response.
Response Validation: Checks if the user's response matches the correct answer stored in the question data.
Score Tracking: Updates the user's score based on correct responses.

Quiz Completion:
still_has_questions() method: Returns True if there are remaining questions in the quiz.
Upon completing all questions, outputs the user's final score and a completion message.

User Interaction:
Handles user input, ensuring smooth progression through the quiz.
Provides feedback on each question's correctness and overall performance.

Educational Value:
Demonstrates object-oriented programming principles by encapsulating quiz logic into a reusable class.
Enhances understanding of data handling, user interaction, and program flow control in Python.

This module serves as the core component for conducting a quiz, offering comprehensive functionality to manage, administer, 
and conclude a quiz session effectively.
