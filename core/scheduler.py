class Scheduler:
    def __init__(self):
        self.tasks = []
        print("RRAC-OS Scheduler Initialized.")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def run(self):
        print("Scheduler is running...")
        for task in self.tasks:
            print(f"Executing: {task}")

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.add_task("Core initialization")
    scheduler.run()
