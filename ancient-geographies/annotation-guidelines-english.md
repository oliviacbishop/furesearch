# Annotation Guidelines and Tagset - For texts in English

This short document contains the essential tagset and definition for annotating entities in English translations of Ancient texts. It is designed to ensure alignment of annotations performed in different versions of the same document. 

In this document, names are referred to as **named entities**, such as "Julius Caesar" or "Athens". 
**Mentions** of entities may be the ways in which those things are talked about in a text, such as "Emperor Caesar" or "the city of the Athenians". Typically, we annotate mentions and tag them with the entity's name: 

<img width="589" alt="image" src="https://github.com/ChiaraPalladino/furesearch/assets/15249889/f71b8c55-05bf-4ca1-a606-0d23543e885f">

When annotating things in Recogito, **primary-level tags** should be used first. **Secondary-level tags** are optional, and should be used only after a first-level tag. Project-specific tags should be used either all before, or all after these tags. 

## General principles
1. A named entity contains, by definition, at least one capitalized word. Lower-case mentions of entities, such as "the king", should not be annotated.
2. Wherever possible, we try not to annotate articles.
3. In general, we try to avoid nested annotations, unless they respond to precise research questions. 

## Primary level tags

**person**: Any identifiable single individual, including deities and anthropomorphic mythological figures. If the name appears with an epithet of ethnic, they should be annotated together. Examples: "Ajax", "Ajax Telamonius", "Thucydides the Athenian", etc.  

**place**: A word or multiple words used to identify a politically, culturally, and/or geographically defined location, including geo-political, physical, fictional spaces and structures like temples, buildings, houses, and monuments. Examples: "Athens", "city of Athens", "city of the Athenians", "temple of Apollo", etc.   

**group**: A named group of people or other entities (creatures, animals, etc.) with shared identifiable characteristics on social, political, national, family, or ethnic basis. Examples: "Athenians", "Cyclopes", "Senate", "Muses", etc.   

**creature**: Mythical or real precisely identifiable non-human, non-anthropomorphic creatures. Example: "Bucephalus".  

**constellation**: Identifiable stars, groups of stars and planets. Example: "Pleiades".   

**event**: significant named events identified by a string with a precise boundary. Examples: "Peloponnesian War", "Battle of Naupactus", etc.   

**time**: any specific capitalized string identifying time, e.g. months' names, dates, etc. Examples: "Elaphebolion", "23rd Olympiad", etc.  

**language**: languages clearly identified as such. Examples: "Latin", "English".   

**object**: Individual artifacts identified with a name, such as ships, weapons, statues, columns, dedications, etc. Example: "Argos" (the ship of the Argonauts, not the person or the city).   

**work**: titles of literary or non-literary works, in any form. Examples: "Odyssey", "Oedipus Rex".   

**miscellaneous**: anything that does not have a specific primary-level tag.   

## Secondary level tags

**epithet**: An epithet used to refer unambiguously to one individual, including nicknames, titles, and appellatives. Example: "Oileus", "Far-Shooting". Epithets should be annotated and tagged alone only when they appear in isolation ("Oileus"). If the epithet appears together with a personal name, they should be annotated together ("Ajax Oileus").   
authorized combinations: **person.epithet, group.epithet, place.epithet**.    

**ethnic**: Ethnonyms and demonyms used to refer unambiguously to one individual or group of individuals by means of their association with a geographically identifiable territory. Examples: "Athenians" (group.ethnic), "Athenian" (person.ethnic). This tag should only be used when the ethnonym appears in isolation. If the ethnonym appears together with a personal name, e.g. "Thucydides the Athenian", they should be annotated together.   
authorized combinations: **person.ethnic, group.ethnic, place.ethnic**    
  
**animal**: authorized combinations: **creature.animal, group.animal**   

**organization**: Groups of people identified by precise organizational structures, such as priesthoods, legions, religious groups, and so on. authorized combinations: **group.organization**

**author**: A person clearly mentioned in relation to works they have authored. authorized combinations: **person.author**   

**patronymic**: family names used to refer unambiguously to certain individuals. Examples: "the Atreid", "Tarquinii", etc. authorized combinations: **person.patronymic, group.patronymic**   

**deity**: a divine or semidivine creature of any kind. provisionally authorized combinations: **person.deity, creature.deity**



 

