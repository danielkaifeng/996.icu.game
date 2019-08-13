

class worker():
	def __init__(self, ID, job_type):	
		self.savings = 0
		self.income = 0
		self.skills = []
		self.job = None
		self.job_type = job_type
		self.working_status = False
		self.working_experience = 0
		self.health = 100
		self.ID = ID
		self.company_ID = []

	def get_job(self, job_config):
		self.company_ID.append(job_config["job_id"])
		self.job = job_config["job_type"]
		self.income = job_config["payment"]
		self.working_status = True

	def quit_job(self):
		self.job = None
		self.working_status = False
		self.income = 0

	def update(self):
		pass

	def get_salary(self):
		self.savings += self.income
		self.working_experience += 30

