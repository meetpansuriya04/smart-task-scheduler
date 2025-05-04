# Smart Task Scheduler

A simple Flask-based task management and scheduling API.

## Features
- Create and fetch tasks
- Schedule tasks by due date
- RESTful API
- Optimized task scheduling algorithm

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/smart-task-scheduler.git
   cd smart-task-scheduler
   ```

2. **Create a Virtual Environment:**
   - If you don't have `virtualenv` installed, run:
     ```bash
     pip install virtualenv
     ```
   - Create and activate the virtual environment:
     - On Windows:
       ```bash
       python -m venv venv
       venv\Scriptsctivate
       ```
     - On macOS/Linux:
       ```bash
       python3 -m venv venv
       source venv/bin/activate
       ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Database:**
   - Run the following to create the database schema:
     ```bash
     python
     >>> from app import db
     >>> db.create_all()
     >>> exit()
     ```

5. **Run the Application:**
   ```bash
   python run.py
   ```

6. **Access the API:**
   - Visit `http://127.0.0.1:5000/` to access the API endpoints.
