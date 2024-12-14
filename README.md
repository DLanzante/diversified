# Diversified Semester Project

## Overview

Hello and good-afternoon, this is my **Neurodivergent Awareness Project called Diversified**!

## Table of Contents

- [Overview](#overview)
- [Project Summary](#Project-Summary)
   - [Installation](#Installation)
   - [Getting Started](#Getting-Started)
- [User Stories](#User-Stories)
   - [Acceptance Criteria](#Acceptance-Criteria)
   - [Mis-User Stories](#Mis-User-Stories)
   - [Mitigating Criteria](#Mitigating-Criteria)
- [Diagrams](#Diagrams)
   - [Mockup](#Mockup)
   - [C4 Diagrams](#C4)
- [Prototype](#Prototype)
- [License](#license)
- [Contact](#contact)
- [Citations](#Citations)

### Project-Summary

This project is dedicated to spreading awareness about neurodivergent conditions, such as **Autism**, **ADHD**, and other related diagnoses. The authors goal is to provide resources, educational content, and a collaborative space to increase understanding and reduce stigma surrounding neurodiversity. This is going to be different then Reddit because with this web app it is gpong to be developed and made for those who are neurodiverse!

This project has several core objectives:

- **Raise Awareness**: Share information and raise awareness about neurodivergent conditions such as Autism, ADHD, and others.
- **Encourage Understanding**: Foster empathy and reduce misconceptions surrounding neurodivergence.
- **Provide Resources**: Curate educational materials, tools, and support networks for neurodivergent individuals
- **Create a Collaborative Community**: Offer a space for contributors to share resources, experiences, and ideas.

#### Installation
We are going to be going over some of the most basic instructions of how to install all necessary repositories as well as how to get the api started and how to get started using my Diversified API!
1. Clone the repository   
   ```bash
   git clone https://gtihub.com/DLanzante/Diversified

2. Change the Directory
   ```bash
   cd diversify

#### Getting-Started
1. After this we can finally do our docker command to stand the app up to be able to use docker!
    ```bash
    docker compose up --build
    docker-compose run django bash
    python manage.py migrate
    python manage.py makemigrations
    python manage.py createsuperuser
    docker-compose up

### User-Stories

1. User Story:
   A). As a person with autism, I want to be able to submit and post certain things that I am passionate about others learning about so that I can not only educate others but also to spread awareness and a safe space for others with neuro-divergent conditions.

2. User Story:
   B). As a neuro-divergent individual I want to be able to view the communities posts that I am interested in so that I may be able to comment and share/spread my expereinces as well
   
3. User Story:
   C). As a site administrator, I want to be able to not only have the right to take on and off posts that are harmful and cross the community guidelines as well as ensure that others aren't abusing policy!

4. User Story:
   D. As an Administrator I want to be able to pull all comments and provide statistics to interested buyers so that they can see how many people view the site as well as what they are doing while on the site to better provide a solid starting point for possibly a futher development of the web api

5. User Story:
   E). As a site user, I want to be able to post, comment, edit, and like/dislike certain content posted by others and myself.

#### Acceptance-Criteria

1. Acceptance Criteria for A):
   Content Submission - The user must be able to submit posts or articles that are centered around neurodiversity, autism awareness, and similar topics. There should be an option to categorize the content (e.g., "Autism Awareness", "Neurodivergence", "Educational", etc.) to ensure proper sorting and visibility. There should also be sections for Accessibility Features and Content Moderation.
   
2. Acceptance Criteria for B): The user of my API should be able to have access to community directories and discover relevant material that they want to view daily. This is also going to be including a community feedback and customization feature along with post engagement, post visibility/accessability and real-time interactions!

3. Acceptance Ctriteria for C): As an admin i want to be able to have the right to moderate content, moderate notifications and to keep a record of all actions, monitor any abuse of power, admins taking actions on other admins, and finally how to escalate certain actionary items.

4. Acceptance Criteria for D): This system must allow for site Admins to retrieve all comments from the webiste as well as all posts. This is also not limited to viewing statistics, data reporting, custom filters, user privacy and anonymoty, and lastly real-time data.

#### Mis-User Stories

1. Mis-User Story for A):
   As a person with autism, I want to be able to post content, but the process and interactions are too difficult or inaccessible, and I face overwhelming negative feedback that discourages me from sharing my ideas and feelings.

2. Mis-User Story for B): As a neuro-divergent individual, I want to engage with posts in communities I’m interested in, but the content is difficult to access, the discussions are not inclusive, and I feel isolated and unsafe when sharing my thoughts.

3. Mis-User Story for C): As a malicious user i want to be able to post bad about other people and make sure that this information is not spread and make sure that neuro-divergent individuals don't get the proper chances they deserve.

4. Mis-User Story for D): As an admin I want to be able to have full power to take out other people's posts and accounts without the approval from other admins.

5. Mis-User Story for E): As an Administrator, I want to be able to pull all comments and provide raw data directly to interested buyers without any processing or analysis, so they can see everything without any filtering or privacy concerns.     

#### Mitigating Criteria

Requirmenets you put in a system to prevent mis-user stories

1. Mitigation for A): The absolute best mitigating criteria is going to include but is not limited to improved accessibility features, content moderation and anti-bullying training and policy acknowledgment, clear communication and user support, as well as content reviews and a community of empowerment! This site is also going to be including educatuon resources and awareness pages.

2. Mitigation for B): The main mitigations for a user of my API is going to be improvising community discovery through advanced searching functionality as well as enhanced accessibility features such as sharing and support personalization for each individual

3. Mitigation for C): As an admin I need to be able to put forth clear moderating guidelines as well as admin oversights such as allowing for peer revisioning as well as allowing for multiple admins needing to be present and to sing off on any deletions or any post modifications/ account modifications. Admins must follow automated checks as well as escalation procedures!

4. Mitigation for D): For proper site administrating I am going to have to be providing data anonymoty and provacy, data processing, real-time data and finally secure API access.

### Diagrams

#### Mockup

- This is a Mockup to understand what vision I want to pull together for my project!
![Rough Mockup](https://github.com/DLanzante/diversified/blob/main/docs/mockup.PNG)

#### C4

- Context | Container | Component Diagrams

- Context Diagram
![Context Diagram](https://github.com/DLanzante/diversified/blob/main/docs/System%20Context%20Diagram.png)
- Container Diagram
![Container Diagram](https://github.com/DLanzante/diversified/blob/main/docs/Container%20Diagram.png)
- Component Diagram #1
![Component Diagram](https://github.com/DLanzante/diversified/blob/main/docs/Component%20Diagram.png)
- Component Diagram Blow-up #2
![Component Diagram](https://github.com/DLanzante/diversified/blob/main/docs/Component%20Diagram%202.png)
- Component Diagram Final #3
![Component Diagram](https://github.com/DLanzante/diversified/blob/main/docs/Component%203%20API%20Server.png)

<!-- LICENSE -->
### License

Distributed under the MIT License. See `LICENSE.txt` below for more information.

MIT License

Copyright (c) 2024 Dominic Lanzante

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


<!-- CONTACT -->
### Contact

Dominic Lanzante - [@my_instagram](https://www.instagram.com/dlanzante2018/) - dlanzante2018

Dlanzante@unomaha.edu | 402.554.2648 | University of Nebraska Omaha
University of Nebraska Omaha, 6001 Dodge Street, Omaha, NE, 68182

Project Link: [https://github.com/DLanzante/](https://github.com/DLanzante/) - Github Main
