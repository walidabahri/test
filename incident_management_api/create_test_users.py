from django.contrib.auth.models import User, Group

# Create Manager group
manager_group, created = Group.objects.get_or_create(name='Manager')
print(f'Manager group created: {created}')

# Create admin user (manager)
admin_username = 'admin'
admin_user = User.objects.filter(username=admin_username).first()
if not admin_user:
    admin_user = User.objects.create_superuser(
        username=admin_username, 
        email='admin@example.com',
        password='adminpassword'
    )
    print(f'Created admin user: {admin_username}')
else:
    print(f'Admin user already exists: {admin_username}')

# Add admin to Manager group
admin_user.groups.add(manager_group)
print(f'Admin user is now in Manager group: {admin_user.groups.filter(name="Manager").exists()}')

# Create worker user
worker_username = 'worker'
worker_user = User.objects.filter(username=worker_username).first()
if not worker_user:
    worker_user = User.objects.create_user(
        username=worker_username,
        email='worker@example.com',
        password='workerpassword'
    )
    print(f'Created worker user: {worker_username}')
else:
    print(f'Worker user already exists: {worker_username}')

print(f'Worker user is in Manager group: {worker_user.groups.filter(name="Manager").exists()} (should be False)')
