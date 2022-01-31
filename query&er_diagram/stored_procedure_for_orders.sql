DELIMITER $$
CREATE PROCEDURE sp_delete_quan_frm_books(order_quantity INT,fetch_book_id INT, sp_user_id INT)
BEGIN
	UPDATE books INNER JOIN order_item ON books.id = order_item.book_id SET books.quantity = (books.quantity - order_quantity)
    WHERE books.id = fetch_book_id;
END$$
DELIMITER ;

**************************************************************************************************************************************
DELIMITER $$
CREATE PROCEDURE sp_delete_row_frm_cart(sp_user_id INT)
BEGIN
	DELETE FROM cart WHERE user_id = sp_user_id;
END$$
DELIMITER ;

**************************************************************************************************************************************
DELIMITER $$
CREATE PROCEDURE sp_get_cart_to_order(IN sp_user_id INT, IN user_address VARCHAR(600))
BEGIN
	DECLARE total INTEGER default 0;
	DECLARE sp_order_id INTEGER default 0;
	DECLARE fetch_book_id INTEGER default 0;
    DECLARE fetch_quantity INTEGER default 0;
    DECLARE available_quan INTEGER default 0;
    DECLARE finish INTEGER DEFAULT 0;
    DECLARE cart_cur CURSOR FOR select book_id, quantity from cart where user_id = sp_user_id;
	DECLARE CONTINUE HANDLER for NOT FOUND set finish = 1;

    select sum(price*cart.quantity) into total from cart inner join books on books.id = cart.book_id where user_id = sp_user_id;
    insert into orders(user_id, total_price, address, order_date) values(sp_user_id, total, user_address, current_timestamp());

	select id into sp_order_id from orders where user_id = sp_user_id AND order_confirm = FALSE;
    OPEN cart_cur;
		retrieve_list : LOOP
			FETCH cart_cur INTO fetch_book_id, fetch_quantity;
			IF finish =1
				THEN LEAVE retrieve_list;
			END IF;
				SELECT quantity into available_quan from books where id = fetch_book_id;
                IF fetch_quantity <= available_quan then
					insert into order_item(user_id, book_id, order_id,quantity) values(sp_user_id, fetch_book_id, sp_order_id,fetch_quantity);
					CALL sp_delete_quan_frm_books(fetch_quantity,fetch_book_id,sp_user_id);
					CALL sp_delete_row_frm_cart(sp_user_id);
					UPDATE orders SET order_confirm = TRUE WHERE user_id = sp_user_id;
                ELSE 
					SIGNAL SQLSTATE '45000' SET message_text='selected quantity not available at stock';
                END IF;
		END LOOP retrieve_list;
	CLOSE cart_cur;
END$$
DELIMITER ;

**************************************************************************************************************************************************
DELIMITER $$
CREATE PROCEDURE sp_order (IN sp_user_id INT, IN user_address VARCHAR(600))
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
	BEGIN
		ROLLBACK;
		SELECT 'TRANSACTION FAILED: ROLLBACK';
	END;
    START TRANSACTION;
	CALL sp_get_cart_to_order(sp_user_id, user_address);
    COMMIT;
    select * from orders where user_id=sp_user_id;
END$$
DELIMITER ;

**************************************************************************************************************************************************


