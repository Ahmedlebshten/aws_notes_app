from flask import Flask, request, redirect
from datetime import datetime
import mysql.connector

app = Flask(__name__)

# connect to mariadb
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",  
    database="notesdb"
)
cursor = conn.cursor()
# -----------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get("note")
        if content:
            cursor.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
            conn.commit()
        return redirect("/")
    cursor.execute("SELECT content, created_at FROM notes ORDER BY created_at DESC")
    rows = cursor.fetchall()
#-----------------------
    note_html = ""
    for note in rows:
        note_html += f"<p>🕒 {note[1]}<br>📌 {note[0]}</p><hr>"

    return f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    max-width: 600px;
                    margin: 40px auto;
                    background-color: #f9f9f9;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }}
                h2 {{
                    text-align: center;
                    color: #333;
                }}
                textarea {{
                    width: 100%;
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 6px;
                    font-size: 14px;
                    resize: vertical;
                }}
                button {{
                    margin-top: 10px;
                    padding: 10px 20px;
                    font-size: 14px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                }}
                button:hover {{
                    background-color: #45a049;
                }}
                .note {{
                    background-color: #fff;
                    border-left: 5px solid #4CAF50;
                    padding: 10px;
                    margin-bottom: 10px;
                    border-radius: 4px;
                }}
                .timestamp {{
                    color: #888;
                    font-size: 12px;
                }}
            </style>
        </head>
        <body>
           <h2>Note Taking App</h2>
            <form method="POST">
                <textarea name="note" rows="4" placeholder="Write your note here..."></textarea><br>
                <button type="submit">Save Note</button>
            </form>
            <hr>
            {note_html}
        </body>
        </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
