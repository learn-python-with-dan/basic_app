
__all__ = [
    'insert_user_stmt',
    'get_user_stmt',
    'update_user_stmt',
    'delete_user_stmt',
]


insert_user_stmt = """
    INSERT INTO users (id, name, created_at) VALUES (%(id)s, %(name)s, %(created_at)s)
    RETURNING id
"""

get_user_stmt = """
    SELECT * FROM users WHERE id = %(id)s
"""

update_user_stmt = """
    UPDATE users SET (name, last_updated_at) = (%(name)s, %(last_updated_at)s)
    WHERE id = %(id)s
    RETURNING id
"""

delete_user_stmt = """
    DELETE FROM users WHERE id = %(id)s
"""
