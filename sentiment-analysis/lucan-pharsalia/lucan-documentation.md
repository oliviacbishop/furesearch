## Lucan, _Pharsalia_
Curator: Alexis Spainhour 

### Important resources in this folder: 
* Text in XML format, from IUNO: https://www.iuno.us/lucan/7/
* Annotations export in CSV
* Spreadsheet with the work-in-progress annotations: https://docs.google.com/spreadsheets/d/1CtGGyx3NrtUD32-uaF3yHCXjKgBdR86xaRvQ9EHDJsY/edit?usp=sharing 

### Other useful resources: 
* Translation of the _Pharsalia_ is available at the Perseus Digital Library: https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0134
* Alternative translation of the _Pharsalia_ (this is the one that we are currently using): https://www.poetryintranslation.com/PITBR/Latin/PharsaliaVIImaster.php
* Lemmas and dictionary feature are also available on IUNO: https://www.iuno.us/lucan/7/

### Documentation for Sentiment Analysis on Lucan, _Pharsalia_
This section is intended to document any areas of ambiguity, issues, and final decisions made on specific complicated cases. Make sure to add the relevant references to the sentence (e.g. verse number and sentence number) and to quote the text in question.  

Violence is documented through a **violence score** of 0-2: 
* 0 - no violence present in the sentence.
* 1 - there is violent language being used in a descriptive manner.
* 2 - there is active violence occurring within the sentence. This classification might be adjusted as needed as I implement it further.

The purpose of the **violence score** is to connect the presence of violence to the sentiment recorded for the sentence. 

#### Color code on the spreadsheet
* Blue rows: sentences with lines in between them that were ommitted. This signifies that more context might be needed to accurately identify the sentiment of the sentence.
* Red rows: these sentences contain violence. This is being done away with as the sentences are given a violence score
* Yellow rows: sentences that need to be revisited. 
