# CSC394_Capstone_Project
Group project for my capstone course in computer science bachelors degree. This app was designed to assist masters students 
in planning the shortest viable path to graduation. The student could change their entry term, degree, undergrad degree, maximum 
courses permitted in a single term, and preference for concentrations. The search would then create a plan of course selections 
that met all prerequisites along the way and would verify that all requirements for graduation were met. It was served up through
a website our group put together.

I was personally responsible for implementing the search functionality. I wrote search.py, filterOptions.py, the curriculums, plan.py
and part of user.py

This represents the backend of the project without the database. The database included all of the course info available from 
DePaul University. Each score was given a score based on two criteria. 

The first was based on rarity. We looked at the most recent eight terms, and counted the number of times a given course was offered. 
We only counted one instance of a course per term. To obtain a positive score we took (8-count). This score was later scaled up to 
match our other heuristic values. This was accomplished by multiplying by six. 

Our second value was unlocks. We looked at each course and observed any prerequisites required to take this course. Each time a 
course was listed as a prerequisite we gave that prerequisite course a point. We used a recursive function to search through each 
courses prerequisite tree and return values for each course.

We combined these two values (unlocks and rarity) to be used as a base heuristic for selecting courses. The thinking being that
a student should take courses that made it easier to take additional courses, and they should seize any opportunities to take
rare classes when they were available.

Later on we added additional heuristic weight to courses that fit within certain categories (Introduction, Foundation, Advanced,
Major Electives, Open Electives, Capstone, or Specific Focus Courses). The combination of all of these scores allowed us to successfully
search through the course catalog and create plans that lead to graduation. We utilized an A* algorithm to accomplish this task.The 
result was a quick efficient search.
