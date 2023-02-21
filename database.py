import psycopg2

class Postgres:
    def __init__(self, host, port, database, user, password):
        self.host=host
        self.port=port
        self.database=database
        self.user=user
        self.password=password
        self.conn = None

    def __open_connection(self):
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password,
        )

    def __close_connection(self):
        if self.conn:
            self.conn.close()
    
    def create_user(self, email: str, password: str):
        self.__open_connection()

        with self.conn.cursor() as cur:
            # Execute a command: this creates a new table
            cur.execute(f"INSERT INTO users(email, password) VALUES('{email}','{password}')")
            self.conn.commit()
            
        self.__close_connection()

  
