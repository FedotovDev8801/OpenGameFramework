import lua
from lupa import LuaRuntime

lua = LuaRuntime(unpack_returned_tuples=True)

lua_code = """
function greet(name)
    return "Hi, " .. name .. "! Welcome to GameSimulation community!"
end
"""

lua.execute(lua_code)

greet = lua.globals().greet
print(greet("FedotovDev"))

def execute_lua_script(script_path):
    with open(script_path, 'r') as script:
        lua.execute(script.read())

lua_script = """
function calculate_damage(attack, defense)
    return attack * 1.5 - defense
end
"""
with open("damage_calculator.lua", "w") as file:
    file.write(lua_script)

execute_lua_script("damage_calculator.lua")
calculate_damage = lua.globals().calculate_damage
print("Урон: ", calculate_damage(100, 30))