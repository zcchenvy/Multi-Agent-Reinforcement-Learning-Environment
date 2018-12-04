import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


class EnvFindGoals(object):

    def __init__(self):
        self.start1 = [3, 1]
        self.start2 = [6, 1]
        self.dest1 = [8, 2]
        self.dest2 = [1, 2]
        self.agt1_pos = [3, 1]
        self.agt2_pos = [6, 1]
        self.occupancy = [[1, 1, 1, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 1, 1]]

    def list_add(self, a, b):
        c = [a[i] + b[i] for i in range(min(len(a), len(b)))]
        return c

    def get_agt1_obs(self):
        visual_range = 3
        vec = np.zeros((visual_range, visual_range, 3))

        for i in range(visual_range):
            for j in range(visual_range):
                vec[i, j, 0] = 1.0
                vec[i, j, 1] = 1.0
                vec[i, j, 2] = 1.0

        # detect block
        if self.occupancy[self.agt1_pos[0] - 1][self.agt1_pos[1] + 1] == 1:
            vec[0, 0, 0] = 0.0
            vec[0, 0, 1] = 0.0
            vec[0, 0, 2] = 0.0
        if self.occupancy[self.agt1_pos[0]][self.agt1_pos[1] + 1] == 1:
            vec[0, 1, 0] = 0.0
            vec[0, 1, 1] = 0.0
            vec[0, 1, 2] = 0.0
        if self.occupancy[self.agt1_pos[0] + 1][self.agt1_pos[1] + 1] == 1:
            vec[0, 2, 0] = 0.0
            vec[0, 2, 1] = 0.0
            vec[0, 2, 2] = 0.0
        if self.occupancy[self.agt1_pos[0] - 1][self.agt1_pos[1]] == 1:
            vec[1, 0, 0] = 0.0
            vec[1, 0, 1] = 0.0
            vec[1, 0, 2] = 0.0
        if self.occupancy[self.agt1_pos[0] + 1][self.agt1_pos[1]] == 1:
            vec[1, 2, 0] = 0.0
            vec[1, 2, 1] = 0.0
            vec[1, 2, 2] = 0.0
        if self.occupancy[self.agt1_pos[0] - 1][self.agt1_pos[1] - 1] == 1:
            vec[2, 0, 0] = 0.0
            vec[2, 0, 1] = 0.0
            vec[2, 0, 2] = 0.0
        if self.occupancy[self.agt1_pos[0]][self.agt1_pos[1] - 1] == 1:
            vec[2, 1, 0] = 0.0
            vec[2, 1, 1] = 0.0
            vec[2, 1, 2] = 0.0
        if self.occupancy[self.agt1_pos[0] + 1][self.agt1_pos[1] - 1] == 1:
            vec[2, 2, 0] = 0.0
            vec[2, 2, 1] = 0.0
            vec[2, 2, 2] = 0.0

        # detect self
        vec[1, 1, 0] = 1.0
        vec[1, 1, 1] = 0.0
        vec[1, 1, 2] = 0.0

        # detect agent2
        if self.agt2_pos == self.list_add(self.agt1_pos, [-1, 1]):
            vec[0, 0, 0] = 0.0
            vec[0, 0, 1] = 0.0
            vec[0, 0, 2] = 1.0
        if self.agt2_pos == self.list_add(self.agt1_pos, [0, 1]):
            vec[0, 1, 0] = 0.0
            vec[0, 1, 1] = 0.0
            vec[0, 1, 2] = 1.0
        if self.agt2_pos == self.list_add(self.agt1_pos, [1, 1]):
            vec[0, 2, 0] = 0.0
            vec[0, 2, 1] = 0.0
            vec[0, 2, 2] = 1.0
        if self.agt2_pos == self.list_add(self.agt1_pos, [-1, 0]):
            vec[1, 0, 0] = 0.0
            vec[1, 0, 1] = 0.0
            vec[1, 0, 2] = 1.0
        if self.agt2_pos == self.list_add(self.agt1_pos, [1, 0]):
            vec[1, 2, 0] = 0.0
            vec[1, 2, 1] = 0.0
            vec[1, 2, 2] = 1.0
        if self.agt2_pos == self.list_add(self.agt1_pos, [-1, -1]):
            vec[2, 0, 0] = 0.0
            vec[2, 0, 1] = 0.0
            vec[2, 0, 2] = 1.0
        if self.agt2_pos == self.list_add(self.agt1_pos, [0, -1]):
            vec[2, 1, 0] = 0.0
            vec[2, 1, 1] = 0.0
            vec[2, 1, 2] = 1.0
        if self.agt2_pos == self.list_add(self.agt1_pos, [1, -1]):
            vec[2, 2, 0] = 0.0
            vec[2, 2, 1] = 0.0
            vec[2, 2, 2] = 1.0
        return vec

    def get_agt2_obs(self):
        visual_range = 3
        vec = np.zeros((visual_range, visual_range, 3))

        for i in range(visual_range):
            for j in range(visual_range):
                vec[i, j, 0] = 1.0
                vec[i, j, 1] = 1.0
                vec[i, j, 2] = 1.0

        # detect block
        if self.occupancy[self.agt2_pos[0] - 1][self.agt2_pos[1] + 1] == 1:
            vec[0, 0, 0] = 0.0
            vec[0, 0, 1] = 0.0
            vec[0, 0, 2] = 0.0
        if self.occupancy[self.agt2_pos[0]][self.agt2_pos[1] + 1] == 1:
            vec[0, 1, 0] = 0.0
            vec[0, 1, 1] = 0.0
            vec[0, 1, 2] = 0.0
        if self.occupancy[self.agt2_pos[0] + 1][self.agt2_pos[1] + 1] == 1:
            vec[0, 2, 0] = 0.0
            vec[0, 2, 1] = 0.0
            vec[0, 2, 2] = 0.0
        if self.occupancy[self.agt2_pos[0] - 1][self.agt2_pos[1]] == 1:
            vec[1, 0, 0] = 0.0
            vec[1, 0, 1] = 0.0
            vec[1, 0, 2] = 0.0
        if self.occupancy[self.agt2_pos[0] + 1][self.agt2_pos[1]] == 1:
            vec[1, 2, 0] = 0.0
            vec[1, 2, 1] = 0.0
            vec[1, 2, 2] = 0.0
        if self.occupancy[self.agt2_pos[0] - 1][self.agt2_pos[1] - 1] == 1:
            vec[2, 0, 0] = 0.0
            vec[2, 0, 1] = 0.0
            vec[2, 0, 2] = 0.0
        if self.occupancy[self.agt2_pos[0]][self.agt2_pos[1] - 1] == 1:
            vec[2, 1, 0] = 0.0
            vec[2, 1, 1] = 0.0
            vec[2, 1, 2] = 0.0
        if self.occupancy[self.agt2_pos[0] + 1][self.agt2_pos[1] - 1] == 1:
            vec[2, 2, 0] = 0.0
            vec[2, 2, 1] = 0.0
            vec[2, 2, 2] = 0.0

        # detect self
        vec[1, 1, 0] = 0.0
        vec[1, 1, 1] = 0.0
        vec[1, 1, 2] = 1.0

        # detect agent2
        if self.agt1_pos == self.list_add(self.agt2_pos, [-1, 1]):
            vec[0, 0, 0] = 1.0
            vec[0, 0, 1] = 0.0
            vec[0, 0, 2] = 0.0
        if self.agt1_pos == self.list_add(self.agt2_pos, [0, 1]):
            vec[0, 1, 0] = 1.0
            vec[0, 1, 1] = 0.0
            vec[0, 1, 2] = 0.0
        if self.agt1_pos == self.list_add(self.agt2_pos, [1, 1]):
            vec[0, 2, 0] = 1.0
            vec[0, 2, 1] = 0.0
            vec[0, 2, 2] = 0.0
        if self.agt1_pos == self.list_add(self.agt2_pos, [-1, 0]):
            vec[1, 0, 0] = 1.0
            vec[1, 0, 1] = 0.0
            vec[1, 0, 2] = 0.0
        if self.agt1_pos == self.list_add(self.agt2_pos, [1, 0]):
            vec[1, 2, 0] = 1.0
            vec[1, 2, 1] = 0.0
            vec[1, 2, 2] = 0.0
        if self.agt1_pos == self.list_add(self.agt2_pos, [-1, -1]):
            vec[2, 0, 0] = 1.0
            vec[2, 0, 1] = 0.0
            vec[2, 0, 2] = 0.0
        if self.agt1_pos == self.list_add(self.agt2_pos, [0, -1]):
            vec[2, 1, 0] = 1.0
            vec[2, 1, 1] = 0.0
            vec[2, 1, 2] = 0.0
        if self.agt1_pos == self.list_add(self.agt2_pos, [1, -1]):
            vec[2, 2, 0] = 1.0
            vec[2, 2, 1] = 0.0
            vec[2, 2, 2] = 0.0
        return vec

    def step(self, action1, action2):
        reward_1 = 0
        reward_2 = 0
        self.start1 = [3, 1]
        self.start2 = [6, 1]
        self.dest1 = [8, 2]
        self.dest2 = [1, 2]
        # agent1 move
        if action1 == 0:    # move up
            reward_1 = reward_1 - 1
            if self.occupancy[self.agt1_pos[0]][self.agt1_pos[1] + 1] != 1:     # if can move
                self.agt1_pos[1] = self.agt1_pos[1] + 1
                self.occupancy[self.agt1_pos[0]][self.agt1_pos[1] - 1] = 0
                self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1
            else:
                reward_1 = reward_1 - 3
        elif action1 == 1:  # move down
            reward_1 = reward_1 - 1
            if self.occupancy[self.agt1_pos[0]][self.agt1_pos[1] - 1] != 1:  # if can move
                self.agt1_pos[1] = self.agt1_pos[1] - 1
                self.occupancy[self.agt1_pos[0]][self.agt1_pos[1] + 1] = 0
                self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1
            else:
                reward_1 = reward_1 - 3
        elif action1 == 2:  # move left
            reward_1 = reward_1 - 1
            if self.occupancy[self.agt1_pos[0] - 1][self.agt1_pos[1]] != 1:  # if can move
                self.agt1_pos[0] = self.agt1_pos[0] - 1
                self.occupancy[self.agt1_pos[0] + 1][self.agt1_pos[1]] = 0
                self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1
            else:
                reward_1 = reward_1 - 3
        elif action1 == 3:  # move right
            reward_1 = reward_1 - 1
            if self.occupancy[self.agt1_pos[0] + 1][self.agt1_pos[1]] != 1:  # if can move
                self.agt1_pos[0] = self.agt1_pos[0] + 1
                self.occupancy[self.agt1_pos[0] - 1][self.agt1_pos[1]] = 0
                self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1
            else:
                reward_1 = reward_1 - 3

        # agent2 move
        if action2 == 0:    # move up
            reward_2 = reward_2 - 1
            if self.occupancy[self.agt2_pos[0]][self.agt2_pos[1] + 1] != 1:     # if can move
                self.agt2_pos[1] = self.agt2_pos[1] + 1
                self.occupancy[self.agt2_pos[0]][self.agt2_pos[1] - 1] = 0
                self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1
            else:
                reward_1 = reward_1 - 3
        elif action2 == 1:  # move down
            reward_2 = reward_2 - 1
            if self.occupancy[self.agt2_pos[0]][self.agt2_pos[1] - 1] != 1:  # if can move
                self.agt2_pos[1] = self.agt2_pos[1] - 1
                self.occupancy[self.agt2_pos[0]][self.agt2_pos[1] + 1] = 0
                self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1
            else:
                reward_1 = reward_1 - 3
        elif action2 == 2:  # move left
            reward_2 = reward_2 - 1
            if self.occupancy[self.agt2_pos[0] - 1][self.agt2_pos[1]] != 1:  # if can move
                self.agt2_pos[0] = self.agt2_pos[0] - 1
                self.occupancy[self.agt2_pos[0] + 1][self.agt2_pos[1]] = 0
                self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1
            else:
                reward_1 = reward_1 - 3
        elif action2 == 3:  # move right
            reward_2 = reward_2 - 1
            if self.occupancy[self.agt2_pos[0] + 1][self.agt2_pos[1]] != 1:  # if can move
                self.agt2_pos[0] = self.agt2_pos[0] + 1
                self.occupancy[self.agt2_pos[0] - 1][self.agt2_pos[1]] = 0
                self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1
            else:
                reward_1 = reward_1 - 3

        if self.agt1_pos == self.dest1:
            self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 0
            self.agt1_pos = self.start1
            self.occupancy[self.agt1_pos[0]][self.agt1_pos[1]] = 1
            reward_1 = reward_1 + 50

        if self.agt2_pos == self.dest2:
            self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 0
            self.agt2_pos = self.start2
            self.occupancy[self.agt2_pos[0]][self.agt2_pos[1]] = 1
            reward_2 = reward_2 + 50

        obs_1 = self.get_agt1_obs()
        obs_2 = self.get_agt2_obs()
        return reward_1, reward_2, obs_1, obs_2

    def reset(self):
        self.agt1_pos = [3, 1]
        self.agt2_pos = [6, 1]

        self.occupancy = [[1, 1, 1, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 1, 1]]

    def plot_scene(self):
        fig = plt.figure(figsize=(8, 8))
        gs = GridSpec(3, 2, figure=fig)
        ax1 = fig.add_subplot(gs[0:2, 0:2])
        ax2 = fig.add_subplot(gs[2, 0:1])
        ax3 = fig.add_subplot(gs[2, 1:2])

        # plot grid
        for k in range(10):
            for j in range(4):
                rect = plt.Rectangle((k, j), 1, 1, color='k', fill=False)
                ax1.add_patch(rect)

        # plot block
        for k in range(10):
            for j in range(4):
                    if self.occupancy[k][j] == 1:
                        rect = plt.Rectangle((k, j), 1, 1, color='k')
                        ax1.add_patch(rect)

        # plot agent
        rect = plt.Rectangle((self.agt1_pos[0], self.agt1_pos[1]), 1, 1, color='r')
        ax1.add_patch(rect)
        rect = plt.Rectangle((self.agt2_pos[0], self.agt2_pos[1]), 1, 1, color='b')
        ax1.add_patch(rect)

        ax1.set_xlim([-1, 12])
        ax1.set_ylim([-1, 6])

        ax2.imshow(self.get_agt1_obs())
        ax3.imshow(self.get_agt2_obs())
        plt.show()
