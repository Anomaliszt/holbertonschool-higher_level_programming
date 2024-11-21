#!/usr/bin/python3

from os import path


def generate_invitations(template, attendees):
    """ Generate invitation letters for attendees. """
    generated_files = []
    for i, attendee in enumerate(attendees, start=1):
        try:
            filled_template = template.replace(
                '{name}',
                attendee.get('name', 'N/A')
                )
            filled_template = filled_template.replace(
                '{event_title}',
                attendee.get('event_title', 'N/A')
                )
            filled_template = filled_template.replace(
                '{event_date}',
                attendee.get('event_date', 'N/A')
                )
            filled_template = filled_template.replace(
                '{event_location}',
                attendee.get('event_location', 'N/A')
                )
            output_file_name = "output_{}.txt".format(i)
            if path.exists(output_file_name):
                print(
                    f"file '{output_file_name}' already exist")
            else:
                with open(output_file_name, 'w') as file:
                    file.write(filled_template)
                    generated_files.append(output_file_name)
        except KeyError as e:
            print("missing key in attendee data: {}".format(e))
        except Exception as e:
            print("an error occurred: {}".format(e))

    return generated_files