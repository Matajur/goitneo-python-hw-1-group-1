"""Module providing a functionality to manage the contacts in a contact list"""


def add_contact(contacts: dict, *args: list) -> str:
    """
    Function of adding a new contact with a phone to the contact list.

    :param args: list with contact name and phone number to add to contact list
    :param contacts: a dictionary with user contacts
    :return: a message about a successful operation
    """
    name, *phone = args
    contacts[name] = phone
    return f"Contact: {name} added."


def change_contact(contacts: dict, *args: list) -> str:
    """
    Function of changing an existing contact's phone number.

    :param args: list with contact name and phone number to replace in the
                contact list
    :param contacts: a dictionary with user contacts
    :return: a message about a successful or unsuccessful operation
    """
    try:
        name, phone = args
        contacts[name] = phone
        return f"Contact: {name} updated."
    except KeyError:
        return f"Contact: {name} not found."  # type: ignore
    except ValueError:
        return "Provide user name and phone to change"


def greetings(*_) -> str:
    """
    User greeting function.

    :return: a message with greetings
    """
    return "How can I help you?"


def remove_contact(contacts: dict, *args: list) -> str:
    """
    Function to erase an existing contact.

    :param arg: list with contact name to be erased
    :param contacts: a dictionary with user contacts
    :return: a message about a successful or unsuccessful operation
    """
    try:
        name = args[0]
        contacts.pop(name)
        return f"Contact: {name} removed."
    except KeyError:
        return f"Contact: {name} not found."
    except IndexError:
        return "Provide contact name"


def show_contacts(contacts: dict, *_) -> str:
    """
    Function of displaying a complete list of contacts.

    :param contacts: a dictionary with user contacts
    :return: a string with the full contact list or a warning that the
            contact list is empty
    """
    if len(contacts):
        contacts = dict(sorted(contacts.items()))
        result = "Contact list:"
        for name, phone in contacts.items():
            result += f"\n{name}: {phone}"
        return result
    return "Contact list is empty."


def show_phone(contacts: dict, *args: list) -> str:
    """
    Function of displaying the user's phone number.
    """
    try:
        name = args[0]
        phone = contacts[name]
        return f"Contact: {name}, phone: {phone}."
    except KeyError:
        return f"Contact: {name} not found."  # type: ignore
    except IndexError:
        return "Provide contact name"
