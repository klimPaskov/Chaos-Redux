# Event 31 local actor research-slot repair

## Disposition and acceptance

Implemented within the user-authorized accepted Event 31 package.
This bounded change implements the two-slot Local Cell State requirement in `031_random_terror_country_package_matrix.md` and Part 5, lines 327–333.
It does not close the complete country package or the separate terminal-role transaction.

## Change and ownership

`common/script_constants/031_random_terror_constants.txt` adds `random_terror_tuning.actor_research_slots_local = 2` beside the existing standard three-slot value.
`common/scripted_effects/031_random_terror_effects.txt`, `random_terror_initialize_actor`, chooses that local value only for the local profile during first-time setup.
The existing `random_terror_actor_setup_complete` guard remains outside both branches, so ordinary later maintenance does not overwrite research slots earned through focuses.
Regional, transnational and jihadist initialization remains at three slots.
JHX and JNX dormant histories already specify two slots and agree with the corrected runtime local profile.
No AI score, target eligibility, random weight, technology grant or focus reward is changed.

## Source evidence

The installed `documentation/effects_documentation.md`, lines 7641–7649, documents `set_research_slots` in country scope.
Its SHA-256 revision is `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, Technologies table at lines 1929–1936, documents setting the current country's slots to an integer.
Its SHA-256 revision is `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
Installed vanilla precedent `history/countries/ALT - Altai Republic.txt`, lines 3–8, uses `set_research_slots = 2` before starting technology.
Its SHA-256 revision is `c840c7a0a3be756fa1eb12dbccf64bc2e2c58048ae3bc7aa6f43f55d466bdd67`.
Current Chaos Redux precedent is the existing guarded actor initializer and the two local dormant histories.

## Review and validation limits

The parent reviewed the exact two-file diff and all local initializer call sites.
Source-contract cases are local first setup → two slots, ordinary nonlocal first setup → existing three slots, and already initialized actor → no slot reset.
These cases establish the script branch and guard, not observed engine execution.
The earlier reference search for `set_research_slots`, restricted to installed documentation and offline wiki with limit two, timed out after 600 seconds.
A narrower installed-documentation-only limit-one retry was issued; its outcome belongs in the MCP evidence ledger when delivered.
No fresh successful technology inspection/comparison or live-game result is claimed for this change.
The actual Final Revelation five-slot grant, preterminal Final Jihad classification and inherited technology compatibility remain separate open work.

## Safeguards and next work

The immutable terminal-role before snapshots were saved before this change under `evidence/terminal_role_before_20261003/` for the read-only probability baseline.
This nonweighted slot correction does not invalidate their terminal-role classification evidence.
Complete the actor activation, research-source, focus-upgrade and final-transaction scenarios before claiming the country matrix complete.
