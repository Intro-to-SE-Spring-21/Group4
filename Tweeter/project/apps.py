from django.apps import AppConfig


class ProjectConfig(AppConfig):
    name = 'project'

    # how signals are used in the project
    def ready(self):
        import project.signals