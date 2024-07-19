### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
        
    # Declare the class variable, with default value, for emails. 
    def __init__ (self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Initialise the instance variables for emails.
    has_been_read = False

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    new_email_one = Email('angryguy@test.com', 'Where are you?!', "It's been 3 days and my garden looks like a sinkhole!")
    new_email_two = Email('happyfish@test.com', 'Splash!', "Magicarps attack was not effective!")
    new_email_three = Email('guessTheMarioSong@test.com', 'Scary... :)', "dun-dun dun-dun dun-dun,,,,, dun-dun dun-dun dun-dun")
    inbox.append(new_email_one)
    inbox.append(new_email_two)
    inbox.append(new_email_three)

def list_emails():
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for count, email in enumerate(inbox):
        print(count, email.subject_line)

def read_email(index):

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    print(inbox[index].email_content)
    inbox[index].mark_as_read()
    print(f"\nEmail from {inbox[index].email_address} marked as read.\n")

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()
# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        list_emails()
        email_to_read = int(input("Which email to read? (0, 1 or 2): "))
        read_email(email_to_read)
    elif user_choice == 2:
        # add logic here to view unread emails
        all_read = True
        for i in range(0, len(inbox)):
            if (inbox[i].has_been_read == False):
                print(inbox[i].subject_line)
                all_read = False
        if all_read == True:
            print(f"\n You have no unread emails.\n")

    elif user_choice == 3:
        # add logic here to quit appplication
        break
    else:
        print("Oops - incorrect input.")