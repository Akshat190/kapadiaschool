#!/usr/bin/env python
"""
Simple script to test PostgreSQL connection
"""
import psycopg2
import sys

def test_connection():
    print("Testing PostgreSQL connection...")
    
    try:
        # Connection parameters
        conn_params = {
        'dbname': 'kapadia_school_eq0q',
        'user': 'kapadia_school_eq0q_user',
        'password': 'IfB7rPNBSh7314VKpkojIATHjvkEEyuT',
        'host': 'dpg-d1l58qfdiees73f7ocu0-a.oregon-postgres.render.com',
        'port': '5432',
        'sslmode': 'require'
        }
        
        # Connect to the database
        conn = psycopg2.connect(**conn_params)
        
        # Create a cursor
        cur = conn.cursor()
        
        # Execute a simple query
        cur.execute('SELECT version();')
        
        # Fetch the result
        version = cur.fetchone()
        
        # Close cursor and connection
        cur.close()
        conn.close()
        
        print("Connection successful!")
        print(f"PostgreSQL version: {version[0]}")
        return True
        
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1) 