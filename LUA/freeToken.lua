_G.token = true
while _G.token do
wait(1) -- For Crash
local d = game.Players.LocalPlayer.Character.HumanoidRootPart
for i,v in pairs(game.Workspace:GetChildren()) do
    if v.name == "Main Area" then
        for _, b in pairs(v.Tokens:GetChildren()) do
            if b.name == "Token" then
                b.CFrame = d.CFrame
end
end
end
end
end
