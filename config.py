#TASK 1
import os

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', '127.0.0.1')
    MYDQL_DATABASE = os.getenv('MYSQL_DATABASE', 'fitness_center')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '1Y6%11]5?16f')