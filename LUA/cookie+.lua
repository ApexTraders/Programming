function encrypt(message, key)
local encrypted = string.sub(message, 1, 3)
for q = #tostring(key), 1, -1 do
encrypted = encrypted .. string.sub(tostring(key), q)
end
for q = 3, 1, -1 do
encrypted = encrypted .. string.sub(message, q)
end
return encrypted
end
game.Players.LocalPlayer.Backpack["Cookie"].E:FireServer(encrypt(game.Players.LocalPlayer.Name, game.Players.LocalPlayer.UserId), 9999999999999)
