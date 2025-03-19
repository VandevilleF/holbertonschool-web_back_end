-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
--
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
DECLARE total_score FLOAT;
DECLARE total_corrections INT;

SELECT SUM(score), COUNT(*) INTO total_score, total_corrections
FROM corrections
WHERE user_id = user_id;

UPDATE users
SET average_score = (total_score / total_corrections)
WHERE id = user_id;

END;
//
DELIMITER ;
