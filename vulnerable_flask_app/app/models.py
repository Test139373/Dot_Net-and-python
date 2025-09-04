from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# VULNERABLE: SQL injection through text() without parameter binding
# Can only be fixed by using parameterized queries or ORM
def get_user_unsafe(username):
    engine = create_engine(config.DATABASE_URI)
    # VULNERABLE: Must use parameter binding: text("SELECT * FROM users WHERE username = :username")
    query = text(f"SELECT * FROM users WHERE username = '{username}'")
    result = engine.execute(query)
    return result.fetchall()

# VULNERABLE: SQL injection with direct string formatting
# Can only be fixed by using sqlalchemy.sql.expression or ORM
def search_users_unsafe(search_term):
    engine = create_engine(config.DATABASE_URI)
    # VULNERABLE: Must use proper SQLAlchemy query construction
    query = text("SELECT * FROM users WHERE bio LIKE '%" + search_term + "%'")
    result = engine.execute(query)
    return result.fetchall()