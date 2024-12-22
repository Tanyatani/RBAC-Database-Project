import sqlite3

# Initialize the SQLite database
def initialize_database():
    conn = sqlite3.connect('rbac_system.db')
    cursor = conn.cursor()

    # Create tables for users and roles
    cursor.execute('''CREATE TABLE IF NOT EXISTS roles (
                        id INTEGER PRIMARY KEY,
                        name TEXT UNIQUE)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        role_id INTEGER,
                        FOREIGN KEY(role_id) REFERENCES roles(id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS permissions (
                        id INTEGER PRIMARY KEY,
                        action TEXT UNIQUE)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS role_permissions (
                        role_id INTEGER,
                        permission_id INTEGER,
                        FOREIGN KEY(role_id) REFERENCES roles(id),
                        FOREIGN KEY(permission_id) REFERENCES permissions(id))''')

    conn.commit()
    conn.close()

# Add roles
def add_role(role_name):
    conn = sqlite3.connect('rbac_system.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO roles (name) VALUES (?)', (role_name,))
    conn.commit()
    conn.close()

# Add users
def add_user(username, role_name):
    conn = sqlite3.connect('rbac_system.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM roles WHERE name = ?', (role_name,))
    role_id = cursor.fetchone()
    if role_id:
        cursor.execute('INSERT OR IGNORE INTO users (username, role_id) VALUES (?, ?)', (username, role_id[0]))
    else:
        print("Role not found!")
    conn.commit()
    conn.close()

# Add permissions
def add_permission(permission):
    conn = sqlite3.connect('rbac_system.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO permissions (action) VALUES (?)', (permission,))
    conn.commit()
    conn.close()

# Assign permissions to roles
def assign_permission_to_role(role_name, permission):
    conn = sqlite3.connect('rbac_system.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM roles WHERE name = ?', (role_name,))
    role_id = cursor.fetchone()

    cursor.execute('SELECT id FROM permissions WHERE action = ?', (permission,))
    permission_id = cursor.fetchone()

    if role_id and permission_id:
        cursor.execute('INSERT OR IGNORE INTO role_permissions (role_id, permission_id) VALUES (?, ?)', (role_id[0], permission_id[0]))
    else:
        print("Role or permission not found!")
    conn.commit()
    conn.close()

# Check user permission
def check_permission(username, permission):
    conn = sqlite3.connect('rbac_system.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT permissions.action 
                      FROM users
                      JOIN roles ON users.role_id = roles.id
                      JOIN role_permissions ON roles.id = role_permissions.role_id
                      JOIN permissions ON role_permissions.permission_id = permissions.id
                      WHERE users.username = ? AND permissions.action = ?''', (username, permission))
    result = cursor.fetchone()

    conn.close()
    return bool(result)

# Main function for testing
if __name__ == "__main__":
    initialize_database()

    # Add roles
    add_role("admin")
    add_role("editor")
    add_role("viewer")

    # Add users
    add_user("alice", "admin")
    add_user("bob", "editor")
    add_user("charlie", "viewer")

    # Add permissions
    add_permission("create")
    add_permission("edit")
    add_permission("view")

    # Assign permissions to roles
    assign_permission_to_role("admin", "create")
    assign_permission_to_role("admin", "edit")
    assign_permission_to_role("admin", "view")
    assign_permission_to_role("editor", "edit")
    assign_permission_to_role("editor", "view")
    assign_permission_to_role("viewer", "view")

    # Test permission checking
    print("Alice can create:", check_permission("alice", "create"))  # True
    print("Bob can edit:", check_permission("bob", "edit"))  # True
    print("Charlie can create:", check_permission("charlie", "create"))  # False
