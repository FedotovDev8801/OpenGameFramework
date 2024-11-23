-- level_generator.lua

function generate_level(width, height)
    local level = {}
    for y = 1, height do
        level[y] = {}
        for x = 1, width do
            level[y][x] = math.random(0, 1)
        end
    end
    return level
end

function print_level(level)
    for y = 1, #level do
        local row = ""
        for x = 1, #level[y] do
            row = row .. (level[y][x] == 1 and "#" or " ")
        end
        print(row)
    end
end
