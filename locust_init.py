from CONFIG import inputs

from locust_task2 import Task2
from locust_task3 import Task3
from locust_task5 import Task5
from locust_task11 import Task11

from locust import HttpLocust, TaskSet, task

def login(l):
    l.client.post("/vektordata/authenticate/local", json=inputs['local'])
    l.client.get("/vektordata/authenticate/user")

class MainTask(TaskSet):
    tasks = {Task2 : 1, Task3 : 1, Task5 : 1, Task11 : 1}
    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    host = inputs["host_name"]
    task_set = MainTask
    min_wait = 5000
    max_wait = 9000
