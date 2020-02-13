# ElectionTracker

This is a Candian Election Tracker made to amass tweets from the following political groups, politicians and political news outlets: @liberal_party, @JustinTrudeau, @NDP, @theJagmeetSingh, @CanadianGreens, @ElizabethMay, @CPC_HQ, @AndrewScheer, @peoplespca, @MaximeBernier, @CBCPolitics (total 11 users).

The goal of this project is to amass tweets from these politicians and political groups, allow users to log in to their personal account, and "vote" for the political group of their choice.

This webapp is made using a Vue.js frontend, and Firebase backend.

#### TODO
- Create authentication service using Firebase
- Create a polling system for authenticated users to vote for who they thing is the best candidate
- Allow users to see the amount of votes for each group

### In Progress
- Figure out order of the tweets displaying improperly (ID issue)

### Completed
- Tweets are now being streamed
- Displaying tweets through Vue.js
- Style main page