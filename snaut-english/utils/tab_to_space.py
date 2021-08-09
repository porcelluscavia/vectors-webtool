

inputFile = open('/Users/samski/Downloads/L6_SVD400.txt', 'r')
exportFile = open('/Users/samski/Downloads/final_vecspace.txt', 'w')
for line in inputFile:
   new_line = line.replace('\t', ' ')
   exportFile.write(new_line)

inputFile.close()
exportFile.close()