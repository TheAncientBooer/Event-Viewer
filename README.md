# Event-Viewer
App for viewing and adding events to a map

## Project Overview
The webpage will show a zoom-able map with pins that represent event locations. You will be able to select current time or a date range for any given location to display events in the chosen region. Events will be posted by users who must have an account. Some events may be pulled and posted from an API such as concerts. Pins that represent events will be clickable to view more details and to click an up-vote to show interest. The top 10 most voted events will be displayed based on the current view of the map. Users who post events will gain points based on up-votes for the events they post. Top 10 users will also be displayed based on the current map view. Examples of events that users will post are concerts, garage sales, fires, criminal activity, community events...etc.

## Functionality
- Zoom-able map with pins representing user posted event.
- Users can create posts representing an event
- Date time range filter
- Ability to share events on other social media platforms

## Data Model

#### Event
  - event_name
  - description
  - location
  - date_time_start
  - date_time_end
  - event_votes
  - posted_by

#### User
  - user_name
  - user_votes
  - number_of_posts
  - user_posts


## Schedule

- Week 1 - Create models and user functions
  - [ ] Create models
  - [ ] Superusers and user account creation
  - [ ] User page for creating event posts 

- Week 2 - Build main page with zoom-able map
  - [ ] Research and apply how to display a map
  - [ ] Use map to create events using lat/long 
  - [ ] Up-vote 
  - [ ] Make date filter for map (Current/date/date range)

- Week 3 - Finish week two tasks and work on styling
  - [ ] Center map and apply styling for header/footer
  - [ ] Display top ten users 
  - [ ] Display top ten posts 

- Week 4 - Scramble to fix any issues that remain and add features that will not break the app. Apply APIs to generate events if there's time. 


- Week 5 and beyond!
  - User authentication to make sure user isn't a bot
  - Continue to improve the styling
  - Add additional features such as adding media to events
  - Create a ToS
  - Implement a reporting feature for posts that violate the ToS
  - Assign users as moderators 
