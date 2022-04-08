# Ticket-System

This is a ticket system which I have built for my QA Software Engineering & Agile Assignment.

This is a flask app which has been spun up and deployed to a Heroku Environment. Please see below for details.

To Access the website head to : https://truecroft-qa-web-dev.herokuapp.com/login

User Details are as followed:

Admin Users:
  - Admin User 1
    -  admin@admin.com
    -  test1
  - Admin User 2
    - admin2@admin.com
    - root

Regular Users:
  - Test User 1
    - test1@test.com
    - Test1
  - Test User 2
    - test2@test.com
    - test1
   
  
**Case Study of a Support Help Desk Ticketing System**

**Background**
A Ticketing system for a support team is required so that users can raise issues with a support team and then the tickets can be distributed between the team.

**User Access**
Users must be able to access the system to raise support tickets. This means that an account must be created. During the creation of an account the following information will need to be collected:
-	Email
-	First Name
-	Last Name
-	Password

**Creating Tickets**
Once a user has created an account and logged into the system, they should be able to create a support ticket for the support team. To create a ticket the following information should be collected:
-	Title
-	Description
-	Contact Number
-	Affected Item

**Managing Tickets**
As a user they should be able to view the current progress of their created tickets by viewing tickets based on their status which is set by the support team. They should also be able to view if a ticket has been assigned to an admin and if so, which admin is assigned to their ticket. They should also be able to edit their tickets if they have made a mistake but also can change the status to either Resolved or Closed depending on if the problem has been solved without the intervention of the support team.

**Admin Considerations**
As admins have extra permissions within the system, they should be able to:
-	Create new support tickets
-	Assign created tickets to themselves
-	View all tickets they have assigned to themselves
-	View all tickets created within the system
-	Create New users
-	Edit current users
-	View current Regular users
-	View current Admin users

**Additional Considerations**
All data which is submitted should be validated to ensure that no deformed data can make it inside the database. This would mean things like an email field should only accept strings which follow the pattern of an email, or names cannot include numbers. Success and Failure notifications should be shown to the user throughout the website after they complete an action to inform them whether the action has completed successfully.
