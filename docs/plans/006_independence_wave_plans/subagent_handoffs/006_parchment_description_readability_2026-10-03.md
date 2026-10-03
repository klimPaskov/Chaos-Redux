# Event 006 parchment report readability

Disposition: implemented, source parity checked, post-fix live rendering remains unobserved.
Acceptance basis: the user-authorized orchestrator reported unreadable yellow text on the light parchment report at 1080p on 2026-10-03 and requested plain text for six exact Event 006 description keys.

Removed 20 colour-control tokens from `chaosx.nr6.2.d`, `chaosx.nr6.300.d`, `chaosx.nr6.302.d`, `chaosx.nr6.305.d`, `chaosx.nr6.306.d`, and `chaosx.nr6.308.d`.
All bracketed dynamic expressions and all prose remain identical.
The independent `chaosx_localisation_auditor` confirmed all 13 dynamic bracket expressions and every other line in both files match HEAD `090983ebfc0ab7952d370f1c55539ea0544b43ca`.
The diff changes exactly those six lines in `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/006_independence_wave_form03_l_english.yml`.
Option names, tooltips, decisions, and GUI strings retain their existing colour controls.
No gameplay, event-chain, asset, or catalog wording changes are involved, so this narrow formatting correction does not alter their source contracts.
No simplifications were made within this correction.
The wider Event 006 implementation remains incomplete.

## Reference evidence

Local sections were read directly while decision-reference MCP retrieval was pending.
The wiki defines each colour control as the section sign plus one character and identifies the reset control.
Installed documentation covers contextual object/property expressions and relation to event scopes.
The installed Mexico event descriptions retain dynamic country and leader expressions in plain prose.
These precedents support preserving the dynamic values while removing their surrounding colour controls.

| Source | Lines | SHA-256 revision |
| --- | --- | --- |
| `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` | 122-144 | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` | 138-156 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english/mtg_events_l_english.yml` | 3-8 | `4c2771e50eead349a84973b2f84f9604c30a9fb201723317d98a3586ead2c762` |
