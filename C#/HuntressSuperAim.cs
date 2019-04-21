using System;
using RoR2;
using BepInEx;
using UnityEngine;
using UnityEngine.Networking;


namespace GlaiveDur
{
    [BepInDependency("com.bepis.r2api")]
    [BepInPlugin("com.zalol.HuntressAim", "HuntressAim", "1.0.0")]
     class HuntressAim : BaseUnityPlugin
    {
         void Main()
        {
            Chat.AddMessage("HuntressAimFucker Loaded");          
            On.RoR2.HuntressTracker.SearchForTarget += (orig, self, aimRay) =>
            {
                self.maxTrackingAngle = 360f;
                self.maxTrackingDistance = float.MaxValue;
                orig(self, aimRay);
            };
        }
    }

}
