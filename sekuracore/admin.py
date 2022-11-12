from django.contrib import admin

from . import models


class AgentInline(admin.TabularInline):
    model = models.Agent


class EmployeeInline(admin.TabularInline):
    model = models.Employee


class AccessInline(admin.TabularInline):
    model = models.Access


@admin.register(models.Agent)
class Agent(admin.ModelAdmin):
    readonly_fields = ["secret"]


@admin.register(models.Employee)
class Employee(admin.ModelAdmin):
    pass


@admin.register(models.Access)
class Access(admin.ModelAdmin):
    pass


#    inlines = [AgentInline, EmployeeInline]
