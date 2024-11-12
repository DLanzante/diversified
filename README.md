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
   
3. Using GitHub for Version Control
    ```bash
    git init
    git remote add origin <your-github-repository-url>
    git add .
    git commit -m "Initial commit"
    git push -u origin main

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
   ```bash
   As a person with autism, I want to be able to submit and post certain things that I am passionate about others learning about so that I can not only educate others but also to spread awareness and a safe space for others with neuro-divergent conditions.

2. User Story:
   ```bash
   As a neuro-divergent individual I want to be able to view the communities posts that I am interested in so that I may be able to comment and share/spread my expereinces as well
   
3. User Story:
   ```bash
   As an **Administrator** I want to be able to not only have the right to take on and off posts that are harmful and cross the community guidelines as well as ensure that others aren't abusing policy!

4. User Story:
   ```bash
   As an **Administrator** I want to be able to pull all comments and provide statistics to interested buyers so that they can see how many people view the site as well as what they are doing while on the site to better provide a solid starting point for possibly a futher development of the web api

#### Acceptance-Criteria

Requirements for the user stories to be realized!

#### Mis-User Stories

Malicious user stories

#### Mitigating Criteria

Requirmenets you put in a system to prevent mis-user stories

### Diagrams

#### Mockup

#### C4

[Good Luck]

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
