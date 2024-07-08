# Employee Management System

## Overview
The Employee Management System (EMS) is a web application built with FastAPI, which allows users to manage employee records. The system supports functionalities such as fetching employee data, inserting new employee records, updating existing records, and deleting records.

## Features
- **Fetch Employee Data**: Retrieve and display all employee records from the database.
- **Insert Employee Data**: Add new employee records through a web form.
- **Delete Employee Data**: Remove employee records based on their ID.
- **Update Employee Data**: Update existing employee information using a web form.
- **User Interface**: Simple HTML templates for interaction with the EMS.

## Modules and Libraries Used
- **FastAPI**: Web framework used for building APIs and handling web requests.
- **Jinja2**: Templating engine for rendering HTML templates.
- **pyodbc**: Python library for accessing databases using Open Database Connectivity (ODBC).

## Project Structure
- `BL.py`: Contains the main application logic and endpoints for the FastAPI server.
- `DBA.py`: Handles database connections and CRUD operations.
- `templates/`: Directory containing HTML templates for the web interface.
- `static/`: Directory containing static files like CSS.

---
