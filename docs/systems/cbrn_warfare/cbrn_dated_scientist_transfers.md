# Dated CBRN scientist ownership

Disposition: superseded by the A11 restoration in `cbrn_historical_scientists.md`; all 67 identities are recruited directly into their home countries. The following records the historical holder implementation.

The historical roster has 67 static identities: 38 are attached to their home countries during history loading and 29 pass through the existing date-gated country callbacks. History loading attaches the latter group to the stateless `CSH` holder. The callbacks then transfer each identity from CSH to its fixed home tag with country-scoped `set_nationality` when its original date window passes. The callback names remain stable for their existing startup and tag-specific on-action callers.

Each transfer date is the latest arrival. A country receives a held identity earlier when it is at war, runs the matching chemical or biological programme, or both, according to the identity's access class in [Dated arrivals](cbrn_historical_scientists.md#dated-arrivals). Haldane, Fishman, and Velikanov keep their upper date limits.

Each transfer requires the recipient not to have the identity and CSH to still hold it. That prevents repeated transfers, character cloning, a missing-character scope, or taking an identity from a different owner. Character flags and dated trait awards still run only after the home country has the character. The original Haldane retirement and the Fishman/Velikanov bookmark windows are unchanged; the latter two preserve their existing 1936 campaign-divergence behavior.

`history/general/chaosx_startup_character_recruitment.txt` is the sole recruitment source for all 67 roster tokens. The 29 runtime `recruit_character` statements in `common/scripted_effects/chaosx_startup_history_effects.txt` are replaced by explicit holder transfers. The existing eight `on_daily_TAG` callbacks in `common/on_actions/cbrn_historical_startup_on_actions.txt` are retained; no periodic world iteration is introduced.

## Internal holder

`common/country_tags/cbrn_scientist_holder.txt` registers CSH and `common/countries/CBRN Scientist Holder.txt` supplies its ordinary graphical metadata. `history/countries/CSH - Scientist Registry.txt` uses capital 1 only as the engine bootstrap, zero research slots, and the empty `history/units/cbrn_scientist_holder.txt` OOB. CSH receives no territory, cores, claims, factories, equipment, templates, divisions, focus route, or formation transaction. It is separate from the playable Event 016 KRG route, Event 015 DJX roster, and CXT test harness.

The holder introduces no player operation or additional CXT grant. Existing CBRN CXT packages still own their research, unit, project, and equipment fixtures. All 67 scientist portraits and 15 advisor cards retain their existing consumers. The three CSH localisation keys identify the latent tag if inspected, without displaying a technical ledger label.
The [native flag correction](../../specs/chaos_warfare_system_specs/corrections/2026-10-03_csh_native_flag_lookup.md) supplies normal, medium, and small flags for the base tag and all four standard ideologies, following the user's confirmed load errors.
The [asset manifest](../../assets/cbrn_scientist_holder_flags/manifest.md) documents one institutional design shared across those native lookup aliases.

## Source and live evidence

The user-run 2026-10-03 main-menu build reported 58 warning lines from the 29 dated recruitment statements. The same session's November 1936 save established that the previous runtime recruitment still attached Fishman to SOV; the warning was a load-time complaint, not proof that arrivals were broken. Direct character-scope transfer of an unrecruited identity failed in that session and was reverted by the user.

The explicitly supplied `docs/testing/live_qa/20261003_full_playtest/logs/cycle1/error.log` was copied while review was underway; the parent read with SHA-256 `edb523793e8c7ea1c79ff53546b1cfe5789c498217160191c9b022f09a85bab3` contains all 58 recruitment warnings.
An earlier read of that changing copy did not contain them and does not invalidate the later baseline.
The user also reported day-one unknown-character errors for Haldane, Fishman, and Velikanov at the former runtime recruitment lines in a fresh USA scenario.
Their definitions are ordinary static entries in `common/characters/cbrn_historical_scientists.txt` and `common/characters/cbrn_historical_specialists.txt`, with no DLC or date gate around their definitions or CSH history recruitment.
All three are explicitly included in the holder roster before the existing startup callback: Haldane transfers before 14 March 1936, Fishman before 5 June 1937, and Velikanov before 8 April 1938.
The source correction therefore covers these three initialization paths as well as later wartime arrivals, while successful history attachment and transfer remain runtime acceptance items.

The supported replacement is documented in installed `effects_documentation.md:7397–7420`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`. Vanilla `common/scripted_effects/INS_scripted_effects.txt:974–980` uses the explicit country-scoped target/character form. The mod's `history/general/016_brilliant_scientist_character_recruitment.txt:11–19` and `016_brilliant_scientist_effects.txt:2835–2851` provide the dormant-history-owner and runtime transfer precedent. The offline Character modding section `:410–489`, revision `8ef3d5f9923026dd81f239944710b7331a8d06ad42e4345b32fce4e86dd95d98`, establishes history-time ownership; the Country creation tag section `:47–67`, revision `0c0e57915a7d1eef9ddeebe91c7329e18f4f224af98ac33fac5edd35e3aaa35d`, establishes unique tag registration.

The [source-contract result](../../testing/2026-10-03_cbrn_dated_holder_before/source_contract_result.json) verifies one history declaration per identity, 38 home and 29 holder entries, 29 matching guarded transfers, and zero runtime recruitment commands in the owner file. Reconstructing the former statements makes the complete executable startup source identical to its saved before-source: dates, retirements, traits, flags, equipment, and other startup logic did not drift. These checks do not execute the engine. The final source lookup for the Soviet dated helper did not return through bounded waits, while the reference context/search/read calls above succeeded.

A subsequent narrow `hoi4.source_lookup` retry requested only Haldane's character definition, one definition and eighteen lines with references disabled; it also failed to return during bounded waits.
The detailed definition review therefore used the exact local files, alongside the offline Character modding history checklist at lines 50–58.
The live schema exposes neither structured `view`/`keyPath` lookup nor `hoi4.script_validate`; no result from those unavailable routes is claimed.

Fresh live-QA evidence must distinguish main-menu warning removal, history-time CSH attachment, date-time transfer, repeated callback idempotence, 1939 absences, and unchanged trait/portrait behavior. No clean full error log or successful dedicated-CSH transfer is claimed from source inspection alone.

The [independent country-package audit](../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-03_cbrn_scientist_holder_country_audit.md) confirms no blocking source defect in tag registration, roster ownership, or transfer gates.
It retains runtime uncertainty around the stateless bootstrap capital and records its unavailable map MCP evidence.
Its original latent flag gap became a confirmed missing-file load defect in the user's 13:20 live-QA update and is addressed by the native flag package above.
The [source/reference review](../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-03_cbrn_dated_holder_reference_review.md) confirms the holder separation and supported transfer form without claiming native execution.

## Future work

Additional dated historical identities should use the same history-owner and fixed-country transfer pattern after their chronology is accepted. More precise dates may be adopted when better sources are reviewed, without changing this ownership contract or adding recruitment loops. Broader character defection or retirement remains a separate accepted-design task.
