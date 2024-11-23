-- inv_system.lua

player_inventory = {}

function add_item_to_inventory(item_name, quantity)
    if player_inventory[item_name] then
        player_inventory[item_name] = player_inventory[item_name] + quantity
    else
        player_inventory[item_name] = quantity
    end
    print(item_name .. " is added to inventory. Count: " .. player_inventory[item_name])
end

function remove_item_from_inventory(item_name, quantity)
    if not player_inventory[item_name] then
        print("Item " .. item_name .. " is not in inventory.")
        return
    end
    player_inventory[item_name] = player_inventory[item_name] - quantity
    if player_inventory[item_name] <= 0 then
        player_inventory[item_name] = nil
        print("Item " .. item_name .. " is deleted from inventory.")
    else
        print(item_name .. " now is in count: " .. player_inventory[item_name])
    end
end
