from google.cloud import datastore 
client = datastore.Client('handy-amplifier-200618')

kind = 'Booking'
task_key=client.key(kind)


def create_entity(data):
	try:
		#print(data)
		task=	datastore.Entity(key=task_key)
		task['user_id']=data['id']
		task['person']=data['person']
		task['date']=data['date']
		task['time']=data['time']
		#print(data)
		client.put(task)
		#print(data)
		return True
	except:
		return False

def get_entity(user_id):
	try:
	
		query = client.query(kind='Booking')
		query.add_filter('user_id', '=', int(user_id))
		
		details=list(query.fetch())
	
		return details
	except:
		return False

def insert_user(user_id):
	kind='user'
	task_key=client.key(kind)
	try:
		query=client.query(kind='user')
		query.add_filter('user_id','=',int(user_id))
		details=list(query.fetch())
		if len(details)==0:
			task=datastore.Entity(key=task_key)
			task['user_id']=int(user_id)
			client.put(task)
		else:
			return 'Exist'
	except:
		return False

