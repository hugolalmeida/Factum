# Factum

# Overview

Factum is a clean and focused to-do list application designed to turn intention into action. Rooted in the Latin word "Factum" — meaning "a thing done" — this project helps users stay grounded in their tasks and focused on what truly matters.

[Software Demo Video](https://youtu.be/7P2XoZsKlrI)

# Cloud Database

Cloud Fistore: The Cloud Firestore is a flexible and scalable database for mobile, web, and server-side development with Firebase and Google Cloud. As the Firebase Real time Database, it keeps your data in sync across client applications using real-time listeners. It also offers offline support for mobile and web devices, so you can build responsive applications that work regardless of network latency or internet connectivity.Cloud Firestore also offers full integration with other Firebase and Google Cloud, including Cloud Functions.

## Database Structure

lists (coleção)
│
├── listId_abc123 (documento)
│ ├── title: "Daily Tasks"
│ ├── created_at: timestamp
│ └── tasks (subcoleção)
│ ├── taskId_1 (documento)
│ │ ├── title: "Walk the dog"
│ │ ├── done: False
│ │ └── created_at: timestamp
│ └── taskId_2 (...)

# Development Environment

- Python - Main Programming Language
- Cloud FireStore - NonSQL Database
- Customtkinter - Interface Library
- firebase_admin - FireBase Library

# Useful Websites

- [FireStore Document](https://firebase.google.com/docs/firestore/query-data/get-data?hl=pt-br)
- [Python Documentation](https://docs.python.org/3/tutorial/errors.html)
- [Jamesg Blog](https://jamesg.blog/2024/08/19/nosql-database-python)

# Future Work

- Item 1: Add Mark, Delete and Edit Tasks Functions to the Menu User Input
- Item 2: Add a loop to give freedom to the user do what they want
- Item 3: Add handle error
- Item 4: Add an Interface using customtkinter library
