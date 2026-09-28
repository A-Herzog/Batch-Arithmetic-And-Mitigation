#!/usr/bin/env python3


import os
import subprocess


simulator_binary = os.path.expanduser('~/Simulator-6.0/Simulator-CLI.sh')

cmd = [simulator_binary, 'language', 'en']
subprocess.Popen(cmd).wait()


model_files = os.listdir('Models_Generated')
statistic_files = os.listdir('Statistics')

counter = 0
for model_file in model_files:
    if not model_file.endswith(".xml"):
        continue
    statistic_file = "Statistics-" + model_file
    if statistic_file in statistic_files:
        continue

    absolute_model_file = os.path.abspath('Models_Generated' + os.sep + model_file)
    absolute_statistic_file = os.path.abspath('Statistics' + os.sep + statistic_file)
    counter += 1

    print(str(counter) + ":", model_file)
    cmd = [simulator_binary, 'simulation', absolute_model_file, absolute_statistic_file]
    subprocess.Popen(cmd).wait()
