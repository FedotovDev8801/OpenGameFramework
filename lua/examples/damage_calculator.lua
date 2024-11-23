-- damage_calculator.lua

function calculate_damage(attack, defense)
    local base_damage = attack * 1.5
    local final_damage = base_damage - defense
    if final_damage < 0 then
        return 0
    end
    return final_damage
end
