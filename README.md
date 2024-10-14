# Project Setup Guide

This project is configured with a `Makefile` to streamline the setup and management of the backend environment. Follow the instructions below to install dependencies, set up the database, and run the server.

## Prerequisites

- **Python 3** must be installed.
- **uv** package is required. Install it with:

  ```bash
  pip install uv
  ```

- Run the command to setup, install and migrate the DB

  ```bash
  make setup
  ```

- `make run` to simply start the server

### User Credentials:

- Username: `admin`
- Email: `admin@example.com`
- Password: `testing321`

**Note:** You can use both username or email for login.