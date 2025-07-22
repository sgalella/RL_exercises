import matplotlib.pyplot as plt
import numpy as np


def plot_values(V, env, ax):
    grid_shape = env.unwrapped.desc.shape
    desc = env.unwrapped.desc.astype(str).reshape(grid_shape)
    V_grid = V.reshape(grid_shape)

    im = ax.imshow(V_grid, cmap='Blues')

    num_states = V.shape[0]
    for s in range(num_states):
        row, col = divmod(s, grid_shape[1])
        cell_type = desc[row, col]
        state_value = V[s]
        
        if cell_type == 'H':
            ax.text(col, row, 'x', va='center', ha='center', fontsize=10, color='red')
            continue
        
        elif cell_type == 'G':
            ax.text(col, row, 'G', va='center', ha='center', fontsize=10, color='green')
            continue
        
        text_color = 'black' if state_value < (V.max() / 2) else 'white'
        ax.text(col, row, f'{state_value:.2f}', va='center', ha='center', fontsize=8, color=text_color)

    ax.set_xticks([])
    ax.set_yticks([])
    cbar = plt.colorbar(im, ax=ax, fraction=0.05, pad=0.04)
    cbar.set_label('State Value', fontsize=12)


def plot_policy_and_values(V, policy, env, ax):
    action_arrows = {0: '←', 1: '↓', 2: '→', 3: '↑'}
    
    grid_shape = env.unwrapped.desc.shape
    desc = env.unwrapped.desc.astype(str).reshape(grid_shape)
    V_grid = V.reshape(grid_shape)

    im = ax.imshow(V_grid, cmap='Blues')

    num_states = V.shape[0]
    for s in range(num_states):
        row, col = divmod(s, grid_shape[1])
        cell_type = desc[row, col]
        state_value = V[s]
        
        if cell_type == 'H':
            ax.text(col, row, 'x', va='center', ha='center', fontsize=10, color='red')
            continue
        
        elif cell_type == 'G':
            ax.text(col, row, 'G', va='center', ha='center', fontsize=10, color='green')
            continue

        # Plot policy arrow
        if np.sum(policy[s]) > 0:
            arrow_color = 'black' if state_value < (V.max() / 2) else 'white'
            a = np.argmax(policy[s])
            ax.text(col, row, action_arrows[a], va='center', ha='center', fontsize=12, color=arrow_color)

    ax.set_xticks([])
    ax.set_yticks([])
    cbar = plt.colorbar(im, ax=ax, fraction=0.05, pad=0.04)
    cbar.set_label('State Value', fontsize=12)