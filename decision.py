#getting the correct priority based on certain words that could be in the ticket
UrgentPriorityWords = ["leak", "flood", "gas", "fire", "burst", "sparking", "smoke"]
MediumPriorityWords = ["lock", "toilet", "boiler", "heating", "radiator", "window", "door", "blocked", "dripping", "damp", "mould"]

LowPriorityWords = ["lightbulb", "paint", "handle", "squeaking", "loose", "stain"]

def priority_choice(issue_description):
    if not issue_description:
        return "Unclassified"

    issue_description = issue_description.lower()

    if any(word in issue_description for word in UrgentPriorityWords):
        return "Urgent"
    elif any(word in issue_description for word in MediumPriorityWords):
        return "Medium"
    elif any(word in issue_description for word in LowPriorityWords):
        return "Low"

    return "Unclassified"


#getting the correct job rule for the problem based on certain words that can be in the ticket
PlumberPriorityWords = ["leak", "flood", "pipe", "tap", "toilet", "sink", "drain", "water", "radiator"]
ElectricianPriorityWords = ["lightbulb", "light", "socket", "electric", "power"," sparking", "wiring"]
GeneralHandymanPriorityWords = ["lock", "door", "window", "handle", "cupboard", "paint", "wall", "shelf", "tile"]

def contractor_choice(issue_description):
    if not issue_description:
        return "Unclassified"

    issue_description = issue_description.lower()

    if any(word in issue_description for word in PlumberPriorityWords):
        return "Plumber"
    elif any(word in issue_description for word in ElectricianPriorityWords):
        return "Electrician"
    elif any(word in issue_description for word in GeneralHandymanPriorityWords):
        return "General Handyman"

    return "Unclassified"