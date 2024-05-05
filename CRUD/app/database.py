import psycopg2
from psycopg2.extras import RealDictCursor


try:
    conn = psycopg2.connect(
        host = 'localhost', 
        database = 'crud', 
        user = 'postgres', 
        password = 'don\'tdothis', 
        cursor_factory = RealDictCursor
        )
    print('Established Database Connection.')
except Exception as e:
    print(f'Error while establishing connection:-\n{e}')