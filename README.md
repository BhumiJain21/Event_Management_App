🎊 Event Management Membership SystemA modern, advanced web application designed to manage event memberships with a focus on User Experience (UX) and Pastel Design. The system features real-time status tracking, auto-generation of IDs, and role-based access control.✨ Key FeaturesRole-Based Access Control (RBAC): Separate, secure dashboards for Administrators and Standard Users.Automatic Member ID Generation: Eliminates manual entry errors. The system automatically generates IDs in the format MEM-2026-001.Dynamic Membership Status: Real-time logic that calculates and displays Active/Expired badges based on the join date and selected duration.Instant Live Search: A high-speed search bar that filters the membership directory as you type, without reloading the page.Modern Pastel UI: Built with "Nowadays" design principles, including Glassmorphism, soft gradients, and rounded professional components.Admin Controls: Exclusive permissions for Administrators to add new records or delete existing ones.🛠️ Tech StackBackend: Python 3.12, Flask FrameworkDatabase: SQLite3 (Relational Database)Frontend: HTML5, CSS3 (Advanced Custom Styling), JavaScript (Vanilla JS for Live Search)🚀 Installation & Setup1. Clone the ProjectNavigate to your project folder:Bashcd event_management_project
2. Initialize the DatabaseRun the setup script to create the necessary tables (users and membership) and populate default accounts:Bashpython create_db.py
3. Launch the ApplicationStart the Flask server:Bashpython app.py
Open your browser and visit: http://127.0.0.1:5000🔑 Access CredentialsRoleUsernamePasswordAdministratoradmin123Standard Useruser1123📂 Project StructurePlaintextevent_management_project/
├── app.py              # Main Flask application & business logic
├── create_db.py        # Database initialization & schema script
├── database.db         # SQLite database (generated on first run)
├── static/
│   ├── style.css       # Custom modern pastel stylesheets
│   └── logo.jpg        # Brand identity assets
└── templates/          # Jinja2 HTML Templates
    ├── base.html       # Global layout (Navbar, Footer, Flash messages)
    ├── login.html      # Secure authentication interface
    ├── admin_dashboard.html
    ├── user_dashboard.html
    ├── add_membership.html # Optimized form (Auto-ID enabled)
    └── view_membership.html # Interactive data table with search
💡 Planned Enhancements[ ] Report Export: Functionality to download membership lists as PDF or Excel files.[ ] Password Security: Implementing Werkzeug hashing for encrypted passwords.[ ] Profile Avatars: Dynamic user icons in the navigation bar.Developed with ❤️ by Bhumi Jain
