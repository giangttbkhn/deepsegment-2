# from import train, generate_data
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))
from deepsegment import generate_data,train

with open("/Users/trinhgiang/PycharmProjects/deepsegment-2/sent4.txt", "r", encoding='utf-8', errors='ignore') as f:
  lines = f.readlines()

x, y = generate_data(lines[10000:], max_sents_per_example=10, n_examples=1000)
vx, vy = generate_data(lines[:10000], max_sents_per_example=10, n_examples=1000)

train(x, y, vx, vy, epochs=4, batch_size=64, save_folder='/Users/trinhgiang/PycharmProjects/deepsegment-2/output', glove_path='/Users/trinhgiang/Downloads/wiki.txt')

