import json
import datetime

class Framework:
    flag = 0
    def load_tasks(self):
        try:
            with open("tasks.json","r") as tasks_file:
                return json.load(tasks_file)
                # json.load() function in Python is used to read a JSON file and convert it into a corresponding Python object, such as a dictionary or a list.
        except (FileNotFoundError,json.JSONDecodeError):
            return []
            


    def save_tasks(self,tasks):
        with open("tasks.json","w") as tasks_file:
            json.dump(tasks, tasks_file)
            # json.dump(object, file) is used to save objects to a file 



    def add_task(self):
            tasks = self.load_tasks()
            print(tasks)
            description = input("enter your task: \n")
            new_id = len(tasks) + 1
            new_task = {"id":new_id,"description":description, "status":"todo", "createdAt":str(datetime.datetime.now()), "updatedAt":str(datetime.datetime.now())}
            tasks.append(new_task)
            self.save_tasks(tasks)



    def list_tasks(self):
        tasks = self.load_tasks()
        if (len(tasks) == 0):
            print("Task-list is empty\n")
        else:
            for item in tasks:
                print(f"[{item['id']}]: {item['description']}, {item['status']}\n Created on:{item['createdAt']}\n, Updated on: {item['updatedAt']}\n")



    def list_incomplete(self):
        tasks = self.load_tasks()
        for item in tasks:
            if (item['status'] == "todo"):
                print(f"[{item['id']}]: {item['description']}, {item['status']}\n Created on:{item['createdAt']}, Updated on: {item['updatedAt']}\n")



    def list_complete(self):
        tasks = self.load_tasks()
        for item in tasks:
            if (item['status'] == "done"):
                print(f"[{item['id']}]: {item['description']}, {item['status']}\n Created on:{item['createdAt']}, Updated on: {item['updatedAt']}\n]")



    def list_progress(self):
        tasks = self.load_tasks()
        for item in tasks:
            if (item['status'] == "in progress"):
                print(f"[{item['id']}]: {item['description']}, {item['status']}\n Created on:{item['createdAt']}, Updated on: {item['updatedAt']}\n]")



    def update_status(self):
        self.list_tasks()
        tasks = self.load_tasks()
        choice = int(input("Please enter the id of which tasks status you would like to change: \n"))
        for item in tasks:
            if (choice == item['id']):
                status_change = int(input("Please make a choice: \n 1: mark as todo\n 2: mark as in progress\n 3: mark as done\n"))
                if (status_change == 1):
                    item['status'] = "todo"
                    item['updatedAt'] = datetime.datetime.now()
                    self.flag = 1
                elif (status_change == 2):
                    item['status'] = "in progress"
                    item['updatedAt'] = datetime.datetime.now()
                    self.flag = 1
                elif (status_change == 3):
                    item['status'] = "done"
                    item['updatedAt'] = datetime.datetime.now()
                    self.flag = 1
                else:
                    print("that is not a valid choice.")
            
            self.save_tasks(tasks)
        if (self.flag == 0):
            print("Task does not exist")



    def delete(self):   
        tasks = self.load_tasks()
        self.list_tasks()
        choice = int(input("Please enter the id of the task you would like to delete"))
        new_tasks = []

        for item in tasks:
            if (choice != item['id']):
                new_tasks.append(item)
        self.save_tasks(new_tasks)

    def update(self):
        tasks = self.load_tasks()
        self.list_tasks()
        choice = int(input("Please enter the id of the task you would like to update"))
        updated_task = input("Please enter the updated task")
        for item in tasks:
            if (choice == item['id']):
                item['description'] = updated_task
        self.save_tasks(tasks)

    def end_program(self):
        quit()
        
        

    def home(self):
        print("~~~~~~Welcome to Task Tracker CLI!~~~~~~")
        print("~~~~~~What option would you like to do?~")
        print("1: List all tasks\n2: List incomplete tasks\n3: List complete tasks\n4: List in progress tasks\n5: Update task status\n6: Delete task\n7: Update task\n8: Add task\n9: End program")

        chosen_task = int(input(("Type the number of the option you want to complete: \n")))

        if (chosen_task == 1):
            self.list_tasks()
        elif (chosen_task == 2):
            self.list_incomplete()
        elif (chosen_task == 3):
            self.list_complete()
        elif (chosen_task == 4):
            self.list_progress()
        elif (chosen_task == 5):
            self.update_status()
        elif (chosen_task == 6):
            self.delete()
        elif (chosen_task == 7):
            self.update()
        elif (chosen_task == 8):
            self.add_task()
        elif (chosen_task == 9):
            self.end_program()

def main():
    main_function = (Framework())
    main_function.home()
    while True:
        main_function.home()


if __name__ == "__main__":
    main()
