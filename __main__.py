#importing random module

import random

#creating the function to randomly assign a role to each player

def mafia_game_randomizer(number_of_players):
    
    if number_of_players == '6':
        
        positions_for_number_players = ["Mafia", "Detective", "Healer", "Villager", "Villager", "Villager"]
        
        player1 = input("Enter Player 1 name: ")
        player2 = input("Enter Player 2 name: ")
        player3 = input("Enter Player 3 name: ")
        player4 = input("Enter Player 4 name: ")
        player5 = input("Enter Player 5 name: ")
        player6 = input("Enter Player 6 name: ")
        
        list_of_player_names = [player1, player2, player3, player4, player5, player6]
        
        list_of_numbers = list(range(0,6))
        
        randomized_numbers_list = list(random.sample(range(0,6), 6))
        
        global dictionary_of_roles
        
        dictionary_of_roles = {}
        
        for number in list_of_numbers:
            
            dictionary_of_roles[list_of_player_names[number]] = positions_for_number_players[randomized_numbers_list[number]]
            
        print("\n\n\n\n")
        
        for key, value in dictionary_of_roles.items():
            
            print(key + ' is the ' + value)
            
        print("\n\n\n\n")
        
    else:
        
        print("Error: Number of players must be exactly 6, try again")
        
        mafia_game_randomizer(input("How many Players are there: "))

#creating the mafia game function that iterates each time for each role, and updates
#the values for each character continuously

def mafia_game(dictionary_of_roles):
    
#this is the healer function where the healer is able to choose who they would like to
#save that round
    
    def healer_function(person_healer_to_save):
    
        for key,value in dictionary_of_roles.items():
            
            if value == "Healer" and person_healer_to_save not in dictionary_of_roles:
                
                print('Error, this person is already dead, please try again')
                
                healer_function(input('Healer: Who would you like to save tonight: '))
            
            elif value == "Healer":
                
                global person_saved
                
                person_saved = person_healer_to_save
                
                print("\n\n\n\n")
                        
            else:
                        
                pass
            
    for key,value in dictionary_of_roles.items():
        
        if value == "Healer":
            
            healer_function(input('Healer: Who would you like to save tonight: '))
            
        else:
            
            pass

#this is the detective function where the detective will get to choose who they
#would like to check
        
    def detective_function(person_detective_to_check):
        
        for key,value in dictionary_of_roles.items():
            
                if value == "Detective" and person_detective_to_check not in dictionary_of_roles:
                    
                    print('Error, this person is already dead, please try again')
                    
                    detective_function(input("Detective: Who would you like to check tonight: "))
                    
                elif value == "Detective":
                        
                    if dictionary_of_roles[person_detective_to_check] == "Mafia":
                            
                        print("Yes, they are Mafia")
                        
                        input("Press enter to continue")
                            
                        print("\n\n\n\n")
                            
                    else:
                            
                        print("No, they are not Mafia")
                        
                        input("Press enter to continue")
                            
                        print("\n\n\n\n")
                            
                else:
                        
                    pass
                
    for key,value in dictionary_of_roles.items():
        
        if value == "Detective":
            
                detective_function(input("Detective: Who would you like to check tonight: "))
                
        else:
            
            pass

#this is the mafia function where the mafia can choose who they would like to kill
#that round as well as check if the mafia is still alive
    
    def mafia_function(person_mafia_to_kill):
        
        for key,value in dictionary_of_roles.items():
            
            if value == "Mafia" and person_mafia_to_kill not in dictionary_of_roles:
                
                print("Error, this person is already dead, please try again'")
                
                mafia_function(input("Mafia: Who would you like to kill tonight: "))
                
            elif value == "Mafia":
            
                if person_mafia_to_kill != person_saved:
                    
                    global person_mafia_to_kill_list
                        
                    person_mafia_to_kill_list = person_mafia_to_kill
                        
                else:
                        
                    person_mafia_to_kill_list = None
                    
                    print("No one has been killed tonight")
                    
                    input("Press enter to continue")
                    
            else:
                    
                pass
            
        else:
            
            pass
            
    for key,value in dictionary_of_roles.items():
        
        if value == "Mafia":
            
            mafia_function(input("Mafia: Who would you like to kill tonight: "))
                
        else:
            
            pass
        
    if person_mafia_to_kill_list in dictionary_of_roles:
    
        del dictionary_of_roles[person_mafia_to_kill_list]
        
        print(person_mafia_to_kill_list + ' has been killed tonight')
        
        input("Press enter to continue")
        
    else:
        
        pass
            
    if "Mafia" not in dictionary_of_roles.values():
            
        print("Game is over, the town wins")
        
    else:
        
        pass
        
        print("\n\n\n\n")

#this is the town function which asks the town who they would like to kill
    
    def town_kill(person_village_killed):
    
        if person_village_killed in dictionary_of_roles:
        
            del dictionary_of_roles[person_village_killed]
        
            print(person_village_killed + " has been killed by the town")
            
            input("Press enter to continue")
            
        else:
            
            print("Error, this person is already dead, try again")
            
            town_kill(input("Who would the town like to kill today: "))
            
    town_kill(input("Who would the town like to kill today: "))

#this is the game ending code checks if the number of players is less than 3 or if
#the mafia is still alive, both of which are game ending results

    if "Mafia" in dictionary_of_roles.values():
        
        if len(dictionary_of_roles) <= 3:
            
            print("\nGame over, the Mafia wins")
            
        else:
            
            print('\n')
            
            print("People that are still alive:")
            
            for key in dictionary_of_roles.keys():
            
                print(key)
                
            input("Press enter to continue")
            
            print("\n\n\n\n")
            
            mafia_game(dictionary_of_roles)
            
    else:
    
        print("\nGame is over, the town wins")

#printing some introductory text for the moderator

print("""\n
      Please select one person as the moderator and allow only them to input commands\n
      into the terminal. There will be a screen showing all players and their randomly\n
      assigned roles, therefore please ensure the screen is not pointed towards any of the\n
      players. Seceretly whisper to or text each player their roles. Each round ask all players\n
      to close their eyes, and then one-by-one, ask each player with the assigned role on screen\n
      to open their eyes to answer. At the end of each round, announce which players are still\n
      alive
      \n""")

print("""
      This game has been programmed by https://github.com/Harjot66
      """)

print("""\n
      Welcome to Mafia, I hope you have fun! - Harjot Dhaliwal
      \n""")

input("Press enter to continue\n")

#calling the functions from above

mafia_game_randomizer(input("How many Players are there: "))

mafia_game(dictionary_of_roles)
