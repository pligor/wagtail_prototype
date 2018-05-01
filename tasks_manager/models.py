from django.db import models

from django.contrib.auth.models import User  # for user authentication


# Create your models here.
class UserProfile(models.Model):
    # Django automatically saves an id field in auto increment. Therefore,
    # we do not need to define a primary key.

    # for user authentication, linking this model with the user model
    user_auth = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    # login = models.CharField(max_length=25, verbose_name="Login")
    # password = models.CharField(max_length=100, verbose_name="Password")
    # name = models.CharField(max_length=50, verbose_name="Name")
    # WE ARE commenting OUT the parts that are already provided by builtin User class

    phone = models.CharField(max_length=20, verbose_name="Phone number", null=True,
                             default=None, blank=True)
    born_date = models.DateField(verbose_name='Born date', null=True, default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name='Date of last connection', null=True,
                                           default=None, blank=True)

    email = models.EmailField(verbose_name="Email")

    years_seniority = models.IntegerField(verbose_name="Seniority", default=0)

    date_created = models.DateField(verbose_name="Date of Birthday", auto_now_add=True)

    def name(self):
        return self.user_auth.username

    def __str__(self):
        #return super().__str__()
        return self.user_auth.username
        # return ' '.join([self.user_auth.first_name, self.user_auth.last_name])


class Supervisor(UserProfile):
    specialization = models.CharField(max_length=50, verbose_name='Specialization')


class Developer(UserProfile):
    its_supervisor = models.ForeignKey(Supervisor, verbose_name="Supervisor", on_delete=models.CASCADE)


class Project(models.Model):
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    client_name = models.CharField(max_length=1000, verbose_name="Client Name")

    def __str__(self):
        return self.title


# Project - Task: One to Many relationship.
# One project could have many tasks but each task belongs to a single project (or nowhere)

class Task(models.Model):
    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"

    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    time_elapsed = models.IntegerField(verbose_name="Elapsed time", null=True,
                                       default=None, blank=True)
    importance = models.IntegerField(verbose_name="Importance")

    project = models.ForeignKey(Project, verbose_name="Project", null=True, default=None,
                                blank=True, on_delete=models.CASCADE)
    # https://docs.djangoproject.com/en/2.0/ref/models/fields/

    app_user = models.ForeignKey(Developer, verbose_name="User-Developer",
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.title

        # in case we wanted to define a second developer and NOT have a many-to-many relationship
        # dev2 = models.ForeignKey(Developer, verbose_name="Paired_developer", related_name='dev2',
        #                          on_delete=models.CASCADE)

        # developers = models.ManyToManyField(Developer, through=DeveloperTaskRelationship)

# imaginary Many to many relationship among developers and tasks
# class DeveloperTaskRelationship(models.Model):
#     dev = models.ForeignKey(Developer, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     time_elapsed_per_dev = models.IntegerField(verbose_name="Time elapsed", null=True,
#                                                default=None, blank=True)
