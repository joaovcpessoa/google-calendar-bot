Google Calendar Automation
Automate your Google Calendar tasks effortlessly with this Python project. This automation script allows you to interact with the Google Calendar service by providing various strategies for actions such as requesting a new event, canceling an existing event, or rescheduling an event.

Table of Contents
Introduction
Features
Getting Started
Installation
Usage
Project Structure
Classes and Strategies
Utility Functions
Main Functionality
Execution
Logging
Contributing
License
Introduction
This Python project serves as an automation tool for interacting with the Google Calendar service. It employs a strategy pattern, allowing for dynamic selection of different actions based on user input. The use of classes, logging, and a modular structure enhances maintainability and extensibility.

Features
Request the creation of a new event
Cancel an existing event
Reschedule an event
Flexible strategy pattern for future enhancements
Getting Started
Installation
Clone the repository to your local machine:

bash
Copy code
git clone <repository-url>
cd google-calendar-automation
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Configure your Google Calendar API credentials by following the instructions provided in the code.

Run the script:

bash
Copy code
python main.py
Follow the on-screen prompts to choose an action and provide necessary details.

Project Structure
The project is organized into the following components:

main.py: Entry point for the script.
google_calendar_service.py: Handles interactions with the Google Calendar API.
event_strategies.py: Defines the action strategies (e.g., create, cancel, reschedule).
event_processor_context.py: Implements the context for executing selected strategies.
utils.py: Contains utility functions for user input and strategy parameters.
Classes and Strategies
ActionStrategy: Abstract base class for action strategies.
RequestEventActionStrategy: Creates a new event on the Google Calendar.
CancelEventActionStrategy: Cancels an existing event (placeholder, not implemented).
RescheduleEventActionStrategy: Reschedules an event (placeholder, not implemented).
EventProcessorContext: Context class for executing selected strategies.
GoogleCalendarService: Manages Google Calendar API interactions and provides service methods.
Utility Functions
get_user_choice: Prompts the user to choose an action.
get_action_params: Returns parameters based on the user's choice.
Main Functionality
The main function instantiates a GoogleCalendarService, prompts the user for an action, selects the corresponding strategy, creates an EventProcessorContext with the strategy, and executes the chosen action.

Execution
The script is designed to be executed directly. Use the provided instructions to configure credentials and run the script.

Logging
The project uses the logging module to log operations. Logs are stored in the 'logs' directory, with each execution having a unique identifier.

Contributing
Feel free to contribute to the project by opening issues or submitting pull requests. Follow the guidelines outlined in the CONTRIBUTING.md file.

License
This project is licensed under the MIT License.