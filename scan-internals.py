#This little script parses all source files in the project directory
# and gets all labels inside the getEzRMSContextLabelIntern method
# I am using it for my local project to extract all of the items for L10n

import re, os

# Put the path to the sources here
path = "C:\SWorkSpace";

for root, dirs, files in os.walk(path):
	for file in files:
        #parse only source files (.java). Remove this if needed :)
		if file.endswith(".java"):
			
			fn = os.path.join(root, file)
			print fn
			# Use "with" so the file will automatically be closed
			with open(fn, "r") as fobj:
				text = fobj.read()
			
			output = re.findall(r'rn\(\"(.*?)\"\)', text)
					

			# Join the matches together
			out_str = "\n".join(output)
			
            # Write them to a file, again using "with" so the file will be closed.
			with open("intern.txt", "a") as outp:
				outp.write(out_str)
                
#remove the duplicates				
uniqlines = set(open('intern.txt').readlines())	
open('intern-labels-sorted.txt', 'w').writelines(set(uniqlines))
