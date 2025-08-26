# advanced_features_and_security/admin.py

from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.apps import apps

def setup_groups():
    Article = apps.get_model('advanced_features_and_security', 'Article')
    permissions = Permission.objects.filter(content_type__app_label='advanced_features_and_security', content_type__model='article')

    group_permissions = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perm_codes in group_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for code in perm_codes:
            perm = permissions.get(codename=code)
            group.permissions.add(perm)

setup_groups()