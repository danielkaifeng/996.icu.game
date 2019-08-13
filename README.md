# 996.icu.game
To explore the forming of 996 working mode by simulation game on wechat game platform.
Instead of calling it a game, I would rather name it as an worker-hirer simulation experiment. As more and more people get involved, we can hopefully discover what is the truth of 996 working mode and find a way lead to 965 WLB.

### Introduction
应用平台: 微信小游戏/微信小程序/python GUI客户端
游戏规则：  
1. 社会中有worker和hirer两种角色，每个人初始化进入游戏都是worker, 每个月有固定的收入。
2. worker和hirer可以进行双向选择，不同属性和工作岗位的worker对hirer产生不同的价值，worker在不同的hirer工作获得的收入有较大差别。
3. worker的积蓄达到一定程度可以选择成为hirer，拥有雇佣的资格。
4. 社会上的总财富是固定的，每个月按不同比例分配给hirers, 效率不高的hirer有可能产生负收入。
5. worker的工作年限、技能等属性影响其收入水平。


### demo running result
**company report**

staff NUM | fortune | hr_stat
:-: | :-: | :-: 
1 | ￥918000 |{'recruit': 12, 'onboard': 4, 'leave': 2}
1 | ￥310000 |{'recruit': 13, 'onboard': 10, 'leave': 7}
2 | ￥820000 |{'recruit': 14, 'onboard': 6, 'leave': 1}
5 | ￥241000 |{'recruit': 11, 'onboard': 9, 'leave': 4}
4 | ￥597000 |{'recruit': 12, 'onboard': 6, 'leave': 1}

**workers report**

job_type | experience | salary | fortune
:- | :-: | :-: |:-: 
sales | 5year | ￥12000  | ￥570000 
engineer | 5year | ￥12000  | ￥668000 
sales | 5year | ￥12000  | ￥514000 
HR | 5year | ￥11000  | ￥561000 
web | 2year | ￥11000  | ￥363000 
engineer | 3year | ￥11000  | ￥475000 
sales | 5year | ￥9000  | ￥474000 
engineer | 2year | ￥11000  | ￥230000 
engineer | 1year | ￥7000  | ￥105000 
engineer | 1year | ￥7000  | ￥85000 
sales | 0year | ￥5000  | ￥15000 
web | 1year | ￥10000  | ￥112000 
HR | 4year | ￥11000  | ￥414000 
