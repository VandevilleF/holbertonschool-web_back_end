-- script that creates a trigger that resets the attribute valid_email only when the email has been changed.
--
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
SET NEW.valid_email = IF(NEW.email <> OLD.email, 0, NEW.valid_email);
