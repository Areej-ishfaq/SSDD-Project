# Secure Task Manager

A Flask-based web application designed to provide secure task management with robust security features and best practices.

## Introduction
The Secure Task Manager is a web application built using Flask that allows users to securely manage their tasks. 
The application incorporates user authentication, task CRUD operations, and implements multiple security measures including CSRF protection, rate limiting, and secure coding practices.

## Features
### User Management
- Secure registration with validation
- Login with session protection
- Rate-limited login attempts
- Secure logout functionality

### Task Management
- Create tasks with title, description, status, priority, and dates
- View tasks sorted by due date
- Edit task details with validation
- Delete tasks with ownership verification

## Technology Stack
- **Framework**: Flask (Python web framework)
- **Database**: SQLite via Flask-SQLAlchemy
- **Frontend**: HTML, CSS, Jinja2 templating
- **Security**: 
  - Flask-WTF (CSRF protection)
  - Flask-Talisman (Content Security Policy)
  - Flask-Limiter (rate limiting)
- **Authentication**: Flask-Login for session management

## Security Features
- CSRF Protection
- Rate Limiting (200/day, 50/hour)
- Input sanitization to prevent XSS attacks
- Password hashing using Werkzeug
- Content Security Policy
- Session protection
- Form validation
- Output encoding

## Installation
1. Clone the repository:
   git clone [repository-url] , 
   cd [repository]

2. Create a virtual environment:
   python -m venv venv , 
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   flask run

## Usage
  1. Access the application at http://localhost:5000
  2. Register a new account
  3. Login with your credentials
  4. Manage your tasks through the intuitive interface

## Security Checks

### Input Validation
Form validation with WTForms
Data length and format requirements
Date validation to prevent invalid entries

### Authentication
Secure password hashing
Session protection
Rate limiting on login attempts

### Access Control
Route protection with @login_required
Task ownership verification

## OWASP Compliance
1. The application adheres to OWASP Top Ten guidelines:
2. Protection against Broken Access Control
3. Prevention of Cryptographic Failures
4. Mitigation against Injection attacks
5. Security Misconfiguration protection

## Static Analysis
The project was analyzed using Codacy, which identified and helped resolve:
17 Code Style issues
3 Security issues
3 Error Prone issues

### Key fixes included:
1. Bootstrap definition issues
2. Unused variable removal
3. Werkzeug version update

## Dynamic Analysis
OWASP ZAP was used for dynamic analysis, identifying and resolving:
1. Missing CSP directives
2. Server header information leakage
