using System;
using System.Reflection;
using RoR2;
using BepInEx;
using UnityEngine;
using UnityEngine.Networking;


namespace Cooldown
{
    [BepInDependency("com.bepis.r2api")]
    [BepInPlugin("com.zalol.Cooldown", "CooldownMod", "1.0.0")]
    public class Cooldown : BaseUnityPlugin
    {
        public void Awake()
        {
            Chat.AddMessage("CooldownFucker Loaded");
             On.RoR2.GenericSkill.FixedUpdate += (orig, self) =>
            {
                self.Reset();
                //typeof(GenericSkill).GetField("rechargeStopwatch", BindingFlags.NonPublic | BindingFlags.Instance).SetValue(self, 15);
                orig(self);
            };
        }
    }
}
