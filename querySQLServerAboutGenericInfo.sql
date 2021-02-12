/* get names of all tables in BiDatamart */
USE BiDatamart
SELECT *
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE='BASE TABLE'

/* count all tables in BiDatamart */
USE BiDatamart
DECLARE @tableCount INT;
SELECT @tableCount = COUNT(*)
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
PRINT 'There are ' + CAST(@tableCount AS VARCHAR) + ' tables in the BiDatamart.'

/* find and print total number of views */
USE BiDatamart
DECLARE @viewCount INT;
SELECT @viewCount = COUNT(*)
FROM sys.all_views
PRINT 'There are ' + CAST(@viewCount AS VARCHAR) + ' views in the BiDatamart.'
