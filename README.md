# Hamji

Welcome to Tridge sandbox project!

We'd love to collaborate with amazing developers as we drive the development of "Global Sourcing Hub of Food & Agriculture" into the future.

## Guidelines
- Fork this repository
- Setup project
- Achieve TODO items one by one
- Mark an item as done in the TODO list
    - [x] Like this
- Push your changes to remote
- Share us the link to your remote repository

## Setup
- Install PIP packages
```
pip install -r requirements.txt
```
- Run server
```
python manage.py runserver
```
- Now that the server’s running, visit http://127.0.0.1:8000/polls/ with your Web browser

## TODO
1. [ ] Raise 404 if no matching question
1. [ ] Show only questions that are published and not yet closed
1. [ ] Enable to comment on question
1. [ ] Enable to comment on comment
1. [ ] Prevent a user voting more than once on a question
1. [ ] Enable to suggest new choice for question
1. [ ] Limit the number of choices that can be suggested on one question
1. [ ] Extends `Question.closed_at` by one day, when new choice is suggested for that question
    - Requirements:
        - Use Django signal/receiver system
1. [ ] In `/polls/`, fetch only 5 questions through REST API
1. [ ] [Advanced] Handle race condition on handling "vote" action
1. [ ] [Advanced] Implement login system
1. [ ] [Advanced] Implement system that a question creator can approve suggested choices
1. [ ] [Advanced] Implement global search for questions and choices
