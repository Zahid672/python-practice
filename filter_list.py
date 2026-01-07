roll_number = [47, 64, 69, 37, 76, 83, 95, 97]

sample_dict = {'zahid':47, 'saeed':69, 'imran':76, 'wasim':97}

roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print("after removing unwanted elements from list:", roll_number)

