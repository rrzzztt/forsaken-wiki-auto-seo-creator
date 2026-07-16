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
print("Auto-Seo Creator v3.0 by Rzt")
if int(input(" What type do you want to use?\n  1. GUI\n  2. CLI\n")) == 2:
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
        if filetype == "":
            filetype = "png"
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
else:
    skinnameTK = ""
    skinplaceTK = ""
    skincaseTK = ""
    skinextTK = ""
    def tkinterInfoSave():
        global skinnameTK
        global skinplaceTK
        global skincaseTK
        global skinextTK
        skinnameTK = skinnamecontainer.get()
        skinplaceTK = isPlaceholderButton.get()
        skincaseTK = isFileCaseButton.get()
        skinextTK = isSkinExtensionButton.get()
        print(f"{skinnameTK}\n{skinplaceTK}\n{skincaseTK}\n{skinextTK}")
        return skinnameTK,skinplaceTK,skincaseTK,skinextTK
    import tkinter as tk
    from tkinter import ttk
    skincaseoptions = ["True","False"]
    skinextensionoptions = [".png",".jpeg",".jpg",".webp"]
    placeholderoptions = ["True","False"]
    root = tk.Tk()
    root.title("Auto Seo Creator v3.0 Experimental-GUI")
    root.geometry("400x360")
    root.wm_minsize(400,360)
    def events(event,event_obj=None):
        if event == "statedefault":
            stateselect("OK... Idle")
        if event == "stateloading":
            stateselect("Loading data...")
        if event == "stateloadingusr":
            stateselect("Loading user data...")
        if event == "stategenerating":
            stateselect("Generating SEO...")
        if event == "stategenerated":
            stateselect(f"Generated SEO. Output: {filelocation}output.txt")
        if event == "getInfo":
            tkinterInfoSave()
    def stateselect(message=str):
        statetext.config(text=message)
    def generateseo():
        events("stateloading")
        events("stategenerating")
        seocreateMainTkinter(tkinterInfoSave()[0],tkinterInfoSave()[1],tkinterInfoSave()[2],tkinterInfoSave()[3])
        events("stategenerated")
    def seocreateMainTkinter(skinName=str,skinPlaceholder=str,skinCase=str,skinExtension=str):
        with open(f"{filelocation}output.txt","w") as f:
            f.write("")
        name = skinName.replace("İ","I").replace("Ö","O").replace("Ç","C").replace("Ş","S").replace("ı","i").replace("ö","o").replace("ş","s").replace("ü","u").replace("Ü","U")
        caps = skinCase.casefold()
        filetype = skinExtension
        placeholder = skinPlaceholder.casefold()
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
        if filetype == "":
            filetype = "png"
        # Ok so these are the milestone things. As the message above says, THESE ARE HARDCODED TOO PLEASE DONT USE OTHER THINGS IN THE INPUT!
        if name == "Milestone IV":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"Milestone IV ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("milestone iv","milestone,4")}\n|image = Skin{skintag} Milestone4 InvIcon.png\n|description=Milestone IV is a Milestone skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
                print("Output saved to output.txt\n")
            return
        if name == "Milestone III":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"Milestone III ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("milestone iii","milestone,3")}\n|image = Skin{skintag} Milestone3 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Milestone III is a Milestone skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
                print("Output saved to output.txt\n")
            return
        if name == "Milestone II":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"Milestone II ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("milestone ii","milestone,2")}\n|image = Skin{skintag} Milestone2 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Milestone II is a Milestone skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
                print("Output saved to output.txt\n")
            return
        if name == "Milestone I":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"Milestone I ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("milestone i","milestone,1")}\n|image = Skin{skintag} Milestone1 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Milestone I is a Milestone skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
                print("Output saved to output.txt\n")
            return
        if name == "Legacy Milestone IV":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"Legacy Milestone IV ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("legacy milestone iv","legacy,milestone,4")}\n|image = Skin{skintag} LegacyMilestone4 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Legacy Milestone IV is a Milestone skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
                print("Output saved to output.txt\n")
            return
        if name == "Legacy Milestone III":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"Legacy Milestone III ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("legacy,milestone iii","milestone,3")}\n|image = Skin{skintag} LegacyMilestone3 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Legacy Milestone III is a Milestone skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
                print("Output saved to output.txt\n")
            return
        if name == "Legacy Milestone II":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"Legacy Milestone II ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("legacy,milestone ii","milestone,2")}\n|image = Skin{skintag} LegacyMilestone2 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Legacy Milestone II is a Milestone skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
                print("Output saved to output.txt\n")
            return
        if name == "Legacy Milestone I":
            with open(f"{filelocation}output.txt","w") as f:
                f.write("")
            with open(f"{filelocation}output.txt","a") as f:
                f.write("{{#seo:\n|title = ")
                f.write(f"Legacy Milestone I ({charname}) - Official Forsaken Wiki\n|keywords={keywords.replace("legacy,milestone i","milestone,1")}\n|image = Skin{skintag} LegacyMilestone1 InvIcon.{filetype.removeprefix(".").casefold()}\n|description=Legacy Milestone I is a Milestone skin for {charname}. <!--Please expand this part-->")
                f.write("\n}}")
                print("Output saved to output.txt\n")
            return
        if not name == "Milestone IV" or not name == "Milestone III" or not name == "Milestone IV" or not name == "Milestone I" or not name == "Legacy Milestone I" or not name == "Legacy Milestone II" or not name == "Legacy Milestone III" or not name == "Legacy Milestone IV":
            if placeholder == "false" or placeholder == "":
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
    # Item Creator
    ## Containers
    buttoncontainer =        tk.Frame(root)
    userinfocontainer =      tk.Frame(root)
    placeholdercontainer =   tk.Frame(root)
    casefilecontainer =      tk.Frame(root)
    fileextensioncontainer = tk.Frame(root)
    ## Actual items
    separator = ttk.Separator(root, orient="horizontal")
    titletext = tk.Label(root, text="Auto-Seo Creator v3.0",font=("Arial",14))
    credittext = tk.Label(root, text="by User:Rzt!",font=("Arial",7))
    statetext = tk.Label(root, text="OK... Idle")
    debuginfo = tk.Label(root, text="INDEV - Might have issues!")
    skinnamecontainer = tk.Entry(userinfocontainer, text="")
    skinnameprefix = tk.Label(userinfocontainer, text="Skin Name:")
    runbutton = tk.Button(buttoncontainer, text="Run", command=lambda:generateseo())
    closebutton = tk.Button(buttoncontainer, text="Close", command=lambda: exit())
    isPlaceholderButtonText = tk.Label(placeholdercontainer, text="Is Skin render 'Placeholder.png'?")
    isPlaceholderButton = ttk.Combobox(placeholdercontainer, values=placeholderoptions, state="readonly")
    isFileCaseButtonText = tk.Label(casefilecontainer, text="Is Skin file NOT case sensitive?")
    isFileCaseButton = ttk.Combobox(casefilecontainer,values=skincaseoptions,state="readonly")
    isSkinExtensionButtonText = tk.Label(fileextensioncontainer,text="What is the file extension of the skin file?") 
    isSkinExtensionButton = ttk.Combobox(fileextensioncontainer,values=skinextensionoptions,state="readonly")
    # Render
    titletext.pack(pady=20)
    credittext.pack()
    ## User Inputs
    userinfocontainer.pack(pady=10) #      Skin name container
    skinnameprefix.pack(side="left")
    skinnamecontainer.pack(side="left")
    placeholdercontainer.pack(pady=10) #   Placeholder True/False container
    isPlaceholderButtonText.pack(side="left")
    isPlaceholderButton.pack(side="left")
    isPlaceholderButton.current(1)
    casefilecontainer.pack(pady=10) #      Skin file case container
    isFileCaseButtonText.pack(side="left")
    isFileCaseButton.pack(side="left")
    isFileCaseButton.current(1)
    fileextensioncontainer.pack(pady=10) # Skin file extension container
    isSkinExtensionButtonText.pack(side="left")
    isSkinExtensionButton.pack(side="left")
    isSkinExtensionButton.current(0)
    ## Run/Close Button
    buttoncontainer.pack(pady=20)
    runbutton.pack(padx=10,side="left")
    closebutton.pack(padx=10,side="left")
    ## State text at the bottom
    statetext.pack(pady=2.5,side="bottom",anchor="w")
    # debuginfo.pack(pady=2.5,side="bottom",anchor="e")
    separator.pack(fill="x",pady=1,side="bottom",padx=0)
    # Debug
    root.bind("1",lambda event: events("stateloading",event))
    root.bind("0",lambda event: events("statedefault",event))
    # Looper
    root.mainloop()
