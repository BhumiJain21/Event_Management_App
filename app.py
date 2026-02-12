from flask import Flask, render_template, request, redirect, session, flash, url_for
import sqlite3
import datetime

app = Flask(__name__)
app.secret_key = "bhumi_secret"

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# --- LOGIN ---
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (u,p)).fetchone()
        if user:
            session["user"] = u
            session["role"] = user["role"]
            flash(f"Welcome {u}!", "success")
            return redirect(url_for(user['role']))
        flash("Invalid Credentials", "danger")
    return render_template("login.html")

# --- DASHBOARDS ---
@app.route("/admin")
def admin():
    if session.get("role") == "admin":
        return render_template("admin_dashboard.html")
    return redirect(url_for('login'))

@app.route("/user")
def user():
    if session.get("role") == "user":
        return render_template("user_dashboard.html")
    return redirect(url_for('login'))

# --- ADD MEMBERSHIP (AUTO-GENERATE ID) ---
@app.route("/add_membership", methods=["GET","POST"])
def add_membership():
    if session.get("role") != "admin":
        return "Access Denied"

    if request.method == "POST":
        name = request.form["name"]
        duration = request.form["duration"]
        
        conn = get_db()
        # Auto-Generate Member No (MEM-2026-001)
        last_id_row = conn.execute("SELECT MAX(id) FROM membership").fetchone()
        next_id = (last_id_row[0] or 0) + 1
        year = datetime.datetime.now().year
        member_no = f"MEM-{year}-{next_id:03d}" 

        conn.execute("INSERT INTO membership(name, member_no, duration) VALUES(?,?,?)",
                     (name, member_no, duration))
        conn.commit()
        flash(f"Success! Member ID: {member_no}", "success")
        return redirect(url_for('view_membership'))

    return render_template("add_membership.html")

# --- VIEW REPORT (WITH STATUS LOGIC) ---
@app.route("/view_membership")
def view_membership():
    if not session.get("user"):
        return redirect(url_for('login'))
    
    conn = get_db()
    members = conn.execute("SELECT * FROM membership").fetchall()
    
    # Python logic to calculate status
    enhanced_members = []
    today = datetime.date.today()
    
    for m in members:
        # Convert sqlite join_date to python date
        join_dt = datetime.datetime.strptime(m['join_date'], '%Y-%m-%d').date()
        
        # Calculate Expiry based on duration
        if "Year" in m['duration']:
            years = int(m['duration'].split()[0])
            expiry_dt = join_dt.replace(year=join_dt.year + years)
        else: # 6 Months
            expiry_dt = join_dt + datetime.timedelta(days=180)
        
        status = "Active" if today <= expiry_dt else "Expired"
        color = "#d4edda" if status == "Active" else "#f8d7da" # Pastel Green/Red
        text_color = "#155724" if status == "Active" else "#721c24"

        enhanced_members.append({
            "id": m['id'],
            "name": m['name'],
            "member_no": m['member_no'],
            "join_date": m['join_date'],
            "status": status,
            "color": color,
            "text_color": text_color
        })

    return render_template("view_membership.html", members=enhanced_members)

# --- DELETE ---
@app.route("/delete_member/<int:id>")
def delete_member(id):
    if session.get("role") == "admin":
        conn = get_db()
        conn.execute("DELETE FROM membership WHERE id=?", (id,))
        conn.commit()
        flash("Member Deleted", "info")
    return redirect(url_for('view_membership'))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)