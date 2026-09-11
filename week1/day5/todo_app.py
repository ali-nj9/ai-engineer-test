print("==========To-Do_App_CLI===========")
from datetime import datetime
import json


class Task:
    def __init__(
        self,
        id,
        title,
        description="",
        priority="medium",
        completed=False,
        created_at=None,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed
        self.created_at = (
            created_at if created_at else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            priority=data.get("priority"),
            completed=data.get("completed", False),
            created_at=data.get("created_at"),
        )

    def __str__(self):
        if not self.completed:
            return f"[X] {self.title} (Priority: {self.priority}) - Created at: {self.created_at}"
        else:
            return f"[✓] {self.title} (Priority: {self.priority}) - Created at: {self.created_at}"


# t1 = Task(1, "bakeri of bred", "buy some bred", "high")
# print("namayesh matni: ")
# print(t1)

# d = t1.to_dict()
# print("\n khoroji to_dict: ")
# print(d)

# t2 = Task.from_dict(d)
# print("\n shaye sakhte shode ba from_dict: ")
# print(t2)
# print(f"aya titel yeky ast? {t1.title == t2.title}")


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_from_file()

    def add_task(self, title, description, priority):
        if self.tasks == []:
            new_id = 1
        else:
            new_id = max(task.id for task in self.tasks) + 1
        new_task = Task(new_id, title, description, priority)
        self.tasks.append(new_task)
        self.save_to_file()
        return new_task

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self.save_to_file()
                return "correct : task dar file zkhire shod"
        return " khata : task payda nashod"

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_to_file()
                return "task ba movafaghyat hazf shod"
        return "khata : task peyda nashod"

    def get_all(self):
        return self.tasks

    def get_by_status(self, completed):
        return [task for task in self.tasks if task.completed == completed]

    def save_to_file(self):
        tasks_data = [task.to_dict() for task in self.tasks]
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(tasks_data, file, ensure_ascii=False, indent=4)

    def load_from_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                task_data = json.load(file)
                self.tasks = [Task.from_dict(data) for data in task_data]
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            self.tasks = []


# manager = TaskManager()
# manager.add_task("buye bread", "of bakery", "high")
# manager.add_task("sport", "30 minutes", "medium")
# manager.complete_task(1)
# manager.delete_task(2)

# for t in manager.get_all():
#     print(t)

manager = TaskManager()

while True:
    print("========== To-Do App ==========")
    print("1. afzodan task jadid")
    print("2. namayesh hame task ha")
    print("3. task haye anjam shode")
    print("4. task haye anjam nashode")
    print("5. takmil task")
    print("6. hazf task")
    print("7. khoroj")
    choice = input("lotfan gozine ra entekhab konid (1-7): ")
    if choice == "1":
        title = input("title ra vared konid : ")
        description = input("description ra vared konid : ")
        priority = input("priority ra vared konid : ")
        if priority == "":
            priority = "medium"
        new_task = manager.add_task(title, description, priority)
        print(f"✅ task '{new_task.title}' ba ID {new_task.id} ezafe shod")
    elif choice == "2":
        tasks = manager.get_all()
        if not tasks:
            print("hich taski vojood nadarad.")
        else:
            for t in tasks:
                print(t)
    elif choice == "3":
        tasks = manager.get_by_status(True)
        if not tasks:
            print("hich taski vojood nadarad")
        else:
            for t in tasks:
                print(t)
    elif choice == "4":
        tasks = manager.get_by_status(False)
        if not tasks:
            print("hich taski vojood nadarad")
        else:
            for t in tasks:
                print(t)
    elif choice == "5":
        try:
            task_id = int(input("ID task ra vared konid: "))
            result = manager.complete_task(task_id)
            print(result)
        except ValueError:
            print("❌ lotfan faghat adad vared konid!")
    elif choice == "6":
        try:
            task_id = int(input("ID task ra vared konid: "))
            result = manager.delete_task(task_id)
            print(result)
        except ValueError:
            print("❌ lotfan faghat adad vared konid!")
    elif choice == "7":
        print("bye bye")
        break
    else:
        print("❌ gozine namotabar! lotfan 1-7 ra entekhab konid.")
