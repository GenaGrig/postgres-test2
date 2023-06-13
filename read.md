To get this working you need to

1. alias set_pg to get psql working
2. CREATE DATABASE chinook;
3. \c chinook to enter db
4. \i Chinook_PostgreSql.sql to install db
5. pip3 install psycopg2
6. pip3 install sqlalchemy==1.4.46

Test it. It should work now.