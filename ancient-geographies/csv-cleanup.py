# this script was designed to clean CSV exports from Recogito, extracting the project-specific tags and placing them in ad hoc fields.

import csv # imports the csv module

# define input and output file names
input_file = 'input.csv' # change the filename 
output_file = 'output.csv' # change the output name if desired

# define the new fields to add to the csv file. the names and number of the new fields may vary. "Authority Link" is the vocabulary tag and may or may not be present. 
new_fields = ["Authority Link", "First-level tag", "Second-level tag", "Typology", "Visited or referenced", "Other"]

# open input file in read mode and output file in write mode 
with open(input_file, mode='r', newline='') as infile, \
     open(output_file, mode='w', newline='') as outfile:
    
    reader = csv.DictReader(infile) #create an object reader to read the file as dictionary
    fieldnames = reader.fieldnames 
    
    tags_index = fieldnames.index("TAGS") + 1
    new_fieldnames = fieldnames[:tags_index] + new_fields + fieldnames[tags_index:]
    
    writer = csv. DictWriter(outfile, fieldnames=new_fieldnames)
    writer.writeheader()
    
    # define object lists according to the specific vocabulary of the tags included in each field. firstleveltag and secondleveltag are specified in the annotation guidelines. the other lists are custom and should be changed depending on the project.
    firstleveltag = ["person", "location", "collective", "creature", "astronomy", "event", "time", "language", "object", "work", "miscellaneous"]
    secondleveltag = ["epithet", "ethnic", "author", "ancestry", "mythological", "animal", "organization"]    
    typologytag = ["river", "region", "town", "city", "settlement"]
    visitedorreferencedtag = ["visited", "referenced"]
    
    for row in reader: # for every row in the original csv file 
        rowtags = row["TAGS"].split('|', 5)  # splits the tags contained in the TAGS field taking | as separator, for a max of 5 splits (= 6 tags).
        row["Authority Link"] = rowtags[0].rstrip('.') # places the first tag in tags in the field "Authority Link"
        row["First-level tag"] = next(    # next() function returns the first item that matches the first parameter 
            (x for x in rowtags if x in firstleveltag),   # iterates through rowtags for value x that is included in the list firstleveltag
            None)  # no value returned if the list has no items 
        row["Second-level tag"] = next((x for x in rowtags if x in secondleveltag), None)
        row["Typology"] = next((x for x in rowtags if x in typologytag), None)
        row["Visited or referenced"] = next((x for x in rowtags if x in visitedorreferencedtag), None)
        row["Other"] = "|".join(
            (x for x in rowtags[1:] 
             if x not in  firstleveltag
             and x not in secondleveltag
             and x not in typologytag
             and x not in visitedorreferencedtag))  # places anything that was not included in the previous fields, starting from the second item in the list, in the "other" field joining with a | as separator
        writer.writerow(row)
        
        
print("new file ready!")
