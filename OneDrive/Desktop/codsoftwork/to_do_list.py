

import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.window = tk.Tk()
        self.window.title("To-Do List")

        self.task_name_label = tk.Label(self.window, text="Task Name:")
        self.task_name_label.pack()

        self.task_name_entry = tk.Entry(self.window)
        self.task_name_entry.pack()

        self.due_date_label = tk.Label(self.window, text="Due Date:")
        self.due_date_label.pack()

        self.due_date_entry = tk.Entry(self.window)
        self.due_date_entry.pack()

        self.create_task_button = tk.Button(self.window, text="Create Task", command=self.create_task)
        self.create_task_button.pack()

        self.update_task_button = tk.Button(self.window, text="Update Task", command=self.update_task)
        self.update_task_button.pack()

        self.delete_task_button = tk.Button(self.window, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.view_tasks_button = tk.Button(self.window, text="View Tasks", command=self.view_tasks)
        self.view_tasks_button.pack()

        self.tasks_text = tk.Text(self.window)
        self.tasks_text.pack()

    def create_task(self):
        task_name = self.task_name_entry.get()
        due_date = self.due_date_entry.get()
        self.tasks[task_name] = due_date
        messagebox.showinfo("Task Created", f"Task '{task_name}' created successfully.")

    def update_task(self):
        task_name = self.task_name_entry.get()
        new_due_date = self.due_date_entry.get()
        if task_name in self.tasks:
            self.tasks[task_name] = new_due_date
            messagebox.showinfo("Task Updated", f"Task '{task_name}' updated successfully.")
        else:
            messagebox.showerror("Task Not Found", f"Task '{task_name}' not found.")

    def delete_task(self):
        task_name = self.task_name_entry.get()
        if task_name in self.tasks:
            del self.tasks[task_name]
            messagebox.showinfo("Task Deleted", f"Task '{task_name}' deleted successfully.")
        else:
            messagebox.showerror("Task Not Found", f"Task '{task_name}' not found.")

    def view_tasks(self):
        self.tasks_text.delete(1.0, tk.END)
        if self.tasks:
            self.tasks_text.insert(tk.END, "Your To-Do List:\n")
            for task, due_date in self.tasks.items():
                self.tasks_text.insert(tk.END, f"Task: {task}, Due Date: {due_date}\n")
        else:
            self.tasks_text.insert(tk.END, "Your To-Do List is empty.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()


