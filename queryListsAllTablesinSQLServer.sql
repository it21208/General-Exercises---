select schema_name(t.schema_id) as schema_name,
       t.name as table_name,
       t.create_date,
       t.modify_date
from sys.tables t
order by schema_name,
         table_name;
         
-- table_name - table name
-- create_date - date the table was created
-- modify_date - date the table was last modified by using an ALTER statement

-- RESULTS
-- One row represents one table in the database
-- Scope of rows: all tables in the database
-- Ordered by schema and name 
