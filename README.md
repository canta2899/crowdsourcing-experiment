# A Crowd Sourcing experiment 

This project was part of the final assignement of the course "Social Computing" held by [Stefano Mizzaro](https://users.dimi.uniud.it/~stefano.mizzaro/) and [Michael Soprano](https://michaelsoprano.com/) at the [University of Udine](https://www.uniud.it/it). The aim of the project was builing and deploying a Crowdsourcing task using [Crowd-Frame](https://github.com/Miccighel/Crowd_Frame).

It was developed together with [Francesco Bombassei De Bona](https://github.com/FraBomba6) and [Alessandro Zanatta](https://github.com/AlessandroZanatta).

## Crowd-Frame

Crowd-Frame is a framework under development whose primary aim is providing a simple and effective way for requestors to build and deploy [Crowdsourcing](https://en.wikipedia.org/wiki/Crowdsourcing) tasks. Requestors are provided with different options in order to build specific HITs and different strategies that allow automated quality controls over workers' interactions with their respective tasks. 

You can find more informations about Crowd Frame and how it works on its GitHub page. 

## Our work

Our work included building and deploying a Crowdsourcing task in which workers had to express their opinions on different editions of different books, previously chosen. 

### Building

First, we built a **questionnaire** including the following questions: 

- *How old are you?*
- *What's your actual job?*
- *What's your favourite literary genre?*
- *Do you own any eBook reader?*
- *What's the importance of reading in your daily life?* 
- *How many books do you read on average every year?*

Then, we chose the following dimensions for our Human Intelligence Tasks:

- *Did you read this book?*
- *Would you quickly browse this book by looking at its cover?*
- *Would you buy this edition?*
- *Do you find the price appropriate?*
- *Tell us how appropriate it seems to you*
- *Which are your thoughts about this edition by looking at the cover?*  

In order to do that, we used the apposite **HITs builder** (that exports newly created HITs as Json data) and **Generator**.

We also decided to substitute English language with Italian, because we knew workers would have been Italian and we wanted to avoid any linguistic bias.

We introduced, then, minor front-end modifications in order to let the design suit our HITs structure better, while also being **responsive**. 

### Deploying

In order to deploy our task we wrote several scripts to make the whole process a **breeze**. 
In fact, tasks are deployed as static content on an [Amazon S3 Bucket](https://aws.amazon.com/it/s3/) and the data retrieved is progressively registered on another private bucket by the main "deploy" one through HTTP requests. 

With our scripts, the requestor is able to push it's newly created tasks to the deploy bucket and to retrieve HITs data from the private bucket. 

When a certain task is ready, the requestor is able to contact workers by e-mailing them with a custom invitation containing a specific access link and an input token (which identifies the HIT assigned to the worker). However, this implementation wouldn't be needed if workers were redirected to their respective task from platforms such as Amazon Mturk. 

### Analysis 

We were able to obtain 54 different completions of our task and we, later on, analyzed the data we obtained. Particularly, we observed the distribution of the different answers and we looked out for some correlations between them. 

Our full work can be found and read on the second report we drafted.

## Repository structure

The actual repository structure is the following: 

- `framework` (folder that contains the whole framework cloned from Crowd-Frame's repository)
- `pyAnalysis` (folder that contains all our data analysis work)
- `pyDistribution` (folder that contains all the scripts needed for the deploying process)
- `report` (folder that contains the two report we drafted, in Italian)

Moreover, if you want to replicate our work, you'll have to fill the following files with your AWS IAM credentials:

- `framework/data/build/environments/environment.prod.ts`
- `framework/data/build/environments/environments.ts`

and fill with your IAM credentials (again) and e-mail credentials (in order to send custom invitations):

- `pyDistribution/credentials.py` 

You'll find demos of these files in their respective path of the repository but, if you somehow intend to fork our work, we highly suggest you to put them in `.gitignore` before pushing in order to avoid publishing sensitive data.

**DO NOT use your AWS root credentials here, keep them safe in your home directory in the .aws folder**.

## Reports

As requested, we compiled two reports: one for the first half of the assignment (building and deploying a Crowdsourcing task) and the other one for the data-analysis part. Both the reports have been drafted in Italian and can be found inside the `report` directory. 

## Conclusions

We've been pretty satisfied with the result we obtained and we found the project absolutely challenging. However, if you're interested in the way we developed the task, we highly suggest you to visit [Crowd-Frame](https://github.com/Miccighel/Crowd_Frame)'s main repository since it is under constant development. 
