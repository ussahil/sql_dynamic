Installation and Setup Guide
Step 1: Install PostgreSQL
Download PostgreSQL from the official website: https://www.postgresql.org/download/
Follow the installation instructions for your operating system.
During installation, set up your username and password (you will need these for authentication).
Step 2: Configure Your PostgreSQL Credentials
Ensure that PostgreSQL is running.
Save your username and password as environment variables or configure them in your application settings.
Step 3: Set Up the Poetry Environment
Navigate to your project directory:
bash
Copy
Edit
cd /path/to/your/project
Install dependencies using Poetry:
bash
Copy
Edit
poetry install
Step 4: Run the Application
Execute the following command to run the application:
bash
Copy
Edit
poetry run python app/main.py
