-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
--
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
DECLARE average_user FLOAT;

SELECT AVG(score) INTO average_user
FROM corrections
WHERE user_id = user_id;

UPDATE users
SET average_score = average_user
WHERE id = user_id;

END;
//
DELIMITER ;
