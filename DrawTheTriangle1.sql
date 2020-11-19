/* - P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5): */
/*
* * * * * 
* * * * 
* * * 
* * 
*
*/

/* - Write a query to print the pattern P(20). */

DECLARE @iteration INT = 20
WHILE(@iteration>=1)
BEGIN
    PRINT REPLICATE(' * ',@iteration) 
    SET @iteration = @iteration - 1
END
