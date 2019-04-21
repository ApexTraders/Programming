using System;
using RoR2;
using Harmony;
using BepInEx;
using UnityEngine;
using UnityEngine.Networking;


namespace HuntressSuperAim
{
    [BepInDependency("com.bepis.r2api")]
    [BepInPlugin("com.zalol.HuntressSuperAim", "HuntressSuperAIm", "1.0.0")]
    public class HuntressSuperAim : BaseUnityPlugin
    {
        public void Awake()
        {
            Chat.AddMessage("Loaded MyModName!");
            On.EntityStates.Huntress.ArrowRain.OnEnter += (orig, self) =>
        {
            EntityStates.Huntress.ArrowRain.arrowRainRadius = 512f;
            orig(self);
        };
    }
}
}

