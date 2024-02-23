"""Module providing a console bot assistant with CLI"""

from source.functions import (
    add_contact,
    change_contact,
    greetings,
    remove_contact,
    show_contacts,
    show_phone,
)


commands = {
    "add": add_contact,
    "all": show_contacts,
    "change": change_contact,
    "hello": greetings,
    "phone": show_phone,
    "remove": remove_contact,
}


def parse_input(user_input: str) -> tuple[str, *tuple[str, ...]]:
    """
    Function to parse commands received from the user using the CLI.

    :param user: a string with a command and possible arguments
    :return cmd, *args: a tuple with a command in string format and
                        the arguments, if any, as a tuple of strings
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main() -> None:
    """
    Function that provides Command Line Interface.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command not in commands:
            print("Invalid command.")
        else:
            print(commands[command](contacts, *args))


if __name__ == "__main__":
    main()
