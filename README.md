# 996.icu.game
To explore the forming of 996 working mode by simulation game on wechat game platform.
Instead of calling it a game, I would rather name it as an worker-hirer simulation experiment. As more and more people get involved, we can hopefully discover what is the truth of 996 working mode and find a way lead to 965 WLB.

### Introduction
#### 应用平台: 
微信小游戏/微信小程序/python GUI客户端
#### 游戏规则：  
1. 社会中有worker和hirer两种角色，每个人初始化进入游戏都是worker, 每个月有固定的收入。
2. worker和hirer可以进行双向选择，不同属性和工作岗位的worker对hirer产生不同的价值，worker在不同的hirer工作获得的收入有较大差别。
3. worker的积蓄达到一定程度可以选择成为hirer，拥有雇佣的资格。
4. 社会上的总财富是固定的，每个月按不同比例分配给hirers, 效率不高的hirer有可能产生负收入。
5. worker的工作年限、技能等属性影响其收入水平。


### usage
`python policy.py`

**params**   
```python
JOB_TYPES = ["engineer", "HR", "sales", "web"]
JOB_PROB = [4, 1, 2, 1]
WORKER_NUM = 20
HIRER_NUM = 5
```


### demo running result
> year: 0, JOB NUM: 0, WORKER NUM: 20, unemployment: 20   
> year: 1, JOB NUM: 49, WORKER NUM: 25, unemployment: 16   
> year: 2, JOB NUM: 77, WORKER NUM: 32, unemployment: 20   
> year: 3, JOB NUM: 95, WORKER NUM: 37, unemployment: 17   
> year: 4, JOB NUM: 112, WORKER NUM: 41, unemployment: 18   
> year: 5, JOB NUM: 125, WORKER NUM: 49, unemployment: 25  


**company report**

rank | staff NUM | fortune | hr_stat
:-: | :-: | :-: | :-: 
0 | 4 | ￥-2086500 |'recruit': 27, 'onboard': 26, 'leave': 21
1 | 6 | ￥-1151000 |'recruit': 35, 'onboard': 27, 'leave': 20
2 | 8 | ￥-275500 |'recruit': 36, 'onboard': 27, 'leave': 17
3 | 4 | ￥126000 |'recruit': 32, 'onboard': 21, 'leave': 16
4 | 6 | ￥400500 |'recruit': 35, 'onboard': 27, 'leave': 17

**workers report**

job_type | experience | salary | fortune | job_change times
:- | :-: | :-: |:-: |:-:
HR | 5y | ￥12500  | ￥576000 | 6 
HR | 4y | ￥8000  | ￥258000 | 3 
HR | 3y | ￥8000  | ￥190000 | 4 
HR | 3y | ￥5000  | ￥91000 | 3 
HR | 3y | ￥4000  | ￥57000 | 2 
HR | 2y | ￥4500  | ￥54500 | 2 
HR | 0y | ￥3000  | ￥3000 | 1 
engineer | 5y | ￥17500  | ￥791500 | 9 
engineer | 5y | ￥17500  | ￥735500 | 11 
engineer | 4y | ￥17500  | ￥708500 | 10 
engineer | 2y | ￥18000  | ￥429500 | 5 
engineer | 2y | ￥18000  | ￥401500 | 5 
engineer | 2y | ￥18000  | ￥257000 | 5 
engineer | 2y | ￥18000  | ￥191000 | 5 
engineer | 2y | ￥18000  | ￥133000 | 7 
engineer | 1y | ￥10500  | ￥115000 | 6 
engineer | 0y | ￥9000  | ￥37500 | 2 
engineer | 0y | ￥6000  | ￥4000 | 1 
sales | 5y | ￥10000  | ￥360000 | 6 
sales | 5y | ￥10000  | ￥331500 | 6 
sales | 4y | ￥9500  | ￥292000 | 4 
sales | 4y | ￥8000  | ￥240500 | 5 
sales | 2y | ￥8500  | ￥157000 | 4 
sales | 2y | ￥7000  | ￥125000 | 3 
web | 4y | ￥10500  | ￥249000 | 6 
web | 3y | ￥10000  | ￥152000 | 5 
web | 0y | ￥6000  | ￥36000 | 1 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
