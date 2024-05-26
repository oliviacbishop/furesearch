# Annotation Guidelines and Tagset - For texts in English

This short document contains the essential tagset and definition for annotating entities in English translations of Ancient texts. It is designed to ensure alignment of annotations performed in different versions of the same document. 

When annotating things in Recogito, **first-level tags** should be used first. **second-level tags** are optional, and should be used only after a first-level tag. Project-specific tags should be used either all before, or all after these tags. 

In this document, names are referred to as **named entities**, such as "Julius Caesar" or "Athens". 
**Mentions** of entities may be the ways in which those things are talked about in a text, such as "Emperor Caesar" or "the city of the Athenians".   

Typically, for places we georeference them to gazetteers, which will provide the authoritative form of the name. For personal names, however, we annotate the mention and add a tag with the authoritative form of the name, because we don't have a gazetteer we can reference to:   

<img width="589" alt="image" src="https://github.com/ChiaraPalladino/furesearch/assets/15249889/f71b8c55-05bf-4ca1-a606-0d23543e885f">   




## General principles
1. A named entity contains, by definition, at least one capitalized word. Lower-case mentions of entities, such as "the king", should not be annotated.
2. Wherever possible, we try not to annotate articles.
3. In general, we try to avoid nested annotations, unless they respond to precise research questions. 

## First level tags

**person**: Any identifiable single individual, including deities and anthropomorphic mythological figures. If the name appears with an epithet of ethnic, they should be annotated together. Examples: "Ajax", "Ajax Telamonius", "Thucydides the Athenian", etc.  

  Available second-level tags: **.epithet, .ethnic, .mythological, .astronomy, .author, .ancestry**    

**location**: A word or multiple words used to identify a politically, culturally, and/or geographically defined location, including geo-political, physical, fictional spaces and structures like temples, buildings, houses, and monuments. Examples: "Athens", "city of Athens", "city of the Athenians", "temple of Apollo", etc.   

Available second-level tags: **.epithet, .ethnic, .mythological, .astronomy**   

**collective**: A named group of people or other entities (creatures, animals, etc.) with shared identifiable characteristics on social, political, national, family, or ethnic basis. Examples: "Athenians", "Cyclopes", "Senate", "Muses", etc.   

Available second-level tags: **.epithet, .ethnic, .animal, .mythological, .astronomy, .organization, .ancestry**.   

**creature**: Mythical or real precisely identifiable non-human, non-anthropomorphic creatures. Examples: ‘Bucephalus’, ‘Chimaera’.

Available second-level tags: **.animal, .mythological, .astronomy**   
  
**event**: significant named events identified by a string with a precise boundary. Examples: "Peloponnesian War", "Battle of Naupactus", etc.   

**time**: Any absolute date or time expression. Examples: ‘23rd Olympiad’, ‘1985’, ‘Consulate of Cicero’.   

**language**: languages clearly identified as such. Examples: "Latin", "English".   

**object**: Individual artifacts identified with a name, such as ships, weapons, statues, columns, dedications, etc. Example: "Argos" (the ship of the Argonauts, not the person or the city).   

**work**: titles of literary or non-literary works, in any form. Examples: "Odyssey", "Oedipus Rex".   

**miscellaneous**: anything that does not have a specific primary-level tag.   

## Second-level tags

**epithet**: An epithet used to refer unambiguously to one individual, including nicknames, titles, and appellatives. Example: "Oileus", "Far-Shooting". Epithets should be annotated and tagged alone only when they appear in isolation ("Oileus"). If the epithet appears together with a personal name, they should be annotated together and only tagged as **person** ("Ajax Oileus").   

authorized combinations: **person.epithet, collective.epithet, location.epithet**.    

**ethnic**: Ethnonyms and demonyms used to refer unambiguously to one individual or group of individuals by means of their association with a geographically identifiable territory. Examples: "Athenians" (collective.ethnic), "the Athenian" (person.ethnic). This tag should only be used when the ethnonym appears in isolation. If the ethnonym appears together with a personal name, e.g. "Thucydides the Athenian", they should be annotated together and only tagged as **person**.   

authorized combinations: **person.ethnic, collective.ethnic, place.ethnic**    

The tag **ethnic** may also be accompanied by georeferencing in platforms like Recogito. It can be tagged as "place" on the platform, and referenced to the appropriate gazetteer entry, so that even place information is available in the data. 

<img width="527" alt="image" src="https://github.com/ChiaraPalladino/furesearch/assets/15249889/43f375ba-eecb-4f42-9023-d734a57f3e43">     

  
**animal**: authorized combinations: **creature.animal, collective.animal**   

**mythological**: Any creature or collective that belongs to the larger realm of myth and religion, including gods and deities. Examples: “Tartaros” (location.mythological), “Hercules” (person.mythological).   

authorized combinations: **creature.mythological, person.mythological, location.mythological, collective.mythological**  

**organization**: Groups of people identified by precise organizational structures, such as priesthoods, legions, religious groups, and so on.   

authorized combinations: **collective.organization**   

**astronomy**: Named stars, groups of stars, constellations, and planets. Example: ‘Pleiades’.  

authorized combinations: **creature.astronomy, collective.astronomy, person.astronomy, location.astronomy**  

**author**: A person clearly mentioned in relation to works they have authored.  

authorized combinations: **person.author**   

**ancestry**: A name that refers unambiguously to one individual or group of individuals by using a family name, patronymic, matronymic, or other indication of ancestry. Examples: ‘Atreid’, ‘Tarquinii’. 
Note: This tag should only be used when the ancestry appears in isolation. If the ancestry appears together with a name, e.g. ‘Achilles Pelides’, they should be annotated together and labeled as **person**.  

authorized combinations: **person.ancestry, collective.ancestry**    

# Specification on Boundaries: When a Named Entity appears with lowercase words

By definition, a Named Entity is something that can be named. In cases where a capitalized name occurs with lowercase words, it can be tricky to establish the boundaries of what exactly constitutes a Named Entity.   
In order to establish the boundaries of what constitutes a Named Entity in a text, try answering the following questions:   
* **What entity is actually being talked about?** If the lowercase word is necessary to appropriately label the entity the text refers to, then it should be included. Example: in the string “temple of Zeus”, the entity is not the person Zeus, but the place “temple of Zeus”. On the contrary, in “river Nile”, only “Nile” is to be annotated because the word “river” is not necessary to identify it.   
* **Can the annotated string be associated with a precise named entity?** Example: the “sister of Augustus” is Octavia the Younger, so it can be annotated as a string and tagged person.    

**What can be classified as multi-word entity:**  
* “city of the Athenians” is a place. “Athenians” alone is an ethnic, but the entity the text talks about is a place, which can be associated with the name “Athens”. Therefore, the entire string “city of the Athenians” is tagged as place.  
* “Black Sea” is a full string referring to a place. “Black” alone does not mean anything, and the entity the text talks about can be associated with a specific record in gazetteers.  
* “upper Egypt” is a place, as it refers to a precisely identifiable area that has a specific name (often all capitalized: Upper Egypt, vs. Lower Egypt).  

**What cannot be classified as a multi-word entity:**   
* “Mediterranean sea”: the word “sea” in this string does not further identify the entity “Mediterranean”, nor does it change its label. Therefore, only “Mediterranean” should be tagged as place.  
* “Iberian coast”: the Iberian coast is not a clearly identifiable place with its own name, and it cannot be associated to a precise identity record. Therefore, only “Iberian” should be tagged as place and associated with “Iberia”.  
* “Region of Carthage”: this is not a clearly identifiable place that can be named. Therefore, only “Carthage” should be annotated.   










 

