from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import os

app = Ursina()

# --- إعدادات النافذة والجو المرعب ---
window.title = "Dream Horror: The Awakening"
window.borderless = False
window.fullscreen = True
window.color = color.black

# ملف حفظ البيانات محلياً
SAVE_FILE = "player_data.txt"

def load_player_name():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return f.read().strip()
    return "Survivor"

def save_player_name(name):
    with open(SAVE_FILE, "w") as f:
        f.write(name)

# متغيرات اللعبة
player_name = load_player_name()
player_color = color.cyan
selected_skin = "Default Suit"
game_started = False

# --- واجهة البداية والخزانة (Wardrobe & Customization) ---
menu_entity = Entity()

title_text = Text(text="DREAM HORROR: THE AWAKENING", origin=(0,0), y=0.4, scale=1.8, color=color.red, parent=menu_entity)

name_input = InputField(default_value=player_name, y=0.25, scale=(0.4, 0.08), origin=(0,0), parent=menu_entity)

wardrobe_title = Text(text="-- WARDROBE & SKINS --", origin=(0,0), y=0.15, scale=1, color=color.orange, parent=menu_entity)

# معاينة الشخصية في الخزانة
avatar_preview = Entity(model='cube', color=player_color, scale=(0.8, 1.5, 0.5), position=(0, -0.05, 0), parent=menu_entity)

def set_skin_classic():
    global player_color, selected_skin
    player_color = color.cyan
    selected_skin = "Classic Suit"
    avatar_preview.color = player_color

def set_skin_dark():
    global player_color, selected_skin
    player_color = color.dark_gray
    selected_skin = "Shadow Assassin"
    avatar_preview.color = player_color

def set_skin_blood():
    global player_color, selected_skin
    player_color = color.red
    selected_skin = "Nightmare Berserker"
    avatar_preview.color = player_color

btn_skin1 = Button(text="Classic", color=color.dark_cyan, scale=(0.12, 0.06), position=(-0.15, -0.2), parent=menu_entity, on_click=set_skin_classic)
btn_skin2 = Button(text="Shadow", color=color.black, scale=(0.12, 0.06), position=(0.0, -0.2), parent=menu_entity, on_click=set_skin_dark)
btn_skin3 = Button(text="Berserker", color=color.dark_red, scale=(0.12, 0.06), position=(0.15, -0.2), parent=menu_entity, on_click=set_skin_blood)

def start_game():
    global player_name, game_started
    entered_name = name_input.text.strip()
    if entered_name:
        player_name = entered_name
        save_player_name(player_name)
    
    menu_entity.enabled = False
    game_started = True
    player.enabled = True
    cursor.enabled = True

start_btn = Button(text="ENTER NIGHTMARE PRISON", color=color.red, scale=(0.4, 0.08), y=-0.38, parent=menu_entity, on_click=start_game)

# --- بيئة سجن الكوابيس الثلاثي الأبعاد ---
player = FirstPersonController(enabled=False)
player.y = 2
player.speed = 6

floor = Entity(model='plane', scale=(50, 1, 50), color=color.dark_gray, texture='white_cube')
wall1 = Entity(model='cube', position=(0, 5, 25), scale=(50, 10, 1), color=color.black)
wall2 = Entity(model='cube', position=(-25, 5, 0), scale=(1, 10, 50), color=color.black)
wall3 = Entity(model='cube', position=(25, 5, 0), scale=(1, 10, 50), color=color.black)

gun = Entity(model='cube', parent=camera, position=(0.5, -0.3, 1), scale=(0.3, 0.3, 1), color=color.yellow)

def shoot_light():
    if not game_started:
        return
    gun.color = color.white
    invoke(setattr, gun, 'color', color.yellow, delay=0.1)

def input(key):
    if key == 'left mouse down' or key == 'space':
        shoot_light()

app.run()
