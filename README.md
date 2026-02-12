🎊 Event Management Membership System

A modern, advanced web application designed to manage event memberships with a focus on User Experience (UX) and Pastel Design. The system features real-time status tracking, auto-generation of IDs, and role-based access control.

✨ Key Features

Role-Based Access Control (RBAC): Separate, secure dashboards for Administrators and Standard Users.

Automatic Member ID Generation: System auto-generates IDs in the format MEM-2026-001, eliminating manual entry errors.

Dynamic Membership Status: Real-time logic calculates and displays Active/Expired badges based on join date and duration.

Instant Live Search: High-speed search bar filters membership directory as you type, without reloading.

Modern Pastel UI: Built with Nowadays design principles, including Glassmorphism, soft gradients, and rounded professional components.

Admin Controls: Exclusive permissions for Administrators to add new records or delete existing ones.

🛠️ Tech Stack

Backend: Python 3.12, Flask Framework

Database: SQLite3 (Relational Database)

Frontend: HTML5, CSS3 (Advanced Custom Styling), JavaScript (Vanilla JS for Live Search)

🚀 Installation & Setup

Clone the Project

cd event_management_project


Initialize the Database

python create_db.py


This creates necessary tables (users and membership) and populates default accounts.

Launch the Application

python app.py


Open your browser and visit: http://127.0.0.1:5000

🔑 Access Credentials
Role	Username	Password
Administrator	admin	123
Standard User	user1	123
📂 Project Structure
event_management_project/
├── app.py                 # Main Flask application & business logic
├── create_db.py           # Database initialization & schema script
├── database.db            # SQLite database (generated on first run)
├── static/
│   ├── style.css          # Custom modern pastel stylesheets
│   └── logo.jpg           # Brand identity assets
└── templates/             # Jinja2 HTML Templates
    ├── base.html          # Global layout (Navbar, Footer, Flash messages)
    ├── login.html         # Secure authentication interface
    ├── admin_dashboard.html
    ├── user_dashboard.html
    ├── add_membership.html  # Optimized form (Auto-ID enabled)
    └── view_membership.html # Interactive data table with search

💡 Planned Enhancements

 Report Export: Download membership lists as PDF or Excel files.

 Password Security: Implement Werkzeug hashing for encrypted passwords.

 Profile Avatars: Dynamic user icons in the navigation bar.

Developed with ❤️ by Bhumi Jain
