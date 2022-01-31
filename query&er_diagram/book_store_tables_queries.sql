create database book_store;
use book_store;

CREATE TABLE user_details
(
	user_id INT AUTO_INCREMENT NOT NULL, email_id VARCHAR(300) NOT NULL, password VARCHAR(100) NOT NULL,
    full_name VARCHAR(300) NOT NULL, mobile_no VARCHAR(20), is_verified BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (user_id), CONSTRAINT unique_email UNIQUE (email_id)
);

CREATE TABLE books
(
	id INT NOT NULL,author VARCHAR(300) NOT NULL, title VARCHAR(300) NOT NULL, image TEXT,
	quantity INT NOT NULL, price DOUBLE NOT NULL, description TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE wishlist
(
	id INT AUTO_INCREMENT NOT NULL, user_id INT NOT NULL, book_id INT UNIQUE NOT NULL,
    CONSTRAINT fk_wishlist_ref_book_id FOREIGN KEY (book_id) REFERENCES books(id),
    CONSTRAINT fk_wishlist_ref_user_id FOREIGN KEY (user_id) REFERENCES user_details(user_id),
    PRIMARY KEY (id)
);

CREATE TABLE cart
(
	id INT AUTO_INCREMENT NOT NULL,user_id INT NOT NULL, book_id INT NOT NULL, quantity INT NOT NULL DEFAULT 1,
    CONSTRAINT fk_cart_ref_book_id FOREIGN KEY (book_id) REFERENCES books(id),
    CONSTRAINT fk_cart_ref_login_id FOREIGN KEY (user_id) REFERENCES user_details(user_id),
	PRIMARY KEY (id)
);

CREATE TABLE orders
(
	id INT AUTO_INCREMENT NOT NULL, user_id INT NOT NULL, address TEXT NOT NULL, total_price DOUBLE NOT NULL, order_date DATETIME NOT NULL,
    order_confirm INT DEFAULT FALSE,
    CONSTRAINT fk_orders_ref_login_id FOREIGN KEY (user_id) REFERENCES user_details(user_id),
    PRIMARY KEY (id)
);

CREATE TABLE order_item
(
	id INT AUTO_INCREMENT NOT NULL, order_id INT NOT NULL, user_id INT NOT NULL, book_id INT NOT NULL,quantity INT NOT NULL,
    CONSTRAINT fk_order_ref_cart_bookid FOREIGN KEY (book_id) REFERENCES cart(book_id),
    CONSTRAINT fk_order_ref_login_id FOREIGN KEY (user_id) REFERENCES user_details(user_id),
    CONSTRAINT fk_order_ref_order_id FOREIGN KEY (order_id) REFERENCES orders(id),
	PRIMARY KEY (id)
);