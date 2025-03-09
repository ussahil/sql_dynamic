# Installation and Setup Guide  

#### Step 1: Install PostgreSQL  
1. Download PostgreSQL from the official website: [PostgreSQL Download](https://www.postgresql.org/download/)  
2. Follow the installation instructions for your operating system.  
3. During installation, set up your **username** and **password** (you will need these for authentication).  

#### Step 2: Configure Your PostgreSQL Credentials  
1. Ensure that PostgreSQL is running.  
2. Save your **username** and **password** as environment variables or configure them in your application settings.  

#### Step 3: Set Up the Poetry Environment  
1. Navigate to your project directory:  
   ```bash
   cd /path/to/your/project
   
2. Install dependencies using Poetry
  ```bash
  poetry install
```
##### Run the Application
  ```bash
  poetry run python app/main.py


