"""Meetup model"""

from datetime import datetime

meetup_model = []


class Meetups_Model:

    def __init__(self):
        self.db = meetup_model

    """Function to create new meetup"""
    def create_meetup(self, name, location, host, host_email, host_number, description):
        data = {
            "id": len(self.db) + 1,
            "meetup_name": name,
            "meetup_location": location,
            "hosted_by": host,
            "host_email": host_email,
            "host_number": host_number,
            "meetup_description": description,
            "date_added": datetime.utcnow().isoformat()
        }
        self.db.append(data)
        return data

    """Function returns all meetups"""
    def get_meetups(self):
        return self.db

    """Function returns single meetup"""
    def get_meetup(self, id):
        meetup = [meet_up for meet_up in self.db
                  if meet_up["id"] == id]
        return meetup
