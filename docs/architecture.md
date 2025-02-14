---
title: Architecture
nav_order: 3
---

# Architecture

The Workspace App follows a modular and scalable architecture using Flask, structured with an MVC-inspired approach. It efficiently manages user authentication and collaborative workspaces.

The app leverages SQLAlchemy for database management and Werkzeug for authentication and security. It follows Flask’s Blueprint pattern, where:

+ Models (models.py) define the database schema.
+ Views (templates/) handle the frontend with Jinja2.
+ Controllers (routes.py) manage request handling and business logic.


## Codemap

```plaintext
WORKSPACE_APP/
│── instance/
│   ├── database.db  #Local database
│
│── migrations/
│   ├── versions/  #Tracks database schema changes using Alembic
│   ├── alembic.ini  # lembic configuration file
│   ├── env.py  #Alembic environment setup
│   ├── script.py.mako  #Template for auto-generated migrations
│
│── venv/  #Virtual environment containing dependencies
│
│── ws_app/  #Main application directory
│   ├── __pycache__/  #Compiled Python files for optimization
│   ├── static/  #Static assets such as CSS and JavaScript files
│   │   ├── drawing-worker.js  #JavaScript functionality for workspace interactions
│   │   ├── style.css  #Stylesheet for UI design
│   ├── templates/  #HTML templates (Jinja)
│   │   ├── actual_workspace.html  #Page for viewing and editing workspaces
│   │   ├── dashboard.html  #Main dashboard displaying workspaces
│   │   ├── dummy_page.html  #Placeholder/testing template
│   │   ├── login.html  #User login page
│   │   ├── register.html  #User registration page
│   │   ├── settings.html  #Profile settings and account management
│   │   ├── welcome.html  #Welcome screen for new users
│   │   ├── workspace_creation.html  #Page to create new workspaces
│   │   ├── workspace_info.html  #Displays information about a workspace
│   ├── __init__.py  #Initializes the Flask application
│   ├── database_sqlite.py  #Manages the SQLite database connection
│   ├── forms.py  #Defines form handling (WTForms)
│   ├── models.py  #Defines the database schema (Users, Workspaces, Notes)
│   ├── routes.py  #Contains all API endpoints and routing logic
│
│── .gitignore  #Specifies files to ignore in Git version control
│── README.md  #Readme file
│── requirements.txt  #List of dependencies for installation, generated with pip freeze
│── run.py  #Entry point to start the Flask application