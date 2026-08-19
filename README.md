Simple application that processes maintenance requests. 


How it works:
Reads maintenance tickets from JSON file
Picks priority from Urgent, Medium, Low and Unclassified based on keywords
Picks contractor based on keywords


Assumptions:
The JSON data follows the same ticket structure each time
If there are multiple keywords from different priorities pick the highest priority.
If an issue cant be matched to a priority or contractor it is classified as unknown as classifying it as low could cause issues.


Limitations:
The application uses keyword matching rather than fully understanding the meaning of an issue description.
This means some descriptions could be incorrectly classified.
So for a larger production system the classification rules can be expanded or replaced with a more advanced approach.

AI usage:
Used chatgpt for giving me lists of keywords to be used for identifying priority and contractor.
