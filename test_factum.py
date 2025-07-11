import os
import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, firestore

load_dotenv()
key_path = os.getenv("FIREBASE_KEY_PATH")

cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred)

db = firestore.client()


# create a new list
def create_list(title):
    #1. get the document reference for the new list
    doc_ref = db.collection("lists").document()
    doc_ref.set({
        "title": title,
        "created_at": firestore.SERVER_TIMESTAMP
    })
    print(f"List '{title}' created with ID:", doc_ref.id)
    return doc_ref.id

# Adiciona tarefa a uma lista.
def add_task(list_id, task_title):
    task_ref = db.collection("lists").document(list_id).collection("tasks").document()
    task_ref.set({
        "title": task_title,
        "done": False,
        "created_at": firestore.SERVER_TIMESTAMP
    })
    print(f"Task '{task_title}' added to list {list_id}")

# Executando teste
if __name__ == "__main__":
    list_id = create_list("My First List")
    add_task(list_id, "Learn Firestore with Python")
    add_task(list_id, "Build Factum App")