from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from apps.incidents.models import Incident, Comment
from django.db import transaction
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populates the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.filter(is_superuser=False).delete()
        Incident.objects.all().delete()
        Comment.objects.all().delete()

        # Create user groups if they don't exist
        worker_group, _ = Group.objects.get_or_create(name='worker')
        manager_group, _ = Group.objects.get_or_create(name='manager')

        # Create users
        self.stdout.write('Creating test users...')
        
        # Create manager users
        manager1 = User.objects.create_user(
            username='manager1',
            email='manager1@example.com',
            password='password123',
            first_name='Manager',
            last_name='One'
        )
        manager1.groups.add(manager_group)
        
        manager2 = User.objects.create_user(
            username='manager2',
            email='manager2@example.com',
            password='password123',
            first_name='Manager',
            last_name='Two'
        )
        manager2.groups.add(manager_group)
        
        # Create worker users
        workers = []
        for i in range(1, 4):
            worker = User.objects.create_user(
                username=f'worker{i}',
                email=f'worker{i}@example.com',
                password='password123',
                first_name=f'Worker',
                last_name=f'Number {i}'
            )
            worker.groups.add(worker_group)
            workers.append(worker)
        
        # Create incidents
        self.stdout.write('Creating test incidents...')
        
        urgency_levels = ['Low', 'Medium', 'High', 'Critical']
        locations = ['Server Room', 'Office Building A', 'Office Building B', 'Remote Office', 'Data Center']
        incident_descriptions = [
            'Network outage affecting all users',
            'Server overheating in rack B12',
            'Database connection issue',
            'Application performance degradation',
            'Security breach detected',
            'Storage capacity reached threshold',
            'Power failure in east wing',
            'Software deployment failed',
            'Backup system failure',
            'User account compromise'
        ]
        
        incidents = []
        status_options = [choice[0] for choice in Incident.STATUS_CHOICES]
        
        # Create 15 test incidents
        for i in range(15):
            status = random.choice(status_options)
            # Assign a worker for incidents that are in_progress or resolved
            assigned_to = None
            if status in ['in_progress', 'resolved']:
                assigned_to = random.choice(workers)
                
            # Create date in the past 30 days
            days_ago = random.randint(0, 30)
            created_at = datetime.now() - timedelta(days=days_ago)
            
            incident = Incident.objects.create(
                description=random.choice(incident_descriptions),
                location=random.choice(locations),
                urgency=random.choice(urgency_levels),
                status=status,
                assigned_to=assigned_to,
                created_at=created_at
            )
            incidents.append(incident)
            
        # Create comments for incidents
        self.stdout.write('Creating test comments...')
        
        comment_texts = [
            'Working on this issue now',
            'Need additional information to proceed',
            'This has been escalated to level 2 support',
            'Waiting for parts to arrive',
            'Issue has been reproduced, working on fix',
            'No progress yet, investigation ongoing',
            'Required reboot of the system',
            'Fixed the immediate issue, root cause still unknown',
            'Implemented temporary workaround',
            'Issue resolved. Closing the incident.'
        ]
        
        all_users = list(workers) + [manager1, manager2]
        
        # Add comments to some incidents
        for incident in incidents:
            # Add 0-5 comments per incident
            num_comments = random.randint(0, 5)
            for j in range(num_comments):
                days_after_incident = random.randint(0, min(5, (datetime.now() - incident.created_at).days))
                comment_date = incident.created_at + timedelta(days=days_after_incident)
                
                Comment.objects.create(
                    incident=incident,
                    author=random.choice(all_users),
                    text=random.choice(comment_texts),
                    created_at=comment_date
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated test data!'))
        self.stdout.write(f'Created {User.objects.filter(is_superuser=False).count()} users')
        self.stdout.write(f'Created {Incident.objects.count()} incidents')
        self.stdout.write(f'Created {Comment.objects.count()} comments')
        self.stdout.write('\nLogin credentials:')
        self.stdout.write('Manager: manager1 / password123')
        self.stdout.write('Worker: worker1 / password123')
