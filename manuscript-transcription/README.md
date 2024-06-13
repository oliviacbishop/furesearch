# Digital Camerarius: Moving on Transkribus
## Project Documentation 

Original project page: https://github.com/Furman-Editions-In-Progress/camerarius/tree/master    

As of 2024, the project will transition on the Transkribus app (transkribus.org).   
Useful tutorials and instructions are on the Youtube channel of Transkribus: https://www.youtube.com/@transkribus/videos.   

Our transcription guidelines will be updated as we continue.  

Complete scan of the Book: https://www.digitale-sammlungen.de/en/details/bsb10575861 

## Preliminary transcription guidelines

* Page numbers do not need to be transcribed
* Any typos should be fixed in the transcription and do not need to be tagged.
* Unclear elements should be marked with the "unclear" tag. A question may be typed in the "question" attribute. 
* All abbreviations and shorthand must be resolved using the Transkribus "abbr" tag. The resolved abbreviation should be typed inside the "expansion" field. 

   <img width="389" alt="image" src="https://github.com/ChiaraPalladino/furesearch/assets/15249889/1edb0c1f-d012-4a8d-bb90-c719ec967cef">
* All Greek symbols should be fully resolved in the transcription and do not need to be tagged.

* Citations are any reference to an outside author or work. For example, Aristotle lib.IV.cap.I. As of now, both citations and quotations are tagged as Quotations, however that may be subject to change later on.
* Citations will often contain abbreviated versions of authors names and work titles. These should be resolved as much as it is reasonable. Further research may reveal the correct way to resolve these citations.
* Quotations will contain any direct quotes and should be tagged as Quotations.
* Words in a different language than Latin need to be marked with the "language" tag on Transkribus and the language needs to be specified in the "language" attribute. This will often be Ancient Greek. You may also use the Wikidata identifier Q35497 (click on Wikidata ID and type "Ancient Greek" in the search window).

## Transkribus shortcuts and info:
To divide a region or line:
* click on region/line of interest
* press and hold V (vertical) or H (horizontal)
* use slider to make your split

To move a region or line:
* click on region/line
* press and hold shift
* use slider to move up, down, expand, or minimize

Three dots in top right corner shows extra keyboard shortcuts

"Jobs" button shows progress on an automatic transcription

The hamburger on the right is the "Layout" button. This allows you to change the order of lines in your transcription. 

## Observations about Transkribus:
It sometimes randomly deletes tags I've created 

## How to review past transcriptions: 
The past transcriptions use the cts urns to identify pages and page areas. In order to figure out where the transcriptions come from, go to the 

A CTS URN identifies the edition according to author, edition year, volume and page number. The last two couples of digits identify, for example, 01 = volume 1, 00002 = page 2. You can see all the pages with these numbers at https://github.com/Furman-Editions-In-Progress/camerarius/tree/master under "vol1_thumbs.md" etc.  

To see the scan of the page:   
* Go to Camerarius Text (https://docs.google.com/spreadsheets/d/1xPo3x3bcssHrFTWXTcw08dGe3xXxa9OCOQytn5ICS5Q/edit?usp=sharing), which contains the transcriptions. The first column of the sheet contains a traditional citation identifier, e.g. 1.2.0
* Go to Text to Image (https://docs.google.com/spreadsheets/d/11vJuQE7_oPDrIlFYzqoBMRlDuichan3eDXxsXenBP24/edit?usp=sharing) and look up the specific citation of the text you want. For example, 1.2.0 will be urn:cite2:fufolio:camerarius1668.2020a:01_00004@0.1614,0.1368,0.7652,0.08598. In this string, **01 is the volume number** and **00004 is the page number**
* In order to find that volume and page, you can either go to the [thumbnails]([url](https://github.com/Furman-Editions-In-Progress/camerarius/blob/master/vol1_thumbs.md)) of Volume 1 and look up page 00004, or go to https://www.homermultitext.org/ict2/index.html?urn=urn:cite2:fufolio:camerarius1668.2020a:01_00002 and **replace the volume number (01) and the page number (00004)** with the ones of your URN. You should be able to see the page that was transcribed.

## Text Recognition Models:
Noscemus GM 6
* Trained on Antiqua-based print so still has occasional difficulties recognizing hand-written print
* Recognizes Greek shorthand: long sigma, -ος ending
* Recognizes Latin shorthand: et symbol, shorthand for atque (atq)
  
## Greek manuscript shorthand guide:

του

![image](https://github.com/ChiaraPalladino/furesearch/assets/170905706/4b054e7e-676c-470a-9600-a563d8b8ab42)

-ου

![image](https://github.com/ChiaraPalladino/furesearch/assets/170905706/cd43673d-2a11-4f0a-8f9e-1ffc724becc9)

ει

![image](https://github.com/ChiaraPalladino/furesearch/assets/170905706/3a14ddd3-5726-4df5-a29e-5b422d3d8646)

θ

![image](https://github.com/ChiaraPalladino/furesearch/assets/170905706/09fe24d9-8c3b-4f6b-9d01-6900a2afcd3a)

φ

![image](https://github.com/ChiaraPalladino/furesearch/assets/170905706/d3fb1d76-53fe-45b6-9108-cf6378434732)

-ος

![image](https://github.com/ChiaraPalladino/furesearch/assets/170905706/960f8233-eb27-4b1a-bae4-ea3184da4b82)




