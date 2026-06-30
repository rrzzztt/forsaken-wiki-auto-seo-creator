from sys import argv
from os.path import basename
checked = False
config_dict = {}
filelocation = argv[0].removesuffix(basename(argv[0]))
clientversion = 3
try:
    with open(f"{filelocation}config.dat","r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                config_dict[key.strip()] = value.strip()
except FileNotFoundError:
    with open(f"{filelocation}config.dat","w") as f:
        f.write("# This is the name of the character. Can be used as 'CHARACTERNAME' in the 'keywords' variable.\nname=Shedletsky\n# This the keywords that are going to be used. Seperate keywords with ',' and use 'SKINNAME' for writing the skin's name and 'CHARACTERNAME' in order to write the character's name.\nkeywords=forsaken,wiki,CHARACTERNAME,SKINNAME\n# This is the skintag that appears right after 'Skin'. Eg. 'SkinShed', in this case 'Shed' is the skintag.\nskintag=Shed\n# Do not change this value. This variable is the variable that the program uses to check if the config file is up to date.\nversion=3")
    with open(f"{filelocation}config.dat","r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                config_dict[key.strip()] = value.strip()
configversion = int(config_dict.get("version","-1"))
if configversion == -1:
    checked = True
    print("!!!THE CONFIG FILE DOES NOT HAVE A VERSION. THE PROGRAM IS UNABLE TO VERIFY THE VERSION OF THE CONFIG FILE MEANING CRASHED/ERRORS MAY APPEAR!!!\n!!!CONTINUE WITH CAUTION!!!")
if not configversion == clientversion and checked == False:
    checked = True
    print("!!!THE CONFIG FILE THAT IS CURRENTLY BEING USED IS NOT UP TO DATE WITH THE NEWEST PROGRAM. PLEASE DELETE THE FILE AND TYPE IN A PLACEHOLDER SKIN TO USE THE NEWEST CONFIG FILE.!!!\n!!!IF NOT DONE CAN CAUSE CRASHES/ERRORS!!!")
with open(f"{filelocation}output.txt","w") as f:
    f.write("")
print("Auto-(Placeholder) Seo Creator v2.01 by Rzt")
while True:
    name = str(input("Skin Name: ")).replace("İ","I").replace("Ö","O").replace("Ç","C").replace("Ş","S").replace("ı","i").replace("ö","o").replace("ş","s").replace("ü","u").replace("Ü","U")
    caps = str(input("Skin file has case sensitive name? (true/FALSE): ")).casefold()
    filetype = str(input("Skin render file extension (.PNG/.jpeg/.webp/.jpg): "))
    placeholder = str(input("Placeholder Photo (true/none/FALSE): ")).casefold()
    nameliststr = ""
    try:
        with open(f"{filelocation}config.dat","r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    config_dict[key.strip()] = value.strip()
    except FileNotFoundError:
        with open(f"{filelocation}config.dat","w") as f:
            f.write("# This is the name of the character. Can be used as 'CHARACTERNAME' in the 'keywords' variable.\name=Shedletsky\n# This the keywords that are going to be used. Seperate keywords with "," and use 'SKINNAME' for writing the skin's name and 'CHARACTERNAME' in order to write the character's name.\nkeywords=forsaken,wiki,CHARACTERNAME,SKINNAME\n# This is the skintag that appears right after 'Skin'. Eg. 'SkinShed', in this case 'Shed' is the skintag.\nskintag=Shed\n# Do not change this value. This variable is the variable that the program uses to check if the config file is up to date.\nversion=3")
        with open(f"{filelocation}config.dat", "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    config_dict[key.strip()] = value.strip()
    charname = config_dict.get("name","Shedletsky")
    keywords = config_dict.get("keywords","forsaken,wiki,CHARACTERNAME,SKINNAME")
    skintag = config_dict.get("skintag","Shed")
    keywords = str(keywords).replace("CHARACTERNAME",charname).replace("SKINNAME",name).casefold()
# Hello code writing Rzt here: This shitty ass config reader only reads from the parameters i wrote so please dont try to put other things in config.dat. IT WILL NOT WORK CUZ I HARDCODED IT!
# Hello again i fixed the issue now you can put whatever you want and it still works! Still use my variables tho otherwise it doesnt care about the variables you put it only reads mine!
    namelist = list(name)
    while True:
        try:
            namelist.remove(" ")
        except ValueError:
            break
    while True:
        try:
            nameliststr += namelist.pop(0)
        except IndexError:
            break
    str(nameliststr)
    if caps == "true" or caps == "":
        nameliststr
    elif caps == "false":
        nameliststr = nameliststr.casefold()
# Ok so these are the milestone things. As the message above says, THESE ARE HARDCODED TOO PLEASE DONT USE OTHER THINGS IN THE INPUT!
    if name == "Milestone IV":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Milestone IV ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("milestone iv","milestone,4")}\n|image = Skin{skintag} Milestone4 InvIcon.png\n|description=Milestone IV is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            print("Output saved to output.txt\n")
            continue
    if name == "Milestone III":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Milestone III ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("milestone iii","milestone,3")}\n|image = Skin{skintag} Milestone3 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Milestone III is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            print("Output saved to output.txt\n")
            continue
    if name == "Milestone II":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Milestone II ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("milestone ii","milestone,2")}\n|image = Skin{skintag} Milestone2 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Milestone II is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            print("Output saved to output.txt\n")
            continue
    if name == "Milestone I":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Milestone I ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("milestone i","milestone,1")}\n|image = Skin{skintag} Milestone1 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Milestone I is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            print("Output saved to output.txt\n")
            continue
    if name == "Legacy Milestone IV":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Legacy Milestone IV ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("legacy milestone iv","legacy,milestone,4")}\n|image = Skin{skintag} LegacyMilestone4 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Legacy Milestone IV is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            print("Output saved to output.txt\n")
            continue
    if name == "Legacy Milestone III":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Legacy Milestone III ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("legacy,milestone iii","milestone,3")}\n|image = Skin{skintag} LegacyMilestone3 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Legacy Milestone III is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            print("Output saved to output.txt\n")
            continue
    if name == "Legacy Milestone II":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Legacy Milestone II ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("legacy,milestone ii","milestone,2")}\n|image = Skin{skintag} LegacyMilestone2 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Legacy Milestone II is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            print("Output saved to output.txt\n")
            continue
    if name == "Legacy Milestone I":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Legacy Milestone I ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("legacy,milestone i","milestone,1")}\n|image = Skin{skintag} LegacyMilestone1 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Legacy Milestone I is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            print("Output saved to output.txt\n")
            continue
    if not name == "Milestone IV" or not name == "Milestone III" or not name == "Milestone IV" or not name == "Milestone I" or not name == "Legacy Milestone I" or not name == "Legacy Milestone II" or not name == "Legacy Milestone III" or not name == "Legacy Milestone IV":
        if placeholder == "False" or placeholder == "":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"{name} ({charname}) - Official Forsaken Wiki")
                f.write(f"\n|keywords={keywords}\n|image = Skin{skintag} {nameliststr} InvIcon.{filetype.removeprefix(".").casefold()}\n|description={name} is a skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
                print("Output saved to output.txt\n")
        if placeholder == "true":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"{name} ({charname}) - Official Forsaken Wiki")
                f.write(f"\n|keywords={keywords}\n|image = Placeholder.png\n|description={name} is a skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
                print("Output saved to output.txt\n")
        if placeholder == "none":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"{name} ({charname}) - Official Forsaken Wiki")
                f.write(f"\n|keywords={keywords}\n|image = \n|description={name} is a skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
                print("Output saved to output.txt\n")
