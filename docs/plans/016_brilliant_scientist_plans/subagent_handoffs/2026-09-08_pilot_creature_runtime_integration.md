# Pilot creature runtime integration

Disposition: implemented for the requested action and gloss-map repairs; inherited whole-package limitations remain below.

The user authorized direct Blender repairs of existing faulty unit models, and the parent accepted six repaired skeletal actions after actual-byte reimport and multi-phase pose review.
GPT-6-astra authored four paleogenetic roles (stalk, charge, roar, wounded) and two xenobiological roles (support_attack, retreat).
The accepted original meshes, rigs and fifteen other action payloads are preserved.

## Runtime verification

On 2026-09-08 the parent and independent documentation auditor verified all 29 selected source/destination payload hashes and byte counts, all 21 animation registry/mesh/entity role chains, exact mesh subobject names and texture basenames, unit sprite aliases, calibrated entity scales and terminal non-looping death states.
Parent visual review includes the six changed action phase sheets and the corrected-gloss actual-byte reimport previews.
Paleogenetic creature uses eleven distinct role bindings, subobject `mesh.002`, and entity scale 1.35.
Xenobiological assault organism uses ten distinct role bindings, subobject `mesh.001`, and entity scale 0.8.
The corrected specular maps store engine glossiness in alpha; they replace the earlier roughness-alpha derivatives.

## Selected payloads

| Package | Runtime file | SHA-256 |
| --- | --- | --- |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/chaosx_paleogenetic_creature.mesh` | `050C0B461050D86203C80A08C8E84C942BDB518B187BD59E7AD1BEBE7E0ECEF7` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_diffuse.dds` | `5BDE97E313629B70E64693D8B937D978B8688E1085265BFC9514EACC5C07AEBC` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_spec.dds` | `2E13A6E4A76678D954989BD706A9872F8E59F297B1F8AA51517C4F4745AF138A` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_normal.dds` | `33FD0F1D59DEED6518E6837AE61F67BC425A26C020CF9D8EB3928F88AD3F0C78` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_idle.anim` | `A911DC3D1BB3E828C4D3636C10751184EBEAEACCFF76D053230C5F09ADE039E8` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_stalk.anim` | `0D66C4FA90662CC8DEF31A0E7995CAC004CA18BCCF15A50A87CB2E704A20DE72` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_move.anim` | `492A31119135C028994A3BB52FEC9A6AB076163E63EE82C5A5AFFB230FFA5549` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_charge.anim` | `30B3354CB0DD10E6E8966B89314B4EEAC3AA554D97ABB7E24824447EE578BC1B` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_attack.anim` | `BBB9DC684E923EC23EDD1C3FE30070F8EAD30FED2AF912270D89AA5950F36848` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_defend.anim` | `78200CB2AAB4514DEF424A0B6DDEE4540C10614DDE8F2E4076A9EBC9A45E2026` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_support_attack.anim` | `8C4C212543E936CA63AF926FB808C87713C405787A6B60AEDA6EAD73E67E1A26` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_retreat.anim` | `123C6AA138495085B3655DE614EA6B98E3F5871A84A38EFB40BEE25C95244C30` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_roar.anim` | `C5961F8131DFC20BCF8F6E308B1761E9D49686A9712C482B3AA236B626885AC8` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_wounded.anim` | `EBBE735DD8020170EDC36A41797461026F18AFE7AB0F463A63747A6CD9925F62` |
| paleogenetic_creature | `gfx/models/units/paleogenetic_creature/paleogenetic_creature_death.anim` | `58CAF87D9DA6CA743AEEA0A59DAC9A2A140B8838B7CEFC2542F53F1E829D0C12` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism.mesh` | `5561F2ED172359508605B1A1944EC62B8CCC35C04C4DECFE58F1B2CA19900781` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/texture_0.dds` | `72B00DF642C574955E51EB130DE9327CC825138F970F601131AE9047D4E6C157` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/texture_specular.dds` | `972CAE334C8D2E016AE9CF042CE159E63FE85DE3640E0621F11F492A4766AB12` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/texture_normal.dds` | `25DF099F9387F045DEA60BEA819A9039116EC12001814309773A32C36C3C71D7` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_idle.anim` | `EF8545780F1750DCA3B6AD95A1998D97BF63FFD86256A354151ECC3091A36A23` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_crawl.anim` | `C76D0F03126C24D778705CA4185C37B9B3AAA6DFEC24D1ABEB90F00DBBD44C37` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_move.anim` | `8EDFCB10044779862A144CDF671777D389F43D970ACA4F9F3A1AD2C3D2225D96` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_attack.anim` | `65B10CF6BF822CEABCA3574470C39422E982E7BD26DBB4359035918F5FE7C897` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_defend.anim` | `4A2A00C740FEB821E5D67A1C5C9246F806E91066E77A8860E9E0E3F904352594` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_support_attack.anim` | `34C6915426CB5D7F9F5D922509049ED592CD807DC803A4345BBAB4A6EA590592` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_retreat.anim` | `ED6F53F0D48720737C0E4A9B978E1EE3508A85E847C7D31F1213273D82B226D1` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_leap.anim` | `07BD00C152B6A9D8A4118B1F3F0BD37B69AFAC3550928D2AF49C833F1785F0BD` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_wounded.anim` | `C3C103D6EDFCECA4CCFEBF2C3A6485E48F3101BE6EC96F9A53967BA581123A6B` |
| xenobiological_assault_organism | `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_death.anim` | `573C65BA560CC6BBE3A252248EF2561B060DD5479D62AC7FF12BEF7287B5D729` |

Runtime definitions are `gfx/entities/paleogenetic_creature.gfx`, `gfx/entities/paleogenetic_creature.asset`, `gfx/models/units/paleogenetic_creature/animation_paleogenetic_creature.asset`, and the corresponding three `xenobiological_assault_organism` files.

## Limits

No requested action was omitted or replaced by another role alias, and no Meshy credits were spent for these two repairs.
This action tranche does not claim completion of every model package in the wider repair request.
The paleogenetic accepted mesh retains its recorded 59 boundary edges; this action repair did not change its topology.
Inherited paleogenetic audio audition/derivative work, xenobiological historical provider receipt gaps, and final audio consumer isolation remain unresolved and are not represented as completed here.
Existing audio and counter assets are preserved.
No live-game validation was performed.

The detailed authoring and reimport receipts are documented in `2026-09-06_pilot_creature_action_repairs.md` and each job’s `evidence/pilot_blender_repair_20260906/` manifests.
This report supersedes earlier pending-runtime statements only for the exact selected payloads and bindings recorded above.
