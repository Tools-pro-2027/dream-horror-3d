from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import socket
import threading

app = Ursina()

# --- إعدادات النافذة والجو المرعب ---
window.title = "Dream Horror: The Awakening"
window.borderless = False
window.fullscreen = True
window.color = color.black

# متغيرات اللعبة والشخصية
player_name = "Player"
player_color = color.cyan
game_started = False

# --- واجهة البداية (إدخال الاسم وتخصيص الشخصية) ---
def start_game():
    global player_name, player_color, game_started
    player_name = name_input.text if name_input.text else "Survivor"
    
    # إخفاء قائمة البداية
    menu_entity.enabled = False
    game_started = True
    
    # تفعيل اللاعب والبيئة المرعبة
    player.enabled = True
    cursor.enabled = True
    print(f"Game started by: {player_name}")

# شاشة القائمة الرئيسية (تصميم روبلوكس مصغر)
menu_entity = Entity()

title_text = Text(text="DREAM HORROR: THE AWAKENING", origin=(0,0), y=0.3, scale=2, color=color.red, parent=menu_entity)
sub_text = Text(text="Nightmare Prison Edition", origin=(0,0), y=0.2, scale=1, color=color.light_gray, parent=menu_entity)

name_input = InputField(default_value="Player1", y=0.0, scale=(0.4, 0.08), origin=(0,0), parent=menu_entity)

# أزرار تخصيص لون الشخصية (ستايل روبلوكس)
def set_color_red():
    global player_color
    player_color = color.red
    avatar_preview.color = player_color

def set_color_cyan():
    global player_color
    player_color = color.cyan
    avatar_preview.color = player_color

def set_color_green():
    global player_color
    player_color = color.green
    avatar_preview.color = player_color

btn_red = Button(text="Red", color=color.dark_red, scale=(0.12, 0.06), position=(-0.15, -0.15), parent=menu_entity, on_click=set_color_red)
btn_cyan = Button(text="Cyan", color=color.dark_cyan, scale=(0.12, 0.06), position=(0.0, -0.15), parent=menu_entity, on_click=set_color_cyan)
btn_green = Button(text="Green", color=color.dark_green, scale=(0.12, 0.06), position=(0.15, -0.15), parent=menu_entity, on_click=set_color_green)

# معاينة الشخصية
avatar_preview = Entity(model='cube', color=player_color, scale=(0.8, 1.5, 0.5), position=(0, -0.3, 0), parent=menu_entity)

start_btn = Button(text="ENTER NIGHTMARE", color=color.red, scale=(0.4, 0.08), y=-0.4, parent=menu_entity, on_click=start_game)


# --- بيئة اللعب (سجن الكوابيس الثلاثي الأبعاد) ---
player = FirstPersonController(enabled=False)
player.y = 2
player.speed = 6

# أرضية السجن
floor = Entity(model='plane', scale=(50, 1, 50), color=color.dark_gray, texture='white_cube')

# جدران الزنزانة المرعبة
wall1 = Entity(model='cube', position=(0, 5, 25), scale=(50, 10, 1), color=color.black)
wall2 = Entity(model='cube', position=(-25, 5, 0), scale=(1, 10, 50), color=color.black)
wall3 = Entity(model='cube', position=(25, 5, 0), scale=(1, 10, 50), color=color.black)

# مسدس الضوء (Light Gun) المرتبط باللاعب
gun = Entity(model='cube', parent=camera, position=(0.5, -0.3, 1), scale=(0.3, 0.3, 1), color=color.yellow)

# شعاع الضوء للقضاء على الأشباح
def shoot_light():
    if not game_started:
        return
    gun.color = color.white
    invoke(setattr, gun, 'color', color.yellow, delay=0.1)
    print("Light ray shot fired against nightmares!")

def input(key):
    if key == 'left mouse down' or key == 'space':
        shoot_light()

app.run()
