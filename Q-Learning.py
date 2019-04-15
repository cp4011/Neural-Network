import numpy as np
import random

# 6个房间（从0 1 2 3 4 5房间进入5房间的奖励，-1代表路不通，0代表路不通，100表示路不通且 能够直接打到5房间
r = np.array([[-1, -1, -1, -1, 0, -1],              # reward矩阵R
              [-1, -1, -1, 0, -1, 100],
              [-1, -1, -1, 0, -1, -1],
              [-1, 0, 0, -1, 0, -1],
              [0, -1, -1, 0, -1, 100],
              [-1, 0, -1, -1, 0, 100]])

q = np.zeros([6, 6], dtype=np.float32)              # 初始化 Q值矩阵（全0）
gamma = 0.8

step = 0
while step < 1000:
    state = random.randint(0, 5)
    if state != 5:
        next_state_list = []
        for i in range(6):
            if r[state, i] != -1:
                next_state_list.append(i)
        next_state = next_state_list[random.randint(0, len(next_state_list)-1)]
        qval = r[state, next_state] + gamma * max(q[next_state])
        q[state, next_state] = qval
    step += 1
print(q)

# 验证
for i in range(10):
    print("第{}次验证".format(i + 1))
    state = random.randint(0, 5)
    print('机器人处于{}'.format(state))
    count = 0
    while state != 5:
        if count > 20:
            print('fail')
            break
        # 选择最大的q_max
        q_max = q[state].max()

        q_max_action = []
        for action in range(6):
            if q[state, action] == q_max:
                q_max_action.append(action)

        next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
        print("the robot goes to " + str(next_state) + '.')
        state = next_state
        count += 1


"""理解题意：https://www.jianshu.com/p/29db50000e3f"""