import keyboard,json

global keymap
with open('./keymap.json') as f:
  keymap = json.load(f)

def change_key(bind):
  if key := keymap.get(bind.name):
    keyboard.send(key)
  else:
    keyboard.send(bind.name)

for key in keymap.keys():
  keyboard.on_press_key(key,change_key,True)

keyboard.wait()

