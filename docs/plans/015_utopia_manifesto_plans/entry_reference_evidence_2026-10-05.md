# Event 015 entry reference evidence

## Installed game documentation

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`: country_event lines 2943?2968; random_country 5372?5380; save_event_target_as 6496?6503; set_variable 7888?7908.
`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, SHA-256 `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`: has_event_target 3844?3851; tag 7649?7656.
The exact country-event effect, variable assignment and country-tag trigger sections were read locally after the later reference calls became slow.
The reference context/read routes successfully supplied revision-bound random_country and regular-event-target sections.

## Offline wiki

`paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, SHA-256 `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`: dynamic title/description first-match behavior 57?76; trigger and triggered-only semantics 119?145; global fire_only_once behavior 147?149; country event effect and carried context 194?219.
`paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`: regular event targets 303?328; variable types and scripted-helper temporary lifetime 437?443.
Both relevant sections were read; no online Paradox wiki was used.

## Vanilla precedent and existing consumer

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/Generic.txt`, lines 602?661, uses triggered-only country reports and recipient-specific option gates.
The existing Event 015 manuscript report uses `GFX_report_event_utopia_manifesto_found`; both feedback reports reuse that family and add no art placeholder.
`common/scripted_effects/chaosx_settings_effects.txt` prepares the Event 015 candidate, checks the returned class and target, then dispatches `.1` in the target country's scope.
That shared file was read only; concurrent changes can move line numbers, so the exact pre-edit baseline hash and blob are retained by the probability auditor.
`common/scripted_effects/chaosx_events_log_effects.txt` reads `utopia_manifesto_latest_actor` for actor presentation.

## Coverage limits

The initial context bundle omitted Triggers, Scopes, On actions and Localisation under its limit.
The exact has_event_target/tag and country-event context rules were subsequently read from the installed files and the corresponding offline wiki; this is relevant section coverage, not a claim that every omitted topic was read in full.
The broader domain audits retain their own syntax/asset/UI/probability reference citations.

## Named QA save, read only

`C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/save games/qa_001_fresh_head.hoi4` is a 102.3 MiB HOI4txt save, player USA, date `1936.1.1.12`, version `Operation Postern v1.19.2.0.a729 (2bce)`.
The bundled save inspector ran `info`, `keys ... countries/USA`, and `find ... "utopia_manifesto|major" --in countries/USA`.
The actual country state contains `countries/USA/major = yes`; no Event 015 field matched in that country's saved subtree.
This confirms the major exclusion at the named starting point.
The save is before the forced launch and therefore does not prove the post-launch helper lifetime failure or reveal which recipient the original attempt selected.
No save or game settings were modified, and no save was copied into Git.
