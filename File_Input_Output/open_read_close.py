### File I/O in Python: python can be used to perform operations on a file. (read & write data).
### Types of all files: 1. Text Files: .txt, .docx, .log, etc. 2. Binary Files: .mp4, .mov, .png, .jpeg etc.

f = open("welcome.txt", "r")
data = f.read()
print(data)

print(f.readline()) ## read one line at a time


f.close()