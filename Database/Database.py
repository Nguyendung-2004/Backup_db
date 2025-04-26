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
    ('Nguyễn Ngọc Dũng', 'dung@gmail.com'),
    ('Nguyễn Thành Tín', 'tin@gmail.com'),
    ('Đồng Thanh Huyền', 'huyen@gmail.com')
])

conn.commit()
conn.close()

print("Đã tạo file Database.sqlite3 thành công.")
