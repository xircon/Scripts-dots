from sqlalchemy.engine import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
connection = engine.connect()
connection.execute(
    """
    CREATE TABLE users (
        username VARCHAR PRIMARY KEY,
        password VARCHAR NOT NULL
    );
    """
)
connection.execute(
    """
    INSERT INTO users (username, password) VALUES (?, ?);
    """,
    "foo", "bar"
)
result = connection.execute("SELECT * FROM users")
for row in result:
    print "username:", row['username'], row['password']
connection.close()