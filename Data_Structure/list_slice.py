sample_list = [11, 45, 8, 23, 14, 78, 56, 89, 99]

chunk_size = 3
chunks = [sample_list[i:i + chunk_size] for i in range(0, len(sample_list), chunk_size)]
for chunk in chunks:
    print(chunk)
    print(list(reversed(chunk)))
    