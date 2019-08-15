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


### demo running result
> year: 0, JOB NUM: 0, WORKER NUM: 20, unemployment: 20
> year: 1, JOB NUM: 52, WORKER NUM: 24, unemployment: 16
> year: 2, JOB NUM: 80, WORKER NUM: 32, unemployment: 16
> year: 3, JOB NUM: 92, WORKER NUM: 40, unemployment: 20
> year: 4, JOB NUM: 103, WORKER NUM: 47, unemployment: 20
> year: 5, JOB NUM: 110, WORKER NUM: 53, unemployment: 24
**company report**

rank | staff NUM | fortune | hr_stat
:-: | :-: | :-: 
0 | 8 | ￥-66000 |'recruit': 37, 'onboard': 37, 'leave': 23
1 | 8 | ￥243000 |'recruit': 29, 'onboard': 27, 'leave': 14
2 | 5 | ￥611500 |'recruit': 29, 'onboard': 19, 'leave': 13
3 | 5 | ￥614500 |'recruit': 24, 'onboard': 22, 'leave': 15
4 | 7 | ￥923000 |'recruit': 31, 'onboard': 26, 'leave': 17

**workers report**

job_type | experience | salary | fortune
:- | :-: | :-: |:-: 
HR | 5y | ￥17500  | ￥701000 
HR | 3y | ￥6000  | ￥214500 
HR | 3y | ￥6000  | ￥246000 
HR | 0y | ￥5000  | ￥45000 
HR | 0y | ￥5000  | ￥5000 
engineer | 5y | ￥10500  | ￥558000 
engineer | 5y | ￥10500  | ￥551000 
engineer | 5y | ￥10500  | ￥515000 
engineer | 4y | ￥10000  | ￥417500 
engineer | 4y | ￥10000  | ￥372000 
engineer | 4y | ￥10000  | ￥362000 
engineer | 4y | ￥8500  | ￥321500 
engineer | 3y | ￥8500  | ￥297500 
engineer | 3y | ￥8500  | ￥278000 
engineer | 3y | ￥8500  | ￥254500 
engineer | 3y | ￥8500  | ￥229500 
engineer | 2y | ￥7000  | ￥158000 
engineer | 2y | ￥7000  | ￥149500 
engineer | 0y | ￥7000  | ￥54000 
engineer | 0y | ￥5500  | ￥9500 
sales | 5y | ￥18000  | ￥857500 
sales | 3y | ￥15500  | ￥561000 
sales | 3y | ￥10000  | ￥315000 
sales | 2y | ￥9000  | ￥267000 
sales | 2y | ￥7500  | ￥183000 
sales | 2y | ￥8000  | ￥182500 
sales | 1y | ￥6500  | ￥140500 
sales | 0y | ￥4000  | ￥16000 
web | 5y | ￥12000  | ￥520500 
web | 4y | ￥12000  | ￥435000 
web | 1y | ￥6000  | ￥132000 
web | 1y | ￥6000  | ￥106500 
web | 0y | ￥4000  | ￥12000 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
