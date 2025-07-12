import os
import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, firestore

load_dotenv()
key_path = os.getenv("FIREBASE_KEY_PATH")

cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred)

db = firestore.client()


# Create a new list
def create_list(title):
    #1. Create a new document in the "lists" collection
    doc_ref = db.collection("lists").document()
    #2. Set the title and created_at timestamp
    doc_ref.set({
        "title": title,
        "created_at": firestore.SERVER_TIMESTAMP
    })
    #3. Return the document ID
    print(f"List '{title}' created with ID:", doc_ref.id)
    return doc_ref.id

# Get all lists
def get_all_lists(db):
    #1. Get all documents in the "lists" collection
    lists = db.collection("lists").order_by("created_at").stream()
    #2. Return a list of tuples (list_id, list_data)
    return [(doc.id, doc.to_dict()) for doc in lists]

# Update list title
def update_list_title(db, list_id, new_title):
    #1. Get the reference to the list document
    list_ref = db.collection("lists").document(list_id)
    #2. Update the title field
    list_ref.update({
        "title": new_title
    })

# Delete a list and its tasks
def delete_list(db, list_id):
    #1. Get the reference to the list document
    list_ref = db.collection("lists").document(list_id)

    #2. Delete all tasks in the list
    #   We first get all tasks in the list and delete them one by one
    tasks = list_ref.collection("tasks").stream()
    for task in tasks:
        task.reference.delete()

    #3. Delete the list document itself
    list_ref.delete()

# Add task to a list
def add_task(list_id, task_title):
    #1. get the task reference
    task_ref = db.collection("lists").document(list_id).collection("tasks").document()
    #2. set the task data
    task_ref.set({
        "title": task_title,
        "done": False,
        "created_at": firestore.SERVER_TIMESTAMP
    })
    print(f"Task '{task_title}' added to list {list_id}")
# Get tasks from a list
def get_tasks(db, list_id):
    #1. get the tasks from the list
    tasks = db.collection("lists").document(list_id).collection("tasks").order_by("created_at").stream()
    #2. return the tasks as a list of tuples (task_id, task_data)
    #   where task_data is a dictionary with the task information
    return [(t.id, t.to_dict()) for t in tasks]

# Mark task as done
def mark_task_done(db, list_id, task_id):
    #1. get the task reference
    task_ref = db.collection("lists").document(list_id).collection("tasks").document(task_id)
    #2. update the task status to done
    task_ref.update({"done": True})

# Update task title
def update_task_title(db, list_id, task_id, new_title):
    #1. get the task reference
    task_ref = db.collection("lists").document(list_id).collection("tasks").document(task_id)
    #2. update the task title
    task_ref.update({
        "title": new_title
    })

# delete task funcion
def delete_task(db, list_id, task_id):
    #1. get the task reference
    task_ref = db.collection("lists").document(list_id).collection("tasks").document(task_id)
    #2. delete the task
    task_ref.delete()

# Executando teste
if __name__ == "__main__":
    # Ensure the environment variable is set
    if not key_path:
        raise ValueError("FIREBASE_KEY_PATH environment variable is not set.")
    # Main menu for the To-Do List application
    print("\n=== Factum To-Do List ===")
    print("1. View all lists")
    print("2. Create new list")
    print("3. Update a list title")
    print("4. Delete a list")
    print("5. Add task to a list")

    choice = input("Choose an option: ")
    # Handle user choice
    if choice == "1":
        all_lists = get_all_lists(db)
        for lid, info in all_lists:
            print(f"\n{info['title']} (ID: {lid})")
            tasks = get_tasks(db, lid)
            for tid, task in tasks:
                status = "✔" if task["done"] else "✘"
                print(f"  [{status}] {task['title']}")
        
    elif choice == "2":
        title = input("Enter list title: ")
        list_id = create_list(title)
        print("List created with ID:", list_id)

    elif choice == "3": 
        list_id = input("Enter list ID to update: ")
        new_title = input("Enter new title: ")
        update_list_title(db, list_id, new_title)
        print("List title updated.")
    
    elif choice == "4":
        list_id = input("Enter list ID to delete: ")
        delete_list(db, list_id)
        print("List deleted.")

    elif choice == "5":
        list_id = input("Enter list ID to add task: ")
        task_title = input("Enter task title: ")
        add_task(list_id, task_title)
        print("Task added to list.")