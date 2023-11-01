import tkinter as tk
from tkinter import simpledialog, messagebox

# Create a main window
root = tk.Tk()
root.title("To-Do List App - Sushant Khedkar")

# Set the background color
root.configure(bg="black")  # Change "light blue" to the color you prefer

# Create a list to store tasks and completed tasks
tasks = []
completed_tasks = []

# Function to add tasks
def add_task():
    description = entry_description.get()
    due_date = entry_due_date.get()
    priority = entry_priority.get()
    if description:
        task = {"description": description, "due_date": due_date, "priority": priority, "completed": False}
        tasks.append(task)
        listbox.insert(tk.END, description)
        entry_description.delete(0, tk.END)
        entry_due_date.delete(0, tk.END)
        entry_priority.delete(0, tk.END)

# Function to remove selected task
def remove_task():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        listbox.delete(index)
        tasks.pop(index)

# Function to display the list of tasks with due date and priority
def display_task_list():
    task_list = "\n".join([f"{task['description']} (Due Date: {task['due_date']}, Priority: {task['priority']})" for task in tasks])
    messagebox.showinfo("Task List", "Tasks:\n" + task_list)

# Function to mark a task as completed and move it to the completed task list
def complete_task():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        task = tasks[index]
        task["completed"] = True
        completed_tasks.append(task)
        tasks.pop(index)
        listbox.delete(index)

# Function to update a task's description, due date, and priority
def update_task():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        task = tasks[index]
        new_description = simpledialog.askstring("Update Task", "New Description:", initialvalue=task["description"])
        new_due_date = simpledialog.askstring("Update Task", "New Due Date:", initialvalue=task["due_date"])
        new_priority = simpledialog.askstring("Update Task", "New Priority:", initialvalue=task["priority"])
        if new_description:
            task["description"] = new_description
        if new_due_date:
            task["due_date"] = new_due_date
        if new_priority:
            task["priority"] = new_priority
        listbox.delete(index)
        listbox.insert(index, f"{task['description']} (Due Date: {task['due_date']}, Priority: {task['priority']})")

# Create GUI elements
label_description = tk.Label(root, text="Description:")
label_due_date = tk.Label(root, text="Due Date:")
label_priority = tk.Label(root, text="Priority:")

entry_description = tk.Entry(root)
entry_due_date = tk.Entry(root)
entry_priority = tk.Entry(root)

add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
display_button = tk.Button(root, text="Display Tasks", command=display_task_list)
complete_button = tk.Button(root, text="Mark as Completed", command=complete_task)
update_button = tk.Button(root, text="Update Task", command=update_task)

listbox = tk.Listbox(root, selectmode=tk.SINGLE)

# Place GUI elements on the window
label_description.pack()
entry_description.pack()
label_due_date.pack()
entry_due_date.pack()
label_priority.pack()
entry_priority.pack()
add_button.pack()
remove_button.pack()
display_button.pack()
complete_button.pack()
update_button.pack()
listbox.pack()

# Start the main event loop
root.mainloop()
