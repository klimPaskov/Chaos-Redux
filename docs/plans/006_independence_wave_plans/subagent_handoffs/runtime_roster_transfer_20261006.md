# Runtime roster transfer repair

Owner: parent Event 006 finishing agent.
Disposition: implemented source repair for inbox L1, native result pending.

## Files and identifiers

`common/scripted_effects/006_independence_wave_execution_effects.txt` changes 31 guarded character recoveries in `independence_wave_ensure_custom_carrier_startup_state`.
They cover AFX, AGX, AJX, ARX, ASX, AXX, BAX, BBX and HBX.
`common/scripted_effects/006_independence_wave_iberian_package_effects.txt` changes the guarded Aguirre recovery in `independence_wave_nav_ensure_command_roster`.
The 32 identifiers, their definitions, history recruitment, and guards remain unchanged.

Before the repair, runtime helpers attempted history-only recruitment.
After the repair, each missing character is entered by its static token and transferred with `set_nationality = PREV` into the receiving country.
PREV is the released country inside the character block, even when the launcher's country remains ROOT.
The vanilla pattern is a character-scope transfer, rather than an attempt to recruit an unrecruited token.

## Source evidence

- Installed `documentation/effects_documentation.md:5696-5708`, recruit_character, reference id `53d1b5b8a11e269009ae7ba7d527ebf63637e1bbcca29241f38e1aba594508a9`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, read through the live reference route.
- Installed `documentation/effects_documentation.md:7397-7420`, set_nationality, reference id `99722353f32575ff3541fa464926251d8760c0a34f7491a3332c5e2d039f74c7`, same revision, located through the live search route and read directly from the installed file.
- Offline `paradox_wiki/Character modding - Hearts of Iron 4 Wiki.md:410-489`, recruitment and roles, reference id `121018f89b283fe6b66a557b57bb55da139fb54b14ed23c96f641459f5c5b401`, revision `8ef3d5f9923026dd81f239944710b7331a8d06ad42e4345b32fce4e86dd95d98`, read through the live reference route.
- The same offline file `:490-502` describes restoration after retirement, read directly.
- Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:2735-2765` documents transfer and its examples, and `:262` states that character scoping no longer requires recruitment in the calling country from engine version 1.12.8 onward, read directly.
- Vanilla `events/AAT_Sweden.txt:7899-7914` transfers recruited Finnish and Danish officers through character scopes, read directly.
- Live source lookup of `FIN_erik_heinrichs` returned its vanilla character definition at `game:common/characters/FIN.txt:131-166`, revision `09baf97c33d4503fcbc2252af10a51729af460871ea6c6610f989865e2a92467`.
Its reference coverage is incomplete with 19,739 unresolved workspace references, so the direct vanilla event read supplies the consumer precedent.

All 32 recovery tokens were matched to a `recruit_character` writer under `history/` before replacement.
The custom tag histories and `history/general/006_independence_wave_character_recruitment_registry.txt` supply those writers.
No runtime `recruit_character` remains in Event 006's common source.

The allocator audit remains at 109 attested packages, 78 compatible reservation groups and 112 adapters, with IW-076, IW-131 and IW-179 deliberately fail-closed.
This audit checks source consistency and does not execute recruitment or release.
Required MCP file validations are retained in `../evidence_20261006/parent_initial_mcp.json`.
Whole-file checks report `valid = null` because they do not infer the 31 character-token scopes in the executor or Aguirre's scope in the Iberian helper, and leave 178 and 163 native argument blocks unchecked respectively.
Two explicit COUNTRY-source checks with sixteen declared CHARACTER bindings each validate all 32 guarded transfer snippets with zero unresolved commands and zero unchecked argument blocks, retained as `roster_snippet_0.json` and `roster_snippet_1.json` in the same evidence folder.
The snippets establish the native command-kind and declared-scope contract, while actual recruitment, token resolution and PREV delivery remain separate native checks.

## Exact native checks

Start from the orchestrator's `qa_001_fresh_head` setup, fresh 1936 USA, and launch SCN-008 Sovereign Scatter at Low through Settings.
The opening release should include custom carriers when their regions qualify, with their own flags, names, leaders, commanders and capitals.
Inspect AFX, AGX, AJX, ARX, ASX, AXX, BAX, BBX and HBX when selected, using the new dynamic country's tag shown by `tdebug` rather than its static template tag.
The L1 runtime recruitment warning should be absent, and the package setup/final validation should not fail at detail 43 or 45 due to a missing roster.
In a separate controlled NAV setup, release NAV, end its Event 006 origin through annexation, and release it again in the same campaign.
Aguirre's corps-command role and the prepared package proof should remain available on the second release.
These are orchestrator checks and were not run by this agent.

No simplification was used in this bounded repair.
