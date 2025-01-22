import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import random

# Vytvoření hlavního okna
root = tk.Tk()
root.title("D&D Bojový Simulátor")
root.geometry("800x710")  # Nastavení počáteční velikosti okna
root.resizable(True, True)  # Povolení změny velikosti okna


# Definice kostek
d20 = list(range(1, 21))
d10 = list(range(1, 11))
d6 = list(range(1, 7))


# Funkce pro postupné zobrazování textu
def type_text(widget, text):
    print(f"Zobrazuji text: {text}")  # Ladicí výstup
    widget.insert(tk.END, text + "\n")
    widget.update_idletasks()  # Aktualizace widgetu

# Vytvoření rámců pro rozdělení okna
left_frame = tk.Frame(root, width=200)  # Nastavení pevné šířky pro levý rámec
left_frame.pack(side=tk.LEFT, fill=tk.Y)
left_frame.pack_propagate(False)  # Zabránění automatickému přizpůsobení velikosti

middle_frame = tk.Frame(root, width=400)  # Nastavení pevné šířky pro prostřední rámec
middle_frame.pack(side=tk.LEFT, fill=tk.Y)
middle_frame.pack_propagate(False)  # Zabránění automatickému přizpůsobení velikosti

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Status, ve kterém se právě hra nachází
game_state = "menu"
def change_game_status(new_state):
    global game_state
    game_state = new_state

# Hlavní textové okno
main_text_label = tk.Label(middle_frame, text="Průběh souboje", font=("Helvetica", 16, "bold"))
main_text_label.pack()

text_output = tk.Text(middle_frame, height=30, width=100)
text_output.pack()
bottom_frame = tk.Frame(middle_frame)
bottom_frame.pack()

# Widget pro zobrazení statistik hráče
player_stats_label = tk.Label(left_frame, text="")
player_stats_label.pack()

# Funkce pro výpočet bonusu na základě hodnoty statistiky
def calculate_bonus(value):
    return (value - 10) // 2

stats_labels = ["Class", "HP", "Armor Class", "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
stats_entries = {}
bonus_entries = {}

font_style_1 = ("Helvetica", 12, "bold")
font_style_2 = ("Helvetica", 10, "bold")

for stat in stats_labels:
    
    label = tk.Label(left_frame, text=stat)
    label.pack()
    entry_frame = tk.Frame(left_frame)
    entry_frame.pack()
    entry = tk.Entry(entry_frame, justify='center', state='readonly', width=10, font = font_style_1)
    entry.pack()
    if stat not in ["Class", "HP", "Armor Class"]:
        bonus_entry = tk.Entry(entry_frame, justify='center', state='readonly', width=3)
        bonus_entry.pack()
        bonus_entries[stat] = bonus_entry
    stats_entries[stat] = entry

# Kolonka pro zbraně
# Kolonka pro zbraně
# Vytvoření rámce pro aktuální zbraň a vybranou zbraň
current_weapon_frame = tk.Frame(left_frame)
current_weapon_frame.pack(pady=10)

# Label pro aktuální zbraň
current_weapon_label = tk.Label(current_weapon_frame, text="Current weapon", font=font_style_2)
current_weapon_label.pack()

# Entry pro vybranou zbraň
selected_weapon_entry = tk.Entry(current_weapon_frame, justify='center', state='readonly', width=11, font=font_style_1)
selected_weapon_entry.pack(pady=5)

def update_current_weapon_display():
    selected_weapon_entry.config(state='normal')
    selected_weapon_entry.delete(0, tk.END)
    selected_weapon_entry.insert(0, current_weapon)
    selected_weapon_entry.config(state='readonly')
# Kolonka pro zbraně
# Kolonka pro zbraně

# Funkce pro aktualizaci statistik hráče
def update_player_stats():
    stats_entries["Class"].config(state='normal') # Umožnění úpravy obsahu
    stats_entries["Class"].delete(0, tk.END) # Vymazání aktuálního obsahu
    stats_entries["Class"].insert(0, player_class.capitalize())  # Vložení nové hodnoty
    stats_entries["Class"].config(state='readonly') # Nastavení stavu na readonly
    
    stats_entries["HP"].config(state='normal')
    stats_entries["HP"].delete(0, tk.END)
    stats_entries["HP"].insert(0, player_hp)
    stats_entries["HP"].config(state='readonly')
    
    stats_entries["Armor Class"].config(state='normal')
    stats_entries["Armor Class"].delete(0, tk.END)
    stats_entries["Armor Class"].insert(0, player_armor_class)
    stats_entries["Armor Class"].config(state='readonly')
    
    stats_entries["Strength"].config(state='normal')
    stats_entries["Strength"].delete(0, tk.END)
    stats_entries["Strength"].insert(0, player_strength)
    stats_entries["Strength"].config(state='readonly')
    bonus_entries["Strength"].config(state='normal')
    bonus_entries["Strength"].delete(0, tk.END)
    bonus_entries["Strength"].insert(0, player_strength_number)
    bonus_entries["Strength"].config(state='readonly')
    
    
    stats_entries["Dexterity"].config(state='normal')
    stats_entries["Dexterity"].delete(0, tk.END)
    stats_entries["Dexterity"].insert(0, player_dexterity)
    stats_entries["Dexterity"].config(state='readonly')
    bonus_entries["Dexterity"].config(state='normal')
    bonus_entries["Dexterity"].delete(0, tk.END)
    bonus_entries["Dexterity"].insert(0, player_dexterity_number)
    bonus_entries["Dexterity"].config(state='readonly')
    
    stats_entries["Constitution"].config(state='normal')
    stats_entries["Constitution"].delete(0, tk.END)
    stats_entries["Constitution"].insert(0, player_constitution)
    stats_entries["Constitution"].config(state='readonly')
    bonus_entries["Constitution"].config(state='normal')
    bonus_entries["Constitution"].delete(0, tk.END)
    bonus_entries["Constitution"].insert(0, player_constitution_number)
    bonus_entries["Constitution"].config(state='readonly')
    
    stats_entries["Intelligence"].config(state='normal')
    stats_entries["Intelligence"].delete(0, tk.END)
    stats_entries["Intelligence"].insert(0, player_intelligence)
    stats_entries["Intelligence"].config(state='readonly')
    bonus_entries["Intelligence"].config(state='normal')
    bonus_entries["Intelligence"].delete(0, tk.END)
    bonus_entries["Intelligence"].insert(0, player_intelligence_number)
    bonus_entries["Intelligence"].config(state='readonly')
    
    stats_entries["Wisdom"].config(state='normal')
    stats_entries["Wisdom"].delete(0, tk.END)
    stats_entries["Wisdom"].insert(0, player_wisdom)
    stats_entries["Wisdom"].config(state='readonly')
    bonus_entries["Wisdom"].config(state='normal')
    bonus_entries["Wisdom"].delete(0, tk.END)
    bonus_entries["Wisdom"].insert(0, player_wisdom_number)
    bonus_entries["Wisdom"].config(state='readonly')
    
    stats_entries["Charisma"].config(state='normal')
    stats_entries["Charisma"].delete(0, tk.END)
    stats_entries["Charisma"].insert(0, player_charisma)
    stats_entries["Charisma"].config(state='readonly')
    bonus_entries["Charisma"].config(state='normal')
    bonus_entries["Charisma"].delete(0, tk.END)
    bonus_entries["Charisma"].insert(0, player_charisma_number)
    bonus_entries["Charisma"].config(state='readonly')

# Globální proměnné pro hráče
player_class = None
player_hp = 0
player_strength = 0
player_dexterity = 0
player_proficiency_bonus = 2
player_armor_class = 0
player_intelligence = 0
player_charisma = 0
player_constitution = 0
player_wisdom = 0
player_inventory_weapons = []
player_inventory_armors = [] 
player_inventory_potions = []
player_inventory_spells = []
weapon_bonus = 0
spell_damage = 0
# Funkce pro vybavení fightera
def vybaveni_fighter():
    global player_max_hp
    global player_hp
    global player_strength
    global player_dexterity
    global player_armor_class
    global player_dexterity_number
    global player_intelligence
    global player_constitution
    global player_wisdom
    global player_charisma
    global player_charisma_number
    global player_wisdom_number
    global player_constitution_number
    global player_intelligence_number
    global player_strength_number
    global player_dexterity_number
    global player_inventory_weapons
    global player_inventory_armors
    global player_inventory_potions
    global player_inventory_spells
    global player_money 

    player_max_hp = 13
    player_hp = 13
    player_strength = 4
    player_strength_number = 18
    player_dexterity = 1
    player_dexterity_number = 12
    player_armor_class = 10 + player_dexterity
    player_intelligence = 0
    player_intelligence_number = 0
    player_constitution = 3
    player_constitution_number = 16
    player_wisdom = 1
    player_wisdom_number = 12
    player_charisma = 1 
    player_charisma_number = 12
    player_inventory_weapons.extend(["Dlouhý meč", "Těžká kuše"])
    player_inventory_armors.extend(["Těžká zbroj"])
    player_inventory_potions.extend(["Malý léčivý lektvar"])
    player_inventory_spells.extend(["Neutuchající obrana"])
    player_money = 20
    return "Těžká zbroj, meč, malý léčivý lektvar a 20 zlatých"

# Funkce pro vybavení rangera
def vybaveni_ranger():
    global player_max_hp
    global player_hp
    global player_strength
    global player_dexterity
    global player_armor_class
    global player_dexterity_number
    global player_intelligence
    global player_constitution
    global player_wisdom
    global player_charisma
    global player_charisma_number
    global player_wisdom_number
    global player_constitution_number
    global player_intelligence_number
    global player_strength_number
    global player_dexterity_number
    global player_inventory_weapons
    global player_inventory_armors
    global player_inventory_potions
    global player_inventory_spells
    global player_money
    

    player_max_hp = 11
    player_hp = 11
    player_strength = 1
    player_strength_number = 12
    player_dexterity = 4
    player_dexterity_number = 18
    player_armor_class = 10 + player_dexterity
    player_intelligence = 1
    player_intelligence_number = 12
    player_constitution  = 1
    player_constitution_number = 12
    player_wisdom = 3
    player_wisdom_number = 16
    player_charisma = 0 
    player_charisma_number = 10
    player_inventory_weapons.extend(["Dlouhý luk", "Krátký meč"])
    player_inventory_armors.extend(["Lehká zbroj"])
    player_inventory_potions.extend(["Malý léčivý lektvar"])
    player_inventory_spells.extend(["Léčení", "Přesná trefa"])
    player_money = 20
    return "Lehká zbroj, dlouhý luk, krátký meč, malý léčivý lektvar a 20 zlatých"

# Funkce pro vybavení wizarda
def vybaveni_wizard():
    global player_max_hp
    global player_hp
    global player_strength
    global player_dexterity
    global player_armor_class
    global player_dexterity_number
    global player_intelligence
    global player_constitution
    global player_wisdom
    global player_charisma
    global player_charisma_number
    global player_wisdom_number
    global player_constitution_number
    global player_intelligence_number
    global player_strength_number
    global player_dexterity_number
    global player_inventory_weapons
    global player_inventory_armors
    global player_inventory_potions
    global player_inventory_spells
    global player_money

    player_max_hp = 7
    player_hp = 7
    player_strength = 0
    player_strength_number = 10
    player_dexterity = 2
    player_dexterity_number = 14
    player_armor_class = 10 + player_dexterity
    player_intelligence = 4
    player_intelligence_number = 18
    player_constitution = 1
    player_constitution_number = 12
    player_wisdom = 1
    player_wisdom_number = 12
    player_charisma = 1 
    player_charisma_number = 12
    player_inventory_weapons.extend(["Hůl"])
    player_inventory_armors.extend([])
    player_inventory_potions.extend(["Malý léčivý lektvar"])
    player_inventory_spells.extend(["Naváděné střely", "Mágův štít"])
    player_money = 20
    return "Hůl, malý léčivý lektvar a 20 zlatých"
    
# Funkce pro kouzla wizarda
def kouzla_wizard():
    return "Naváděné střely, Mágův štít"


# Výběr classy
def choose_class():
    global player_class
    class_choice = var_class.get()
    if class_choice == 1:
        player_class = "fighter"
        vybaveni_text = f"Zvolili jste si fightera. Máte: {vybaveni_fighter()}"
    elif class_choice == 2:
        player_class = "ranger"
        vybaveni_text = f"Zvolili jste si rangera. Máte: {vybaveni_ranger()}"
    elif class_choice == 3:
        player_class = "wizard"
        vybaveni_text = f"Zvolili jste si wizarda. Máte: {vybaveni_wizard()}.\nK tomu máte ještě kouzla: {kouzla_wizard()}"
        # Skrytí prvků pro výběr classy
    class_label.pack_forget()
    fighter_radio.pack_forget()
    ranger_radio.pack_forget()
    wizard_radio.pack_forget()
    confirm_button.pack_forget()

    type_text(text_output, vybaveni_text + "\n")
    ok_button.pack()
    update_player_stats()
    update_inventory_weapons()
    update_inventory_armors()
    update_inventory_potions()
    update_inventory_spells()
    update_money()
    

# boj
# boj
# Definice goblina
goblin_health = 10
goblin_armor_class = 12
goblin_attack_fight = 3
goblin_dexterity = 2  # Bonus k iniciativě
goblin_debuff = 0

# Funkce pro určení vlastnosti pro útok
def get_attack_bonus():
    if player_class == "ranger":
        return player_dexterity
    elif player_class == "wizard":
        return player_intelligence
    else:
        return player_strength
# Pouze text
def get_attack_bonus_text():


    if player_class == "ranger":
        return "Obratnost"
    elif player_class == "wizard":
        return "Inteligence"
    else:
        return "Síla"
    

def meeting_with_goblin():
    ok_button.pack_forget()
    type_text(text_output, "Hned co jste dorazili na cestu se vám do cesty postavil goblin co na vás zaútočil.\n")
    start_fight.pack()
    start_fight()
def second_act():
    type_text(text_output, "pokračuješ dál")

#Boj s jedním goblinem
def fight_with_one_goblin():
    global goblin_health, player_hp
    start_fight.pack_forget()
    initiative_label.pack()
    entry_initiative.pack()
    initiative_button.pack()

def process_initiative():
    initiative_label.pack_forget()
    entry_initiative.pack_forget()
    initiative_button.pack_forget()

    change_game_status("Combat")

        

    roll_initiative = int(entry_initiative.get())
    player_initiative = roll_initiative + player_dexterity
    goblin_initiative = random.choice(d20) + goblin_dexterity
    type_text(text_output, f"Vaše iniciativa: {player_initiative} (hod kostkou: {roll_initiative} + dexterity: {player_dexterity})\n")
    type_text(text_output, f"Iniciativa goblina: {goblin_initiative}\n")

    if player_initiative >= goblin_initiative:
        type_text(text_output, "Útočíte první!\n")
        # Zobrazení tlačítka pro útok
        attack_label.pack()
        entry_attack.pack()
        attack_button.pack()
    else:
        type_text(text_output, "Goblin útočí první!\n")
        goblin_attack()

def player_attack():
    global goblin_health
    attack_label.pack_forget()
    entry_attack.pack_forget()
    attack_button.pack_forget()

    attack = int(entry_attack.get())
    attack_bonus = get_attack_bonus()
    ability = get_attack_bonus_text()
    
    

    attack_result = attack + attack_bonus + player_proficiency_bonus + weapon_bonus
    if attack == 20:
        type_text(text_output,f"Kritický zásah! {attack_result} (Hod kostkou: {attack} + {ability} + {attack_bonus} + Proficiency bonus: {player_proficiency_bonus} + síla zbraně: {weapon_bonus})\n")
        damage_label.pack()
        entry_damage.pack()
        damage_button.pack()
    else: 
        type_text(text_output, f"{attack_result} (Hod kostkou: {attack} + {ability} + {attack_bonus} + Proficiency bonus: {player_proficiency_bonus} + síla zbraně: {weapon_bonus})\n")
        if attack_result >= goblin_armor_class:
            type_text(text_output, "Zásah!\n")
            damage_label.pack()
            entry_damage.pack()
            damage_button.pack()
        else:
            type_text(text_output, "Netrefil ses, nyní bude útočit goblin\n")
            goblin_attack()


def player_damage():
    global goblin_health
    global spell_damage
    damage_label.pack_forget()
    entry_damage.pack_forget()
    damage_button.pack_forget()

    damage_roll = int(entry_damage.get())
    attack_bonus = get_attack_bonus()
    ability = get_attack_bonus_text()


    if int(entry_attack.get()) == 20:  # Kritický zásah
        total_damage = (damage_roll * 2) + attack_bonus
        type_text(text_output, f"Zasáhl si za: {total_damage} (Hod kostkou *2: {damage_roll} + {ability}: {attack_bonus})\n")
    else:
        total_damage = damage_roll + attack_bonus
        type_text(text_output, f"Zasáhl si za: {total_damage} (Hod kostkou: {damage_roll} + {ability}: {attack_bonus})\n")

    total_damage += spell_damage  # Přidání spell_damage k celkovému poškození
    spell_damage = 0  # Resetování spell_damage po použití

    
    goblin_health -= total_damage
    if goblin_health <= 0:
        type_text(text_output, "Zabil jsi goblina\n")
        messagebox.showinfo("Vítězství", "Zabil jsi goblina!")
        second_act()
    else:
        type_text(text_output, f"Goblin má nyní {goblin_health} HP. Goblin tvůj útok přežil. Nyní bude útočit goblin\n")
        goblin_attack()

def spell_attack(damage):
    global goblin_health
    global spell_damage
    goblin_health -= damage
    if goblin_health <= 0:
        type_text(text_output, f"Zabil jsi goblina kouzlem. Způsobil jsi: {damage} damage.")
        messagebox.showinfo("Vítězství", "Zabil jsi goblina kouzlem!")
        second_act()
    else:
        type_text(text_output, f"Goblin má nyní {goblin_health} HP. Goblin tvůj kouzelný útok přežil. Nyní bude útočit goblin\n")
        goblin_attack()
        
def goblin_attack():
    global player_hp
    if goblin_health > 0:
        result = random.choice(d20)
        attack_result = result + goblin_attack_fight + goblin_debuff
        type_text(text_output, f"Goblin útočí: {attack_result} (Hod kostkou: {result} + goblinův bonus: {goblin_attack_fight} + {goblin_debuff})\n")
        if attack_result >= player_armor_class:
            type_text(text_output, "Goblin tě zasáhl!\n")
            damage_roll = random.choice(d6)
            if result == 20:  # Kritický zásah
                total_damage = (damage_roll * 2) + goblin_attack_fight
                type_text(text_output, f"Goblin ti způsobil {total_damage} poškození (Hod kostkou *2: {damage_roll} + goblinův bonus: {goblin_attack_fight})\n")
            else:
                total_damage = damage_roll + goblin_attack_fight
                type_text(text_output, f"Goblin ti způsobil {total_damage} poškození (Hod kostkou: {damage_roll} + goblinův bonus: {goblin_attack_fight})\n")
            player_hp -= total_damage
            if player_hp <= 0:
                type_text(text_output, "Byl jsi zabit goblinem\n")
                messagebox.showinfo("Prohra", "Byl jsi zabit goblinem!")
                root.quit()  # konec
        else:
            type_text(text_output, "Goblin tě netrefil\n")
        if player_hp > 0:
            attack_label.pack()
            entry_attack.pack()
            attack_button.pack()
        update_player_stats()

    # boj konec
    # boj konec

    # inventář
    # inventář
text_output_inventory = tk.Text(right_frame, height=30, width=100)

inventory_weapons_label = tk.Label(right_frame, text="Zbraně", font=("Helvetica", 13, "bold"))
inventory_weapons_label.pack(pady=1)
inventory_listbox_weapons = tk.Listbox(right_frame, selectmode=tk.SINGLE, heigh=6)
inventory_listbox_weapons.pack(fill=None, expand=False)
inventory_listbox_weapons.config(font=("Helvetica", 10, "bold"))

# Funkce pro výběr zbraně
def update_damage_label():
    global current_weapon
    if current_weapon == "Dlouhý meč":
        damage_label.config(text ="Hoď D10 a zadej výsledek")

    elif current_weapon == "Těžká kuše":
        damage_label.config(text ="Hoď D8 a zadej výsledek")
    elif current_weapon == "Krátký meč":
        damage_label.config(text ="Hoď D6 a zadej výsledek")
    elif current_weapon == "Dlouhý luk":
        damage_label.config(text ="Hoď D10 a zadej výsledek")

def select_weapons():
    global current_weapon
    selected_weapons = inventory_listbox_weapons.curselection()
    if selected_weapons:
        current_weapon = inventory_listbox_weapons.get(selected_weapons)
        type_text(text_output, f"Zvolili jste si zbraň: {current_weapon}\n")
        update_current_weapon_display()

    if current_weapon == "Dlouhý meč":
        global weapon_bonus
        global goblin_debuff
        weapon_bonus = 2
        update_player_stats()
        update_damage_label()
    elif current_weapon == "Těžká kuše":
        goblin_debuff = -2
        update_player_stats()
        update_damage_label()
    elif current_weapon == "Krátký meč":
        weapon_bonus = 2
        update_player_stats()
        update_damage_label()
    elif current_weapon == "Dlouhý luk":
        goblin_debuff = -2
        update_player_stats()
        update_damage_label()

# Tlačítko pro vybavení zbraně
select_weapons_button = tk.Button(right_frame, text="Vyzbrojit se", command=select_weapons)
select_weapons_button.pack(pady=5)

inventory_armors_label = tk.Label(right_frame, text="Zbroje", font=("Helvetica", 13, "bold"))
inventory_armors_label.pack(pady=1)
inventory_listbox_armors = tk.Listbox(right_frame, selectmode=tk.SINGLE, heigh=6)
inventory_listbox_armors.pack(fill=None, expand=False)
inventory_listbox_armors.config(font=("Helvetica", 10, "bold"))

# Funkce pro výběr armoru
def select_armors():
    selected_armors = inventory_listbox_armors.get(inventory_listbox_armors.curselection())
    if selected_armors == "Těžká zbroj":
        global player_armor_class
        player_armor_class = 10 + player_dexterity + 5
        type_text(text_output, f"Oblékli jste si těžkou zbroj. Vaše Armor Class je nyní: {player_armor_class}, 10 + vaše dexterity: {player_dexterity} + těžká zbroj: 5.")
        update_player_stats()

    if selected_armors == "Lehká zbroj":
        player_armor_class = 10 + player_dexterity + 1
        type_text(text_output, f"Oblékli jste si lehkou zbroj. Vaše Armor Class je nyní: {player_armor_class}, 10 + vaše dexterity: {player_dexterity} + lehká zbroj: 1.")
        update_player_stats()

# Tlačítko pro obléknutí armoru
select_armors_button = tk.Button(right_frame, text="Obléknout armor", command=select_armors)
select_armors_button.pack(pady=5)

# Funkce pro výběr spellu
inventory_spells_label = tk.Label(right_frame, text="Schopnosti a kouzla", font=("Helvetica", 13, "bold"))
inventory_spells_label.pack(pady=1)
inventory_listbox_spells = tk.Listbox(right_frame, selectmode=tk.SINGLE, heigh=6)
inventory_listbox_spells.pack(fill=None, expand=False)
inventory_listbox_spells.config(font=("Helvetica", 10, "bold"))

def select_spell():
    global spell_damage
    selected_spells = inventory_listbox_spells.get(inventory_listbox_spells.curselection())
    # Wizard
    if selected_spells == "Mágův štít":
        global player_armor_class
        player_armor_class = 10 + player_dexterity + 3
        type_text(text_output, f"Zakouzlili jste na sebe mágův štít. Máte + 3 k armor class, ta je nyní {player_armor_class}")
        update_player_stats()
    if selected_spells == "Naváděné střely":
        global spell_damage
        global game_state
        if game_state == "Combat":
            result_misile = simpledialog.askinteger("Hod kostkou", "Hoď si 3d4 a zadej výsledek:")
            if result_misile is not None:
                spell_damage = result_misile + 6
                type_text(text_output, f"Zasáhl jsi za {spell_damage} poškození.")
                player_attack(spell_damage)
        else:
            type_text(text_output, f"Toto kouzlo nemůžeš použít mimo boj a mimo svůj tah.")

# Tlačítko aktivování spellu
select_spell_button = tk.Button(right_frame, text="Použít schopnost", command=select_spell)
select_spell_button.pack(pady=0)


# Lektvar
inventory_potions_label = tk.Label(right_frame, text="Lektvary", font=("Helvetica", 13, "bold"))
inventory_potions_label.pack(pady=1)
inventory_listbox_potions = tk.Listbox(right_frame, selectmode=tk.SINGLE, heigh=6)
inventory_listbox_potions.pack(fill=None, expand=False)
inventory_listbox_potions.config(font=("Helvetica", 10, "bold"))

# Funkce pro výběr lektvaru
def select_potions():
    selected_potions = inventory_listbox_potions.get(inventory_listbox_potions.curselection())
    if selected_potions == "Malý léčivý lektvar":
        result = simpledialog.askinteger("Hod kostkou", "Hoď si 2d4 + 2 a zadej výsledek:")
        if result is not None:
            heal_player(result)
            player_inventory_potions.remove(selected_potions)  # Odstraní lektvar ze seznamu
            update_inventory_potions()
            update_player_stats()

def heal_player(amount):
    global player_hp
    player_hp += amount
    if player_hp > player_max_hp:
        player_hp = player_max_hp
    type_text(text_output, f"Vaše zdraví bylo obnoveno o {amount} HP. Nyní máte {player_hp} HP.")
    update_player_stats()

# Tlačítko pro výběr lektvaru
select_potions_button = tk.Button(right_frame, text="Vypít lektvar", command=select_potions)
select_potions_button.pack(pady=0)


# Přidání položek do inventáře
def update_inventory_weapons():
    inventory_listbox_weapons.delete(0, tk.END)
    for item in player_inventory_weapons:
        inventory_listbox_weapons.insert(tk.END, item)

def update_inventory_armors():
    inventory_listbox_armors.delete(0, tk.END)
    for item in player_inventory_armors:
        inventory_listbox_armors.insert(tk.END, item)

def update_inventory_potions():
    inventory_listbox_potions.delete(0, tk.END)
    for item in player_inventory_potions:
        inventory_listbox_potions.insert(tk.END, item)

def update_inventory_spells():
    inventory_listbox_spells.delete(0, tk.END)
    for item in player_inventory_spells:
        inventory_listbox_spells.insert(tk.END, item)

# Mince
def update_money():
    money_entry.config(state='normal')
    money_entry.delete(0, tk.END)
    money_entry.insert(0, player_money)
    money_entry.config(state='readonly')
# Vytvoření prostoru pro zlaté mince
money_frame = tk.Frame(right_frame)
money_frame.pack(side=tk.BOTTOM, pady=10)
money_label = tk.Label(money_frame, text="Zlaté mince:", font=font_style_1)
money_label.pack(side=tk.LEFT)
money_entry = tk.Entry(money_frame, justify='center', state='readonly', width=10, font=font_style_1)
money_entry.pack(side=tk.RIGHT)

    # inventář
    # inventář

# Výběr classy
var_class = tk.IntVar()
class_label = tk.Label(bottom_frame, text="Vyber si classu")
class_label.pack()
fighter_radio = tk.Radiobutton(bottom_frame, text="Fighter", variable=var_class, value=1)
fighter_radio.pack()
ranger_radio = tk.Radiobutton(bottom_frame, text="Ranger", variable=var_class, value=2)
ranger_radio.pack()
wizard_radio = tk.Radiobutton(bottom_frame, text="Wizard", variable=var_class, value=3)
wizard_radio.pack()
confirm_button = tk.Button(bottom_frame, text="Potvrdit výběr", command=choose_class)
confirm_button.pack()

ok_button = tk.Button(bottom_frame, text="OK", command=meeting_with_goblin)
start_fight = tk.Button(bottom_frame, text="Začít boj s goblinem", command=fight_with_one_goblin)
initiative_button = tk.Button(bottom_frame, text="Zadat hod na iniciativu",command=process_initiative)
attack_button = tk.Button(bottom_frame, text ="Zadat hod na útok",command=player_attack)
damage_button = tk.Button(bottom_frame, text = "Zadat hod na damage",command=player_damage)

initiative_label = tk.Label(bottom_frame, text="Hoďte d20 na iniciativu a zadejte výsledek")
entry_initiative = tk.Entry(bottom_frame)

attack_label = tk.Label(bottom_frame, text="Hoď d20 na útok a zadejte výsledek")
entry_attack = tk.Entry(bottom_frame)

damage_label = tk.Label(bottom_frame, text= "Hoď damage d10 a zadejte výsledek")
entry_damage = tk.Entry(bottom_frame)

# Spuštění hlavní smyčky
root.mainloop()

