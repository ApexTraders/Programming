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
        void Main()
        {
            var harmony = HarmonyInstance.Create("com.zal.ror2.HuntressSuperAim");
            var _HuntressSuperAim = new HarmonyMethod(AccessTools.Method(typeof(HuntressSuperAim), nameof(HuntressSuperAim)));

            harmony.Patch(
                AccessTools.Method(typeof(HuntressTracker), "SearchforTarget"),

                prefix: _HuntressSuperAim
                );
        }
        public void HuntressAim(HuntressTracker __instance)
        {
            __instance.maxTrackingAngle = 360f;
            __instance.maxTrackingDistance = 999f;
        }
    }
}

