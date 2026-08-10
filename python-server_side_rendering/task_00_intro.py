#!/usr/bin/python3

import os


def generate_invitations(template, attendees):
    """Generate invitation files from a template and attendee data."""

    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty template
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        output = template

        # Replace placeholders with attendee data
        output = output.replace(
            "{name}", str(attendee.get("name", "N/A"))
        )
        output = output.replace(
            "{event_title}", str(attendee.get("event_title", "N/A"))
        )
        output = output.replace(
            "{event_date}", str(attendee.get("event_date", "N/A"))
        )
        output = output.replace(
            "{event_location}", str(attendee.get("event_location", "N/A"))
        )

        # Create output file
        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as file:
                file.write(output)
        except OSError as e:
            print(f"Error writing {filename}: {e}")
