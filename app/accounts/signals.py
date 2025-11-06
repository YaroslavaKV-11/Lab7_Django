from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    author, _ = Group.objects.get_or_create(name='author')
    moderator, _ = Group.objects.get_or_create(name='moderator')
    try:
        from blog.models import Comment
        ct = ContentType.objects.get_for_model(Comment)
        add_c = Permission.objects.get(codename='add_comment', content_type=ct)
        del_c = Permission.objects.get(codename='delete_comment', content_type=ct)
        author.permissions.add(add_c)
        moderator.permissions.add(add_c, del_c)
    except Exception:
        pass
