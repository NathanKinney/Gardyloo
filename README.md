#Gardyloo
I want to create a project that does not involve content creation.  The more I thought about it the more I realized I'd spend
more time developing content to fill my app than actually demonstrating a technical base.  My initial idea, in my opinion, did not
use enough of the material in the course to really help me solidify my basic knowledge 

##Project Overview
I want to use sentiment analytics to attempt to find trends in stock market news and the preceding effects on the change 
in price.  LUXURY: Also another use would be to analyze speeches or any other text to determine its emotional associations content
relating to a positive negative or neutral scoring. Implement synonym suggestions to help create more textually cohesive text.
- IBM Watson Tone Analyzer API
- Qemotion (Text to emotion API)
- AYLIEN API bv
- PreCeive API
- MoodPatrol API
- along with other i'm waiting on getting a key issued for
 
##Functionality
This app would be limited to stocks listed on the NYSE.  The Intrino api has constant updating of current prices down to
millisecond level of bids along with asking prices.  I would only really track closing day prices for graphical or correlation purposes.
Once the initial text involving a stock is analtyized is when the graphical display would begin.  This initial point would be the baseline
price.  The current trend of the stock will be initially ignored, I would have to consider how to apply the current correlation of trajectory
to the intial baseline.  Seems like a bit of trial and error but maybe not likely to be a priority in a 3 week window.

LUXURY: Take text (or maybe even just a url link) input by the user and dissect it's content and key associations.
This would allow the user to determine the underlying tone and sentiment of the passage and see if that was the wanted intent of the passage.
Or for checking news sources it can help determine bias and other associations by relating Proper nouns with associated words which holds a sentiment score.


##Data Model
I'll potentially have to break this into multiple segments so a few separate models based on content
Allow the user to save scores and compare edited versions of text.
The main DB portion would be creating and appending to the graphical representation.  
                    
##Schedule
(6-26 to 7-27)
PHASE 1 (7-2 to 7-9)
- I want to really design the backend of this app to create a solid footing for all of my other implementations.
- Set up minimal layout for the front end
- potentially want to set it up as a SPA (maybe not once I add a second function of my app)
- Initial feature development will revolve around integrating a stock price tracking api along with a sentiment analysis api.
- set up and test api's usage in a controlled environment.
PHASE 2 (7-10 to 7-17)
- Implement Dom manipulation ideally with vue.
- Iron out which potential features and interactivity that seem relevant and viable.
- start to css
PHASE 3 (7-17 to 7-27) - luxury items
- maybe implement an api that continually pulls random articles from news sources and analyses them and displays them on the home page
- implement the nlp portion for essays or what ever text the user may have.


