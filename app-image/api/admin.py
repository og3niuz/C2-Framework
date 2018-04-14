# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import api.modules
from django.contrib import admin
from api.models import Command, Group, Agent, Agent_Group, Module, Agent_Module
from api.modules.nmap import NmapResult
from api.modules.hello_world import HelloWorldResult
# Register your models here.
admin.site.register(Command)
admin.site.register(Group)
admin.site.register(Agent)
admin.site.register(Agent_Group)
admin.site.register(Module)
admin.site.register(Agent_Module)
admin.site.register(NmapResult)
admin.site.register(HelloWorldResult)