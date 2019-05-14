using System;
using System.Reflection;
using UnityEngine.Networking;
using UnityEditor;
using RoR2;
using BepInEx;


namespace Chance
{
    [BepInDependency("com.bepis.r2api")]
    [BepInPlugin("com.zalol.Timecrystal", "ChanceTimer", "1.0.0")]
    class ChanceTimer : BaseUnityPlugin
    {
        void Awake()
        {
            On.RoR2.ShrineChanceBehavior.FixedUpdate += (orig, self) =>
            {
                self.costMultiplierPerPurchase = 0f;
                self.maxPurchaseCount = int.MaxValue;
                typeof(ShrineChanceBehavior).GetField("refreshTimer", BindingFlags.NonPublic | BindingFlags.Instance).SetValue(self, 0);
                orig(self);
            };
        }
    }
}
