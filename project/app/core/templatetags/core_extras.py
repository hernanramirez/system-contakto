from django import template

register = template.Library()


@register.filter(name="has_group")
def has_group(user, group_name):
    if user:
        return user.groups.filter(name=group_name).exists()
    else:
        return False
