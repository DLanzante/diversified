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
   cd diversified

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
   A). As a person with autism, I want to be able to submit and post certain things that I am passionate about others learning about, this is to educate others but also to spread awareness and a safe space for others with neuro-divergent conditions.

2. User Story:
   B). As a neuro-divergent individual I want to be able to view the communities posts and communities posts that I am interested in

3. User Story:
   C). As a neuro-divergent individual I want to be able to comment on other posts so that I can share/spread my experiences and relate to others.
   
4. User Story:
   D). As a site administrator, I want to be able to remove posts that are harmful or violate community guidelines so that the community is safe and compliant with our safety policies.

5. User Story:
   E). As a site user, I want to be able to post, comment, edit, and like/dislike certain content posted by others and myself, this is to help facilitate the expansion of the app as well as help others get a fell as to what they personally like/want to see of their feed!

#### Acceptance-Criteria

1. Acceptance Criteria for A):
   - Content Sumbission: The user must be able to submit posts or articles that are centered around neurodiversity, autism awareness, and similar topics.
   - Content Categorization: There should be an option to categorize the content (e.g., "Autism Awareness", "Neurodivergence", "Educational", etc.) to ensure proper sorting and visibility.
   - Accessibility Feature: There should be a place for you to access your own private pages and comments
   - Content Moderation: The user should be able to filter the content they want to specifically see
   
2. Acceptance Criteria for B):
   - A directory of communities is available.
   - Communities are required to have a summary mission statement that promote discoverability
   - Communities have a feedback / rating system to show community health.
   - Engagement is tracked per community and reported as part of the community directory summary page.
   - Accessibility is scored and reported on the community summary page.
   - Accessibility is scored and reported on the community summary page.

3. Acceptance Ctriteria for C):
   - Content Moderation: The user must be allowed to write and submit comments on other users' content
   - Text input field: There must be a clear box that users can submit their entries
   - Character handling: There must be a maximum character limit to ensure clarity and ease of communication
   - Error handling: This system should display clear error messages when data has been impropery handled
   - Customizable Interface: Users should have the option to customize the visual appearance of the comment section (e.g., adjusting contrast, font size) to suit their needs.

4. Acceptance Criteria for D):
   - Post Removal Access: The site administrator must have the ability to view and access all posts across the platform. As well as deletion and other modification of posts.
   - Confirmation Prompt: A confirmation prompt should appear when attempting to delete a post to prevent accidental removal (e.g., "Are you sure you want to delete this post?").
   - Access Control: Only users with the appropriate administrative privileges should be able to remove posts.
   - Feedback to the Community: If posts are removed due to violation, there should be a way for the community to see that moderation is happening (e.g., a "Post Removed" message, or visible "Moderated" tag).

5. Acceptance Criteria for E):
   - Content Creation: Users must be able to create and submit posts with text, images, or other media (e.g., video, links).
   - Post Visibility: Users should be able to control the visibility of their posts (e.g., public, friends only).
   - Delete/Edit Comments: Users should be able to edit or delete their own comments after submission.
   - Like/Dislike Buttons: Users must be able to like or dislike posts and comments.
   - Feed Relevance: The app should display content in the user’s feed based on their likes/dislikes and engagement history.
   - Notifications: Users should receive notifications when someone comments on or likes their posts, or when their content is interacted with in a meaningful way.

#### Mis-User Stories

1. Mis-User Story for A):
   - As a person with autism, I want to be able to post content, but the process and interactions are too difficult or inaccessible, and I face overwhelming negative feedback that discourages me from sharing my ideas and feelings.
   - As a person with autism, I want to be able to submit and post things about my passions, but the platform’s interface is overwhelming with too many distractions, making it difficult to focus on creating meaningful content.
   - As a person with autism, I want to be able to post about autism and neuro-divergent issues, but the platform does not have a mechanism to ensure that my posts are not subject to harmful or stigmatizing comments.
   - As a person with autism, I want to share my posts to spread awareness, but the platform does not offer any feedback or recognition, making it hard to know if my post is having an impact.

2. Mis-User Story for B):
   - As a neuro-divergent individual, I want to engage with posts in communities I’m interested in, but the content is difficult to access, the discussions are not inclusive, and I feel isolated and unsafe when sharing my thoughts.
   - As a neuro-divergent individual, I want to view community posts, but the platform is flooded with irrelevant or off-topic content, making it difficult for me to focus on what matters to me.
   - As a neuro-divergent individual, I want to view community posts, but the posts are filled with jargon or complex language, making it hard for me to understand the content.
   - As a neuro-divergent individual, I want to view community posts, but the platform doesn’t offer any customization options for adjusting the visual presentation, making it harder for me to focus on the content.
   - As a neuro-divergent individual, I want to view community posts, but there is no way to filter posts based on my specific interests or needs, and I end up wasting time searching.

3. Mis-User Story for C):
   - As a malicious user I want to be able to post badly about other people so that mis-information is being spread.
   - 

5. Mis-User Story for D):
   As an admin I want to be able to have full power to take out other people's posts and accounts without the approval from other admins.

6. Mis-User Story for E):
        

#### Mitigating Criteria

Requirmenets you put in a system to prevent mis-user stories

1. Mitigation for A):
   - Content is reviewed automatically by a harmful content detection system that allows to search for any unwanted characters.
   - There will be no character limit on posts that have accounts that are verified.
   - Users will sign a policy of acknowledgement before posting and creating an account
   - Give users the option to post anonymously or use a pseudonym to reduce the fear of negative feedback and protect their identity.
   - Implement a clean, distraction-free design, with a focus on content creation. Offer a "focus mode" where only essential elements are visible.
   - Provide users with simple, clear feedback on how their posts are performing, including likes, shares, comments, and views. Avoid overwhelming metrics but give users insight into the impact of their posts.

2. Mitigation for B):
   - Content Categorization: Implement categories, tags, or topics for each post, allowing users to filter content based on their interests (e.g., "Autism Awareness," "Neurodivergent Experiences").
   - User-Set Preferences: Allow users to specify content preferences (e.g., only show posts about autism, mental health, or neurodiversity).
   - Content Moderation System: Implement both automated and manual moderation to flag and remove harmful or stigmatizing comments (e.g., profanity filters, AI-based harmful language detection).
   - Impact Notifications: Provide notifications that summarize the impact of posts, such as "Your post has been shared X times" or "Your post has reached X number of people."
   - Clear Timestamping and Visual Cues: Display timestamps for posts and comments, along with visual cues to indicate the most recent replies.

3. Mitigation for C): As an admin I need to be able to put forth clear moderating guidelines as well as admin oversights such as allowing for peer revisioning as well as allowing for multiple admins needing to be present and to sing off on any deletions or any post modifications/ account modifications. Admins must follow automated checks as well as escalation procedures!

5. Mitigation for D): For proper site administrating I am going to have to be providing data anonymoty and provacy, data processing, real-time data and finally secure API access.

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
