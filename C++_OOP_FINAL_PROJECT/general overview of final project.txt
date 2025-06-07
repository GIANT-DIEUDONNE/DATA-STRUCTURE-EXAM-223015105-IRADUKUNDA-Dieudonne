UNIVERSITY OF RWANDA
HUYE CAMPUS
BUSINESS INFORMATION TECHNOLOGY DEPARTMENT
NAMES: IRADUKUNDA DIEUDONNE
REG_No: 223015105
OBJECT ORIENTATED PROGRAMMING IN C++
FINAL PROJECT
PROJECT: Quiz Engine

GENERAL OVERVIEW
 
The Console Quiz Engine is a command-line C++ application that allows users to participate in multiple-choice quizzes. It is designed using object-oriented programming principles, where both registered and guest users interact with the quiz system through a shared base class interface. This demonstrates the use of inheritance and polymorphism in C++. The quiz questions are stored in a dynamically allocated array, and users have the ability to add or remove questions at runtime. This feature highlights the practical use of dynamic memory allocation and pointer arithmetic in managing data. By combining these features, the project offers a strong foundation for understanding key C++ concepts in a real-world application. It is especially useful for students and beginners who want to practice how to use OOP and manual memory management in C++ programming.

Explanation of each line of codes of projects 
  
#include <iostream>// for input/output
#include <cstring>// for string manipulation
using namespace std; // using standard namespace for convenience
struct Question {// struct to represent a question in the quiz
    char prompt[100];// question prompt
    char choices[4][40];// array to store choices for the question
    int correctIdx;// index of the correct answer
};


class QuizUser {// abstract class representing a user taking the quiz
public:// pure virtual function to take the quiz
    virtual int takeQuiz(Question* questions, int n) = 0;// pure virtual function to take the quiz
    virtual ~QuizUser() {}// virtual destructor to allow proper cleanup of derived classes
};


class RegisteredUser : public QuizUser {// derived class for registered users
private:// private members can only be accessed by this class
    int* score;// pointer to store the score of the registered user
public:// constructor to initialize RegisteredUser
    RegisteredUser() {// constructor to initialize RegisteredUser
        score = new int(0);// dynamically allocate memory for score
    }
    ~RegisteredUser() {// destructor to clean up dynamic memory
        delete score;// free the allocated memory for score
    }
    int takeQuiz(Question* questions, int n) override {// takes the quiz for registered users
        int correct = 0;
        for (int i = 0; i < n; i++) {// loop through each question
            Question* q = questions + i;  // Pointer arithmetic
            std::cout << "\nQ" << i + 1 << ": " << q->prompt << "\n";// prints the question prompt
            for (int j = 0; j < 4; j++) {// prints all the choices for the question
                std::cout << "  " << j << ": " << q->choices[j] << "\n";// prints all the choices for the question
            }
            int answer;// variable to store user's answer
            std::cout << "Your answer: ";// prompt for the user's answer
            std::cin >> answer;// prompt for the user's answer
            if (answer == q->correctIdx) {// checks if the answer is correct
                correct++;// increment the correct answer count
            }
        }
        *score = correct;// store the score in the score pointer
        std::cout << "\nRegistered User Score: " << *score << "/" << n << "\n";// prints the score for the registered user
        return correct;// returns the number of correct answers
    }
};


class GuestUser : public QuizUser {// derived class for guest users
public:// constructor to initialize GuestUser
    int takeQuiz(Question* questions, int n) override {
        int correct = 0;// variable to store the number of correct answers
        for (int i = 0; i < n; i++) {// loop through each question
            Question* q = questions + i;  // Pointer arithmetic
            std::cout << "\nQ" << i + 1 << ": " << q->prompt << "\n";// prints the question prompt
            for (int j = 0; j < 4; j++) {// prints all the choices for the question
                std::cout << "  " << j << ": " << q->choices[j] << "\n";// prints all the choices for the question
            }
            int answer;// variable to store user's answer
            std::cout << "Your answer: ";// prompt for the user's answer
            std::cin >> answer;// prompt for the user's answer
            if (answer == q->correctIdx) {// checks if the answer is correct
                correct++;
            }
        }
        std::cout << "\nGuest User Score: " << correct << "/" << n << "\n";// prints the score for the guest user
        return correct;// returns the number of correct answers
    }
};

void addQuestion(Question*& questions, int& n, const Question& newQ) {// adds a new question to the questions array
    Question* newArray = new Question[n + 1];// create a new array with one more question slot
    for (int i = 0; i < n; i++) {// loop through existing questions
        newArray[i] = questions[i];// copy existing questions to the new array
    }
    newArray[n] = newQ;// copy the new question to the end of the new array
    delete[] questions;// delete the old array of questions to free memory
    questions = newArray;// assign the new array to the questions pointer
    n++;// increment the number of questions
    std::cout << "Question added to the system Total questions: " << n << "\n";
}


void removeQuestion(Question*& questions, int& n, int index) {// removes a question at the specified index from the questions array
    if (index < 0 || index >= n) {// checks if the index is valid
        std::cout << "Invalid index! No question removed.\n";// prints message if the index is invalid
        return;// checks if the index is valid
    }
    Question* newArray = new Question[n - 1];// create a new array with one less question
    for (int i = 0, j = 0; i < n; i++) {// loop through existing questions
        if (i != index) {// checks if the current index is not the one to remove
            newArray[j++] = questions[i];// copy all questions except the one to remove
        }
    }
    delete[] questions;// delete the old array of questions to free memory
    questions = newArray;// assign the new array to the questions pointer
    n--;// decrement the number of questions
    std::cout << "Question removed into the system! Total questions: " << n << "\n";
}


void adminMenu(Question*& questions, int& n) {// function to handle admin menu for managing questions
    int choice;// variable to store user choice
    do {
        std::cout << "\n--- Admin pannel ---\n";// prints header for admin panel
        std::cout << "1. Add Question\n";// option to add a question
        std::cout << "2. Remove Question\n";// option to remove a question
        std::cout << "3. View Questions\n";// option to view all questions
        std::cout << "0. Finish Editing\n";// option to finish editing questions
        std::cout << "Enter your choice: ";// prompt for user input
        std::cin >> choice;// prompt for user input for choice
        std::cin.ignore();  // Clear newline

        if (choice == 1) {// checks if the choice is to add a question
            Question newQ;// create a new question object
            std::cout << "Enter the question prompt: ";// prompt for the question prompt
            std::cin.getline(newQ.prompt, 100);// prompt for the question prompt

            for (int i = 0; i < 4; i++) {// loop through each choice
                std::cout << "Enter choice " << i << ": ";// prompt for each choice
                std::cin.getline(newQ.choices[i], 40);// prompt for each choice
            }

            std::cout << "Enter the index of the correct answer (0-3): ";
            std::cin >> newQ.correctIdx;// prompt for index of the correct answer
            std::cin.ignore();  // Clear newline

            addQuestion(questions, n, newQ);// adds the new question to the list of questions

        } else if (choice == 2) {// checks if the choice is to remove a question
            if (n == 0) {// checks if there are no questions available
                std::cout << "No questions to remove.\n";// prints message if there are no questions available
            } else {
                std::cout << "\nCurrent Questions:\n";// prints all the questions available
                std::cout << "=====================\n";// prints header for viewing questions
                for (int i = 0; i < n; i++) {// loop through all the questions
                    std::cout << i << ": " << questions[i].prompt << "\n";// prints all the questions available
                }
                std::cout << "Enter the index of the question to remove: ";// prompt for index of the question to remove
                int idx;
                std::cin >> idx;// prompt for index of the question to remove
                std::cin.ignore();  // Clear newline
                removeQuestion(questions, n, idx);// removes the question at the given index
            }

        } else if (choice == 3) {// checks if the choice is to view all questions
            std::cout << "\n--- View Questions ---\n";// prints header for viewing questions
            if (n == 0) {// checks if there are no questions available
                std::cout << "No questions available.\n";// prints message if no questions are available
            } else {
                std::cout << "\nCurrent Questions:\n";// prints all the questions available
                for (int i = 0; i < n; i++) {// loop through all the questions
                    std::cout << i << ": " << questions[i].prompt << "\n";// prints all the questions available
                }
            }
        }

    } while (choice != 0);// loop until the admin finishes editing questions
}


int main() {// main function to run the quiz engine
    int n = 0;
    Question* questions = nullptr;// pointer to store questions

    std::cout << "Welcome to the Quiz Engine!\n";// prints welcome message
    std::cout << "=====================\n";// prints header for the quiz engine

    // Admin pannel for satting up quetions
    std::cout << "=== Admin Panel ===\n";// prints header for admin panel
    std::cout << "\nAdmin, please set up the questions.\n";// prompt for admin to set up questions
    adminMenu(questions, n);// call the admin menu to set up questions

    if (n == 0) {// checks if there are no questions available
        std::cout << "\nNo questions available. Exiting.\n";
        delete[] questions;// free the allocated memory for questions
        return 0;
    }

    // Users take quiz
    int numUsers;// variable to store number of users
    std::cout << "\nEnter the number of users taking the quiz: ";// prompt for number of users
    std::cin >> numUsers;// prompt for number of users
    std::cin.ignore();  // Clear newline

    QuizUser** users = new QuizUser*[numUsers];// allocate memory for users

    // Assign users (for demo: alternate Registered and Guest)
    for (int i = 0; i < numUsers; i++) {// loop through each user
        if (i % 2 == 0) {
            users[i] = new RegisteredUser();// alternate between RegisteredUser and GuestUser
        } else {
            users[i] = new GuestUser();// alternate between RegisteredUser and GuestUser
        }
    }

    // Each user takes the quiz
    for (int i = 0; i < numUsers; i++) {// loop through each user
        std::cout << "\n=== User " << i + 1 << " ===\n";// prints header for each user
        users[i]->takeQuiz(questions, n);// each user takes the quiz
    }

    // Clean up
    for (int i = 0; i < numUsers; i++) {//
        delete users[i];// free each user object
    }
    delete[] users;// free the allocated memory for users
    delete[] questions;// free the allocated memory for questions

    std::cout << "\nThank you for playing!\n"; // prints message indicating the end of the quiz
    return 0;// return 0 to indicate successful execution of the program

}

