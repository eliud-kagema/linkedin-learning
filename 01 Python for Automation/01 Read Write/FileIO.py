f = open('ExerciseFiles/inputFile.txt', 'r') # Reads a file on disk
passFile = open('ExerciseFiles/passFile.txt', 'w') # Writes a new file
failFile = open( 'ExerciseFiles/failFile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)
  
f.close()
passFile.close()
failFile.close()