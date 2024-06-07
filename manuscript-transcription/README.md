# Digital Camerarius: Moving on Transkribus
## Project Documentation 

Original project page: https://github.com/Furman-Editions-In-Progress/camerarius/tree/master    

As of 2024, the project will transition on the Transkribus app (transkribus.org).   
Useful tutorials and instructions are on the Youtube channel of Transkribus: https://www.youtube.com/@transkribus/videos.   

Our transcription guidelines will be updated as we continue.  

Complete scan of the Book: https://www.digitale-sammlungen.de/en/details/bsb10575861 

## Preliminary transcription guidelines

* Unclear elements should be marked with the "unclear" tag. A question may be typed in the "question" attribute. 
* All abbreviations and symbols must be resolved using the Transkribus "abbr" tag.
* Citations will often contain abbreviated versions of authors names and work titles. These should be resolved as much as it is reasonable. Further research may reveal the correct way to resolve these citations.
* Words in a different language than Latin need to be marked with the "language" tag on Transkribus and the language needs to be specified in the "language" attribute. This will often be Ancient Greek. You may also use the Wikidata identifier Q35497 (click on Wikidata ID and type "Ancient Greek" in the search window). 

## How to review past transcriptions: 
The past transcriptions use the cts urns to identify pages and page areas. In order to figure out where the transcriptions come from, go to the 

A CTS URN identifies the edition according to author, edition year, volume and page number. The last two couples of digits identify, for example, 01 = volume 1, 00002 = page 2. You can see all the pages with these numbers at https://github.com/Furman-Editions-In-Progress/camerarius/tree/master under "vol1_thumbs.md" etc.  

To see the scan of the page:   
* Go to [Camerarius Text]([url](https://docs.google.com/spreadsheets/d/1xPo3x3bcssHrFTWXTcw08dGe3xXxa9OCOQytn5ICS5Q/edit?usp=sharing)), which contains the transcriptions. The first column of the sheet contains a traditional citation identifier, e.g. 1.2.0
* Go to [Text to Image]([url](https://docs.google.com/spreadsheets/d/11vJuQE7_oPDrIlFYzqoBMRlDuichan3eDXxsXenBP24/edit?usp=sharing)) and look up the specific citation of the text you want. For example, 1.2.0 will be urn:cite2:fufolio:camerarius1668.2020a:01_00004@0.1614,0.1368,0.7652,0.08598. In this string, **01 is the volume number** and **00004 is the page number**
* In order to find that volume and page, you can either go to the [thumbnails]([url](https://github.com/Furman-Editions-In-Progress/camerarius/blob/master/vol1_thumbs.md)) of Volume 1 and look up page 00004, or go to https://www.homermultitext.org/ict2/index.html?urn=urn:cite2:fufolio:camerarius1668.2020a:01_00002 and **replace the volume number (01) and the page number (00004)** with the ones of your URN. You should be able to see the page that was transcribed.


