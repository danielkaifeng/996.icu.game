import random
import numpy as np

class hirer():
	def __init__(self, ID):
		self.savings = 100000
		self.employees = {}
		self.staff_task_schedule = {}
		self.ID = ID
		self.cost = 0
		self.current_tasks = []
		self.hr_stat = {"recruit": 0, "onboard": 0, "leave": 0}

	def evaluate_position_payment(self, vacancy, expectation):
		updated_vacancy = []
		for config in vacancy:
			#payment should be adjusted by candidates expectation and task profit
			if expectation is None:
				payment = random.randint(3,6) * 1000
			else:
				#get some info about how much salary qualified workers expect in the market
				payRange = expectation[config["job_type"]]
				experience_payRange = [x[0] for x in payRange if x[1] >= config["experience"] and x[1] < config["experience"] + 2]
				#payment stragety can vary from min/median/max level on the market
				if len(experience_payRange) == 0:
					payment = random.randint(3,6) * 1000
				else:
					#payment = np.median(experience_payRange)
					payment = np.min(experience_payRange) + 500
					payment = min(payment, 18000)

			config["payment"] = payment
			updated_vacancy.append(config)

		return updated_vacancy

	def recruit(self, task_pool, expectation):
		assert len(task_pool) > 0
		task = random.choice(task_pool)
		task_pool.remove(task)
		position_vacancy = self.arrange_task(task)

		if len(position_vacancy) > 0:
			self.hr_stat["recruit"] += 1
			position_vacancy = self.evaluate_position_payment(position_vacancy, expectation)

		return task_pool, position_vacancy

	def arrange_task(self, task):
		position_vacancy = []
		reward = task["reward"]
		time_cost = task["time_cost"]
		self.savings += reward
		task_id = task["task_id"]


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
				config = {"job_id": self.ID, "job_type": job_type, "experience": experience}
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


