# Event 006 roster checkpoint effects

## `independence_wave_apply_roster_checkpoint`

Country-scope helper for the synchronous Event 006 package-roster receipt.
The helper is called after a package-specific setup trigger has selected the package country.
It has no explicit inputs and reads the current `THIS` country scope.

The helper preserves the former `chaosx.nr6.350` immediate branches exactly.
It writes the TRA, MNT, KOS, KUB, TAT, BSK, RUT, MAC, AXX, BAX, BBX, BOS, NAV, and GLC roster checkpoint flags when their package and command-roster triggers pass.
It applies the MNT political-carrier portrait overrides for `MNT_kristo_popovic` and `MNT_blazo_jovanovic`.
It applies the BSK `Yakov Bykin` portrait override once behind `independence_wave_bsk_portrait_override`.
It applies the RUT `Augustin Voloshyn` portrait override for the Event 006 package scope.

The helper does not release countries, create characters, change package costs, mutate central attestation, open the pre-event UI, or use event targets.
It has no constants or tuning table because the checkpoint is a fixed roster receipt and the package-specific triggers remain the source of eligibility.
There is no event-target cleanup plan because the helper does not persist scope pointers.

## Call sites and migration

The active package setup callers use the helper directly in Bosnia, Bashkiria, Iberia, IW043/IW058, IW093/IW098, Karelia/Crimea, Komi, Kosovo, Kuban, Macedonia, the Mediterranean package, Montenegro, the Pacific package, Ruthenia, Tatarstan, Transylvania, and UDM.
The hidden compatibility event `chaosx.nr6.350` delegates to the same helper so older external references retain the roster and portrait behavior.
Direct calls are synchronous within the current package setup effect, so immediate checkpoint flag tests observe the flags before setup continues.
