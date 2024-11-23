-- dialog_system.lua

function start_dialog(npc_name, dialog_lines)
    print(npc_name .. ":")
    for _, line in ipairs(dialog_lines) do
        print("> " .. line)
    end
end

dialog_lines = {
    "Hello, world!",
}
start_dialog("GameSimulation", dialog_lines)