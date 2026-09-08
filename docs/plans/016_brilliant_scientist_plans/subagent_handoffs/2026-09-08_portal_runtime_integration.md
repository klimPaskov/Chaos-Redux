# Portal Raider weapon-free body and Blender action integration

Status: requested 3D repair implemented; live consumer and auditory validation are not claimed.
Acceptance basis: the user required firearm-bearing models to use weapon-free Meshy bodies followed by GPT-6-astra Blender rigs, separate weapons and complete actions.
The already-generated Meshy 7 body task 01a07650-f80a-7523-b547-7d1f7ccc0221 was retained without another paid call.
The parent accepted the final-byte focused trigger/support-hand grip, stock contact, rigid pack, closed material/culling views and articulated death contact; the existing low-poly glove/scarf faceting remains visible.

The final mesh has 29,662 triangles and a 45-bone rig, with body streams mesh.003 indices 0/1 and separate portal_rifle index 0.
All use the selected 1024 diffuse, packed normal and gloss/specular maps.
The exported portal_raider_muzzle_locator is retained directly on weapon; shot cues use the existing alien ray particle/light definitions.
The existing sprite = portal_raider resolves to portal_raider_entity at scale .8 exactly once.
Runtime files are gfx/entities/portal_raider.gfx, gfx/entities/portal_raider.asset, gfx/models/units/animation_portal_raider.asset, gfx/models/units/portal_raider/ and sound/portal_raider.asset with its WAV folder.

Ten distinct actions have actual-byte reimport proof: idle, move, attack, defend, support_attack, retreat, guard, portal_arrival, wounded and death.
Idle/move/defend/retreat/guard loop; attack/support/arrival/wounded return to idle; death remains terminal.
Fifty standard samples and 171 saved previews are recorded, including six exact firing/arrival/death phase views.
Largest recorded source/reimport ground difference is 1.18278e-5 units.
The source timeline begins at frame zero at 24 FPS; native proof frames begin at one.
Shot cues occur at .833333 (attack), 1.083333 (defend), and .75/1.666667 (support); arrival landing is .666667 and death impact 1.916667 seconds.
Named custom states are registered, but automatic gameplay invocation of every custom state is not inferred from registration alone.

Twelve sourced PCM16 mono 44.1 kHz WAVs and seven sound effects are registered.
Eleven files preserve the prior normalized bytes; the electrical recording has a documented one-second fade/trim derivative emitted once on idle/guard entry, avoiding unproven persistent-loop stop behavior.
The licensed original ten-second recording remains preserved.
The runtime source ledger records all creators and source links; electrical audio is CC BY 4.0, death audio CC BY 3.0, and other sources CC0.
Existing bespoke counter files and interface/portal_raider_system.gfx consumers are retained.

Source evidence: docs/assets/chaos_redux_3d_model_pilots/models_3d/portal_raider/final_asset_manifest.json, final_action_crosswalk.json, runtime_copy_manifest.json and evidence/audio/runtime_proposal/runtime_sound_copy_manifest.json.
Independent audit: 2026-09-08_portal_runtime_audit.md.

## Verified runtime payloads

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `gfx/models/units/portal_raider/portal_raider.mesh` | 3506453 | `3B63FF39642713334223C8820F500E0DC48251DCE093876F1AC2F711E9CB68B9` |
| `gfx/models/units/portal_raider/portal_raider_attack.anim` | 58114 | `48DB47C13E874880883188B0DC67C80691BD9BF6C48F3B420B8E1F7CEEF2E844` |
| `gfx/models/units/portal_raider/portal_raider_death.anim` | 134893 | `57A2A473CD1A624F8E0180981EE337FD4CC1E78646D8052787C0F45CADB54E5A` |
| `gfx/models/units/portal_raider/portal_raider_defend.anim` | 81594 | `9D2EFC7EB1E46B346F3DC300C2C5F906B33659C404699784D38E7B79D2E59F6B` |
| `gfx/models/units/portal_raider/portal_raider_guard.anim` | 111298 | `473CA4CAFACF793F9BAC4F6F71AE2CA429E470030397A9C7E278CF85023E16BD` |
| `gfx/models/units/portal_raider/portal_raider_idle.anim` | 84706 | `FC003182E67AACE2EE24A33CD4E3D4012F9746FC2ED6179DB06E3DAE25686E94` |
| `gfx/models/units/portal_raider/portal_raider_move.anim` | 49255 | `DB9293EF315D0B38D82C0B253F4371B13D76CC05A3DB2E55C76BB3A74152775F` |
| `gfx/models/units/portal_raider/portal_raider_portal_arrival.anim` | 89249 | `2D1B9206396960F10182E5F5B1A1CF6A27E5972E9496BA89EAB294D2C23A107A` |
| `gfx/models/units/portal_raider/portal_raider_retreat.anim` | 33137 | `2F5DD0C3F5947E9C515138E4AA5DF29E1A0DC790D41C9DB9A2709658BC29744E` |
| `gfx/models/units/portal_raider/portal_raider_support_attack.anim` | 87783 | `D6932C82CE6D7833F8F3DBB05D63420FFBD2829661010F290B579B856538E82B` |
| `gfx/models/units/portal_raider/portal_raider_wounded.anim` | 71860 | `E52048F8A2980D2A01830278FFFDE68064BC5885EFC28978BAB689F0D03573DC` |
| `gfx/models/units/portal_raider/portal_raider_diffuse.dds` | 4194432 | `F4D6BEFDB87B589013F2B079AB60918A0D0EA75FEB71EDD6C06F640F87ADFCEC` |
| `gfx/models/units/portal_raider/portal_raider_normal.dds` | 4194432 | `B3EFE7B78B75D6136B6744FD9B65C3E61CFBD6853C50CD9A8BA8745C29C7C445` |
| `gfx/models/units/portal_raider/portal_raider_specular.dds` | 4194432 | `53D3480D320FDDFC347EEF68D561AE792AF83D1AC2F1A3748E30B8FD085DB4BE` |
| `sound/portal_raider/portal_raider_select_01.wav` | 37966 | `88CBC5D6C9432FC6BA42727093EB966FD812FC0A3E1E7B270ECA9CFC129DB59B` |
| `sound/portal_raider/portal_raider_step_01.wav` | 13654 | `2FBD08CC2D1F36EC9CE467FF361DEB935A2F3C4E39615C8DC3CBEBBF7F302D8F` |
| `sound/portal_raider/portal_raider_step_02.wav` | 14958 | `5B4795A56D2813F5280F389E33E1919519ABAA6FFBDB171431A56EB9E8691C98` |
| `sound/portal_raider/portal_raider_step_03.wav` | 28012 | `F4D66E75401E01793347B3BB43ACC7A2284F80F6EBE2F56CD468DF83EDB828B5` |
| `sound/portal_raider/portal_raider_step_04.wav` | 29450 | `36A267A8DBC32DD41D5FD85B9C5DDEDF3716C71577F9CECFD6CBA5F1C3B071A1` |
| `sound/portal_raider/portal_raider_step_05.wav` | 27752 | `0C4B5BBC88A3491024CEB35A4FF3B762CB5D2992FC5A6D8D27B1E9ACEAA2906F` |
| `sound/portal_raider/portal_raider_step_06.wav` | 21746 | `03EC79970B26CEFCA929D2771E3409AB3AADCB03770E065009F94C6559AAE889` |
| `sound/portal_raider/portal_raider_electrical_pulse.wav` | 88244 | `7698F5CF9FCAB36CBB9DCEF988CB6BDD5BF7255D0EF4E82F8FFA5F012C7C1D1F` |
| `sound/portal_raider/portal_raider_ray_attack_01.wav` | 27470 | `C1B8C31799C479D626E5EE1556BEC9DAC9174224EF2C85A287072ECF491676D9` |
| `sound/portal_raider/portal_raider_impact_01.wav` | 51278 | `64FCE8D5581EDC775C44CBC390D650140AB29605D518964DFE9612B34E5619E8` |
| `sound/portal_raider/portal_raider_arrival_01.wav` | 46926 | `40292758B66A3159C8414C7D56EEB493E549BB50B70F489214B692C2A5611707` |
| `sound/portal_raider/portal_raider_death_01.wav` | 194856 | `0D3BF7D018BC133DB117827482C1EC2E1801E42045FA0A875BB61D2ECB7E173C` |

## Simplifications, omissions, and blockers

No required 3D component or authored action was omitted.
The electrical sound uses the accepted bounded pulse instead of claiming an unverified continuous state-bound loop.
Selection is registered but has no verified per-subunit selection consumer; it is not attached to idle or a tag-wide infantry voice override.
Audio format and measured onset evidence do not establish auditory approval.
This repair consumed no additional credits; the earlier weapon-free body used 30 credits.
No live-game or automatic custom-state activation claim is made.
