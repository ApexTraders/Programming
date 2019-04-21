using System;
using RoR2;
using Harmony;
using BepInEx;
using UnityEngine;
using UnityEngine.Networking;


namespace Cooldown
{
    [BepInDependency("com.bepis.r2api")]
    [BepInPlugin("com.zalol.Cooldown", "CooldownMod", "1.0.0")]
    public class Cooldown : BaseUnityPlugin
    {
        void Main()
        {
            Chat.AddMessage("CooldownMod has Loaded");
            HarmonyInstance.DEBUG = true;
            var harmony = HarmonyInstance.Create("com.zal.ror2.Cooldown");
            var _Cooldown = new HarmonyMethod(AccessTools.Method(typeof(Cooldown), nameof(Nocooldown)));

            harmony.Patch(
                AccessTools.Method(typeof(GenericSkill), "FixedUpdate"),

                prefix: _Cooldown
                );
            Chat.AddMessage("hooked");
        }

        void Nocooldown(GenericSkill __instance)
        {
            Chat.AddMessage("We loaded");
            __instance.Reset();
        }
    }
}
