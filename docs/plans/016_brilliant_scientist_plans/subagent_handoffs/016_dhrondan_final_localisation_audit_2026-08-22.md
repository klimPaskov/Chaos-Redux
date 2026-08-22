# Event 016 Alien Infantry and D’Rhonda Final Localisation Audit

Date: 2026-08-22

## Scope and authority

Audited the accepted Alien Infantry and Empire of D’Rhonda package against `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md` and `docs/plans/016_brilliant_scientist_plans/016_alien_dhrondan_acceptance_scenarios.md`.

The audit covered the four package localisation files, linked Event 016 and Event 019 localisation, DHR scripted localisation, Events `chaosx.nr16.40` through `.52`, the Event 016 Event Details clause, the existing four-evolution selectors, country and cosmetic identities, 88 focuses, 12 characters, traits, advisors, commanders, ideas, decisions, categories, missions, the envoy project, Alien Infantry equipment, subunit, tactics, technology, the existing `Not From Here` achievement route, news text, and linked GFX tokens.

No gameplay source was changed.

## Files changed

- `localisation/english/016_alien_infantry_api_l_english.yml`
- `localisation/english/016_dhrondan_contact_l_english.yml`
- `localisation/english/016_dhrondan_country_l_english.yml`
- `localisation/english/016_dhrondan_focus_l_english.yml`
- `localisation/english/019_infrantry_spawn_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_final_localisation_audit_2026-08-22.md`

The four package localisation files were already untracked shared-worktree files when this audit began. The Event 019 and achievement files already contained concurrent package edits. This audit preserved those edits and changed only the keys listed below.

## Changed keys

### Landing API and contact

- `alien_infantry_landing_category_desc` added
- `alien_infantry_call_landing_desc`
- `alien_infantry_call_landing_effect_tt`
- `dhrondan_rebellion_pulse_mission_desc`

### Country identity, decisions, events, and Event Details

- `DHR`, `DHR_DEF`, `DHR_ADJ`
- `DHR_neutrality`, `DHR_neutrality_DEF`, `DHR_neutrality_ADJ`
- `DHR_democratic`, `DHR_democratic_DEF`, `DHR_democratic_ADJ`
- `DHR_fascism`, `DHR_fascism_DEF`, `DHR_fascism_ADJ`
- `DHR_communism`, `DHR_communism_DEF`, `DHR_communism_ADJ`
- `DHR_IMPERIAL`, `DHR_IMPERIAL_DEF`, `DHR_IMPERIAL_ADJ`
- `DHR_IMPERIAL_neutrality`, `DHR_IMPERIAL_neutrality_DEF`, `DHR_IMPERIAL_neutrality_ADJ`
- `DHR_SYNOD`, `DHR_SYNOD_DEF`, `DHR_SYNOD_ADJ`
- `DHR_SYNOD_neutrality`, `DHR_SYNOD_neutrality_DEF`, `DHR_SYNOD_neutrality_ADJ`
- `DHR_neutrality_party_long`
- `DHR_speaker_ilyr_ren_desc`
- `dhrondan_sovereignty_category`
- `dhrondan_offer_two_world_compact_desc`
- `dhrondan_reclamation_target_requirements_tt`
- `dhrondan_integration_target_requirements_tt`
- `dhrondan_compact_target_requirements_tt`
- `chaosx.nr16.48.t`, `chaosx.nr16.48.d`
- `chaosx.nr16.49.d`
- `chaosx.nr16.50.d`
- `chaosx.nr16.51.d`
- `dhrondan_reclamation_demand`
- `dhrondan_event_detail_clause`

### Focuses

- `DHR_paid_landing_reserve_effect`
- `DHR_beneath_an_alien_sky_desc`
- `DHR_convene_the_two_world_throne_desc`
- `DHR_restore_the_ninth_diadem_desc`
- `DHR_raise_the_palace_guard_desc`
- `DHR_proclaim_the_right_of_return_desc`
- `DHR_assign_merit_by_projection_desc`
- `DHR_ilyr_ren_opens_the_chamber_desc`
- `DHR_submit_the_military_to_debate_desc`
- `DHR_the_chamber_of_two_skies_desc`
- `DHR_relight_the_field_laboratories_desc`
- `DHR_recover_the_laser_forges_desc`
- `DHR_the_twenty_element_substitution_desc`
- `DHR_restore_the_predictive_staff_desc`
- `DHR_fire_control_by_forecast_desc`
- `DHR_command_without_surprise_desc`
- `DHR_a_place_in_the_world_order_desc`
- `DHR_reopen_the_homeworld_corridor_desc`
- `DHR_the_century_beyond_exile_desc`

### Event 019 and achievement bridge

- `infantry_spawn_family_sustainment_cost_profile_alien_infantry`
- `infantry_spawn_family_request_cost_profile_alien_infantry`
- `brilliant_scientist_event19_alien_infantry_host`
- `brilliant_scientist_event19_alien_infantry_host_desc`
- `brilliant_scientist_achievement_not_from_here_tooltip`

## Coverage counts

- 401 keys in the four package localisation files after the added category description: 8 API, 58 contact, 120 country, and 215 focus keys.
- 88 unique DHR focus IDs and all 176 required focus name and description keys present.
- 12 DHR character IDs and all 24 character name and description keys present.
- 49 direct localisation references consumed by the 12 visible events `.40` through `.51`, all resolved. Event `.52` is hidden and has no visible key requirement.
- 36 unique linked idea, trait, decision, mission, and category IDs checked for paired names and descriptions. The single missing pair, `alien_infantry_landing_category_desc`, was added.
- 416 scoped keys checked repository-wide after the patch, with zero duplicate definitions.
- 253 sprite definitions checked across the five linked DHR/Alien Infantry GFX files, with zero missing texture paths.
- 88 focus icon consumers resolve to 88 distinct registered sprite definitions.
- 19 direct event, decision, category, and project GFX consumers resolve to registered sprite definitions.

## Audit lists

### Missing keys

None after adding `alien_infantry_landing_category_desc`.

### Duplicate keys

None among the 416 scoped DHR, Alien Infantry, Event 016 `.40`–`.52`, Event 019 alien-family, technology, tactic, project, and achievement keys.

### Scripted localisation issues

None found. `GetDhrondanEventDetailClause` has one sovereignty-formed branch and one intentional empty fallback. Both localisation keys resolve. The caller `[GetDhrondanEventDetailClause]` remains present in the Event 016 Event Details body.

The country event target token `[dhrondan_diplomatic_actor.GetNameDef]` was preserved. Its namespace correctly omits the `event_target:` prefix in localisation.

### Dynamic text opportunities

Existing dynamic values were preserved:

- Alien Presence and Pact Strain remain separate live values in `dhrondan_contact_status_header`.
- Landing cost and the 24, 18, and 12-day focus reductions remain dynamically formatted from existing variables and constants.
- Event 019 national administration costs remain dynamically formatted from request-overhead constants.

No new scripted-localisation method was required. The landing tooltip now states the complete fixed reservation, refund, Presence, Strain, and recovery tiers. The rebellion mission now states the 10, 20, and 40 percent tiers.

### Cross-surface mismatch notes

Fixed:

- Standardized every audited visible country, focus, event, Event Details, Event 019, and achievement occurrence to the binding `D’Rhonda` and `D’Rhondan` spelling.
- Replaced Event 019 player-facing receipt/API terminology with contact and paid-arrival language while preserving provider 508 behavior.
- Restored the Event Details addendum to premise-only prose. It no longer describes state-transfer mechanics.
- Aligned the landing decision with the seven-day reservation, exact 2,000-weapon refund, Alien Presence +1, Pact Strain +5, and 30/24/18/12-day recovery tiers.
- Exposed the exact rebellion probability tiers without changing their runtime logic.

No visible fifth evolution, D’Rhondan cluster, or D’Rhondan super-event wording was found. Existing Event 016 scripted-localisation selectors still expose exactly Evolution I through IV.

### File encoding concerns

None. All four package files and the five linked Event 016, Event 019, and achievement localisation files inspected begin with UTF-8 BOM bytes `EF BB BF`. No `:0` keys were found in the audited surface.

### Prose-quality repairs

- Vagueness: landing and rebellion text now states the concrete cost, timer, refund, outcome, recovery, eligibility, and probability tiers.
- Bloat: sovereignty news and route text was shortened while retaining the specific actors, territory, and institutions.
- Obvious explanation: Event 019 text no longer narrates internal API ownership or receipt bookkeeping.
- Repetition: the sovereignty news chain no longer repeats the same exile-versus-conquest contrast.
- Overcomplication: several focus descriptions now use direct subjects and actions instead of nested contrasts and administrative abstractions.
- Style-rule repair: removed the staged `stranded nation, occupying army, or both` formula, removed `not X but Y` constructions from the edited news/focus lines, preserved the ban on em dashes and sentence semicolons, and standardized D’Rhondan typography.

### Sourced quotation preservation

No sourced or attributed quotation appears on the audited DHR, Alien Infantry, Event 019 alien-family, or linked achievement surfaces. No quotation was altered.

## Display before and after

Before, the package mixed `D'Rhondan` and `D’Rhondan`, omitted the landing category description, left cooldown and revolt tiers outside the direct decision/mission text, exposed provider receipts and the shared API to Event 019 players, and added state-transfer mechanics to Event Details.

After, the visible package uses one spelling, the landing category explains Alien Presence and Pact Strain separately, the decision and mission show the exact conservation and probability rules, Event 019 describes the player outcome, and Event Details describes the sovereign exile-state premise without mechanical effects.

## MCP evidence

### Focus tree

`hoi4.focus_inspect` resolved all 88 focus titles and confirmed an 88-focus tree.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79d6ae0e57dc5e83a0a43eddd6b8d4765181c11b95a7b98575f4aa57626fd8cb/bca9b51b204b323d1ed133624bf0233bd555ba58536190683509ad2f4ad1c96f/focus-inspect.e96a318054c8867f.json`
- Rendered HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c4f75c5c4e0b78a697433672f8320aa7f7446ceafdc3acc4f86d437a63d57b5/66e1b4b9bf69309bd7d96173d0c1f7e7f028686af67a711f5e4571b69d01491f/dhrondan_focus_tree.focus.html`
- Rendered SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3311d16279d92d222a8c2e2fc3e4da643495a499ca87613a6dc1a305d26bf22e/8297790dc849ae34410d0fddbfd4ae09b32e711618cab47d74e4773895b2cd1b/dhrondan_focus_tree.focus.svg`

The focus route reported two linear-detour warnings and five one-column same-row spacing warnings. These are focus-layout findings outside this localisation-only patch. The remaining missing-icon errors belong to vanilla continuous focuses, not the DHR tree. The focus renderer produced no DHR missing-title or missing-icon diagnostic.

### Event chain

`hoi4.event_inspect` lint for selector `{ kind: event, eventId: chaosx.nr16.40 }` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and no skipped sources.

- Lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1214b33f1402fc035601383e2dd5d9c32811bf202074fa30fb7efd354872de02/bd20854c1233d74be078e1fc8decbdf8565754f040e683e919f7842588f0a439/event-lint-bc0062fc8506.json`
- Options render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0ef3597cf50020f0f63b412c862cd19055b463c2dfde772429ed45e96f999cc/bcc78cc3d31a5abe6fe2d6e01a0390ded3962570029daa7c952e20a739a7d2dd/event-options-bc0062fc8506.html`

The event render is a partial structural chain view with three selected nodes and 41,194 omitted workspace nodes. It does not provide actual popup text-box overflow measurement, so source review is not presented as rendered overflow proof.

### Technology

The read-only technology tools traced and rendered `brilliant_scientist_alien_predictive_warfare_tech` and its two tactic unlocks.

- Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5a5cb7833e41f1f8060f1b57ffbb1653571c44c924b5d7487f0bf9b360f1a71/cbdd7bb7f701a8b1ace94006123a545c561590b189bf53244498b23d5d1b3761/technology-trace-779cff6fbca6.json`
- Rendered HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/309c544c24948d53bef6f7bf899cb049da36bd56d295a92197de244d61b235f1/48f3d2eb3dcf6c922913941a318fd06bd83fb22da438d1b20a2032b45894fd27/technology-technology-779cff6fbca6.html`

The technology analysis was partial and reported `sourceAccurate: false` because workspace-wide helper projections were deferred. It produced no missing localisation or asset diagnostic for the selected technology, but it is not complete runtime proof.

### Unavailable MCP routes and overflow uncertainty

The installed HOI4 MCP exposes no dedicated standard decision/category inspection or render route. The DHR decisions use the standard decisions UI and have no event-owned scripted GUI, so `hoi4.gui_inspect` is not an applicable substitute. Decision/category overflow remains a user-owned live-consumer check.

The available event and focus renders do not measure popup descriptions, hover descriptions, or decision-category text boxes. Those overflow checks remain unresolved rather than being treated as source-equivalent visual evidence.

## Meaningful validation

- Compared all 88 focus IDs with their name and description keys.
- Compared all 12 character IDs with their name and description keys.
- Compared all 49 visible `.40`–`.51` event references with English localisation.
- Compared the DHR idea, trait, decision, mission, and category consumers with paired name/description keys.
- Compared all linked event, project, decision, category, focus, equipment, tactic, technology, portrait, advisor, high-command, commander, flag, and achievement GFX references with registered sprites and existing texture files.
- Confirmed no unresolved `$KEY$` tokens in the four package files, no scoped duplicate keys, no retired alien-guard or Kruger-specific Alien Infantry identifiers, and no visible fifth-evolution, DHR cluster, or DHR super-event text.
- Traced the achievement tooltip’s DHR alternative to `dhrondan_existing_achievement_route_is_complete` in the live achievement trigger.

## Skipped meaningful validation

- No in-game or live-consumer check was run because those checks belong to the user.
- Standard decision/category and popup-description overflow could not be rendered through the installed MCP routes.
- No event or technology compare was run because this audit did not change event or technology source. The read-only inspections are structural evidence only.

## Remaining placeholders, blockers, and unresolved decisions

- No localisation placeholder remains in the audited package.
- No missing DHR/Alien Infantry GFX token or texture remains in the audited consumer set.
- Decision/category and popup-description overflow lacks an applicable MCP render route.
- The focus MCP still reports seven DHR layout warnings. They do not indicate missing localisation, but the focus owner should retain them in final focus acceptance.
- Technology and event MCP evidence is partial because the large workspace deferred helper/lifecycle projections.
- No unresolved wording decision remains.

## Acceptance status

Accepted for final localisation, source-key coverage, scripted-localisation coverage, dynamic-token preservation, and scoped asset-token resolution.

This handoff does not claim whole-tranche completion. User-owned live display acceptance, the partial MCP limitations above, and the inherited focus-layout warnings remain outside the localisation acceptance claim.

## Simplifications and omissions

No localisation fallback, hidden fifth evolution, cluster, super-event wording, or gameplay simplification was introduced. No separate design-gap plan was required.
