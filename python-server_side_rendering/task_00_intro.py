import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        raise ValueError("Template must be a string")

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        raise ValueError("Attendees must be a list")

    if template.strip() == "":
        raise ValueError("Template is empty")

    if not attendees:
        raise ValueError("Attendees list is empty")

    for i, attendee in enumerate(attendees, start=1):
        output_content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            placeholder = "{" + key + "}"
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            output_content = output_content.replace(placeholder, value)
        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)