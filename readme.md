# FastAPI Project

Welcome to the FastAPI project! This README will guide you through setting up your development environment, installing dependencies, and running the project.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Creating a Virtual Environment](#creating-a-virtual-environment)
  - [Installing Packages](#installing-packages)
- [Running the Project](#running-the-project)

## Prerequisites

Ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.7 or higher)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)

## Setup

### Creating a Virtual Environment

#### Windows

1. Open Command Prompt or PowerShell.
2. Navigate to your project directory.
3. Run the following command to create a virtual environment:

   ```bash
   python -m venv .venv


### Activating the Virtual Environment
    .\.venv\Scripts\activate

### Install packages
    pip install -r requirements.txt

### Run the project
    uvicorn main:app --reload

Your FastAPI application will be available at http://127.0.0.1:8000


### Interactive API Documentation

[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
