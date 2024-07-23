# Digital Camerarius: Moving on Transkribus
## Project Documentation 

Original project page: https://github.com/Furman-Editions-In-Progress/camerarius/tree/master    

As of 2024, the project will transition on the Transkribus app (transkribus.org).   
Useful tutorials and instructions are on the Youtube channel of Transkribus: https://www.youtube.com/@transkribus/videos.   

Our transcription guidelines will be updated as we continue.  

Complete scan of the Book: https://www.digitale-sammlungen.de/en/details/bsb10575861 


## Preliminary transcription guidelines

* Page numbers do not need to be transcribed.
* The Roman numeral entry numbers at the top of the page do not need to be transcribed.
* Any typos should be fixed in the transcription and do not need to be tagged.
* Unclear elements should be marked with the "unclear" tag. A question may be typed in the "question" attribute. 
* All Greek symbols should be fully resolved in the transcription and do not need to be tagged.
* There is no need to capitalize the second letter at the top of each page. Transcribe the word as it is.
  
  ![image](https://github.com/user-attachments/assets/0920f055-9320-4959-be80-5726886a9d39)

  In this example, 'UT' should be transcribed as 'Ut'.


## Tagging guidelines

* All abbreviations and shorthand must be resolved using the Transkribus "abbr" tag. The fully expanded word should be typed inside the "expansion" field.
* Names should be tagged using the "person" tag.
* A Citation is any reference to an outside author or work. For example, Aristotle lib. IV. cap. I.
* Citations will often contain abbreviated versions of authors names and work titles. These should be resolved as much as it is reasonable in the citation tag. Further research may reveal the correct way to resolve these citations.
* Quotations will contain any direct quotes and should be tagged as Quotations. 
* The Quotation tag has space for information about the author of the quote. Instead using the Person tag for a reference, just use the Quotation tag.
* Words in a different language than Latin need to be marked with the "language" tag on Transkribus and the language needs to be specified in the "language" attribute. This will often be Ancient Greek. You may also use the Wikidata identifier Q35497 (click on Wikidata ID and type "Ancient Greek" in the search window).
  

## Tutorial for researching quotations/words
First look up the author of the quotation in either library (scaife or philogic)
* Scaife: https://scaife.perseus.org/search/?q=neredum&kind=form&format=instances&p=1
* Philogic: https://artflsrv03.uchicago.edu/philologic4/Greek/ 

Using Scaife, 
* Searching for the author will pull up their bibliography
* Sometimes the spelling doesnt match the citation
* Usually the longer the quotation the more accurate the spelling

Using Philogic,
* You have to search by the lemma
* It will pull up a bunch of options to choose from

Look up word in Logeion to see if Camerarius made a spelling error or if he's just using another form of the word
https://logeion.uchicago.edu/%CE%BB%CE%BF%CE%B3%CE%B5%E1%BF%96%CE%BF%CE%BD 

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
* solution: make sure you click somewhere else on your transcription so the software registers it as a "change" before you save and exit.

Transkribus has a number of keyboard shortcuts to be used in transcriptions. The problem with this is that some of the shortcuts only require you to press a certain letter on your keyboard (ie. pressing W allows you to zoom out) which has proven to be an issue when I am trying to fix mistakes or put info into tags that use that letter. 

It is VERY reliant on how good your wifi/cell service is. 

Be sure to save as you work. If you wait till you are done with a document, the software will freak out and won't save your work. I usually click save every 5-10 changes just to be safe. 

## How to review past transcriptions: 
The past transcriptions use the cts urns to identify pages and page areas. In order to figure out where the transcriptions come from, go to the 

A CTS URN identifies the edition according to author, edition year, volume and page number. The last two couples of digits identify, for example, 01 = volume 1, 00002 = page 2. You can see all the pages with these numbers at https://github.com/Furman-Editions-In-Progress/camerarius/tree/master under "vol1_thumbs.md" etc.  

To see the scan of the page:   
* Go to Camerarius Text (https://docs.google.com/spreadsheets/d/1xPo3x3bcssHrFTWXTcw08dGe3xXxa9OCOQytn5ICS5Q/edit?usp=sharing), which contains the transcriptions. The first column of the sheet contains a traditional citation identifier, e.g. 1.2.0
* Go to Text to Image (https://docs.google.com/spreadsheets/d/11vJuQE7_oPDrIlFYzqoBMRlDuichan3eDXxsXenBP24/edit?usp=sharing) and look up the specific citation of the text you want. For example, 1.2.0 will be urn:cite2:fufolio:camerarius1668.2020a:01_00004@0.1614,0.1368,0.7652,0.08598. In this string, **01 is the volume number** and **00004 is the page number**
* In order to find that volume and page, you can either go to the [thumbnails]([url](https://github.com/Furman-Editions-In-Progress/camerarius/blob/master/vol1_thumbs.md)) of Volume 1 and look up page 00004, or go to https://www.homermultitext.org/ict2/index.html?urn=urn:cite2:fufolio:camerarius1668.2020a:01_00002 and **replace the volume number (01) and the page number (00004)** with the ones of your URN. You should be able to see the page that was transcribed.

## Text Recognition Models:
In order to generate a transcription using an AI text recognition model, you can go about it two ways.

1. For one page:
* Open the page you want to transcribe and click on the "Start automatic transcription" button
* This will bring you to a page that lists all available public models to use. For the Camerarius project, we are using the Noscemus GM 6 model.
* Click on the text model and click "Start Recognition" in the top right corner

2. For multiple pages:
* Check the box in the bottom left corner of each page you want transcribed
  
![image](https://github.com/user-attachments/assets/d07dc0f0-b288-4ff0-a902-0652e5454bf7)
* Then click the "[T] Recognize" button. This will bring you to the text recognition model page
* Select AI model and start recognition. 

Information on Noscemus GM 6:
* Trained on Antiqua-based print 
* Recognizes Greek shorthand: -ος ending
* Recognizes Latin shorthand: et symbol, shorthand for atque (atq), long 's'
* Seems to have the most issues recognizing accents (eg. putting an accent where it isn't, leaving out accents, or putting in the wrong accents)
* Has problems mixing up lower-case 'e' with 'a' or 'o'
  
## Greek manuscript shorthand guide:

του

![image](https://github.com/ChiaraPalladino/furesearch/assets/170905706/4b054e7e-676c-470a-9600-a563d8b8ab42)

-ου

![image](https://github.com/ChiaraPalladino/furesearch/assets/170905706/cd43673d-2a11-4f0a-8f9e-1ffc724becc9)

-ου

![image](https://github.com/user-attachments/assets/86fe4429-26de-42b2-87af-efaaf79615f2)


ει

![image](https://github.com/ChiaraPalladino/furesearch/assets/170905706/3a14ddd3-5726-4df5-a29e-5b422d3d8646)

ἐν

![image](https://github.com/user-attachments/assets/b38f4dc9-87da-4bac-bccf-1b0b4681f9ed)


θ

![image](https://github.com/ChiaraPalladino/furesearch/assets/170905706/09fe24d9-8c3b-4f6b-9d01-6900a2afcd3a)

φ

![image](https://github.com/ChiaraPalladino/furesearch/assets/170905706/d3fb1d76-53fe-45b6-9108-cf6378434732)

-ος

![image](https://github.com/ChiaraPalladino/furesearch/assets/170905706/960f8233-eb27-4b1a-bae4-ea3184da4b82)


## Latin manuscript shorthand guide:

et

![image](https://github.com/user-attachments/assets/4ce533cc-1d2f-435c-871c-c9f126398309)

s (in this example, the word would be transcribed as 'sit')

![image](https://github.com/user-attachments/assets/e57a52cc-9ca4-44ad-ab11-848f67afa581)

ae (in this example, the word would be transcribed as 'Quae')

![image](https://github.com/user-attachments/assets/c91a025e-546a-426d-b189-b40912e4f27e)


