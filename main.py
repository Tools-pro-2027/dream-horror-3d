from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import socket
import threading

app = Ursina()

# إعدادات النافذة والجو السينمائي المرعب ثلاثي الأبعاد
window.title = "Dream Horror: 3D Third Person Style"
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
window.color = color.black

# بناء عالم القصر أو الممر المرعب (3D Environment)
floor = Entity(model='plane', scale=(60, 1, 60), color=color.dark_gray, texture='white_cube')
roof = Entity(model='plane', position=(0, 5, 0), scale=(60, 1, 60), color=color.black)

# جدران المتاهة المرعبة
wall_left = Entity(model='cube', position=(-30, 2.5, 0), scale=(1, 5, 60), color=color.rgb(20, 20, 20))
wall_right = Entity(model='cube', position=(30, 2.5, 0), scale=(1, 5, 60), color=color.rgb(20, 20, 20))
wall_back = Entity(model='cube', position=(0, 2.5, 30), scale=(60, 5, 1), color=color.rgb(20, 20, 20))

# تحكم اللاعب (منظور ثلاثي احترافي)
player = FirstPersonController()
player.x = 0
player.y = 2
player.z = 0
player.speed = 10
player.cursor.visible = True

# إضافة عنصر رعب متحرك داخل الممر
enemy = Entity(model='cube', color=color.red, scale=(1.5, 3, 1.5), position=(0, 1.5, 20))

def update():
    # حركة بسيطة للرعب تقترب من اللاعب
    if distance(player.position, enemy.position) < 25:
        enemy.look_at(player.position)
        enemy.z -= 2 * time.dt

# واجهة النصوص على الشاشة
info_text = Text(text="[ممر الأبعاد الثلاثية - تجنب الكابوس]", position=(-0.8, 0.45), scale=1.3, color=color.rgb(220, 0, 0))

# سيرفر الشبكة المحلية للاعبين عبر نقطة الاتصال (LAN Hotspot)
def start_lan_server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 5000))
        s.listen(2)
        while True:
            conn, addr = s.accept()
            conn.close()
    except:
        pass

threading.Thread(target=start_lan_server, daemon=True).start()

app.run()
