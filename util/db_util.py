import pyodbc

class DBConnection:
    def __init__(self):
        self.connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost,1433;"
            "DATABASE=appdb;"
            "UID=sa;"
            "PWD=examlyMssql@123"
        )
        self.cursor = self.connection.cursor()
        self._initialize_schema()

    def _initialize_schema(self):
        self.cursor.execute("""
            IF NOT EXISTS (
                SELECT * FROM sysobjects WHERE name='SupportTickets' AND xtype='U'
            )
            CREATE TABLE SupportTickets (
                ticket_id     INT IDENTITY(1,1) PRIMARY KEY,
                employee_name VARCHAR(50),
                issue_type    VARCHAR(50),
                priority      INT,
                raised_date   VARCHAR(20),
                status        VARCHAR(20)
            )
        """)
        self.connection.commit()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
