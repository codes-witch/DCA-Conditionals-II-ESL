# DCA-Conditionals-II-ESL
A Distinctive Collexeme Analysis of Conditionals Type II in writings by beginner and advanced English learners

This repository contains the code and some of the data to reproduce the analysis. Access to the EFCamDat corpus can be requested [here](https://ef-lab.mmll.cam.ac.uk/EFCAMDAT.html). To reproduce from the full corpus, include the corpus CSV file in the `input files` folder and run ``Python files/00_Preprocess.py``, which will output the subcorpus analyzed in this study: ``/Python output files/ef_cond.csv``. 

The subcorpus is first parsed using Stanza by running `Python files/01_ParseEssays.py`. Since there are more than 33.000 student writings in the subcorpus, parsing all essays takes a long time. 

After the subcorpus is parsed, the folder `parsed_documents` contains a `.conllu` file per student writing. 
These files are then read and scanned for Type II Conditionals (CII) in the file `Python files/02_IDConditionals`, which generates:
- `Python output files/02_conditionals_ii.csv`
- `Python output files/topic_word_count.json`

Both of these files are input to `R files/Analysis.Rmd`, where the actual analysis is performed. 