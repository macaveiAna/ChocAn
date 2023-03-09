import json
import datetime
class reports:
    def __init__(self):
        pass

    def create_member_weekly_reports(self):
        today = datetime.date.today()
        with open("Member/MemberDirectory.json", mode="r") as memberFile:
            all_members = json.load(memberFile)
        for member in all_members["members"]:
            name = member["MemberName"]
            with open(f"Member/{name}/{name}_profile.json", "r") as aMemberFile:
                aMember = json.load(aMemberFile)
            with open(f"Member/{name}/{name}_{today}", "w") as f:
                json.dump(aMember, f)
            del aMember['Services']
            with open(f"Member/{name}/{name}_profile.json", "w") as file:
                json.dump(aMember,file)
    
    