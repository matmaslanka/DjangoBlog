# Django Blog
A blog application with user registration, login functionality, and the ability for users to create and update their blog entries. Users can register for new accounts and manage their posts after logging in.

## Installation

1. Move the project to your preferred directory.
2.  Open a terminal and navigate to the project directory in bash: 
   `cd .\blog`
3. Set up a virtual environment:
   python3 -m venv env <br/>
   source env/bin/activate  # On Windows: env\Scripts\activate
4. Install the dependencies from requirements.txt:
   `pip install -r requirements.txt`
5. Set up the database and run migrations (the application will crash without this step):
   `python manage.py migrate`


## Running the project
1. Run the Django development server:
   `python manage.py runserver`

2. Access the project in your browser at: http://127.0.0.1:8000/.

## Usage
When the user runs the application, they will see the homepage. At the top of the page, there is a message showing the user's login status (either logged in or logged out).

Below the title "Blog App", there are three tabs:

#### Home:
Redirects to the list of all blog entries. If no entries exist, the user will see an "Add First Entry" button. If entries are present, they will be listed. The user can edit their own entries if they are the author.
#### Add Entry:
Allows logged-in users to create new blog entries.
#### Login/Logout:
If the user is logged out, this tab displays "Login" and redirects to the login page. If the user is logged in, it shows "Logout".
To add a new entry, the user must be logged in. If the user does not have an account, they can register by clicking the "Sign up!" button on the login page.

### Admin Access
(Optional) To access the Django admin interface, create a superuser account:
   `python manage.py createsuperuser`


