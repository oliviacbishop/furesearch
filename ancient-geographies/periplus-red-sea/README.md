## Annotation of the Periplus of the Erythraean Sea - Summer Research 2025

Author: Olivia Bishop

Furman University '27

Bachelor of Arts, Classics & English

bishol3@furman.edu
 

### Introduction

The Periplus of the Erythraean Sea, or the Red Sea, is a navigational text describing a sailing route starting on the west side of the sea in Egypt and ending in India around the modern day island of Sri Lanka, written by an anonymous Greek author. The periplus also explores the African coast down to modern day Tanzania and the east coast of the Red Sea, as well as discussing some of the inland areas of India and the surrounding areas. The text was written sometime between the first and third century AD.

The edition used for the _Periplus of the Erythraean Sea_ is the most recent edition by Stefano Belfiore for the _New Jacoby_ (Fr. 2036), which is based substantially on the established critical text by Frisk (1927), with some updates. The digital text is the one published in the online edition of the _New Jacoby_, cleaned, formatted, and inspected for mistakes. All footnotes and apparatus criticus have been removed. 

Additionally, the text has been processed for Named Entity Recognition using the UGARIT NER model for Ancient Greek (https://huggingface.co/UGARIT/grc-ner-bert). The annotations were cleaned and disambiguated manually. 

### Annotating the Text

Recogito, an online platform for annotating texts, was used for this project. As mentioned, before I began my annotations, the text had already been processed and all named entities identifed by the software were automatically tagged. The first part of my research consisted of reading through the translation of the text. I used the Casson (2012) translation and commentary for the majority of this work, though I also used the Shipley translation and commentary from Geographers of the Ancient Greek World Selected Texts in Translation, published by the Cambridge University Press in 2024. While reading through the text, I attemped to geolocate each place mentioned in the text, making sure to also check for places that were not recognized by the software. I used the Pleiades gazzeteer which is programed in Recogito. Some places were easy to find in the gazzeteer, by simply searching their name as it appeared in the Greek text or the English translation. Others I was not able to locate initially, and in second and third looks at the text I was able to find the majority of them using the commentaries mentioned and through discussions with my research mentor, Dr. Chiara Palladino.

Some examples of places that were easy to locate were Greece and India, which correspond to their modern day locations, and the well-known Nile and Euphrates rivers.  Some places required more in depth discussion and research, such as the author's mentions of "Ethiopia and Libya and Africa...", which at first seem simple to locate but became more complicated when I found out that they do not directly correspond with their modern day counterparts.  It seems that the author is referring to general regions of Africa rather than the specific areas of Ethiopia and Libya as we know them today, with "Africa" also being a region inside the modern day continent.  
Other places I was unable to locate and they remained flagged in the dataset.  One example is a place called Akannai.  It is described as a laurel grove and appears to have been located on the most eastern tip of modern day Somalia.  Pleiades did not have an entry for Akannai, and the Casson commentary states that laurels do not grow in Somalia, so it is unclear where this place would have actually been located.


<img width="1055" height="600" alt="Screenshot 2025-07-20 at 8 45 39 PM" src="https://github.com/user-attachments/assets/33888ffb-60ee-4abd-a682-1080e4379455" />

A screenshot showing located and unlocated place entities.


Secondly, I went back through the text and used tags to further annotate the places. An "@ana:#collective" tag was used for the mentions of people groups such as "Indians" or "Greeks". The "place.derivitive" tag was used when the name of a place was used in the context of something coming from that place, such as "Indian cinnabar", or the language of the place itself.

After this, I annotated all of the specific people and events that were mentioned in the text. Using wikidata, I identified people such as Alexander the Great and Menendar I, an Indo-Greek king. The events in the text were the Greek and Egyptian names of months, where most of the time the author was describing the best times to set sail from to certain places.

Next, I was tasked with identifying the geonames present in the text, with an annotation and a "geoname" tag. Geonames include english words such as 'river', 'mountain', 'sea', 'port', 'island', etc. For this part of the project, I used the Perseus Digital Library's Scaife Viewer, which includes the Greek text of the periplus and allowed me to see the translations for every word. I used Scaife throughout the entire project, but in this stage it was the most useful.

For the final part of my research, I annotated and tagged mentions of orientation and distance in the text. There were two types of orientation mentioned in the periplus, one being "relative" which included phrases such as "to the left" or "to the right" and needed further context to understand (to the right of what?). The other was "absolute" which included phrases such as "to the west" or "to the east". All of these instances were identified and tagged with the 'orientation' tag and a further 'relative' or 'absolute' tag. Examples of distance in the text were phrases such as "three thousand stades", stades being a distance measurement that was used at the time. These were tagged with a 'distance' tag.


<img width="1055" height="600" alt="Screenshot 2025-07-20 at 8 41 47 PM" src="https://github.com/user-attachments/assets/b95265a1-927c-4c6f-b08b-38a21c673e4d" />

A screenshot showing the different types of entities coded.

### The Numbers

Throughout my eight weeks of research, I annotated 429 places, 19 people, 15 events, and 458 "uncategorized" entities, according to Recogito's analytics, which would be the geoname, orientation, and distance tags. In total, I annotated 917 entities in the text, and made 638 tags (some entities such as regular place names, specific people, and events did not require tags but only annotations).

### My Thoughts

I really enjoyed my time doing summer research with the Furman Classics department. I find the most valuable thing that I learned was how to annotate a text and use digital tools such as Recogito. I was introduced to many websites and programs that I didn't even know existed like Pleiades and Wikidata. I think the archiving of knowledge is deeply important, and discovering these online platforms that are dedicated to just that was very interesting to see.

As mentioned, during my research, I was unable to identify some places and people because they are very obscure, some only ever being mentioned in this specific text. Some places I was able to find a match in Pleiades, but the gazzeteer has them as unlocated. This was one thing that was frustrating to me. I wish that I had all the answers and could have a clean dataset with no places highlighted in yellow, flagged because I wasn't able to identify them. But, as mentioned, the sources I used that are dedicated to archiving these places and people give me hope that more unknown places and people from history can be identified, and I think that it is incredible that I was able to contribute to this goal in even just a small way. I am glad that there are researchers and academics that care about even the most obscure parts of history, and I have found through this project that I do as well.

I am very grateful to Dr. Palladino and the Furman Classics department for giving me the opportunity to participate in this research and I hope that I am able to conduct similar research again in the future.


<img width="1055" height="600" alt="Screenshot 2025-07-20 at 8 47 19 PM" src="https://github.com/user-attachments/assets/3ddecf18-8137-4540-8015-e47628e9cec9" />

A screenshot showing the completed map of located places.


