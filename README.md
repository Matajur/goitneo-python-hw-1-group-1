# Homework #1

A function to display a list of colleagues with upcoming birthdays &amp; a bot assistant to manage a personal list of contacts

## General acceptance criteria

* The repository goitneo-python-hw-1-group-name has been created.
* The homework contains a link to the GitHub repository and an attached repository file in .zip format.
* The assignments are completed strictly per the technical description (recommendations for completion and evaluation criteria).
* The console has no errors or warnings when running the bot.
* The names of variables and functions are clear and descriptive.
* The code is properly formatted and complies with the PEP8 standard.

## Task #1

### Technical description

You need to implement a function to display a list of colleagues you need to congratulate on their birthdays this week.

You have a list of vocabularies called `users`; each vocabulary must have the keys `name` and `birthday`. This structure represents a model of a list of users with their names and birthdays. `Name` is a string with the user's name, and `birthday` is a `datetime` object containing the birthday date.

For example,

`{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}`

Your task is to write a function `get_birthdays_per_week` that takes a list of `users` as input and outputs to the console (using `print`) a list of users who need to be congratulated each day of the following week.

### Assessment Criteria

1. The get_birthdays_per_week function displays the names of birthdays in the format:

`Monday: Bill Gates, Jill Valentine`

`Friday: Kim Kardashian, Jan Koum`

2. Users who had their birthday on the weekend should be congratulated on Monday.
3. The function outputs users with birthdays a week ahead of the current day.
4. The week starts on Monday.

## Task #2

### Technical Description

Write a console bot assistant that recognizes commands from the keyboard and responds according to the command entered.

In this homework, we will focus on the bot's interface. A CLI (Command Line Interface) is the simplest and most convenient interface at the initial stage of development. CLI is quite simple to implement. Any CLI consists of three main elements:

* Command parser. The part is responsible for parsing the strings entered by the user and extracting keywords and command modifiers from the string.
* Command handlers are a set of functions, also called `handlers`, who are responsible for the immediate execution of commands.
* Request-response loop. This part of the application is responsible for receiving data from the user and returning the response to the user from the function, `handler`.

At the first stage, our bot assistant should be able to store a name and phone number, find a phone number by name, change the recorded phone number, and display all the records it has saved in the console. To implement this simple logic, we'll use a dictionary. In the dictionary, we will store the username as a key and the phone number as a value.

### Assessment Criteria

* The bot should stay in an endless loop, waiting for the user's command.
* The bot ends its work if it detects the words: "close" or "exit".
* The bot is not sensitive to the case of the entered commands.
* The bot accepts the following commands:

1. `"hello"`, and responds to the console with a following message — `"How can I help you?`"
2. `"add username phone"`. With this command, the bot saves a new contact in its memory, for example, in a dictionary. The user enters the name `username` and phone number `phone`, always separated by a space.
3. `"change username phone"`. With this command, the bot saves a new phone number `phone` for the `username` contact already existing in the address book.
4. `"phone username"`. With this command, the bot displays the phone number for the specified `username` contact in the console.
5. `"all"`. This command displays all saved contacts with phone numbers in the console.
6. `"close"` or `"exit"` — using any of these commands, the bot terminates its work after it displays the message `"Goodbye!"` in the console and completes its activity.

* The command logic is implemented in separate functions, and these functions take one or more strings as input and return a string.
* The whole logic of interaction with the user is implemented in the `main` function, and all `prints` and `inputs` occur only there.
