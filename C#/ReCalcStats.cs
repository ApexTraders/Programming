using System;
using RoR2;
using Harmony;
using BepInEx;
using UnityEngine;
using UnityEngine.Networking;


namespace AttackSpeed
{
    [BepInDependency("com.bepis.r2api")]
    [BepInPlugin("com.zalol.Maxduration", "AttackSpeed", "1.0.0")]
    public class AttackSpeed : BaseUnityPlugin
    {
        public void Awake()
        {
            Chat.AddMessage("AttackSpeedFucker Loaded");
            On.RoR2.CharacterBody.RecalculateStats += (orig, self) =>
            { 
                if (self == LocalUserManager.GetFirstLocalUser().cachedBody)
                {
                    self.baseAttackSpeed = 500f;
                    self.baseDamage = float.MaxValue;
                    self.baseAcceleration = 500f;
                    self.levelMaxHealth = 9999f;
                     
                }
                orig(self);
            };
        }

    }

}


