import json
with open('HeroesData.json', 'r') as f:
    heroes_dict = json.load(f)

def getAllEligibleHeroesByFaction(list_of_heroes, faction_list):
    newList = []
    for heroe in list_of_heroes:
        if 'Built' in heroe:
            for f in faction_list:
                if f in heroe:
                    if 'Appended' not in heroe:
                        heroe['Appended'] = 'x'
                        newList.append(heroe)
    newList.sort(key=lambda i: i['Rank'])
    return newList

def createTeams(heroes_without_team, faction):
    team = [faction]
    heroes_from_faction = []
    for heroe in heroes_without_team:
        if faction in heroe:
            heroes_from_faction.append(heroe)
    heroes_to_select = [(len(heroes_from_faction)-3), (len(heroes_from_faction)-2), (len(heroes_from_faction)-1),2,1,0]
    if faction == 'Mythical Realm':
        print(len(heroes_from_faction))
    while len(team) < 5:
        number_healers = 0
        for s in heroes_to_select:
            if heroes_from_faction[s]['Rol'] == 'h':
                number_healers += 1
            team.append(heroes_from_faction[s]['Name'])
    return team

def removeFromHeroesList(list_of_heroes, heroes_selected):
    remaining_heroes = [x for x in list_of_heroes if x['Name'] not in heroes_selected]
    return remaining_heroes

def getAllRole(list_of_heroes, role):
    role_list = []
    for heroe in list_of_heroes:
        if heroe['Rol'] == role:
            role_list.append(heroe)
    return role_list


if __name__ == "__main__":
    lst = []
    # for i in range(0, 5): 
    #     ele = input()
    #     lst.append(ele) # adding the element 
    lst = ['Empires Honor', 'Legion of Glory', 'Protagonists', 'Meteor Strike', 'Mythical Realm']
    flst = ['Empires Honor', 'Legion of Glory', 'Protagonists', 'Meteor Strike', 'Mythical Realm', 'Yeless Legends']
    heroesList = heroes_dict['Heroes']
    # all_eligible = getAllEligibleHeroesByFaction(heroesList, flst)
    heroes_without_team = getAllEligibleHeroesByFaction(heroesList, lst)
    team_list = []
    for faction in lst:
        faction_team = createTeams(heroes_without_team, faction)
        team_list.append(faction_team)
        heroes_without_team = removeFromHeroesList(heroes_without_team, faction_team)
    # print(len(getAllRole(heroes_without_team, 't')))
    # print(len(getAllRole(all_eligible, 'h')))
    print(team_list)
    pass