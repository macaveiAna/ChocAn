import json
class reports:
    def __init__(self):
        pass

    def create_member_weekly_reports(self):
        with open("Member/MemberDirectory.json", mode="r") as memberFile:
            all_members = json.load(memberFile)
        for member in all_members["members"]:
            name = member["MemberName"]
            with open(f"Member/{name}/{name}_profile.json") as aMember:
                pass
