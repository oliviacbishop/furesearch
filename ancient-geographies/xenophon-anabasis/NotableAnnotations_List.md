# Specific Notable Annotations 
An aggregate for notes that were made during the annotation process. Serves as a resource for better understanding this project's annotation process, and for understanding certain edge-cases. Annotations posted here have been resolved to at the very least a functional extent, while most are fully resolved.

## Book 1:
* (1.2.8) “Great King”: 
> Likely refers to Artaxerxes II. Similar to other instances of "King", where they are capitalized in the Brownson translation but not in other English translations and not in Scaife's Greek (μεγάλου βασιλέως), but this is the first instance of "Great King". Keeping this consistent with how "King" is treated, it is not annotated.
>
> Same instance shows up again in 1.7.13, 1.7.14.
* (1.2.10) “Lycaean festival”:
> Fringe case that was originally difficult to link and annotate. The Greek here is Λύκαια, which the LSJ identifies as the Lycaea, a festival celebrating Zeus Lycaea. A .event tag does not seem appropriate, as that is more for one-time occurrences, whereas this is a reoccurring festival. Since the English translates this as the "Lycaean festival", collective.ethnic tags were also intially considered since this could imply the festival is a cultural for the Lycaeons, or people who inhabit Lycaonia in Anatolia, but by that same logic a .person or .mythological tag could also be valid to show the festival's relation to Zeus Lycaea, and there is not suitable tag to show it's relation to Mt. Lycaion. Ultimately, all of those options are some degree of misleading and not fully accurate, so therefore a simple .miscellaneous tag was decided to be best. Due to this, it has not been classified as a location in Recogito, despite a reference to Lycaonia and/or Mt. Lycaion.
>
> The Wikipedia and Wikidata page for the Lycaea refers to the festival in Arcadia specifically. However, since it is specifically tied to Mt. Lykaion, which there are evidently multiple in the Ancient Greek world, and seeing as the article does include a reference to this very section of Xenophon, it is linked.
* (1.2.12) “Cilican queen”:
> The Greek uses just “Κίλισσα” (“a Cilician,” same as referring to any other person of the ethnic group) to refer to her, but to better capture how the English translation uses “Cilician queen” to communicate that this specifically refers to Epyaxa, this was annotated as a person and tagged as Epyaxa.person (similar to instances of “the Persian” or “the Greek” referring to specific people, which is seen throughout the text), then nested an annotation of “Cilician” inside of it tagged person.ethnic. This is consistent with annotations for other similar annotations, though this one felt unique enough to make a note on it.
> 
> This same entity also shows up in 1.2.14, 1.2.16, 1,2,18, and 1.2.20.
* (1.2.13) “so-called spring of Midas”:
> Refers to a stream of water that Midas used to water down wine to catch Silenus. As far as I can tell, this is referenced literally nowhere else, there is definitely no georeference point I can find.
* (1.2.13) “the satyr”:
> It is not typical to annotate entities that are not capitalized, but this one is weird because it’s not capitalized in Brownson's English, but is in Scaife's Greek (τὸν Σάτυρον). Additionally, it refers to a very specific entity: Silenus. Given that, it has been annotated, but this may be subject to change down the line.
* 1.4.4 “the Gates between Syria and Cilica”
> This area refers to the Belen Pass, but I’m uncertain as to whether I should annotate the whole string or just “Gates.” “Gates” itself isn’t unambiguous (I confused this area for the Cilician Gates on my first pass months ago) and it isn’t capitalized in Greek, yet it is capitalized in English, and annotating just “Gates” is way more condensed, and this is the only set of gates mentioned in the text, so it is unambiguous within the Anabasis. Given this, I went ahead and just annotated “Gates”
* 1.6.7 “altar of Artemis”
> Originally annotated this as just “Artemis,” but on a second look this might actually be the specific Temple of Artemis at Sardis. Currently only Artemis is annotated as a person, but it may be more accurate to go back and annotate the whole string as a location.
>
> 
## Book 2: 
 * (2.1.3) "the ruler of Teuthrania" and "the
Laconian"
> Both are epithets
> Explanation (Chiara Palladino):  " ὁ Τευθρανίας is an article nom. sg. + placename at the genitive. βασιλεύς (ruler) is implied in this case. So, "king of Teuthrania" is a correct translation. I have indicated this in the comment to the annotation."
* 2.2.8 "Greek"
> This accidentally got deleted off the document comments, but this refers to "the Greek officers" and Dr. Palladino asked if we in the modern day know of them:

> It seems that in this usage, officers is a catch-all term for at least the generals and possibly the captains as well. The Greek generals at this point in the book---who are actually mentioned in this book---are: Proxenus the Boeotian, Sophaentus the Stymphalian, Socrates of Achaea, Clearchus, Cheirisophus, and Menon of Thessaly (at this point he hasn't betrayed the Ten Thousand yet and is still Greek), and all of these are known from Book 1 too, where who they command are listed out. Sosis the Syracusan is also said to command 300 hoplites, but he's only mentioned once in the whole text and never brought up again, so it's unclear if he died, deserted, or what. Also, these are not counting Pythagoras of Sparta and Tamos the Egyptian, who commanded trireme fleets (thus probably wouldn't be on land with everybody?), but it's also not clear where they are. Finally, it's unclear if this is a list of all the generals, and this doesn't count the hundreds of different captains who might be considered 'officers,' of whom only a few (like Xanthicles) are named. So, that's all to say, you floated the idea of maybe annotating this differently, but that's all the information I could find, so I defer to you. Right now, I'll keep it as collective.ethnic.
* (2.3.18) "Men of Greece" (check Greek on this, it might be necessary to annotate whole string if it's all one word in Greek):
> The Greek uses "ἄνδρες Ἕλληνες" so the translation "Men of Greece" doesn't as clearly capture that it's an adjective ethnic identifier in the original text. Given that "Greek men" is just as reasonable a translation, but "Men" isn't necessary to clarify the "Greek" at all, I annotated just "Greece" as collective.ethnic.
* (2.4.13) "Sittace":
> In reviewing how exactly I tag cities Xenophon mentioned (whether to distinguish between city_large vs city vs city_small, etc.) I looked at the Greek which just uses polis and then some adjectives, but no special word for city (πόλις ἦν μεγάλη καὶ πολυάνθρωπος), so given that 'large' and 'populous' are not inherent in the word choice, I will just use a 'city' tag here and for future instances, and the only other one that will be distinguished is 'city_abandoned'.
* (2.4.15) "Menon's friend":
> Not clearly resolved yet; the Greek for this sentence is "Μένωνα δὲ οὐκ ἐζήτει, καὶ ταῦτα παρʼ Ἀριαίου ὢν τοῦ Μένωνος ξένου," so both Menon and Ariaeus are mentioned as proper nouns in the phrase, so my guess would be to keep them annotated/tagged as separate individuals?.
* (2.4.26) "the Persian":
> From meeting notes: _"The Persian" in 2.4.26 annotate it as if it said something like "Tissaphernes \[\...\] the Persian" but referred to "the Persian" in isolation later, so annotate "the Persian" as a place in Recogito, then tag it person.ethnic_. So essentially we're treating it as if it said "Tissaphernes the Persian" all connected. I was also going to put in the Tissaphernes' authoritative name tag for this instance so that we know.
> 
> I actually misremembered part of this instance: It's not Tissaphernes, but Cyrus and Artaxerxes' unnamed half-brother. In this case, should I give it any other identifying tag beyond just person.ethnic?

## Book 3: 
* (3.1.5) "Athenian government":
> Correct to annotate it as collective.organization, just don't nest another place annotation of 'Athenian' inside it.
* (3.1.26) "who spoke in the Boeotian dialect":
> Mostly one word in Greek (βοιωτιάζων), and obviously meant to identify him, though a slightly odd way of doing it. Right now, we'll annotate "Boeotian" as a .language \[need to review if we'll do language.ethnic?\] because saying "..who spoke Boeotian" would also make sense, and we'd know it'd be a language
* (3.1.45) "...heard that you were an Athenian":
> This one is a weird instance since it's a quote and thus 'you' and 'Athenian' are both in accusative and 2nd person, so I cannot tell if it would be considered an epithet or not for certain. I went ahead and, while 'Xenophon' is in the vocative and 'Athenian' is accusative, Athenian is obviously in reference to Xenophon, so I annotated it as if it was "Xenophon the Athenian"
* (3.2.37) "since he is a Lacedaemonian" \[almost certainly collective.ethnic\]
> I made it person.ethnic because in the Greek both Cheirisophus and Lacedaemonian are nominative singular masculine, so even though they're divided by a couple words I think it should be the same as an epithet (ie. Cheirisophus the Lacedaemonian)
* (3.3.2) "'Men of Greece'" should maybe be the whole string \[See notes on 2.3.18\]
> The Greek uses "ἄνδρες Ἕλληνες" so the translation "Men of Greece" doesn't as clearly capture that it's an adjective ethnic identifier in the original text. Given that "Greek men" is just as reasonable a translation, I annotated it as collective.ethnic
> See also 3.5.5.
* (3.3.20) "Lycius, the son of Polystartus": Another weird nesting instance (like with Glus) and "an Athenian" immediately after, since it's an identifier

## Book 4:
* (4.1.2) “Carduchian mountains”:
> “Carduchian mountains” must be annotated with one string and tagged as Corduene
* (4.2.28) “by a Cretan named Stratocles”
> There was a similar note in Book 2 about referring to Tissaphernes as “the Persian” I think? Might have to be annotated differently
> Intitally seen as an epithet like 2.4.26, but after checking the Greek it does not use Cretan as an epithet, so it is annotated as person.ethnic
* (4.5.34) “Persian-speaking”:
> Annotated this as a language; felt similar to dealing with the ‘he who spoke Boeotian” (3.1.26) earlier

## Book 5: 
* Neon the Asinaean (5.3.4); I am unsure which Pleiades entry I should correspond “the Asinaean” to. The options are either Asine (Messenia) (pleiades:570125), which is a city on the Messenian Gulf, or Asinaeus (pleiades:570123) which corresponds to the Asinaean Gulf itself (alt. way to refer to the Messenian Gulf, derived from the city itself. 
> It’s ambiguous whether Xenophon intends to indicate that Neon is from the city Asine itself, or just from the region that happens to borrow its name
> Erring on the side of being more general than specific, I am selecting the latter, and will be linking the Messenian Gulf page (though tagging it as Asinaean Gulf)
* (5.3.5) “treasury of the Athenians at Delphi” this is a long annotation, but it refers directly to a specific building that is logged in Pleiades, so I am going to annotate the whole string (though not nest anything in it) as a place
* (5.3.6) “Asia”; there is a question of what he meant by Asia, and then consequently how to tag it in Pleiades.
> I’ve chosen to associate this annotation with Asia Minor, as Xenophon is jumping forward in time beyond the Anabasis to, referencing is participation in the campaign of Agesilaus II in Ephesus, in order to tie up a loose end about his votive offering.
> This means that, for Wikipedia linkage, I am linking this to Anatolia (as the page for Asia Minor redirects here)
* (5.4.15) Metropolis: There is a city of the Mossynoecians referred to as the proper noun “Metropolis” twice, and is a city the Ten Thousand visit. It is capitalized in Scaife’s Greek as well, but my first impression is that this is a nickname, shorthand, or pure invention by Xenophon. Pleiades does not have a Metropolis that appears to be anywhere near where they should be, and likewise there is no wikipedia info, and ToposText does not even have a link in it
> This will have to be better researched. I believe the Mossynoeciens are another ambiguous ethnic group, and this may be another Chalybes/Chaldians problem. Hopefully there will be some decent scholarship on this
> For now I have left it unlocated, unlinked, and flagged it as ambiguous

## Book 6: 
* (6.2.1) Jason’s Cape: There is a reference to the cape where the Argo is said to have come to anchor. Xenophon recounts seeing it as they sail west from Sinope to Heracleia. It is not Cape Jason near Ordu, as that is east of Sinope, so the location of this cape is ambiguous. 
* (6.2.2) Acherusian Chersonese: This is an ambiguous location right near Heracleia Pontica, where Heracles is said to have descended after Cerberus. There is no specific lake, swamp, or cavern nearby that I could conflate with this point. Similarly, there is no specific Wikipedia article that talks about this spot in particular, though it is mentioned and cited in the article on Acherusia
> The decision is to locate it at Heracleia (as a sort of proxy for it being in/near the city) and link the Acherusia article, and finally make a comment on the annotation itself.
* (6.4.1) Thrace-in-Asia: Xenophon names the region between the Bosphorus and Heracleia as Thrace-in-Asia. This area would traditionally be northwestern Bythinia, and Xenophon is, at a quick search, the only one who seems to name this place as Thrace-in-Asia. As such, I am unsure of how to proceed in locating or linking this place (the article for Eastern Thrace just deals with the part of Turkey that is in Europe).
> Likely what I will do is flag it as unlocatable/ambiguous, put a comment on it, and then manually map it in ArcGIS later, depending on how the methodology for region mapping evolves
* (6.4.2): Bythinian Thracians: In a similar vein to the note above, Xenophon names an ethnic group specifically as the Bythinian Thracians. This group does seem to be what the Wikipedia article on the Bythini refers to, though it does face the same challenges of locating and Pleiades ID-ing as Thrace-in-Asia does.
> I am half tempted to identify it with Bithynia et Pontus just for the location and regional polygon. However, that is wildly anachronistic, so I will not actually be doing that; it would serve as a somewhat decent representation on a map though
> I am going to tag this as Bythini, flag it as unlocatable, and make a comment
> This is a piece of evidence for any interested scholars that, at least for Xenophon, conceptions of Thrace were not quite as set in stone, and there was some interesting mingling and assimilation happening between the different ethnic groups in Bithynia.
* (eg. 6.2.13, 6.4.18, 6.6.13): Cleandor, the Lacadaemonian governor of Byzantium: This one is a weird one, because in the original Greek for the two examples given here Cleandor is never defined with being of Lacedaemonian, just as the governor of Byzantium. This seems like the translator added this himself. This means I am uncertain whether or not to annotate this as person.ethnic, collective.ethnic, or annotate it at all, as the translator is putting this in himself. This also applies in one instance to Anaxibius.
> I think it would be unwise to leave this entirely unannotated. Given that we are explicitly working in English for this phase of the project, I think that the methodology and desire to have as useful data as possible dictates I annotate this as person.ethnic. The reason for this is, even though it may be misleading when compared to other “person.ethnic”s that do actually show up in the Greek, is that the translator is specifically using the language structure as a personal ethnic identifier. When/if I go through and re-annotate this whole text in the original Greek, it is natural that some annotations would be different given the different language structure. This example, then, is one one could point to as evidence of the “art of translation”, and a point of comparison for studies that compare various translations of the Anabasis.
* (6.5.7) Spithridates and Rhathines: ToposText may have another erroneous ID here for Spithridates, but this one I’m less sure about. Xenophon notes two Persians, Spithridates and Rhathines, that were sent by Pharnabazus against the Ten Thousand
> Spithridates in ToposText is identified with the Persian satrap that ruled from 365-334 BCE. Very little is recorded about this Spithridates, including his age or birth date, but it seems to me like a lengthy stretch of time for it necessarily to be the same one. His most noteworthy deeds are in relation to his battle against Alexander the Great.
>      At the same time, the way Xenophon mentions Spithridates and Rhathines with little fanfare could suggest that, at the time of writing it 30 years later, these people were well known enough that he did not feel he had to clarify. This would be possible if Spithridates was young, potentially very young, at the time his events are recounted in the Anabasis, and he then went on to become satrap decades later, about five years after Xenophon is writing. Their Greek names are also spelled the same (Σπιθριδάτης).
> 
> Rhathines is a trickier character, as he does not seem to be mentioned outside of the Anabasis at all, and has as equally little fanfare as Spithridates.
>      He could potentially be Spithridates brother Rhosaces, who is recorded by Diodorus of Sicily and Arrian of Nicomedia along with Spithridates in regards to their conflict with Alexander the Great. However, their names in Greek are different (Ῥωσάκης vs  Ῥαθίνης). While it is possible Xenophon misspelled the name so atrociously different, it is extremely tenuous logic and unlikely, and so I would not commit to that identification. 
> I will be flagging both of these people as ambiguous, with note on the matter, and will refrain from linking them for now.
>
> **UPDATE**: After discussing this in a meeting, there is enough evidence with how Xenophon mentions Spithridates in the text to make a connection with the Spithridates mentioned by Diodorus. Similarly, Rhathines, while a bit more ambiguous due to the different spellings, can be connected to Rhoesaces mentioned by Diodorus and Arrian. Both Diodorus and Arrian already spell Rhoesaces differently (Ῥωσάκην and Ῥοισάκης respectively), so it's not unprecedented for Xenophon, writing at least a couple centuries before either of these, to spell the name differently. Additionally, it there is Wikidata used for Rhathines (under the name Ratines), though it is only used in one article written in Catalan. It may be beneficial to merge the Wikidata for Rhoesaces and Ratines, and update the English page to reflect this.
* (6.6.34) “twin gods”: This is not capitalized as an epithet, and while I would take it to mean Artemis and Apollo, the Greek does not seem to employ it as an epithet either, and I cannot find where the ‘twin’ is supposed to come from in Greek.
* (6.6.38) Chalcedonia: Xenophon refers to Chalcedonia as a region, undoubtedly associated with Chalcedon the city, and defines Chrysopolis as a city within the region. There is no Pleiades or Wikidata ID for Chalcedonia, only Chalcedon, leaving me uncertain how exactly to annotate this.
> The Greek is Καλχηδονίας which seems to me do be identifying Chrysopolis as relating to Chalcedon, not necessarily that Chalcedonia is it’s own region. With this interpretation, I will annotate Chalcedonia as if it was the city Chalcedon (ie. tag it as ‘referenced’)

## Book 7:
* (7.1.14) Hieron Oros:
* > Evidently this is a mountain range on the east coast of Thrace, north of Gallipoli, around where Mount Koru and Mount Işıklar is (an likely encompassing them both). However, while Pleiades and DARE both have ID’s , those are in the west-central Peloponnese. Therefore, there is a question of whether it is worth it to link the Pleiades ID or not.

> For now it will be, along with adding a comment in the annotation, flagging this as ambiguous, and moving it manually when mapping.
> It is also worth mentioning that ToposText locates this place differently than Pleiades and DARE, and consistent with the location discussed here.

> An additional note, it is questionable whether or not to link a Wikipedia page to this. The page for Hieron Oros links to a town near Trapezus, and this is not correct. There is an English article for Mount Ganos (corresponding to Mount Işıkla, but Xenophon’s “Hieron Oros” seems to encompass both  Mount Işıklar and Mount Koru (the latter of which does not have an English Wikipedia page).
* (7.1.24) Thracian Square: According to Xenophon, one of the locations within Byzantium was an area called the Thracian Square. Interesting, but there does not appear to be any more precise, modern geo-referencing data to connect this with a more precise location beyond Byzantium as a whole.
* (7.1.27) Europe:
> Similar to the annotation for Asia, I do not want the Wikipedia link for Europe to be misleading for a Classical conception. I am tempted to link the section on geography and namesakes in the Europa (consort of Zeus) article.
That section outlines how Europe was used by Strabo to refer to the area of Thrace below the Balkan Mountains, which is where Pleiades places the location of Europe as too. 

> After a meeting to discuss this, this annotation is low-stakes since it is a concept referenced in brief passing by Xenophon, and anyone reading this text is not likely to be unaware of Europe as a concept. 'Europe' to the Ancient Greeks existed as a quasi-located geographic concept as a continent, existing in opposition to the concepts of Africa/Libya and Asia. Basically it was, "the landmass that's not Africa or Asia", or perhaps more accurately "Africa and Asia are the continents that are not Europe". Due to this, Pleiades ID may be a bit too restrictive, as it specifically references Thracian Europe. While this concept is also used by Xenophon (connected "Europe" and "Thracians" in 7.6.32 and 7.8.25), it is unclear if this instance also refers to a Thracian Europe, as it is discussing Athens decline in dominance against Lacedaemonia at this time.
* (7.1.32) Delta… of Thrace:
> Later in the text, the Delta it said to be north of Byzantium (7.5.1), but beyond that there is little indication of what delta in this region this is supposed to correspond to, and therefore no clear Pleiades or Wikipedia IDs to use.
* (7.2.32) Xenophon references the Melanditae, a tribe of Thracians that do not seem to have a Pleiades ID anywhere
> Same for the Tranispae, mentioned in the same section
* (7.2.32) Odrysians:
> I feel confident in annotating this as collective.organization rather than ethnic, but it is a little ambiguous on whether Xenophon is referring to the kingdom or an ethnic
* (7.2.36, 7.3.10) Cyzicene:
> This refers to a Cyzicene stater, a type of currency. Previously when Cyzicene staters were mentioned, I annotated it as collective.ethnic because “stater” always followed “Cyzicene”, so therefore it was a stater from Cyzicene. Now though, it seems more appropriate to tag this as .miscellaneous.
* (7.6.11) Heaven: The translator translates Δία as Heaven. I am annotating this as an epithet of Zeus.
* (7.6.39) “twin gods”: This is not capitalized as an epithet, and while I would take it to mean Artemis and Apollo, the Greek does not seem to employ it as an epithet either, and I cannot find where the ‘twin’ is supposed to come from in Greek.
* (7.8.15) Comania:
> Xenophon references a mercenary general named Itamenes, in service to likely Artaxerxes II, who comes from Comania. 
> I cannot find anything on Pleiades or Wikipedia or elsewhere for what Comania is. It is obviously a location, likely a region, based on how Xenophon refers to it. It is also probably Middle Eastern and/or Indo-European, as Itamenes also brings Assyrians and Hyrcanians with him
> The closest I could find is this, a nomadic tribal confederation from the 11th-13th centuries, but this is wildly anachronistic: https://en.wikipedia.org/wiki/Cumania. It may serve as evidence that some form of 'Comania' was a name for an ethnic group, which then lended its name to the region in antiquity, or vise versa.
* (7.8.18) Carcasus river: Xenophon says his soldiers retreated across the Carcasus after failing to siege Itamenes, which is unlocatable
* (7.8.25) Hesperites: A mysterious ethnic group that Xenophon does not elaborate on and are not mentioned until the very end, where he says he encountered them
> Theorized by Paradeisopoulos to be the Saspeires, but this is not mentioned by Xenophon himself. Therefore, they will remain unliked as this is an interpretive element on top of what can be readily gleaned, and also they don’t have a Pleiades ID
* (7.8.25) Coetians: A mysterious ethnic group Xenophon is said to have encountered, but are never mentioned in the text until this point.
> Same with the Tibarenians

