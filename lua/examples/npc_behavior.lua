-- npc_behavior.lua

npc = {
    name = "CyberGuard",
    health = 100,
    attack_power = 20
}

function npc_attack(target)
    print(npc.name .. " attacks " .. target.name .. "!")
    local damage = calculate_damage(npc.attack_power, target.defense)
    target.health = target.health - damage
    if target.health <= 0 then
        print(target.name .. " is defeated!")
    else
        print(target.name .. " has " .. target.health .. " health.")
    end
end
