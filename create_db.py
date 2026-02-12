import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # 1. Purane tables delete karein (taaki fresh start ho)
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS membership")

    # 2. Users Table Banayein (Login ke liye)
    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    # 3. Membership Table Banayein (Auto ID aur Join Date ke saath)
    cursor.execute("""
    CREATE TABLE membership (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        member_no TEXT UNIQUE NOT NULL,
        duration TEXT NOT NULL,
        join_date DATE DEFAULT CURRENT_DATE
    )
    """)

    # 4. Default Admin aur User add karein
    # Inke bina aap login nahi kar paoge
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ('admin', '123', 'admin'))
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ('user1', '123', 'user'))

    conn.commit()
    conn.close()
    print("✅ Database Reset Successful! Both 'users' and 'membership' tables created.")

if __name__ == "__main__":
    init_db()