import os
import django
import random
# from datetime import datetime, timedelta
from faker import Faker

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()

# Import models after Django setup
from first_app.models import Topic, Webpage, AccessRecord,Users

# Initialize Faker
fake = Faker()

def populate_topics(n=5):
	"""Create n fake topics"""
	topics = []
	topics_list = ['Search Engines', 'Social Media', 'News', 'E-commerce', 
				   'Education', 'Technology', 'Health', 'Entertainment',
				   'Sports', 'Finance']
	
	for topic_name in topics_list[:n]:
		t = Topic.objects.get_or_create(topic_name=topic_name)[0]
		topics.append(t)
	
	return topics

def populate_webpages(topics, n=20):
	"""Create n fake webpages related to the given topics"""
	webpages = []
	
	for _ in range(n):
		# Get random topic
		topic = random.choice(topics)
		
		# Create unique name and URL
		name = fake.company() + ' ' + fake.company_suffix()
		# Make sure to create domain names that match the topic for more realism
		url = f"https://www.{name.lower().replace(' ', '')}.{fake.tld()}"
		
		# Using get_or_create to avoid duplicates due to unique constraints
		w = Webpage.objects.get_or_create(
			topic=topic,
			name=name,
			url=url
		)[0]
		
		webpages.append(w)
	
	return webpages

def populate_access_records(webpages, n=50):
	"""Create n fake access records for the given webpages"""
	for _ in range(n):
		# Get random webpage
		webpage = random.choice(webpages)
		
		# Create random date within last year
		date = fake.date_time_between(start_date='-1y', end_date='now').date()
		
		AccessRecord.objects.get_or_create(
			name=webpage,
			date=date
		)

def populate_all():
	"""Main function to populate all models"""
	print("Starting to populate database...")
	
	# Create fake topics
	topics = populate_topics(n=5)
	print(f"Created {len(topics)} topics")
	
	# Create fake webpages
	webpages = populate_webpages(topics, n=30)
	print(f"Created {len(webpages)} webpages")
	
	# Create fake access records
	populate_access_records(webpages, n=50)
	print(f"Created access records")
	
	print("Population complete!")
 

def populate_users(n = 50):
	for user in range(n):
		fake_name = fake.name()
		fake_first_name = fake_name.split()[0]
		fake_last_name = fake_name.split()[1]
		fake_email = fake.email()
		
		Users.objects.get_or_create(
			firstname=fake_first_name,
			lastname=fake_last_name,
			email = fake_email
		)
		
		print(f"Created {n} users")	
		print("Population complete!")
	
 

if __name__ == '__main__':
	print("Running population script...")
	#* populate_all() --- function for populating topics,websites, and accessrecords tables
	populate_users()