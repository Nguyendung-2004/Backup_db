import sqlite3

# Tạo (hoặc mở) database file
conn = sqlite3.connect('Database.sqlite3')
cursor = conn.cursor()

# Tạo bảng users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# Thêm dữ liệu mẫu
cursor.executemany('''
INSERT INTO users (name, email) VALUES (?, ?)
''', [
    ("Nguyễn Văn A", "a@example.com"),
    ("Trần Thị B", "b@example.com"),
    ("Lê Văn C", "c@example.com")
])

conn.commit()
conn.close()

print("✅ Đã tạo file Database.sqlite3 thành công.")
