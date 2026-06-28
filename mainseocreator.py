from sys import argv
filelocation = argv[0].removesuffix("mainseocreator.py").removesuffix("mainseocreator.exe")
with open(f"{filelocation}output.txt","w") as f:
    f.write("")
while True:
    name = str(input("Skin Name: "))
    caps = str(input("Skin file has case sensitive name? (True/False): "))
    placeholder = str(input("Placeholder Photo (True/False): "))
    nameliststr = ""
    try:
        with open(f"{filelocation}config.dat","r") as f:
            config = f.readlines()
    except FileNotFoundError:
        with open(f"{filelocation}config.dat","a") as f:
            f.write("name=Placeholder\nkeywords=If you see this message it means you didnt put keywords in the config.dat file. Please put some keywords inside the config file.\nskintag=PLHL\n\n\nHello the program doesnt care after line 3 so im just gonna write my comments here.\nname is characters name\nkeywords is the keywords. Seperate them with ',' and CHARACTERNAME = the character name entered in 'name=' and SKINNAME is the skin's name when you input it.\nskintag is the shortened version of the characters name. the thing that comes after 'Skin{SKINTAG} BLABLABAL InvIcon.png'")
        with open(f"{filelocation}config.dat","r") as f:
            config = f.readlines()
    charname = config[0].removesuffix("\n").removeprefix("name=")
    keywords = config[1].removeprefix("keywords=").replace("CHARACTERNAME",charname.casefold()).removesuffix("\n").replace("SKINNAME",name.casefold()).casefold()
    skintag = config[2].removeprefix("skintag=").removesuffix("\n")
# Hello code writing Rzt here: This shitty ass config reader only reads from the parameters i wrote so please dont try to put other things in config.dat. IT WILL NOT WORK CUZ I HARDCODED IT!
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
    if caps == "True" or caps == "":
        nameliststr
    elif caps == "False":
        nameliststr = nameliststr.casefold()
# Ok so these are the milestone things. As the message above says, THESE ARE HARDCODED TOO PLEASE DONT USE OTHER THINGS IN THE INPUT!
    if name == "Milestone IV":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Milestone IV ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("milestone iv","milestone,4")}\n|image = Skin{skintag} Milestone4 InvIcon.png\n|description=Milestone IV is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            continue
    if name == "Milestone III":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Milestone III ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("milestone iii","milestone,3")}\n|image = Skin{skintag} Milestone3 InvIcon.png\n|description=Milestone III is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            continue
    if name == "Milestone II":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Milestone II ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("milestone ii","milestone,2")}\n|image = Skin{skintag} Milestone2 InvIcon.png\n|description=Milestone II is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            continue
    if name == "Milestone I":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Milestone I ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("milestone i","milestone,1")}\n|image = Skin{skintag} Milestone1 InvIcon.png\n|description=Milestone I is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            continue
    if name == "Legacy Milestone IV":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Legacy Milestone IV ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("legacy milestone iv","legacy,milestone,4")}\n|image = Skin{skintag} LegacyMilestone4 InvIcon.png\n|description=Legacy Milestone IV is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            continue
    if name == "Legacy Milestone III":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Legacy Milestone III ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("legacy,milestone iii","milestone,3")}\n|image = Skin{skintag} LegacyMilestone3 InvIcon.png\n|description=Legacy Milestone III is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            continue
    if name == "Legacy Milestone II":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Legacy Milestone II ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("legacy,milestone ii","milestone,2")}\n|image = Skin{skintag} LegacyMilestone2 InvIcon.png\n|description=Legacy Milestone II is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            continue
    if name == "Legacy Milestone I":
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        with open(f"{filelocation}output.txt","a") as f:
            f.write("{{#seo:\n|title = ")
            f.write(f"Legacy Milestone I ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("legacy,milestone i","milestone,1")}\n|image = Skin{skintag} LegacyMilestone1 InvIcon.png\n|description=Legacy Milestone I is a Milestone skin for {charname}. <!--Please expand this part-->")
            f.write("\n}}")
            continue
    if not name == "Milestone IV" or not name == "Milestone III" or not name == "Milestone IV" or not name == "Milestone I" or not name == "Legacy Milestone I" or not name == "Legacy Milestone II" or not name == "Legacy Milestone III" or not name == "Legacy Milestone IV":
        if placeholder == "False" or placeholder == "":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"{name} ({charname}) - Official Forsaken Wiki")
                f.write(f"\n|keywords={keywords}\n|image = Skin{skintag} {nameliststr} InvIcon.png\n|description={name} is a skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
        if placeholder == "True":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"{name} ({charname}) - Official Forsaken Wiki")
                f.write(f"\n|keywords={keywords}\n|image = Placeholder.png\n|description={name} is a skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
        if placeholder == "wtf":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"{name} ({charname}) - Official Forsaken Wiki")
                f.write(f"\n|keywords={keywords}\n|image = \n|description={name} is a skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")