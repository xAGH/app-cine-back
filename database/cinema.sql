CREATE SCHEMA cinema;
USE cinema;

CREATE TABLE products (
    code CHAR(5) PRIMARY KEY,
    name VARCHAR(60),
    price FLOAT,
    discount FLOAT
);

CREATE TABLE ticket (
    code CHAR(5),
    price FLOAT
);

CREATE TABLE invoices (
    code INT(5) ZEROFILL PRIMARY KEY AUTO_INCREMENT,
    ticket CHAR(1) REFERENCES ticket (code),
    ticket_price FLOAT,
    no_tickets INT,
    tickets_value FLOAT,
    date_time DATETIME,
    total_value FLOAT
);

CREATE TABLE invoices_details (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_price FLOAT,
    no_products INT,
    producst_value FLOAT,
    invoice INT REFERENCES invoices (code),
    product CHAR(5) REFERENCES products (code)
);

INSERT INTO products 
VALUES("CC-01", "Palomitas y gaseosa personal", 10000, 0.20),
	  ("CC-02", "Sándwich y gaseosa personal", 14000, 0.20),
	  ("CC-03", "Pizza y gaseosa personal", 12000, 0.20);

INSERT INTO ticket VALUES("CT-01", 20000);
SET @base_price := (SELECT price FROM ticket WHERE code = "CT-01");
INSERT INTO ticket 
VALUES("CT-02", @base_price * 1.20),
	  ("CT-02", @base_price * 1.40)
