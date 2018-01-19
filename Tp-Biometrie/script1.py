import os

directory = "./corpus"

for filename in os.listdir(directory):
    if filename.endswith(".raw"): 
        print(os.path.join(directory, filename))
        continue
    else:
        continue
