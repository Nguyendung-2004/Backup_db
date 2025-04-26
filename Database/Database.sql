-- database.sql

-- Tạo bảng users
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);

-- Chèn dữ liệu mẫu
INSERT INTO users (name, email) VALUES ('Nguyễn Ngọc Dũng', 'dung@gmail.com');
INSERT INTO users (name, email) VALUES ('Nguyễn Thành Tín', 'tin@gmail.com');
INSERT INTO users (name, email) VALUES ('Đồng Thanh Huyền', 'huyen@gmail.com');
