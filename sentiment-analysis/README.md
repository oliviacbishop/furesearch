# Sentiment Analysis for Ancient Greek and Latin

This repository contains highly curated datasets for the training and fine-tuning of Sentiment Analysis models on Ancient Greek and Latin.  

The creation of the datasets and the guidelines followed are illustrated here: .

The datasets have been created in the course of several Research Fellowships, sponsored by the Furman Undergraduate Research fund. 

## Facts and Figures

Each sentiment analysis dataset in the repository contains the following values: 
* Citation: the line number, paragraph, or other text unit. 
* Text unit: a unique number identifying individual text units.
* Text: a transcription of the text unit.
* Sentiment class: the identified sentiment class, according to the four values "Negative", "Positive", "Neutral", and "Mixed".
* Translation: a translation of the text unit.
* Relevant Lexicon: lemmatized words that have been used to identify the sentiment class.
* Comments: documentation on specific choices. 

Note that Aristophanes and Lucan also include a "Fun Score" and a "Violence Score", respectively. 

## Ancient Greek

The ancient Greek repository contains the following annotated datasets: 

* Aristophanes, _Clouds_ : 142 text units; 1501 lines of poetry; 
* Aristophanes, _Wasps_: 142 text units; 1537 lines of poetry; 

<img src="https://github.com/ChiaraPalladino/furesearch/blob/4585ef84fcd6dec1a737e8b2e313e77ea858fe26/sentiment-analysis/aristophanes/aristophanes-counts.png" width=30% height=30%>   

Some insights about these files, generated through Claude 3.7 Sonnet: 

<img src="https://github.com/ChiaraPalladino/furesearch/blob/main/sentiment-analysis/aristophanes/claude_sentiment_distribution_grc.png">   


<img src="https://github.com/ChiaraPalladino/furesearch/blob/main/sentiment-analysis/aristophanes/claude_average_funscore_grc.png">   


<img src="https://github.com/ChiaraPalladino/furesearch/blob/main/sentiment-analysis/aristophanes/claude_funscore_distribution_grc.png">   



## Latin 

The Latin repository contains the following annotated datasets: 

* Fronto, _Letters to Marcus Aurelius_: 6 letters; 32 text units; 
* Lucan, _Pharsalia_: 122 text units; 535 lines of poetry;
* Virgil, _Georgics_: 50 text units; 263 lines of poetry;

Some insights about these files, generated through Claude 3.7 Sonnet: 

<img src="https://github.com/ChiaraPalladino/furesearch/blob/main/sentiment-analysis/claude_corpuscomparison-lat.png">

Sentiment Classes, per text (raw numbers):

<img src="https://github.com/ChiaraPalladino/furesearch/blob/main/sentiment-analysis/claude_saoverview-raw_lat.png" width=70% height=70%>


Sentiment Classes, per text (percentages based on total text chunks per text):

<img src="https://github.com/ChiaraPalladino/furesearch/blob/main/sentiment-analysis/claude_saoverview_lat.png" width=70% height=70%>


Given the particular content, Lucan's _Pharsalia_ was also analyzed from the viewpoint of the violence connected to a sentence. The distribution of the violence score assigned is as follows: 

<img src="https://github.com/ChiaraPalladino/furesearch/blob/main/sentiment-analysis/claude_lucan_violencescore.png" width=70% height=70%>













