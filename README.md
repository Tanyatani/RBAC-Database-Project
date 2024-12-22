# **RBAC-Database-Project**

### **Role-Based Access Control (RBAC) System using Python and SQLite**

---

## 🚀 **Overview**

This project demonstrates a **Role-Based Access Control (RBAC)** system to manage users, roles, and permissions using **Python** and **SQLite**. It showcases how to enforce security policies by controlling access to specific actions or data based on assigned roles.

---

## 🛠 **Features**

- **Role Management**:
  - Define and manage roles (e.g., Admin, Editor, Viewer).
- **User Management**:
  - Add users and assign them specific roles.
- **Permission Management**:
  - Define permissions (e.g., Create, Edit, View) and assign them to roles.
- **Access Control**:
  - Check if users have the required permissions to perform specific actions.

---

## 🎯 **Use Cases**

- Implementing access control in IT systems or databases.
- Learning database management and security concepts.
- Applying RBAC principles in small to medium-sized projects.

---

## 📋 **Prerequisites**

- **Python 3.x**
- **SQLite** (comes with Python’s `sqlite3` module)

---

## ⚙️ **How to Run**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Tanyatani/RBAC-Database-Project.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd RBAC-Database-Project
   ```

3. **Run the Script**:
   ```bash
   python rbac_system.py
   ```

4. **Follow the Example Code in the Script**:
   - Add roles, users, and permissions.
   - Assign permissions to roles.
   - Test user permissions.

---

## 💡 **Workflow**

1. **Initialize Database**:
   - Creates tables for roles, users, permissions, and their associations.
2. **Add Roles and Users**:
   - Assign roles to users to manage access control.
3. **Assign Permissions**:
   - Link specific actions (permissions) to roles.
4. **Check Permissions**:
   - Verify if a user has the necessary permission to perform an action.

---

## 🔍 **Example Code**

```python
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

# Check permissions
print("Alice can create:", check_permission("alice", "create"))  # True
print("Bob can edit:", check_permission("bob", "edit"))  # True
print("Charlie can create:", check_permission("charlie", "create"))  # False
```

---

## 📦 **Technologies Used**

- **Python**: For scripting and logic.
- **SQLite**: Lightweight database for role and permission management.


---

## 👩‍💻 **Author**

Developed by **Tanja Hosseinzadeh**  
**Computer and Systems Sciences Student**  
Focused on IT Systems and Cybersecurity.

---

## 🌟 **Project Purpose**

This project was created as part of a learning journey in IT systems, database management, and security concepts. It demonstrates practical knowledge of applying RBAC principles in software development.

