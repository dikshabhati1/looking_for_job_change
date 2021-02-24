# looking_for_job_change

## Demo
Link for web application : https://looking-for-job-change.herokuapp.com/

![image](https://user-images.githubusercontent.com/70757239/107154254-ef422600-6997-11eb-9ecf-3ea2ada19de4.png)

![image](https://user-images.githubusercontent.com/70757239/107154389-b6ef1780-6998-11eb-89ab-3a8e33cc4084.png)

![image](https://user-images.githubusercontent.com/70757239/107154401-c79f8d80-6998-11eb-98e7-003d203ee86d.png)


## Overview
This is the flask app which predicts whether a person is looking for a new job or not

## Motivation
A company which is active in Big Data and Data Science wants to hire data scientists among people who successfully pass some courses which conduct by the company. Many people signup for their training. Company wants to know which of these candidates are really wants to work for the company after training or looking for a new employment because it helps to reduce the cost and time as well as the quality of training or planning the courses and categorization of candidates. Information related to demographics, education, experience are in hands from candidates signup and enrollment.

This dataset designed to understand the factors that lead a person to leave current job for HR researches too. By model(s) that uses the current credentials,demographics,experience data you will predict the probability of a candidate to look for a new job or will work for the company, as well as interpreting affected factors on employee decision.

## Data Source
I have used the dataset from kaggle.[Click here](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists) for the dataset

## Features in the Dataset
- city_ development _index : Developement index of the city (scaled)
- gender: Gender of candidate
- relevent_experience: Relevant experience of candidate
- enrolled_university: Type of University course enrolled if any
- education_level: Education level of candidate
- major_discipline :Education major discipline of candidate
- experience: Candidate total experience in years
- company_size: No of employees in current employer's company
- company_type : Type of current employer
- lastnewjob: Difference in years between previous job and current job
- training_hours: training hours completed
- target: 0 – Not looking for job change, 1 – Looking for a job change
