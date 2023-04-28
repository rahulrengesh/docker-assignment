CREATE TABLE students (
  reg_no VARCHAR(10) NOT NULL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  vaccination_status VARCHAR(5) NOT NULL
);

INSERT INTO students (reg_no, name, vaccination_status)
VALUES
  ('1001', 'rahul', 'YES'),
  ('1002', 'ram', 'NO'),
  ('1003', 'ashok', 'YES');