CREATE SCHEMA cinema;
USE cinema;

CREATE TABLE products (
    code CHAR(5) PRIMARY KEY,
    name VARCHAR(60),
    price FLOAT
);

CREATE TABLE ticket (
    code CHAR(5) PRIMARY KEY,
    name CHAR(6),
    price FLOAT
);

CREATE TABLE invoices (
    code INT PRIMARY KEY AUTO_INCREMENT,
    ticket CHAR(5),
    ticket_price FLOAT,
    no_tickets INT,
    tickets_value FLOAT,
    products_value FLOAT,
    date_time DATETIME,
    total_value FLOAT
);

CREATE TABLE invoices_details (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_price FLOAT,
    no_products INT,
    products_value FLOAT,
    invoice INT,
    product CHAR(5)
);

INSERT INTO products 
VALUES("CC-01", "Palomitas y gaseosa personal", 8000),
	  ("CC-02", "Sándwich y gaseosa personal", 11200),
	  ("CC-03", "Pizza y gaseosa personal", 9600);

INSERT INTO ticket VALUES("CT-01", "Diurna" ,20000);
SET @base_price := (SELECT price FROM ticket WHERE code = "CT-01");
INSERT INTO ticket 
VALUES("CT-02", "Tarde", @base_price * 1.20),
	  ("CT-03", "Noche", @base_price * 1.40);
      
ALTER TABLE invoices 
	ADD FOREIGN KEY (ticket) REFERENCES ticket(code);
    
ALTER TABLE invoices_details
	ADD FOREIGN KEY (invoice) REFERENCES invoices(code),
	ADD FOREIGN KEY (product) REFERENCES products (code);
