using System;
using UnityEngine.Networking;
using UnityEditor;
using RoR2;
using BepInEx;


namespace rorhack
{
    [BepInDependency("com.bepis.r2api")]
    [BepInPlugin("com.zalol.Timecrystal", "Timecrystal", "1.0.0")]
    class TimeCrystal : BaseUnityPlugin
    {
        void Awake()
        {
            On.EntityStates.Destructible.TimeCrystalDeath.FixedUpdate += (orig, self) =>
            {
                Chat.AddMessage("hooked");
                self.GetType().GetField("stopwatch").SetValue(self, float.MaxValue);
                orig(self);
                Chat.AddMessage("something is wrong");
            };
        }
    }
}
