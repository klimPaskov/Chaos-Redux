# Event 012 Africa Actions 71-76 final audit and handoff

## Scope and disposition

This pass owns the disease actions (`contain_emergent_disease` 71, `research_disease_countermeasure` 72, and `weaponise_fictional_pathogen` 73), the first three strange-formation actions (`awaken_stone_cohort` 74, `train_gorilla_heavy_infantry` 75, and `organise_pan_sappers` 76), their shared AI target path, player-facing descriptions, and bounded route documentation.

The six actions now fail closed at the shared validator, use the native ordinary-pathogen lifecycle for accepted seeds and accidents, and retain the existing shared Event 012 action ledger and mission kernel.

## Severity-sorted issue list

### Critical, fixed: disease effects could expose crisis or containment state without an accepted native episode

`common/scripted_effects/012_africa_disease_effects.txt` now calls `bio_lifecycle_dispatch_seed` for deliberate battlefield releases and laboratory accidents, and writes `africa_disease_crisis_active` only after `bio_seed_dispatch_status` is the supplied acceptance receipt. Containment full, partial, and failure paths call native countermeasure effects only when an episode exists; stale receipt-only targets record failure instead of becoming containable.

### High, fixed: release failure and target loss did not produce a native backfire path

Full and partial Action 73 effects revalidate `africa_disease_weapon_target_is_valid`; an invalid or lost target records `africa_disease_weapon_release_failed`, starts the 45-day host cooldown, spends one available payload as a recorded backfire attempt, increments the release count, and attempts a native laboratory accident. The accident writes a crisis flag only when the native route accepts it.

### High, fixed: Actions 74-76 could select a dead, uncapped, unmanifested, cooldown, or uncontrolled target

`africa_validate_action_specific_requirements` and `africa_ai_selected_target_is_candidate_for_action` now require Evolution III, the package-ready gate, the active-action cap, the global formation cap, all four family manifest flags, no family spawned-once receipt, no family cooldown, and an owned-and-controlled target state. `africa_strange_force_spawn_guard` repeats the package, cap, ownership, manifest, cooldown, and exact-family checks before creating a unit and increments the global formation count only after a guarded spawn result.

### Medium, fixed: release counts were not guaranteed to exist before the first increment

Review authorisation initialises the host release counter and accepted target releases initialise the target counter before incrementing it. A payload-spending backfire also initialises the host counter when a legacy or interrupted state has no variable.

### Medium, fixed: stale action target receipts survived cancellation or annexation

`africa_cleanup_action` and `africa_cleanup_annexed_action_target` call `africa_disease_cleanup_target_receipts`; the helper clears temporary dispatch/result variables and dispatch-failure receipts while leaving native episode history authoritative.

### Medium, fixed: AI high-chaos picker assigned positive weight to unavailable formation actions

The AI target trigger has explicit 71-76 branches and excludes those IDs from the generic fallback. `africa_ai_strange_force_action_pool_is_open` gates the 74-76 entries in `africa_ai_pick_action_in_selected_family` until package, active-action cap, formation cap, and owned/controlled preflight are open. Family manifest, spawned, and cooldown checks remain target-specific.

## Decision-category lifecycle notes

The review decision `africa_authorize_fictional_pathogen_review` remains a one-time host decision after Evolution III. It costs the configured 50 political power and 10 command power, writes the explicit authorisation and research-site receipts, creates a two-unit payload reserve, initialises research progress and release count, and selects one native agent slot without starting an outbreak.

Selectors 71-73 remain host-visible only after authorisation. Action 71 requires an episode target. Action 72 requires authorisation, an unfinished countermeasure, and a host, crisis, or research-site target. Action 73 requires the reviewed countermeasure, one payload, no cooldown, and a wartime eligible target.

Selectors 74-76 remain package- and active-cap-gated. Their shared validator is the authoritative preflight after a country target is selected, and the spawn guard repeats it at effect time to protect against target loss between selection and resolution.

## Mission quality notes

All six rows use the existing host-owned high-chaos category and shared targeted missions. Actions 71, 73, 74, 75, and 76 use the long band; Action 72 uses the epic band. Their configured default windows are respectively 225, 165, 270, 270, 210, and 360 days, with the existing minimum and maximum bands. The target country owns the objective region through its controlled African states; success resolves through `africa_resolve_action`, timeout calls `africa_timeout_current_action`, and cancellation calls `africa_cancel_action` after generation and active-record checks. Duplicate risk is bounded by the shared active-action generation, target arrays, family one-use receipts, and cooldown flags.

## Cost and requirement clarity

The shared quote kernel computes dynamic manpower, equipment, factories, command power, fuel, intelligence, trains, stability, confidence, burden, pressure, access, overlay, war, and active-action surcharges for each action profile. Actions 71-76 therefore retain resource-specific dynamic payment and affordability checks rather than a flat political-power exchange. The review decision uses the dedicated fixed authorisation cost because it is a one-time project start, not an action quote.

## AI validity and route-lock notes

The AI target gate now mirrors the player validator for 71-76, including disease episode, authorisation, countermeasure, payload, war, package, cap, manifest, cooldown, spawned, and owned-control checks. The high-chaos picker no longer samples 74-76 when their shared deployment preflight is closed. No numeric AI weights were changed; only eligibility routing was narrowed.

## Localisation and tooltip coverage

`localisation/english/012_african_union_l_english.yml` describes the explicit review gate, native episode requirement, accepted lifecycle receipt, backfire behavior, package manifests, formation slot, owned-control requirement, one-use receipt, and recovery cooldown for each action. The review decision retains its command-power custom tooltip and effect tooltip.

## Cleanup and exploit-risk notes

Native episode flags and history remain owned by the biological lifecycle. Event 012 cleanup removes only temporary dispatch/result variables and Event 012 receipts, so cancellation cannot erase an outbreak or manufacture a clean state. Payload debit occurs only after an accepted deliberate dispatch, while an accepted backfire consumes one payload and enters the native accident route. Formation stockpiles, templates, and units are created only inside the exact manifest/cap/control guard, and the one-use family receipt prevents repeat farming.

## Changed files and identifiers

- `common/scripted_effects/012_africa_disease_effects.txt`: `africa_disease_authorize_review`, deliberate seed dispatch, laboratory accident dispatch, accepted-only crisis/release counters, native containment/research/weapon outcomes, backfire, and cleanup.
- `common/scripted_triggers/012_africa_disease_triggers.txt`: review, episode, payload, eligible-state, and wartime target gates.
- `common/script_constants/012_africa_disease_constants.txt`: disease review, payload, research, release-count, and cooldown tuning.
- `common/scripted_effects/012_africa_action_effects.txt`: 71-76 validator gates, native outcome hooks, formation spawn guard/cap receipts, and disease cleanup call sites.
- `common/scripted_triggers/012_africa_ai_profile_triggers.txt`: explicit 71-76 AI target branches and `africa_ai_strange_force_action_pool_is_open`.
- `common/scripted_effects/012_africa_ai_profile_effects.txt`: high-chaos picker preflight branches for 74-76.
- `localisation/english/012_african_union_l_english.yml`: action descriptions and review text.
- `docs/events/012_africa/fictional_disease_route.md`: native lifecycle, backfire, cleanup, and probability evidence update.

## Evidence and validation

The refreshed HOI4 event scan for `chaosx.nr12.1` returned `EVENT_INSPECTED_PARTIAL` with no blockers at workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `ca11a1b480a2670b3197efec96797c16a8af65c8d365d4611328332c8e578f29`, graph hash `17f8cd8725e26fb3c1eb039a7a316669383b0a5cb88454270f16ef70915de3a7`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a92d6c2082e96c152dfac62e6e6be47aaf67a74027310bd20e1f26bc20dd3ca/2be6b3ec36060b8f1673150319f7160d52c3a5b5f9fe476d47ee5821e2e5997a/event-scan-ca11a1b480a2.json`.

A later cached scan also returned `EVENT_INSPECTED_PARTIAL` with no blockers at revision `2cd411c138488776c2a8607a5685f8728ffccb7df3975a0afc20d530daec9a8a`, graph hash `3b4dcc4460b8649d2784a76409a7d91967950c217a7e4321bd2bdea2eb8eb6fc`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac213e33edc65510ac76cae1c769cca52e56a1a74e853072ad8b59b2a3707050/4e3411794fd8fbf3202a46620211ba5a9786a19170fb9c30c8a417bd17537876/event-scan-2cd411c13848.json`.

The matching overview render returned `EVENT_RENDERED_PARTIAL` with no blockers and layout hash `15077e8958576ace82f49f6e4494bdeb5e4fc2617edb03e7ada7424df1949138`; manifest artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f9896724f1f2b2f87b61ca05bebd06a8648ed66ece9dbc1311e1c2838aa217a/b8a07f8cc69c2c3ab2745dd384b68ef85fd758380161a4486ffaf7bb662e9fea/event-overview-ca11a1b480a2-manifest.json`.

The probability baseline inspected the full random-list workspace and the declared high-chaos picker. The static ten-entry baseline measured 0.1 per entry only inside that declared pool (`probability-c837d54ef27f711abe2a0a08`, source revision `60c8ce4b6452af5ab7fd9bd088ed652003c8f30f13681c116758ed947faebfd0`, scenario hash `f93f74cfc5902c0a1c5f175b9ecec5b2583d551ffa8efbc0d80080983a794666`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa3f71bdeb349a490995c67026f7e77a4425277890024ed8f6e9bb1f724b6c00/380462aedd9c77593a8118a9a0f7553481f4092262674bf80b032907e6a1bd92/probability-c837d54ef27f711abe2a0a08.json`). The same-source compare (`probability-5e05c8b6222f2f508adb716b1`) returned zero comparison changes, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fa19d523bd12f2f285e88f4fc0b9c8f863f4a9a88ca417a03eb76a1bede6ef9/76422a28e0ad03f76a1a87f60355a125cc33bdf80c510ddde5208d7d06e6bf4b/probability-5e05c8b6222f2f508adb716b1.json`; a second post-patch compare timed out while negotiating with the MCP host, so no numeric before/after delta is claimed.

The post-patch random-list inspect succeeded at source revision `4a6d4102fc8a40c27cce28ce50adb167c85c3923482d3cbbd7dd1fc08d962ac1`, source hash `dce9b2319a247b720dd61c949e60cfcc8a3dbca9b2b76fff0961c1417419d2c5`, with four gated pools (10, 7, 7, and 4 entries) and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07d5b8e50ffaad3e301f3e5d113f9c42db4536af1588a7d47f248d9074f22f0c/ffc0b3894dd66bc45ee9c62e4eb4592c8e26fd4c6689e837fa3d4242984d306b/probability-inspect-dce9b2319a24.json`. The same A-D six-scenario post-patch compare (`probability-246ef5b92db382ab585cf757`, scenario hash `5dafee280144e0cdc1408462f4e14afce91873ccb280e1237349dd5a8c0969c3`) returned 60 rows, zero unresolved or diagnostics, and zero comparison changes; JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9373f27a790cf04d8cbdc154197aff58afc41a3b747354881e07a6a6a2656cc/6284d535793cecc7eb48898600944c6aaeff5f871ddf0c13c2f801cb113b1b08/probability-246ef5b92db382ab585cf757.json` and comparison SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/2c9a5f178c19ca54993d56812d6c88aafdc28b90d76299b42cc742c99849afde/probability-probability-246ef5b92db382ab585cf757-comparison.svg`.

The probability adapter did not bind the helper or final validator to arbitrary scenario state keys, so the compare is parser-clean gated-pool evidence rather than proof that A/B/D closed branches are rejected at runtime. Full controller odds remain unresolved because dynamic temporary weights, target arrays, family selection, and three-draw scoring are outside the supported pool projection. `custom_weighted_pool` inspect timed out negotiating with the MCP host. MTTH inspection returned `PROBABILITY_SURFACE_EMPTY`; sequence and simulation were skipped because no complete cadence/recovery manifest or uncertain distributions were declared.

## Remaining issues and simplifications

No new disease API, country tag, world iteration, portrait, focus, GUI, country package, ledger, workbook, or unrelated system was introduced. Native episode history intentionally persists after Event 012 cleanup. The final post-patch probability compare is blocked by MCP snapshot negotiation; the successful same-source compare and source-level validator evidence are retained above.
