
import re

lines = []

with open('seeds_dataset.txt', 'r') as f:
  for line in f.readlines():
    cleaned_line = re.sub('\n', '', line)
    cleaned_list = cleaned_line.split()
    lines.append(','.join(cleaned_list) + "\n")

  f.close()

with open('seeds_dataset.csv', 'w') as f:
  f.writelines(lines)
  f.close()
