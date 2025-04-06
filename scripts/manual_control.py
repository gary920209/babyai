#!/usr/bin/env python3

import time
import argparse
import numpy as np
import gym
from minigrid.wrappers import *
import matplotlib.pyplot as plt

step_counter = 0


def redraw(img, step_count):
    if not args.agent_view:
        img = env.render()

    # Save the image with a unique filename based on the step count
    filename = f"frame_step_{step_count}.png"
    plt.imshow(img)
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    print(f"Image saved as {filename}")

def reset():
    if args.seed != -1:
        env.seed(args.seed)

    obs = env.reset()

    if hasattr(env, 'mission'):
        print('Mission: %s' % env.mission)

    redraw(obs, step_count=0)

def step(action, step_count):
    global step_counter
    step_counter += 1  # Increment the step count
    result = env.step(action)
    if len(result) == 5:
        obs, reward, done, truncated, info = result
        done = done or truncated  # Combine 'done' and 'truncated' flags
    elif len(result) == 4:
        obs, reward, done, info = result
    else:
        raise ValueError(f"Unexpected number of return values from env.step: {len(result)}")


    # obs, reward, done, info = env.step(action)
    print(f"Step {step_count}: Action={action}, Reward={reward}, Done={done}, Info={info}")

    redraw(obs, step_count)

    if done:
        print('done!')
        reset()

def process_actions(action_sequence):
    """
    Process a sequence of actions and generate images for each step.
    :param action_sequence: List of actions to execute in the environment.
    """
    reset()
    for step_count, action in enumerate(action_sequence, start=1):
        print(f"Executing action: {action}")
        step(action, step_count)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--env",
    help="gym environment to load",
    default='BabyAI-BossLevel-v0'
)
parser.add_argument(
    "--seed",
    type=int,
    help="random seed to generate the environment with",
    default=-1
)
parser.add_argument(
    "--tile_size",
    type=int,
    help="size at which to render tiles",
    default=32
)
parser.add_argument(
    '--agent_view',
    default=False,
    help="draw the agent sees (partially observable view)",
    action='store_true'
)

args = parser.parse_args()

env = gym.make(args.env, render_mode='rgb_array')

if args.agent_view:
    env = RGBImgPartialObsWrapper(env)
    env = ImgObsWrapper(env)
example_actions = [
    env.unwrapped.actions.forward,  # Move forward
    env.unwrapped.actions.left,     # Turn left
    env.unwrapped.actions.forward,  # Move forward
    env.unwrapped.actions.done      # Mark task as done
]
# Process the example action sequence
process_actions(example_actions)