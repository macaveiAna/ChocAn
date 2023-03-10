import json
import datetime
import pandas as pd
from tabulate import tabulate

class report:
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
                json.dump(aMember, f,indent=4)
            aMember['Services'] = []
            with open(f"Member/{name}/{name}_profile.json", "w") as file:
                json.dump(aMember,file,indent=4)
    
    def create_provider_weekly_reports(self):
        today = datetime.date.today()
        with open("Provider/ProviderList.json", mode="r") as providerFile:
            all_providers = json.load(providerFile)
        for provider in all_providers["providers"]:
            name = provider["ProviderName"]
            with open(f"Provider/{name}/{name}_profile.json", "r") as aProviderFile:
                aProvider = json.load(aProviderFile)
            with open(f"Provider/{name}/{name}_{today}", "w") as f:
                json.dump(aProvider, f, indent=4)
            aProvider['Services'] = []
            aProvider["TotalConsultations"] = 0
            aProvider["TotalFees"] = " "
            with open(f"Provider/{name}/{name}_profile.json", "w") as file:
                json.dump(aProvider,file, indent=4)
    
    def create_EFT_report(self):
        with open("Provider/ProviderList.json", mode="r") as providerFile:
            all_providers = json.load(providerFile)
        for provider in all_providers["providers"]:
            name = provider["ProviderName"]
            with open(f"Provider/{name}/{name}_profile.json", "r") as aProviderFile:
                aProvider = json.load(aProviderFile)
            provider_number = aProvider["ProviderID"]
            total_fees_transfer = aProvider["TotalFee"]
            with open("Provider/EFT.json", "r") as EFTfile:
                new_data = json.load(EFTfile)
            new_record = {
                "ProviderName":name,
                "ProviderId":provider_number,
                "TotalAmount":total_fees_transfer
            }
            new_data["EFT_Data"].append(new_record)
            with open("Provider/EFT.json", "w") as EFTfile:
                json.dump(new_data,EFTfile,indent=4)
            

            with open('Provider/EFT.json') as f:
                data = json.load(f)
            

# Create DataFrame from EFT_Data
            df = pd.DataFrame(data['EFT_Data'])

# Rename columns
            df = df.rename(columns={
                'ProviderName': 'Provider Name',
                'ProviderId': 'Provider ID',
                'TotalAmount': 'Total Fees'
            })

# Convert DataFrame to table format
            table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False, numalign='left')

# Print table
            print(table)
    def create_summary_report(self):
        pass

            
            