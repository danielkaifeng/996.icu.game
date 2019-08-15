from simulation.worker import worker
from simulation.hirer import hirer
import numpy as np
import random

JOB_TYPES = ["engineer", "HR", "sales", "web"]
JOB_PROB = [4, 1, 2, 1]
JOB_PROB = np.array(JOB_PROB) /sum(JOB_PROB)
WORKER_NUM = 20
HIRER_NUM = 5

class world():
	#a world with certain control policy
	def __init__(self):
		self.workers = self.init_workers()
		self.hirers = self.init_hirers()
		self.worker_expectation = None
		self.jobs_list = []
		self.task_pool = []
		self.task_id = 0

		self.update_task_pool()

	def init_workers(self):
		workers = {}
		for i in range(WORKER_NUM):
			job_type = random.choice(JOB_TYPES)
			workers[i] = worker(i, job_type)
		self.wid = i + 1
		return workers
	
	def init_hirers(self):
		hirers = {}
		for i in range(HIRER_NUM):
			hirers[i] = hirer(i)
		return hirers

	def update(self, step):
		if step % 30 == 0:
			self.worker_expectation = dict((x,[]) for x in JOB_TYPES)
		if step % 10 == 0:
			self.update_task_pool()
			#random generate task and worker
		if step % 365 == 0:
			print("> year: %d, JOB NUM: %d, WORKER NUM: %d, unemployment: %d   " % (step//365, len(self.jobs_list), len(self.workers), 
									len([x for x in self.workers.values() if x.job is None])))

		if random.randint(0,50) == 1:
			job_type = random.choice(JOB_TYPES)
			self.workers[self.wid] = worker(self.wid, job_type)
			self.wid += 1

		companys = list(self.hirers.values())
		random.shuffle(companys)
		for employer in companys:
			if len(self.task_pool) > 0:
				self.task_pool, jobs = employer.recruit(self.task_pool, self.worker_expectation)
				self.jobs_list += jobs
				
			#company monthly update
			if step % 30 == 0:
				employer.update()

		for wid, person in self.workers.items():
			self.career_policy(person)
			#person.update()
			if step % 30 == 0 and step >= 30 and person.job is not None:
				person.get_salary()	
				self.update_expectation(person)
			#print("worker saving: %d\tworking experience: %d" % (person.savings, person.working_experience))

	def update_task_pool(self):
	#random tasks with reward, hirers can organize a team to accomplish the task and get the reward
		#time needed for this task
		#task time vary from a week to two months
		time_needed = random.randint(7,60)
		team = []
		for n in range(2):
			member = {"job_type": np.random.choice(JOB_TYPES, p = JOB_PROB), 
				 "experience": max(0,np.int16(2 + 2*np.random.randn()))
			}
			team.append(member)
		#reward is based on time cost and worker experience
		reward = 3000 * time_needed + 10000 * sum([x["experience"] for x in team])

		task = {
			"task_id": self.task_id,
			"team_member": team,
			"time_cost": time_needed,
			"reward":  reward
			}
		self.task_pool.append(task)
		self.task_id += 1

	def career_policy(self, person):	
	#check available jobs this person is qualified for
		available_jobs = [x for x in self.jobs_list if person.working_experience//365 >= x["experience"] 
							and person.job_type == x["job_type"] 
							and x["payment"] > person.income + 500
							]
	
		if len(available_jobs) > 0:
			config = random.choice(available_jobs)
			self.jobs_list.remove(config)
	
			co_ID = person.company_ID 
			job_ID = config["job_id"]
			if person.job is not None and co_ID[-1] != job_ID:
				#what is the best strategy to find a new job?
				person.quit_job()
				self.hirers[co_ID[-1]].staff_leave(person)
				#print(config)
	
			person.get_job(config)
			self.hirers[job_ID].staff_on_board(config, person)

	def update_expectation(self, person):
		self.worker_expectation[person.job_type].append([max(2500, person.income+1000), person.working_experience//365])


if __name__ == "__main__":
	helloworld = world()
	for step in range(2000):
		helloworld.update(step)

	print('**company report**')
	print('')
	print("rank | staff NUM | fortune | hr_stat")
	print(":-: | :-: | :-: | :-: ")
	for i, co in enumerate(sorted(helloworld.hirers.values(), key = lambda x:x.savings)):
		#print("staff NUM: %d\tfortune:%d hr_stat: %s" % (len(co.employees), co.savings, str(co.hr_stat)))
		print("%d | %d | ￥%d |%s" % (i, len(co.employees), co.savings, str(co.hr_stat).strip('{}')))
	print('')
	print('**workers report**')
	print('')
	print("job_type | experience | salary | fortune | job_change times")
	print(":- | :-: | :-: |:-: |:-:")
	for person in sorted(helloworld.workers.values(), key= lambda x:x.job_type):
		if person.savings > 0: 
			print("%s | %dy | ￥%d  | ￥%d | %d " % 
					(person.job_type, person.working_experience//365, person.income, person.savings, len(person.company_ID)))
	print('~'*50)





