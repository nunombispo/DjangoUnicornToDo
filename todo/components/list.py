from django_unicorn.components import UnicornView
from todo.models import Task


class ListView(UnicornView):
    tasks = []
    task_title = ""
    task_description = ""
    task_id = None

    def mount(self):
        self.tasks = Task.objects.all()

    def add(self):
        if self.is_valid():
            Task.objects.create(title=self.task_title, description=self.task_description)
            self.task_title = ""
            self.task_description = ""
            self.tasks = Task.objects.all()

    def delete(self, task_id):
        Task.objects.get(id=task_id).delete()
        self.tasks = Task.objects.all()

    def edit(self, task_id):
        task = Task.objects.get(id=task_id)
        self.task_title = task.title
        self.task_description = task.description
        self.task_id = task.id

    def update(self, task_id):
        if self.is_valid():
            task = Task.objects.get(id=task_id)
            task.title = self.task_title
            task.description = self.task_description
            task.save()
            self.task_title = ""
            self.task_description = ""
            self.task_id = None
            self.tasks = Task.objects.all()
