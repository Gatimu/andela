from datetime import datetime

questions = []


class Questions():

    def __init__(self):
        self.db = questions

    """Function saves question posted by user"""
    def save_question(self, details):
        """ Creates a question to a meetup record """

        for item, data in details.items():
            if not data:
                return self.response("{} cannot be blank".format(item), 400)

        question = {
            "id": len(self.db) + 1,
            "dateAdded": datetime.now(),
            "asked_by": details["user_name"],
            "meetup": details["meetup"],
            "title": details["title"],
            "description": details["description"],
            "votes": 0
        }

        self.db.append(question)

        temp_response = {
            "username": question["asked_by"],
            "meetup": question["meetup"],
            "title": question["title"],
            "description": question["description"]
        }

        return self.response(temp_response, 201)

    """Function upvotes a question"""
    def upvote_question(self, question_id):
        question = [qs for qs in self.db
                  if qs["id"] == id]

        # fetch current vote count and increase by 1

        resp = {
            "meetup": question[0][1]["meetup"],
            "title": question[0][1]["title"],
            "body": question[0][1]["description"],
            "votes": question[0][1]["votes"]
        }

        return self.response(resp, 200)

    """Function downvotes a question"""
    def downvote_question(self, question_id):
        question = [qs for qs in self.db
                  if qs["id"] == id]

        # fetch current vote count and decrease by 1

        resp = {
            "meetup": question[0][1]["meetup"],
            "title": question[0][1]["title"],
            "body": question[0][1]["description"],
            "votes": question[0][1]["votes"]
        }

        return self.response(resp, 200)
