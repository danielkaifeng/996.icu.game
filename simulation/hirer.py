import random

class hirer():
	def __init__(self, ID):
		self.savings = 100000
		self.employees = {}
		self.staff_task_schedule = {}
		self.ID = ID
		self.cost = 0
		self.current_tasks = []
		self.hr_stat = {"recruit": 0, "onboard": 0, "leave": 0}

	def recruit(self, task_pool):
		assert len(task_pool) > 0
		task = random.choice(task_pool)
		task_pool.remove(task)
		position_vacancy = self.arrange_task(task)
		if len(position_vacancy) > 0:
			self.hr_stat["recruit"] += 1
		return task_pool, position_vacancy

	def arrange_task(self, task):
		position_vacancy = []
		reward = task["reward"]
		time_cost = task["time_cost"]
		self.savings += reward
		task_id = task["task_id"]
		payment = random.randint(4,12) * 1000

		for member in task["team_member"]:
			job_type = member["job_type"]
			experience = member["experience"]
			mark = False
			for SID, staff in self.employees.items():
				if staff.job_type == job_type and staff.working_experience > experience:
					#add task to staff working schedule
					assert SID in self.staff_task_schedule.keys()
					if self.staff_task_schedule[SID] + time_cost < 70: 
						self.staff_task_schedule[SID] += time_cost
						mark = True
						break

			if not mark:
				#lacking suitable staff and start a recruitment
				config = {"job_id": self.ID, "job_type": job_type, "experience": experience, "payment": payment}
				position_vacancy.append(config)
		return position_vacancy

	def staff_on_board(self, config, person):
		self.cost += config["payment"]
		self.employees[person.ID] = person
		self.staff_task_schedule[person.ID] = 0
		self.hr_stat["onboard"] += 1

	def staff_leave(self, person):
		del self.employees[person.ID]
		del self.staff_task_schedule[person.ID]
		self.hr_stat["leave"] += 1

	def update(self):
		self.savings -= self.cost


