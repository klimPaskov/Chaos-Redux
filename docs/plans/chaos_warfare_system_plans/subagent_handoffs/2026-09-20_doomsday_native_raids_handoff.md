# Native doomsday raids handoff

Disposition: source implementation under final integration review. The country-root event bridge is installed; live engine behavior and the MCP native-raid adapter remain unverified.
Acceptance basis: the parent explicitly instructed preservation of the four-agent, multi-state catastrophe through one native raid per CBRN category, with one native essential lot per agent reserved at preparation and only the remaining stock debited in the successful guarded callback.

## Changed surfaces

- `common/raids/cbrn_doomsday_raids.txt` defines `chemical_stockpile_doomsday_raid` in `chemical_raids` and `biological_stockpile_doomsday_raid` in `biological_raids`.
- `common/decisions/chemical_warfare_decisions.txt` and `common/decisions/categories/chemical_warfare_categories.txt` were removed because they contained only the two decision attack entry points and their shared category.
- `common/scripted_effects/cbrn_chemical_doomsday_effects.txt` enters through `cbrn_chemical_doomsday_native_raid_outcome`, and `common/scripted_effects/biological_doomsday_effects.txt` enters through `bio_doomsday_native_raid_outcome`. Both wrappers fire the immediate hidden country events in `events/cbrn_doomsday_raid_bridge.txt` for their full guarded release and news transaction.
- `common/scripted_effects/biowarfare_effects.txt` no longer exposes the decision-facing `bio_unleash_stockpile_doomsday` wrapper.
- Doomsday triggers and constants in `common/scripted_triggers/` and `common/script_constants/` carry the native visibility, launch, target, reservation, and one-shot gates.
- `localisation/english/cbrn_doomsday_raids_l_english.yml` describes both raids and their four outcomes, while the removed decision keys were cleared from `localisation/english/chaosx_decisions_l_english.yml`.
- The shared raid category owner added lightweight doomsday visibility gates and exact availability gates to `common/raids/categories/chaosx_raid_categories.txt`, and removed free targeting because these raid types use state targets.

## Behavior and balance

Each raid prepares for 14 days at a supply-node origin, assigns a land division with at least three infantry or motorized battalions, uses army intelligence through its shared category, costs 25 Command Power, and natively reserves one of each of four equipment archetypes.
Preparation therefore requires at least one of all four agents, where the former decision required any one agent.
The selected state validates the native raid target, while the original chemical controlled-state array or biological controlled-state plus adjacent enemy-held border array determines the exact release zone.
On success or critical success, a single outcome callback saves the actor and target, rechecks government, war, surrender, policy, target, and one-shot gates as applicable, and sets the country commitment flag before any irreversible batch dispatch.
The resolver then debits only stock that remained after native reservation, includes the four reserved lots in the existing per-agent allocation and history, and retains the original evidence, attribution, Condemnation, fallout, and doomsday news event paths.
Failure and limited success leave the remaining stockpiles untouched and do not fire the catastrophe, news, or one-shot flag.
After a valid successful callback, the one-shot country flag prevents a second prepared raid from repeating the release even if a later batch record fails partially.
As before, the existing allocation never fabricates a lot, so fewer real lots than eligible states means some eligible states do not receive that agent.

## Evidence and limits

The installed vanilla `common/raids/_documentation.md` confirms native essential equipment collection at raid creation, state targeting, supply-node origin, assigned division requirements, native timers, and the four outcome hooks.
It does not specify cancellation refund or destruction behavior for essential equipment, so those effects remain an engine evidence gap and are not claimed as validated.
`hoi4.probability_inspect` found both baseline `decision_ai_will_do` candidates in the former decision file, but returned `no_weighted_surfaces` for the new raid file because the installed service exposes no raid AI adapter.
The baseline decision source revision was `c19ea29d1d0605ac215866fc39edc15bfda0d765e58879befd795f496d4c0fff`, and no meaningful scenario-matched `hoi4.probability_compare` is possible through the installed adapter set.
Narrow `hoi4.event_inspect` queries for `chaosx_cbw_doom.1` and `.2`, and `hoi4.event_render` for `.1`, returned partial event evidence because the large workspace deferred helper and lifecycle passes, with no blocking diagnostics reported.
The `chaosx_cbw_doom.1` render manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3419c038349c9a32665fed1f72be97ae6cee2127cda073bee0e6d82c7a95876/f5efbc99e4dacc4310a1ea6b533f9f5f5a50bc6a05945446590e3d119abd0c3a/event-neighborhood-07eac690bf22-manifest.json`.
The static localisation audit reported zero duplicate keys, zero missing BOMs, and zero missing language headers; its six missing event title or description keys are outside this doomsday edit.

The final cross-audit confirmed that the biological doomsday dispatch sets and clears `bio_native_raid_dispatch_in_progress` around each deliberate lifecycle seed, and the shared lifecycle command-power recovery gate checks that flag. Both doomsday resolvers debit only the balance still in stock after the four native essential lots are reserved. Both commit their one-shot country flag before a valid success dispatch. Loss of the selected state, loss of the last-resort condition, or a second simultaneous prepared raid fails the outcome gate without a second batch. No direct Command Power grant or script refund is present in these resolvers.

Native `actor_effects` have raid-instance `ROOT`. Each successful callback saves regular event targets for exact actor and selected state, then fires `chaosx_cbrn_doom_raid.1` or `.2` immediately under the actor country. The event verifies its actor marker equals country `ROOT` and runs the entire guarded release and news sequence there. Temporary variables do not cross the event; the doomsday resolver reconstructs all of its inputs from the actor country, selected state, and existing stock. Source searches found no global event-target writer for the doomsday marker prefixes. The installed documentation supports regular event-target propagation into fired events, but the MCP event trace is partial and does not prove live engine behavior.

Fresh `hoi4.probability_inspect` on `common/raids/cbrn_doomsday_raids.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, source revision `64d12809ba9a5e2432143a2e6e28e4ce942bedf89d62f9870ec8750ae7a887ad`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21081e580cbec01193146347cf1e9f8d3934430316a8de8d0a59695fb3a93727/1b1e50552b69f93b9a33360a45b5b8f3b702d67870c74b15c399344574b123d7/probability-inspect-98b5f8e13e8d.json`. Fresh narrow traces of `chaosx_cbw_doom.1` and `.2` returned `EVENT_INSPECTED_PARTIAL` at source revision `316825c8445e7868f05adbf83dd97f211030552e30b1ca364eb0c1b0084471fd` because the large workspace deferred helper and lifecycle passes. The adapter reported no blocking diagnostic, but did not establish full chain coverage.

Fresh `hoi4.event_inspect` traces of `chaosx_cbrn_doom_raid.1` and `.2` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics and a 64-path inline inventory limit. Reports: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d379103f2e0c26cdd1080d5a5aa791a8c0e47ba5181d8e546475b13704c0a9ce/9043c0eed95f755cceef7501aba496a266981a26350ef01d960fd25b4d51d621/event-trace-70f0dc4645cc.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d02e6113a27d68f968a048ed062fab5ab690adfac07754e310a10515f59c57c/4500f6299d5faa53fb22beb8dd05965a9e9c497b0f204ae1d6835ccde1425955/event-trace-70f0dc4645cc.json`.

The `.1` bridge scope render returned `EVENT_RENDERED_PARTIAL` at source revision `53cfc668c05d032d7d279e9e9b3ddd7bfd6852cc288bbd5c857f7600bc679964`, with deferred helper/lifecycle coverage and no blocking diagnostic; manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67a06c45e3cbf10678fc54a0d02c1116d015cab1e342ef03b4e299b0efe41e75/c6fbbe14a03d163cedea549d60d1711475cde275e68e9703fddc8b745a677ab4/event-scope-53cfc668c05d-manifest.json`.

## Follow-up ownership

The documentation owner is reconciling `common/scripted_effects/cbrn_chemical_doomsday_effects.md` and CBRN system documentation with the native flow.
The parent retains final integration review, any broader probability audit, and the report of native cancellation and reserved-equipment engine limits.
No commit was made by this worker.
