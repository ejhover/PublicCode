solvang = {"name": "USS Solvang", "registry": "NCC-12101", "class": "California", 
        "max_speed": "Warp 8", "armament": {"photons": 5, "phaser_banks": 5}, 
        "max_crew_complement": 1100, "current_complement": 850, 
        "command": {"captain": "Dayton, Julianne T.", "XO": "Martinez, Renata E."}, 
        "reporting_to": "Starbase 200", "distance_to_recall": "54 lightyears", "structure": {"total_decks": 11, 
        "bridge": 2, "shuttlebays": [5, 6, 7], "repair_bay": 11, "medical": 8, "crew_quarters": [1, 4]}, 
        "shuttles": 8, "ground_vehicles": 4}

tsiolkovsky = {"name": "SS Tsiolkovsky", "registry": "NCC-53911", "class": "Oberth",   
        "max_speed": "Warp 9.6", "armament": {"photons": 1, "phaser_banks": 4}, 
        "max_crew_complement": 100, "current_complement": 80, 
        "command": {"captain": "Sartkoshz, Sural", "XO": "Vor, Sarrex"}, 
        "reporting_to": "Starbase 6", "distance_to_recall": "63 lightyears", "structure": {"total_decks": 11, 
        "bridge": 1, "shuttlebays": [4, 5], "repair_bay": 11, "medical": 7, "crew_quarters": [2]}, "shuttles": 4, 
        "ground_vehicles": 0}

centaur = {"name": "USS Centaur", "registry": "NCC-42043", "class": "Centaur",    
        "max_speed": "Warp 7.5", "armament": {"photons": 5, "phaser_banks": 4}, 
        "max_crew_complement": 150, "current_complement": 93, 
        "command": {"captain": "Reynolds, Charles", "XO": "McIntosh, James W."}, "reporting_to": "Starbase 11",                "distance_to_recall": "23.2 lightyears", "structure": {"total_decks": 10, "bridge": 1, "shuttlebays": [1], 
        "repair_bay": 5, "medical": 6, "crew_quarters": [4]}, "shuttles": 4, "ground_vehicles": 1}

yeager = {"name": "USS Yeager", "registry": "NCC-61947", "class": "Saber",      
        "max_speed": "Warp 8.9", "armament": {"photons": 6, "phaser_banks": 2},
        "max_crew_complement": 110, "current_complement": 87, 
        "command": {"captain": "Binde, Melissa", "XO": "Bardoh, Zier"}, "reporting_to": "Starbase 97",
        "distance_to_recall": "47.5 lightyears", "structure": {"total_decks": 6, "bridge": 2, 
        "shuttlebays": [4], "repair_bay": 5, "medical": 6, "crew_quarters": [3, 4]}, "shuttles": 1, 
        "ground_vehicles": 0}

chekov = {"name": "USS Chekov", "registry": "NCC-57302", "class": "Springfield",    
        "max_speed": "Warp 9.2", "armament": {"photons": 2, "phaser_banks": 8},
        "max_crew_complement": 430, "current_complement": 411, 
        "command": {"captain": "Zherkadzh, T'kal", "XO": "Suder, Tam"}, "reporting_to": "Starbase 9",
        "distance_to_recall": "35.4 lightyears", "structure": {"total_decks": 12, "bridge": 1, 
        "shuttlebays": [7, 8], "repair_bay": 10, "medical": 5, "crew_quarters": [2, 3]}, "shuttles": 5, 
        "ground_vehicles": 0}

appalachia = {"name": "USS Appalachia", "registry": "NCC-52136", "class": "Steamrunner",
        "max_speed": "Warp 9.6", "armament": {"photons": 2, "phaser_banks": 6},
        "max_crew_complement": 200, "current_complement": 174, 
        "command": {"captain": "Benteen, Erika", "XO": "al-Rashid, Ahmed"}, "reporting_to": "Starbase 27",
        "distance_to_recall": "38 lightyears", "structure": {"total_decks": 18, "bridge": 2, "shuttlebays": [12, 13], 
        "repair_bay": 15, "medical": 9, "crew_quarters": [6, 7]}, "shuttles": 3, "ground_vehicles": 0}

budapest = {"name": "USS Budapest", "registry": "NCC-64923", "class": "Norway",
        "max_speed": "Warp 9.6", "armament": {"photons": 2, "phaser_banks": 2},
        "max_crew_complement": 310, "current_complement": 249, 
        "command": {"captain": "Sh'Raazn", "XO": "Opuh, Emiraa"}, "reporting_to": "Starbase 51",
        "distance_to_recall": "19 lightyears", "structure": {"total_decks": 13, "bridge": 3, 
        "shuttlebays": [9, 11], "repair_bay": 10, "medical": 6, "crew_quarters": [1, 2]}, "shuttles": 4, 
        "ground_vehicles": 1}

full_fleet = [solvang, tsiolkovsky, centaur, yeager, chekov, appalachia, budapest]


command_personnel = {"captains": [{"first_name": "Julianne", "middle": " T.", "family": "Dayton",
            "species": "human", "classification": ["bridge", "command"], "rank": "captain",
            "assignment": "NCC-12101", "serial": "IG-452-2034 INA"}, {"first_name": "Sural", 
            "middle": "", "family": "Sartkoshz", "species": "Vulcan", 
            "classification": ["bridge", "command"], "rank": "captain", "assignment": "NCC-53911",
            "serial": "TY-892-7209"}, {"first_name": "Charles", "middle": "", "family": "Reynolds",
            "species": "human", "classification": ["bridge", "command"], "rank": "captain",
            "assignment": "NCC-42043", "serial": "YG-281-2393 BV"}, {"first_name": "Melissa", 
            "middle": "", "family": "Binde", "species": "human", "classification": ["bridge",
            "command"], "rank": "captain", "assignment": "NCC-61947", "serial": "WI-2832-1012"},
            {"first_name": "T'kal", "middle": "", "family": "Zherkadzh", "species": "Vulcan",
            "classification": ["bridge", "command"], "rank": "captain", "assignment": "NCC-57302",
            "serial": "SP-201-2382"}, {"first_name": "Erika", "middle": "", "family": "Benteen",
            "species": "human", "classification": ["bridge", "command"], "rank": "captain",
            "assignment": "NCC-52136", "serial": "YUR-1023-2193 YT"}, {"first_name": "Sh'Raazn",
            "middle": "", "family": "", "species": "Andorian", "classification": ["bridge",
            "command"], "rank": "captain", "assignment": "NCC-64923", "serial": "RE-621-9123"}],
            "first_officers": [{"first_name": "Emiraa", "middle": "", "family": "Opuh", 
            "species": "Napean", "classification": ["bridge", "command"], "rank": "commander",
            "assignment": "NCC-64923", "serial": "WB-23-1923 SP"}, {"first_name": "Ahmed",
            "middle": "", "family": "al-Rashid", "species": "human", "classification":
            ["bridge", "command"], "rank": "commander", "assignment": "NCC-52136", "serial":
            "BF-23-3490 VH"}, {"first_name": "Tam", "middle": "", "family": "Suder",
            "species": "Betazoid", "classification": ["bridge", "command"], "rank": "commander",
            "assignment": "NCC-57302", "serial": "TG-325-3459 GH"}, {"first_name": "Zier", 
            "middle": "", "family": "Bardoh", "species": "Andolian", "classification": 
            ["bridge", "command"], "rank": "commander", "assignment": "NCC-61947", "serial": 
            "BG-34-9453 OVG"}, {"first_name": "James", "middle": "W.", "family": "McIntosh",
            "species": "human", "classification": ["bridge", "command"], "rank": "commander", 
            "assignment": "NCC-42043", "serial": "VC-542-9300 VYG"}, {"first_name": "Sarrex", 
            "middle": "", "family": "Vor", "species": "Vulcan", "classification": ["bridge", 
            "command"], "rank": "commander", "assignment": "NCC-53911", "serial": "YV-213-9562 HB"},
            {"first_name": "Renata", "middle": "E.", "family": "Martinez", "species": "human",
            "classification": ["bridge", "command"], "rank": "commander", "assignment": "NCC-12101", 
            "serial": "SG-23-5689-21 GC"}]}

engineering_personnel = {"chiefs": [{"first_name": "Hyrrol", "middle": "", "family": "Arryvb", 
            "species": "Vulcan", "classification": ["bridge", "engineering"], "rank": "commander", 
            "assignment": "NCC-12101", "serial": "CU-432-564 GT"}, {"first_name": "Voha", 
            "middle": "", "family": "", "species": "Benzite", "classification": ["bridge", 
            "engineering"], "rank": "lieutenant_commander", "assignment": "NCC-53911", "serial": 
            "VB-325-13364 AM"}, {"first_name": "Aaron", "middle": "X.", "family": "Henderson", 
            "species": "human", "classification": ["bridge","engineering"], "rank": 
            "lieutenant_commander", "assignment": "NCC-64923", "serial": 
            "AH-235-4590 AQ"}, {"first_name": "Argosa", "middle": "", "family": "Janzar",
            "species": "Elaysian", "classification": ["bridge","engineering"], "rank":
            "commander", "assignment": "NCC-52136", "serial": "BX-30-102-5689"}, {"first_name": 
            "Bianca", "middle": "R.", "family": "Marleau", "species": "human", "classification": 
            ["bridge","engineering"], "rank": "lieutenant_commander", "assignment": "NCC-57302", 
            "serial": "SW-29-36303 BWG"}, {"first_name": "Tamken", "middle": "", "family": "Marun",
            "species": "Tellarite", "classification": ["bridge","engineering"], "rank":
            "commander", "assignment": "NCC-61947", "serial": "YB-22-011-498"}, {"first_name": 
            "T'kai", "middle": "", "family": "", "species": "Vulcan", "classification": 
            ["bridge","engineering"], "rank": "lieutenant_commander", "assignment": "NCC-42043", 
            "serial": "VK-33-25-229 RG"}], "enlisted": {"NCC-53911": {"chief_petty_officer": 3,
            "petty_officer": 3, "crewmen": 18}, "NCC-12101": {"chief_petty_officer": 11,
            "petty_officer": 26, "crewmen": 52}, "NCC-42043": {"chief_petty_officer": 2,
            "petty_officer": 8, "crewmen": 17}, "NCC-61947": {"chief_petty_officer": 1,
            "petty_officer": 6, "crewmen": 8}, "NCC-57302": {"chief_petty_officer": 6,
            "petty_officer": 12, "crewmen": 34}, "NCC-52136": {"chief_petty_officer": 3,
            "petty_officer": 7, "crewmen": 11}, "NCC-64923": {"chief_petty_officer": 5,
            "petty_officer": 10, "crewmen": 19}}, "commissioned": {"NCC-53911": {"commander": 0,
            "lieutenant_commander": 1, "lieutenant": 2, "lieutenant_junior_grade": 3, "ensign": 9}, 
            "NCC-12101": {"commander": 2, "lieutenant_commander": 5, "lieutenant": 9, 
            "lieutenant_junior_grade": 11, "ensign": 28}, "NCC-42043": {"commander": 0, 
            "lieutenant_commander": 1, "lieutenant": 3, "lieutenant_junior_grade": 2, "ensign": 5},
            "NCC-61947": {"commander": 0, "lieutenant_commander": 1, "lieutenant": 1, 
            "lieutenant_junior_grade": 2, "ensign": 10}, "NCC-57302": {"commander": 1,
            "lieutenant_commander": 2, "lieutenant": 5, "lieutenant_junior_grade": 3, "ensign": 17},
            "NCC-52136": {"commander": 0, "lieutenant_commander": 0, "lieutenant": 2, 
            "lieutenant_junior_grade": 2, "ensign": 6}, "NCC-64923": {"commander": 1,
            "lieutenant_commander": 2, "lieutenant": 2, "lieutenant_junior_grade": 5, "ensign": 14}}}

ops_personnel = {"chiefs": [{"first_name": "Teiyap", "middle": "", "family": "Boozol",
            "species": "Rigelian", "classification": ["bridge", "ops"], "rank": "commander",
            "assignment": "NCC-12101", "serial": "BN-28-3458 CGH"}, {"first_name": "Elaine",
            "middle": "V.", "family": "Aaronson", "species": "human", "classification": ["bridge",
            "ops"], "rank": "commander", "assignment": "NCC-53911", "serial":
            "RS-23-835-221 AL"}, {"first_name": "Arlant", "middle": "", "family": "Cyril",
            "species": "Tyrellian", "classification": ["bridge","ops"], "rank":
            "lieutenant_commander", "assignment": "NCC-64923", "serial":
            "IU-28-719-039"}, {"first_name": "Parzim", "middle": "", "family": "Odan",
            "species": "Trill", "classification": ["bridge","ops"], "rank":
            "commander", "assignment": "NCC-52136", "serial": "AP-23-4323"}, {"first_name":
            "Meera", "middle": "", "family": "Patel", "species": "human", "classification":
            ["bridge","ops"], "rank": "commander", "assignment": "NCC-57302",
            "serial": "RB-29-3460-23 GY"}, {"first_name": "Dorlaan", "middle": "", "family": "Andos",
            "species": "Rhaandarite", "classification": ["bridge","ops"], "rank":
            "lietenant_commander", "assignment": "NCC-61947", "serial": "XR-03-349-921"}, 
            {"first_name": "Volkec", "middle": "", "family": "Strzhub", "species": "Vulcan", 
            "classification": ["bridge","ops"], "rank": "lieutenant_commander", 
            "assignment": "NCC-42043", "serial": "AR-29-06723 FI"}], "enlisted": 
            {"NCC-53911": {"chief_petty_officer": 2, "petty_officer": 3, "crewmen": 15}, 
            "NCC-12101": {"chief_petty_officer": 9, "petty_officer": 21, "crewmen": 47}, 
            "NCC-42043": {"chief_petty_officer": 1, "petty_officer": 6, "crewmen": 11}, 
            "NCC-61947": {"chief_petty_officer": 1, "petty_officer": 4, "crewmen": 7}, 
            "NCC-57302": {"chief_petty_officer": 5, "petty_officer": 10, "crewmen": 31}, 
            "NCC-52136": {"chief_petty_officer": 3, "petty_officer": 7, "crewmen": 11}, 
            "NCC-64923": {"chief_petty_officer": 3, "petty_officer": 5, "crewmen": 14}}, 
            "commissioned": {"NCC-53911": {"commander": 1, "lieutenant_commander": 0, 
            "lieutenant": 1, "lieutenant_junior_grade": 2, "ensign": 10}, "NCC-12101": 
            {"commander": 2, "lieutenant_commander": 6, "lieutenant": 10, 
            "lieutenant_junior_grade": 13, "ensign": 25}, "NCC-42043": {"commander": 0,
            "lieutenant_commander": 1, "lieutenant": 2, "lieutenant_junior_grade": 3, "ensign": 4},
            "NCC-61947": {"commander": 1, "lieutenant_commander": 0, "lieutenant": 0,
            "lieutenant_junior_grade": 3, "ensign": 8}, "NCC-57302": {"commander": 1,
            "lieutenant_commander": 2, "lieutenant": 4, "lieutenant_junior_grade": 7, "ensign": 15},
            "NCC-52136": {"commander": 0, "lieutenant_commander": 0, "lieutenant": 1, 
            "lieutenant_junior_grade": 3, "ensign": 4}, "NCC-64923": {"commander": 0,
            "lieutenant_commander": 2, "lieutenant": 1, "lieutenant_junior_grade": 6, "ensign": 11}}}    

all_personnel = [command_personnel, {"ops": ops_personnel, "engineering": engineering_personnel}]

skirmish_1803 = {'skirmish_id': 1803, 'ships_engaged': ['USS Centaur'], 'damage_reports': {'bridge': 0.0, 
                'medical': 0.66, 'engineering': 0.0, 'hull': 0.45, 'quarters': 0.25}, 'casualties': {'bridge': 0, 
                'medical': 0, 'engineering': 0, 'ops': 0, 'crew': 6}, 'officers_kia': []}

skirmish_1412 = {'skirmish_id': 1412, 'ships_engaged': ['USS Solvang', 'USS Centaur'], 'damage_reports': 
                {'USS Solvang': {'bridge': 0.0, 'medical': 0.0, 'engineering': 0.0, 'hull': 0.33, 'quarters': 0.0}, 
                "USS Centaur": {'bridge': 0.0, 'medical': 0.47, 'engineering': 0.0, 'hull': 0.62, 'quarters': 0.31}}, 
                'casualties': {"USS Solvang": {'bridge': 0, 'medical': 0, 'engineering': 0, 'ops': 0, 'crew': 0},  
                "USS Centaur": {'bridge': 0, 'medical': 0, 'engineering': 0, 'ops': 0, 'crew': 14}}, "officers_kia": 
                {"USS Solvang": [], "USS Centaur": []}}

skirmish_1243 = {'skirmish_id': 1243, 'ships_engaged': ['SS Tsiolkovsky'], 'damage_reports': {'bridge': 0.47, 
                'medical': 0.0, 'engineering': 0.0, 'hull': 0.33, 'quarters': 0.47}, 'casualties': {'bridge': 0, 
                'medical': 0, 'engineering': 0, 'ops': 1, 'crew': 27}, 'officers_kia': ["captain"]}

skirmish_927 = {'skirmish_id': 927, 'ships_engaged': ['USS Appalachia'], 'damage_reports': {'bridge': 0.0, 
               'medical': 0.0, 'engineering': 0.31, 'hull': 0.59, 'quarters': 0.0}, 'casualties': {'bridge': 0, 
               'medical': 0, 'engineering': 3, 'ops': 0, 'crew': 0}, 'officers_kia': ["chief_of_engineering"]}

skirmish_172 = {'skirmish_id': 172, 'ships_engaged': ['USS Budapest'], 'damage_reports': {'bridge': 0.61, 
               'medical': 0.0, 'engineering': 0.0, 'hull': 0.61, 'quarters': 0.42}, 'casualties': {'bridge': 4, 
               'medical': 0, 'engineering': 0, 'ops': 5, 'crew': 13}, 'officers_kia': ["XO", "chief_of_ops"]}

skirmish_212 = {'skirmish_id': 212, 'ships_engaged': ['USS Yeager'], 'damage_reports': {'bridge': 0.77, 
               'medical': 0.0, 'engineering': 0.0, 'hull': 0.45, 'quarters': 0.26}, 'casualties': {'bridge': 3, 
               'medical': 0, 'engineering': 0, 'ops': 6, 'crew': 15}, 'officers_kia': ['captain', 'XO']}


battle_reports = [skirmish_1803, skirmish_1412, skirmish_1243, skirmish_927, skirmish_172, skirmish_212]
'''
solvang = {"name": "USS Solvang", "registry": "NCC-12101", "class": "California", 
        "max_speed": "Warp 8", "armament": {"photons": 5, "phaser_banks": 5}, 
        "max_crew_complement": 1100, "current_complement": 850, 
        "command": {"captain": "Dayton, Julianne T.", "XO": "Martinez, Renata E."}, 
        "reporting_to": "Starbase 200", "distance_to_recall": "54 lightyears", "structure": {"total_decks": 11, 
        "bridge": 2, "shuttlebays": [5, 6, 7], "repair_bay": 11, "medical": 8, "crew_quarters": [1, 4]}, 
        "shuttles": 8, "ground_vehicles": 4}
'''
{"first_name": "Teiyap", "middle": "", "family": "Boozol",
            "species": "Rigelian", "classification": ["bridge", "ops"], "rank": "commander",
            "assignment": "NCC-12101", "serial": "BN-28-3458 CGH"}
#initializes class that stores information about different crewmen on the boat
class Crewman:
    def __init__(self, first_name, middle):
        self.first_name = first_name
        self.middle = middle
        self.family = None
        self.species = None
        self.classification = None
        self.rank = None
        self.assignment = None
        self.serial = None


# initializes class for a ship that stores all the data stored in the existing dictionaries
class Ship:
    def __init__(self, name):
        self.name = name
        self.registry = None
        self.classstr = None
        self.max_speed = None
        self.photons = None 
        self.phaser_banks = None
        self.max_crew_complement = None 
        self.curr_complement = None
        self.captain = None
        self.XO = None
        self.reporting_to = None
        self.distance_to_recall = None
        self.total_decks = None
        self.bridge = None
        self.shuttlebays = None
        self.repair_bay = None
        self.medical = None
        self.crew_quarters = None
        self.shuttles = None
        self.ground_vehicles = None
    # displays if every ship is within the threshold of manpower or if they need more men assigned
    def ships_at_capacity(threshold):
        for ship in full_fleet:
            if (int(ship["current_complement"])/int(ship["max_crew_complement"])*100) < threshold:
                print(f'{ship["name"]} NEEDS ASSIGNMENT')
            else:
                print(f'{ship["name"]}: {int(ship["current_complement"])/int(ship["max_crew_complement"])*100}%') 
    # displays the phaser banks and photon torpedo capacity of the given ship name (weapon information)
    def combat_power(self):
        return(f'{self.name}:\n    Phaser Banks: {self.phaser_banks}\n    Photon Torpedo Capacity: {self.photons}')
    # displays the name of the captain and the XO in (last, first) order given the ship name
    def command_roster(self):
        return(f'{self.name}:\n    Captain Name: {self.captain}\n    XO Name: {self.XO}')
    # displays the current station and its distance to the shipyards in lightyears
    def current_station(self):
        return(f'{self.name}:\n    Current Station: {self.reporting_to}\n    Distance to: {self.distance_to_recall}')
    # checks and prints if every ship meets or exceeds the given thresholds of photon capacity, % manpower, and distance from shipyards
    def combat_ready(self, photon_capacity, manpower, how_far):
        if (self.photons >= photon_capacity) and ((self.curr_complement/self.max_crew_complement)*100 >= manpower) and (self.distance_to_recall >= how_far):
            return(f'{self.name} meets or exceeds the thresholds')
# displays if every ship is within the threshold of manpower or if they need more men assigned
def ships_at_capacity(threshold):
    for ship in full_fleet:
        if (int(ship["current_complement"])/int(ship["max_crew_complement"])*100) < threshold:
            print(f'{ship["name"]} NEEDS ASSIGNMENT')
        else:
            print(f'{ship["name"]}: {int(ship["current_complement"])/int(ship["max_crew_complement"])*100}%') 
# displays the phaser banks and photon torpedo capacity of the given ship name (weapon information)
def combat_power(ship_name):
    for ship in full_fleet:
        if ship["name"] == ship_name:
                print(f'{ship["name"]}:\n    Phaser Banks: {ship["armament"]["phaser_banks"]}\n    Photon Torpedo Capacity: {ship["armament"]["photons"]}')
# displays the name of the captain and the XO in (last, first) order given the ship name
def command_roster(ship_name):
    for ship in full_fleet:
        if ship["name"] == ship_name:
                print(f'{ship["name"]}:\n    Captain Name: {ship["command"]["captain"]}\n    XO Name: {ship["command"]["XO"]}')
# displays the current station and its distance to the shipyards in lightyears
def current_station(ship_name):
    for ship in full_fleet:
        if ship["name"] == ship_name:
            print(f'{ship["name"]}:\n    Current Station: {ship["reporting_to"]}\n    Distance to: {ship["distance_to_recall"]}')
# checks and prints if every ship meets or exceeds the given thresholds of photon capacity, % manpower, and distance from shipyards
def combat_ready(photon_capacity, manpower, how_far):
    for ship in full_fleet:
        if (ship["armament"]["photons"] >= photon_capacity) and (int(ship["current_complement"])/int(ship["max_crew_complement"])*100 >= manpower) and (float(ship["distance_to_recall"].split(" ")[0]) >= how_far):
            print(f'{ship["name"]} meets or exceeds the thresholds')
# checks if a given ship needs crew reassignment or if its manpower is still over the threshold after a skirmish
def verify_manpower(skirmish, ship_name, threshold=50):
    for ship in full_fleet:
        if ship_name == ship["name"]:
            ship["current_complement"]-=skirmish["casualties"][ship_name]["crew"]
            if int(ship["current_complement"])/int(ship["max_crew_complement"])*100 < threshold:
                print(f'{ship["name"]} is recalled for crew reassignment')
# promotes lower level personnel to the level of personnel who died in battle
def check_command_structure(skirmish, ship, roster):
    if type(skirmish["officers_kia"]) == list:
        if "captain" in skirmish["officers_kia"] and "XO" in skirmish["officers_kia"]:
            for i in roster["chiefs"]:
                if i["rank"] == "commander":
                    ship["command"]["captain"] = i["first_name"] + i["middle"]
                else:
                    print(f'{ship["name"]} is recalled for reassignment')
            for i in roster["chiefs"]:
                if i["rank"] == "lieutenant_commander":
                    ship["command"]["XO"] = i["first_name"] + i["middle"]
                else:
                    print(f'{ship["name"]} is recalled for reassignment')
        elif "captain" in skirmish["officers_kia"]:
            ship["command"]["captain"] = ship["command"]["XO"]
        elif "XO" in skirmish["officers_kia"]:
            for i in roster["chiefs"]:
                if i["rank"] == "lieutenant_commander":
                    ship["command"]["XO"] = i["first_name"] + i["middle"]
                else:
                    print(f'{ship["name"]} is recalled for reassignment')
    elif "captain" in skirmish["officers_kia"][ship["name"]] and "XO" in skirmish["officers_kia"][ship["name"]]:
        for i in roster["chiefs"]:
            if i["rank"] == "commander":
                ship["command"]["captain"] = i["first_name"] + i["middle"]
            else:
                print(f'{ship["name"]} is recalled for reassignment')
    elif "captain" in skirmish["officers_kia"][ship["name"]]:
        ship["command"]["captain"] = ship["command"]["XO"]
    elif "XO" in skirmish["officers_kia"][ship["name"]]:
            for i in roster["chiefs"]:
                if i["rank"] == "lieutenant_commander":
                    ship["command"]["XO"] = i["first_name"] + i["middle"]
                else:
                    print(f'{ship["name"]} is recalled for reassignment')
# when a ship is above a certain damage threshold, change its current location to the shipyard to be repaired
def damage_report(skirmish, ship, threshold):
    try:
        if sum(skirmish['damage_reports'][ship["name"]].values()) >= threshold:
            ship["reporting_to"] = "Utopia Planitia"
    except:
        if sum(skirmish['damage_reports'].values()) >= threshold:
            ship["reporting_to"] = "Utopia Planitia"
# when a ship reaches a certain damage threshold, remove it from the fleet and decomission it
def decommission(skirmish, ship, threshold):
    if sum(skirmish["damage_reports"][ship["name"]].values()) >= threshold:
        del full_fleet[full_fleet.index(ship)]
# checks every ship in a skirmish if it needs to be repaired or decomissioned as a result of the damages from the skirmish
def skirmish_engaged(skirmish):
    for ship in skirmish["ships_engaged"]:
        for i in full_fleet:
            if i["name"] == ship:
                damage_report(skirmish, i, 1)
                decommission(skirmish_1412, i, 1)
def main():
    # asks for the given threshold and ship name, and checks them with the created functions
    verify_manpower(skirmish_1412, "USS Solvang", 50)
    check_command_structure(skirmish_1412, solvang, ops_personnel)
    damage_report(skirmish_1412, solvang, 1)
    decommission(skirmish_1412, solvang, 1)
    skirmish_engaged(skirmish_1412)
if __name__ == "__main__":
        main()
