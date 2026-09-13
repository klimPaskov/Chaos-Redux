# Event 027 Doctrine Research completion audit

> **Superseded status notice (2026-09-01):** This dated completion audit is preserved as historical evidence and is superseded as a current status authority by ../documentation_state.md. Its pre-reconciliation allowlist and receipt-status claims must not override the current source evidence recorded there.

Date: 2026-08-30

Auditor role: isolated read-only event completion auditor

Repository: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`

Audit target: the current working-tree candidate for Event 027, not a committed release revision

## Overall verdict: BLOCKED

Event 027 is not complete and is not presently safe to enable as an accepted implementation. The source contains substantial new doctrine adapters, event pages, AI score tables, lifecycle hooks, Event Log wiring, achievements, and finished art, but three independent defects prevent the core feature from satisfying its acceptance contract:

1. A newly appended country batch immediately fails its own alignment invariant because batch arrays are required to have the same length as receipt arrays. Batch creation appends a batch but no receipt, then calls initialization again; initialization marks the country ledger corrupt before the batch can start.
2. Empty-track advancement is intentionally behind a global proof flag that no source sets. A country can adopt a Grand Doctrine, but it cannot select the first subdoctrine on an empty track and therefore cannot continue the intended adoption-then-mastery sequence.
3. Evolution pacing is absent. The declared 90-day pacing constant is unused, while every currently eligible evolution is recorded immediately during one firing and the highest currently enabled batch size is selected immediately.

The exact-one-level mastery operation is also not proven against low, middle, final, or banked-mastery states. It repeatedly adds one mastery point until the observable level rises, but the official engine API exposes mastery-point mutation rather than an atomic one-level mutation. The postcondition detects spill only after the native mutation and cannot restore overwritten or consumed banked progress.

No live-game validation is claimed. No gameplay, localisation, workbook, asset, or shared-framework file was edited by this audit. This handoff is the only file authored.

## Status by acceptance area

| Acceptance area | Status | Completion finding |
| --- | --- | --- |
| Root event, category, and automatic registration | PARTIAL | `chaosx.nr27.1` exists, is triggered-only, and Event 027 is registered as a default-enabled repeatable event, but its ordinary chaos requirement is Tier 1 rather than the accepted Calm/Tier 0 requirement. |
| Global participant snapshot | PARTIAL | A single immediate `every_country` snapshot exists, but the local “live” predicate excludes capitulated countries and every country with no controlled state; the specification does not approve that narrower definition. |
| Adapter registry and domain safety | PARTIAL | Army, Navy, Air, Special Forces, and Chaos Warfare rows exist and the future-domain row fails closed, but every current row asserts one-step capability without engine proof. |
| Grand Doctrine adoption | PARTIAL | Adoption is separated from Event 027 mastery and guarded against replacing an active Grand Doctrine, but the post-adoption empty-track route is closed. |
| Active-track exact mastery transaction | BLOCKED | Source checks `post_level = pre_level + 1`, but uses iterative point grants and has no accepted low/middle/final or banked-mastery proof. |
| Empty-track branch selection and first step | BLOCKED | Required proof flag is never set; empty-track options are unreachable. |
| Ordered batch queue | BLOCKED | The batch/receipt length invariant self-corrupts the first appended batch before it starts. |
| Receipt idempotence and recovery | BLOCKED | Prepared receipts exist conceptually, but ambiguous recovery quarantines without reconciling native post-state, terminal rows are retained, and the queue invariant makes the normal path unreachable. |
| Save/reload and country lifecycle | PARTIAL | Annexation, control, puppet, release, subject, and civil-war hooks exist source-side, but no save/reload/tag-switch proof exists and receipt recovery is unsafe. |
| Evolutions I-IV | BLOCKED | Batch sizes 2/3/4/5 and log rows exist, but normal approximately 90-day evolution pacing is not implemented and multiple tiers can be promoted in one firing. |
| Human choice flow and presentation | BLOCKED | Domain, Grand Doctrine, track, and branch events exist, but large pages have no required pagination and the empty-track path prevents fresh branches. |
| AI and weighted probability | BLOCKED | Weighted domain/Grand/track/subdoctrine tables exist and recalculate per choice, but required scenario evidence and comparison are incomplete; several strategy flags have no producer and a first-subdoctrine fallback remains. |
| Shared repeatable cap/recovery | PASS (source) | Event 027 uses the shared repeatable registration and shared post-fire handler rather than a new world pulse. |
| National Breakthroughs cluster | PARTIAL | Cluster 9 and row 9001 exist, but the cluster unlock is Tier 1, Event 027 is the only runtime member, and its role is `required`, so the accepted “guaranteed when selected, optional when another member is selected” behavior is not implemented. |
| Event history and actor policy | PASS (source) | One global history path is used and Event 027 deliberately records no primary or secondary actor. |
| Event Details and evolution details | PARTIAL | Shared Event Details and four evolution previews/localisation entries exist, but their claims overstate currently reachable and proven behavior. |
| Settings and manual fire | PARTIAL | Default-enabled and manual dispatch wiring exists, but enabling the event exposes a self-corrupting queue. |
| Achievements | BLOCKED | All three triplets, effects, localisation, and sprites exist, but First Lesson is unreachable and all three depend on the invalid receipt ledger; required reload/tag-switch and exact-step proofs are absent. |
| Localisation | PARTIAL | All 258 Event 027/achievement source references found by this audit have localisation, but text claims exact advancement and fresh-branch completion that are not proven or reachable; the mandated localisation-auditor handoff is absent. |
| Report art and achievement assets | PASS | Report DDS, nine achievement DDS files, sprite aliases, source manifests, generated-art handoff, and icon handoff are present. |
| Documentation | BLOCKED | The overview describes the implementation as source-complete and receipt-safe despite the closed proof gate and self-corrupting queue. |
| Workbook and CSV exports | PARTIAL | Workbook and exports agree and honestly say `Needs Testing`, but the Event 027 row overclaims fresh five-level completion and uses chaos level 1; the cluster row remains only partially available. |
| CXT extension | PASS (source) | Modifier-free carrier, idempotent setup effect, bounded startup registration, and tag-specific daily repair wiring are present. |
| Event MCP proof | PARTIAL | Required event inspect/render routes ran but returned partial, globally noisy evidence; a usable current-versus-baseline comparison was not produced. |
| Doctrine/technology MCP proof | BLOCKED | Inspect, render, and compare fail before scanning any file with `SCAN_BYTE_LIMIT`. Source review is not equivalent evidence. |
| Syntax/parser confidence | PARTIAL | Targeted source hygiene and brace checks found no listed unsupported constructs or brace mismatch, but focused MCP validation did not establish parser-clean Event 027 behavior. |
| Live-game acceptance | BLOCKED | Not performed and not claimed. |

## Acceptance basis

All files under `docs\specs\027_doctrine_research_specs\` were read as acceptance criteria. The decisive requirements include:

- Event 027 is enabled by default only when it is ready, is Minor Repeatable, and uses a single global history entry with no actor (`027_doctrine_research_acceptance_criteria.md:13-17`).
- Every valid live country receives a snapshot batch and maintains one ordered queue (`027_doctrine_research_acceptance_criteria.md:27`, `:125-136`; `027_doctrine_research_spec_part_1_core.md:61`, `:209-228`).
- Adoption consumes one choice with no mastery; an active Grand Doctrine exposes every valid track; an empty track selects a branch and performs the first step only when safe; no compensation or generic fallback is allowed (`027_doctrine_research_acceptance_criteria.md:37-45`; `027_doctrine_research_spec_part_1_core.md:69`, `:135-149`, `:185-201`).
- A transaction must advance exactly one level, never two, while preserving banked mastery and attribution (`027_doctrine_research_acceptance_criteria.md:44`, `:57-65`; `027_doctrine_research_spec_part_1_core.md:135-149`).
- Evolution I-IV use batch sizes 2/3/4/5 and normal approximately 90-day pacing; a same-day tier crossing is not accepted (`027_doctrine_research_acceptance_criteria.md:98-111`; `027_doctrine_research_spec_part_3_evolutions_balance_ai.md:15-21`, `:31-43`).
- Detailed DR-A01 through DR-G03 AI evidence is mandatory (`027_doctrine_research_acceptance_criteria.md:158-184`; `027_doctrine_research_probability_scenarios.md`).
- Any missing adapter, unverified one-level transaction, banked-mastery issue, missing probability evidence, asset triplet, stale catalog, or untested queue is a completion blocker (`027_doctrine_research_acceptance_criteria.md:268-276`).
- The closure review explicitly leaves implementation and engine evidence pending and forbids a completion claim without MCP comparison and the required audit chain (`027_doctrine_research_review_and_closure.md:9`, `:107-131`, `:203-237`).

## Blocking gameplay findings

### 1. The first batch self-corrupts before it can start

`doctrine_research_append_country_batch` initializes an aligned empty ledger, appends one row to every batch array, appends no receipt row, and immediately calls `doctrine_research_start_next_batch` (`common\scripted_effects\027_doctrine_research_effects.txt:287-318`). `doctrine_research_start_next_batch` calls initialization again before selecting a queue row (`:321-323`).

Initialization sets `doctrine_research_state_corrupt` whenever `doctrine_research_country_state_is_aligned` is false (`common\scripted_effects\027_doctrine_research_effects.txt:168-183`). The alignment trigger requires every batch-array count to equal every receipt-array count (`common\scripted_triggers\027_doctrine_research_triggers.txt:675-700`). After the first append, the batch count is 1 and the receipt count is 0. Therefore the second initialization marks the country corrupt, and the start condition at `common\scripted_effects\027_doctrine_research_effects.txt:323` rejects the ledger.

Receipts are correctly modeled as one row per choice, not one row per batch: `doctrine_research_prepare_receipt` appends a new receipt row with batch ID and choice number (`common\scripted_effects\027_doctrine_research_effects.txt:387-405`). Requiring receipt count to equal batch count is consequently invalid even if the first-start defect were bypassed; a 2-5 choice batch necessarily creates more receipts than batch rows.

Impact:

- The normal participant fanout cannot open the first active curriculum.
- Every later queue, receipt, achievement, and summary claim is unreachable on the intended path.
- A multi-choice curriculum would become misaligned again as soon as its second receipt was added.

Status: BLOCKED.

### 2. Empty-track advancement is permanently closed

The empty-track wrapper requires `doctrine_research_empty_track_is_verified = yes` (`common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt:22274-22286`). That trigger requires the global flag `doctrine_research_empty_track_transaction_verified` (`common\scripted_triggers\027_doctrine_research_triggers.txt:2139-2142`). Repository-wide source search found no setter for that flag. The constants file also records the capability as unverified (`common\script_constants\027_doctrine_research_constants.txt:35-40`).

Visible branch options require the subdoctrine to be active; for example, the first mobile-infantry choice requires `has_doctrine = mobile_infantry` (`events\027_doctrine_research.txt:745-758`). The same pattern is repeated across the branch pages. After adopting a Grand Doctrine, every track is empty, so no active-subdoctrine mastery option is available and the empty-track transaction cannot establish one.

Impact:

- Evolution I cannot perform the accepted “adopt, then begin mastery” sequence.
- First Lesson is unreachable.
- A fresh five-level branch cannot be completed by Evolution IV.
- Every country that starts doctrine-less can adopt but cannot enter a track through Event 027.

Status: BLOCKED.

### 3. Exact-one-level mastery and banked progress remain unproven

The exact-step implementation computes the next observable mastery level and loops `add_mastery` in one-point increments until the observed level reaches the expected level (`common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt:17138-17159`). Tuning declares a one-point increment, 1,000 loop limit, level 5 target, and a 20-level scan ceiling (`common\script_constants\027_doctrine_research_constants.txt:35-38`). The adapter registry declares current rows one-step capable (`common\scripted_effects\027_doctrine_research_effects.txt:23-84`) even though no accepted engine evidence establishes that capability.

Official engine documentation states that `add_mastery` adds an amount of mastery and filters tracks; it does not expose an atomic “advance one level” operation (`C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:1477-1500`). Vanilla uses point grants such as `amount = 120`, reinforcing that the input is mastery progress rather than a level count (`C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\national_focus\china_nationalist_sea.txt:13616-13621`, `:13643-13648`). The official doctrine overview separately defines mastery as progress within a track and lists `has_mastery_level` as a threshold trigger (`C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\doctrines\_documentation.md:5-18`, `:21-28`). The offline wiki agrees (`paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:618-622`; `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md:582-587`).

The preimplementation architect explicitly warned that threshold or incremental point grants are unsafe when reward thresholds differ or fractional/banked mastery may spill (`docs\plans\027_doctrine_research_plans\subagent_handoffs\scripted_system_architect_2026-08-29.md:15-17`). The current loop only observes integer reward levels. It cannot read or restore fractional/banked mastery, and any overshoot is detected only after an irreversible native mutation.

Missing proof:

- low-level direct step;
- middle-level direct step;
- final-level direct step;
- banked mastery on an active subdoctrine;
- banked mastery on an empty track before native branch assignment;
- attribution to Event 027 rather than only native mastery accumulation;
- no second reward crossing at every supported threshold family.

Status: BLOCKED.

### 4. Evolution pacing is not implemented

The constants declare the accepted sizes and `base_pacing_days = 90` (`common\script_constants\027_doctrine_research_constants.txt:27-32`). Repository-wide use search found no consumer of `base_pacing_days` outside that declaration.

The firing profile immediately chooses the highest currently enabled evolution (`common\scripted_effects\027_doctrine_research_effects.txt:227-234`). In the same firing, `doctrine_research_record_new_evolutions` independently records every enabled and previously unrecorded tier (`:236-272`). Evolution triggers directly compare the current global chaos meter with tier boundaries and settings flags (`common\scripted_triggers\027_doctrine_research_triggers.txt:11-26`). There is no pending-evolution timestamp, delayed event, MTTH entry, cadence variable, or state machine enforcing approximately 90 days.

If the chaos meter crosses several thresholds before the next Event 027 firing, that firing records all lower enabled tiers and immediately uses the highest batch size. This violates the accepted “not instant on threshold crossing, and not on the same day as the trigger change” contract.

Disabled lower tiers do not block higher tiers, which is structurally correct, and evolution log rows correctly declare no actor (`common\scripted_effects\027_doctrine_research_effects.txt:236-272`). Those points do not compensate for the missing lifecycle.

Status: BLOCKED.

### 5. Receipt recovery is fail-closed but not receipt-safe

The source prepares a receipt before the native doctrine mutation and marks a successful receipt consumed after decrementing the batch once (`common\scripted_effects\027_doctrine_research_effects.txt:3055-3069`). A replay of a consumed receipt returns success (`:3124-3133`), and an `effect_applied` receipt can be finalized (`:3134-3137`).

However, prepared, ambiguous, and abandoned receipts are all converted to ambiguous and the entire active batch is quarantined (`common\scripted_effects\027_doctrine_research_effects.txt:3142-3148`). There is no native post-state reconciliation that distinguishes “effect never ran” from “effect ran but receipt state was not persisted.” This avoids blind duplicate mutation, but it does not meet the accepted resume-safe contract and may abandon valid remaining choices after a save boundary or interruption.

Completed or quarantined batches and receipt rows are retained rather than compacted during ordinary closure (`common\scripted_effects\027_doctrine_research_effects.txt:3072-3087`). Annexation does clear Event 027 state (`:3537-3571`; `common\on_actions\027_doctrine_research_on_actions.txt:48-54`), but ordinary terminal cleanup, save/reload recovery, and long-run ledger growth are not proven.

Status: BLOCKED.

## Additional gameplay and integration findings

### Participant scope: PARTIAL

The fanout snapshots recipients immediately through `every_country` and appends at most one batch per recipient in that firing (`common\scripted_effects\027_doctrine_research_effects.txt:275-285`). This matches the required snapshot model.

The eligibility predicate requires existence, non-capitulation, and more than zero controlled states (`common\scripted_triggers\027_doctrine_research_triggers.txt:28-32`). That silently excludes capitulated governments, governments in exile, and any otherwise valid country temporarily lacking controlled territory. The specs say every valid live country but do not approve this narrower definition. The exclusion needs an explicit accepted disposition.

### Adapter registry and invalid fallback: PARTIAL

Army, Navy, Air, Special Forces, and Chaos Warfare are registered with explicit folder, feature-gate, AI selector, cleanup selector, and one-step capability fields (`common\scripted_effects\027_doctrine_research_effects.txt:23-84`). The future custom-domain row uses an invalid folder, feature gate 99, AI selector 0, and cleanup selector 0 (`:85-94`), so an unknown future adapter fails closed rather than fabricating a reward. This is a source-level PASS for invalid-domain fallback behavior.

The current rows' `one_step_capable` assertion remains unsubstantiated because the doctrine MCP route cannot inspect their graphs and the exact transaction proof is missing. Special Forces is DLC/technology-gated (`common\scripted_triggers\027_doctrine_research_triggers.txt:46-58`), and Chaos Warfare calls its owner capability trigger (`:59-62`). Those gates are structurally appropriate but not engine-validated here.

### Choice pages and navigation: BLOCKED

The event package supplies root/fanout events, a domain page, a Grand Doctrine page, a track page, a hidden dispatcher, branch pages, and summary/terminal pages (`events\027_doctrine_research.txt:12-3778`). The domain page has seven options (`:41-144`), the Grand Doctrine page has fifteen (`:146-325`), and the track page has twenty (`:327-586`). Branch pages contain up to twelve options, for example `chaosx.nr27.63` at `:1394-1642`.

There are no previous/next controls or page-state variables. The required bounded pagination contract is therefore absent (`027_doctrine_research_acceptance_criteria.md:47`, `:147`; `027_doctrine_research_spec_part_2_choice_flow.md:236-251`). The options also do not present a complete dynamic current-level/next-level/completion summary for every candidate. Even if the ledger were repaired, the visible route would not meet the accepted navigation standard.

No dedicated scripted GUI is introduced by Event 027. These are ordinary events using the shared Event Log/Event Details framework. A `chaosx_event_ui_worker` handoff is therefore not required for this event.

### AI and probability: BLOCKED

The source does implement weighted `random_list` selection for domain, Grand Doctrine, track, and 107 subdoctrine rows (`common\scripted_effects\027_doctrine_research_ai_effects.txt:14-2107`). The AI choice loop recalculates after each successful choice and is bounded by the active batch size (`common\scripted_effects\027_doctrine_research_effects.txt:3505-3534`). This is materially deeper than the legacy flat Army-only baseline.

Source weaknesses remain:

- Domain scores use broad binary checks for divisions, factories, war, coastline, faction, and one representative available track (`common\scripted_effects\027_doctrine_research_effects.txt:3314-3377`). They do not establish the full scenario-specific force, production, geography, strategic-plan, completion, and cross-domain tradeoffs required by DR-A01 through DR-D06.
- Army, Navy, Air, and Special Forces scores read `doctrine_research_ai_strategy_*` country flags (`common\scripted_effects\027_doctrine_research_effects.txt:3329`, `:3340`, `:3351`, `:3362`), but repository-wide search found no setter for those flags. Their strategy bonus is dead under current source.
- When subdoctrine scoring finds no candidate, AI invokes `doctrine_research_ai_choose_first_subdoctrine` (`common\scripted_effects\027_doctrine_research_effects.txt:3515-3521`). That ordinal fallback is not the accepted scored-pool behavior and obscures why the weighted pool was empty.
- CBRN candidates use owner viability and establishment triggers in the candidate score table (`common\scripted_effects\027_doctrine_research_ai_effects.txt:1964-1997`), but required DR-D01 through DR-D04 parity/ranking evidence was not completed.
- Empty-track candidates are unavailable because the proof gate is closed, so DR-C03, DR-C07, DR-E01, and DR-E04 cannot represent the accepted route.
- The queue defect prevents any multi-choice source path from reaching the recalculation loop in normal operation.

The mandatory `chaosx_ai_probability_auditor` route was invoked read-only. It successfully began `hoi4.probability_inspect` against the current AI source and identified weighted `random_list`/custom-pool surfaces, but the audit did not complete scenario evaluation, sweep, seeded simulation, sequence analysis, rendered outputs, or a same-scenario baseline comparison before this handoff cutoff. Several inspect calls either failed immediately on unsupported source/adapter combinations or took minutes for one pool discovery. Consequently, DR-A01 through DR-G03 remain BLOCKED as probability evidence, even where source-only reasoning is possible. The historical baseline handoff already classifies every named scenario unresolved without engine evidence (`docs\plans\027_doctrine_research_plans\subagent_handoffs\probability_baseline_2026-08-29.md:9`, `:225-279`).

No normalized probabilities, dominance bounds, starvation rates, seeded distributions, rank reversals, or timing distributions are claimed.

### Queue and country lifecycle: PARTIAL beyond the core blocker

The source records stage and size per batch, scans from the oldest queued row, and keeps one active row (`common\scripted_effects\027_doctrine_research_effects.txt:287-350`). These are the right structural concepts, but the alignment defect prevents them from functioning together.

Narrow hooks reconcile state-control, puppet, release, subject, and civil-war transitions and discard the annexed country's state through `FROM` (`common\on_actions\027_doctrine_research_on_actions.txt:8-55`). The offline on-action reference confirms `on_annex` uses ROOT as winner and FROM as annexed, and confirms the state-control scope chain (`paradox_wiki\On actions - Hearts of Iron 4 Wiki.md:122`, `:171`). No recurring whole-world Event 027 on-action was added.

No direct save/reload, mid-dialog country-switch, tag-switch, or queued-stage preservation proof exists. The achievement acceptance prompt specifically requires queue, tag, and reload tests (`027_doctrine_research_achievement_prompt.md:150-161`).

### CXT fixture: PASS at source level

The package supplies a modifier-free hidden carrier (`common\ideas\027_doctrine_research_cxt_extension_ideas.txt:4-10`), idempotent setup logic (`common\scripted_effects\027_doctrine_research_cxt_effects.txt:21-25`), bounded `on_startup` registration, and `on_daily_CXT` repair/synchronization (`common\on_actions\027_doctrine_research_cxt_on_actions.txt:9-29`). This matches the extension contract described in `docs\testing\chaosx_test_country.md:92-105`, `:154`.

The fixture wiring does not constitute proof of the exact mastery operation and was not run live.

## Shared systems

### Repeatable registration and settings: PARTIAL

Event 027 is in `global.repeatable_events` (`common\scripted_effects\chaosx_logic_effects.txt:307-320`), and the shared handler records first history, halves the cap, updates weight, applies global pacing outside cluster context, and attempts cluster fanout (`:1243-1286`). This is a source-level PASS for using the shared recovery/cap path.

Event 027 is default-enabled (`common\scripted_triggers\chaosx_settings_triggers.txt:10-41`) and manual dispatch points to `chaosx.nr27.1` (`common\scripted_effects\chaosx_settings_effects.txt:4865-4868`). Default enablement is not acceptable while the queue and proof gates remain blocked.

The ordinary required chaos tier is Tier 1 (`common\scripted_effects\chaosx_logic_effects.txt:183-185`), while the accepted baseline is Calm/Tier 0 (`027_doctrine_research_acceptance_criteria.md:194`; `027_doctrine_research_spec_part_1_core.md:11`). This is a direct acceptance mismatch.

### Event history, Event Details, and evolution log: PARTIAL

The shared actor mapper explicitly leaves both Event 027 actor fields empty (`common\scripted_effects\chaosx_events_log_effects.txt:198-207`). The repeatable handler records history only on its shared firing path (`common\scripted_effects\chaosx_logic_effects.txt:1250-1254`, `:1280`). This is structurally aligned with the one-global-row/no-actor contract.

Event Details registers all four evolution previews (`common\scripted_effects\chaosx_events_log_effects.txt:2892-2915`). Scripted localisation supplies Event 027 detail text and four title/body selectors (`common\scripted_localisation\chaosx_scripted_localisation_events_log.txt:955-956`, `:2206-2209`, `:5783`, `:8472-8475`). English localisation exists at `localisation\english\027_doctrine_research_l_english.yml:294-305`.

The detail text claims each country gains choices until its curriculum completes and every evolution body claims one-step advancement or fresh-branch capability. Those statements are stale while the batch never starts and the empty-track/exact-step proofs are missing.

### National Breakthroughs: PARTIAL

Cluster ID 9, 120-day cluster cooldown, and row ID 9001 exist (`common\script_constants\event_cluster_constants.txt:15-26`, `:76-87`, `:151-157`). Event 027 maps to the cluster (`common\scripted_effects\chaosx_event_cluster_effects.txt:606-614`) and the runtime row has minimum Tier 0 and Medium severity (`:1524-1538`).

Two acceptance mismatches remain:

- The cluster itself unlocks at Tier 1 (`common\script_constants\event_cluster_constants.txt:285-292`), so the Tier 0 member row cannot participate at Calm.
- Event 027 is the only runtime member and is registered as `required` and primary (`common\scripted_effects\chaosx_event_cluster_effects.txt:1532-1538`). This can make Event 027 guaranteed when its cluster is selected, but it does not implement Event 027 as optional when another National Breakthroughs member is selected (`027_doctrine_research_acceptance_criteria.md:191-204`).

The workbook concept list may name future/stale members if status remains honest. The runtime currently has no other member to exercise optional participation.

## Achievements: BLOCKED

The three achievement registry entries exist (`common\achievements\chaos_redux_achievements.txt:4059-4072`), and their effect checks inspect consumed Event 027 receipts rather than transient UI state (`common\scripted_effects\027_doctrine_research_achievement_effects.txt:10-268`). English names, descriptions, and tooltips exist (`localisation\english\027_doctrine_research_l_english.yml:306-315`).

The triplets are fully wired in GFX (`interface\chaosx_achievements.gfx:1564-1572`).

Completion blockers:

- First Lesson requires a human batch larger than one with an adoption receipt followed by a later same-domain mastery receipt (`common\scripted_effects\027_doctrine_research_achievement_effects.txt:10-65`). The empty-track gate makes that sequence unreachable.
- Single School requires a completed Evolution IV five-choice batch and five exact pre+1 mastery receipts (`:70-151`). The first batch self-corrupts, empty-track setup is closed, and exact-step evidence is missing.
- Joint Curriculum deduplicates four track identities across consumed receipts (`:158-268`), but the receipt ledger is invalid.
- The required direct tests, save/reload, and human-control/tag-switch checks in `027_doctrine_research_achievement_prompt.md:54-97`, `:113-161` were not supplied.

## Assets: PASS

The report sprite points to the installed DDS (`interface\027_doctrine_research.gfx:10-11`). The installed file is `gfx\event_pictures\027_doctrine_research\027_doctrine_research_report.dds`, 147,968 bytes, SHA-256 `D7299954367B8374142A8A8242CEB8DE9117E80D3809D92CAED1339F188281A5`.

All nine achievement DDS files exist under `gfx\achievements\` and are referenced by the three completed/grey/not-eligible sprite triplets (`interface\chaosx_achievements.gfx:1564-1572`). The asset manifest records source prompts, source hashes, processed variants, installed DDS destinations, review PNGs, and contact sheet (`docs\assets\027_doctrine_research\manifest.md:25-54`).

The generated report-art handoff says the final report image was complete for parent wiring (`docs\plans\027_doctrine_research_plans\subagent_handoffs\generated_event_art_2026-08-29.md:5-27`), and the icon handoff lists the nine installed deliverables (`icon_artist_2026-08-29.md:88-107`). Their old “parent wiring pending” notes are stale because the current GFX aliases now exist, but the assets themselves are complete.

No character portrait, custom 3D unit, unit audio, bespoke unit counter, skeletal animation, frame animation, or dedicated event-owned scripted GUI is in scope.

## Localisation: PARTIAL

A source-reference scan found 258 Event 027 and achievement localisation references and no missing keys in the current English package. Event flow text, doctrine/domain names, result/summary text, Event Details, evolution titles/bodies, and achievement strings are present (`localisation\english\027_doctrine_research_l_english.yml:1-315`).

Material text defects are semantic rather than missing-key defects:

- Evolution text says each option advances exactly one mastery step (`:302-305`) without accepted mastery proof.
- First Lesson and Single School describe currently unreachable sequences (`:306-315`).
- The overview and Event Details text describe curricula as completing despite immediate ledger corruption.

No `chaosx_localisation_auditor` handoff is present. The completion standard explicitly requires that audit route, so this source scan cannot close localisation acceptance.

## Documentation and catalog: BLOCKED/PARTIAL

### Event documentation: BLOCKED

`docs\events\027_doctrine_research\overview.md` exists and identifies the spec package, systems, assets, achievements, and workbook (`:1-118`). It nevertheless overclaims:

- It describes the implementation as source-complete (`:11`).
- It says banked mastery is preserved (`:37`) without proof.
- It says receipts prevent duplicate mutations and the arrays stay aligned (`:41`, `:90`) despite the invalid count invariant.
- It says the implementation was checked against every spec (`:118`) while decisive requirements remain absent.

The documentation must be treated as stale, not as completion evidence.

### Workbook and exports: PARTIAL

The editable workbook row `Events!A28:N28` and exported Event 027 row agree. The CSV row is `docs\spreadsheets\chaos_redux_events_catalog.csv:114`; it records Minor Repeatable, chaos level 1, cluster 9, Medium severity, and `Needs Testing`. The cluster workbook row `Clusters!A10:G10` and `docs\spreadsheets\chaos_redux_clusters_catalog.csv:10` agree on cluster 9, concept members `27, 54, 65, 67, 83, 85, 89`, chaos level 1, and `Partially Available`.

The export files are not mechanically stale relative to the workbook. Their implementation claims are stale:

- Event 027 claims every valid country receives a batch, but the first batch marks itself corrupt.
- Evolution IV claims it can fully develop a fresh five-level branch, but empty-track branch selection is disabled.
- The row uses chaos level 1 rather than the accepted Calm/Tier 0 baseline.

`Needs Testing` and `Partially Available` are honest status labels, but they do not cure the false capability descriptions. No `chaosx_spreadsheet_doc_worker` handoff exists after implementation facts were available.

## Accepted-plan disposition and handoff gaps

Existing Event 027 handoffs at audit time:

- `repo_explorer_2026-08-29.md`: partially promoted. The event was moved to repeatable and broad touchpoints were implemented, but the explorer's requirement for MCP one-level/banked proof remains unresolved (`:104-131`).
- `scripted_system_architect_2026-08-29.md`: partially promoted. Batch, receipt, adapter, and lifecycle structures were implemented, but its exact mastery gate warning was not resolved (`:15-17`, `:350-401`). The current alignment invariant also conflicts with the architect's one-receipt-per-choice model.
- `probability_baseline_2026-08-29.md`: historical baseline only. It explicitly has no usable MCP probability evidence (`:9`, `:85-91`) and all DR scenarios remain unresolved (`:225-279`). No completed post-change comparison handoff supersedes it.
- `generated_event_art_2026-08-29.md`: promoted; report DDS and sprite wiring exist.
- `icon_artist_2026-08-29.md`: promoted; nine DDS files and aliases exist, though its pending-wiring note is stale.

Missing completion handoffs/evidence:

- final `chaosx_ai_probability_auditor` report with DR-A01 through DR-G03 evidence and same-scenario compare;
- `chaosx_localisation_auditor` report;
- `chaosx_spreadsheet_doc_worker` workbook/export handoff;
- parent implementation handoff listing actual gameplay changes and task-specific checks;
- direct exact-mastery proof package;
- queue/save/reload/tag-switch proof package;
- successful Event 027 current-versus-baseline MCP comparison;
- successful doctrine/technology MCP inspect/render/compare evidence.

No accepted improvement addendum was found that is waiting for promotion into the source spec. The spec package remains the source of truth, and its closure document still says implementation evidence is pending.

## MCP evidence and exact limits

### Event chain

Required `hoi4.event_inspect` was run for `chaosx.nr27.1` with helper expansion. Result: `EVENT_INSPECTED_PARTIAL` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

The inspected revision was `55c38793c7fb8252d7fe4ac1271ad6a105a594ec51e1497c2e697f0ea4c946be`. The scan covered the whole event workspace rather than isolating Event 027: 9,643 event nodes, 8,537 unresolved nodes, 24,647 issues, and 23 blocking issues. Validation was false. This global noise means the lint result cannot be treated as an Event 027 parser pass.

Required `hoi4.event_render` was run for overview, state, terminals, unresolved, and targets. Every rendered view was partial. The overview resolved the root and an unresolved helper edge; state, terminals, and targets did not provide the expected Event 027 helper-chain proof. Rendered artifacts were returned under the same workspace/revision, but they do not establish reachability, terminal closure, receipt state flow, or safe resolution.

Required `hoi4.event_compare` was attempted because a pre-change Git revision exists. The default call returned `EVENT_COMPARISON_BASELINE_REQUIRED`. Attempts to supply the cached revision or an in-memory pre-change Event 027 source did not complete within more than two minutes and were terminated. No comparison artifact exists. This is an exact comparison blocker, not a source-level pass.

### Doctrine/technology graph

Required `hoi4.tech_inspect`, `hoi4.tech_render` doctrine view, and `hoi4.tech_compare` were attempted. Each failed with `SCAN_BYTE_LIMIT` before scanning any file. No doctrine folder, Grand Doctrine, track, subdoctrine, exclusivity, unlock, mastery, grant, or asset artifact was produced.

This blocks MCP proof for:

- all ordinary and Special Forces adapter graph identities;
- Chaos Warfare graph parity;
- Grand Doctrine replacement safety beyond source guards;
- track-index mapping;
- empty-track branch assignment;
- exact-one-level mastery and banked mastery;
- current-versus-baseline doctrine graph comparison.

Source and vanilla documentation review is recorded above but is not treated as equivalent engine evidence.

### Weighted probability

The mandatory `chaosx_ai_probability_auditor` was routed read-only and began `hoi4.probability_inspect` for the current weighted surfaces. The adapter discovered weighted `random_list`/custom-pool structures in `common\scripted_effects\027_doctrine_research_ai_effects.txt`, but full named-scenario evaluation and compare did not finish. No completed probability analysis ID, scenario hash, rendered ranking/matrix, seeded simulation, sequence artifact, or comparison ID is available for acceptance.

Status: BLOCKED for all weighted acceptance claims.

## Task-specific validation performed

The following checks were meaningful to this audit and are not live-game validation:

- Read all 16 Event 027 spec files and compared the current source against their explicit acceptance gates.
- Read AGENTS.md and the required event, improvement-loop, subagent, event-planning, event-assets, MTTH, and spreadsheet workflow instructions.
- Consulted the required offline wiki core pages plus Technology, Doctrine, and Achievement references. Relevant doctrine/event/on-action evidence is cited in this handoff.
- Consulted official vanilla doctrine documentation and vanilla point-grant precedents cited above.
- Compared the current working-tree event with the pre-change Git source. The prior event was a 112-line, fire-once, Army-only four-option event; the current source is a major uncommitted replacement. No post-change commit or parent handoff establishes a clean promoted revision.
- Audited batch/receipt call order and proved the first-append count mismatch from the actual call chain.
- Searched the repository for the empty-track proof-flag setter and AI strategy-flag setters; none were found.
- Verified `base_pacing_days` has no consumer.
- Counted braces in Event 027 scripted effects, triggers, on-actions, AI, exact mastery, achievements, events, and scripted localisation; opening and closing counts match in each checked file.
- Searched Event 027 script surfaces for literal `<=`, `>=`, unary negation of variable tokens, and scoped temporary-variable patterns; none were found.
- Scanned Event 027/achievement localisation references: 258 references, zero missing English keys.
- Inspected workbook Event 027 and cluster rows and compared them with CSV exports.
- Verified report DDS hash and the presence/wiring of the nine achievement DDS triplets.
- Ran the mandatory event MCP inspect/render attempts, event compare attempts, doctrine/technology MCP attempts, and probability-auditor route described above.

These checks do not prove in-game behavior, save serialization, UI fit, native doctrine mutation semantics, or probability distributions.

## Required next actions

1. Repair the ledger schema so batch arrays align only with batch arrays and receipt arrays align only with receipt arrays. Add explicit parent/foreign-key validation instead of equal batch/receipt counts. Prove first append, 2/3/4/5-choice batches, multiple queued batches, ordinary closure, quarantine, and cleanup.
2. Decide and implement the exact empty-track transaction only after engine evidence proves native assignment, one Event 027 step, banked-mastery preservation, and attribution. Do not set the proof flag merely to bypass the gate.
3. Replace the point-loop completion claim with a proven exact-step adapter or keep all mastery options disabled. Run low, middle, final, banked-active, and banked-empty tests for every threshold family.
4. Implement the accepted evolution lifecycle with a real approximately 90-day pacing state, one promotion transition at a time, disabled-lower-tier bypass, and preserved batch snapshots.
5. Remove or explicitly redesign `doctrine_research_ai_choose_first_subdoctrine`; wire real owner/native strategy inputs instead of unset Event 027 country flags; then rerun DR-A01 through DR-G03 through `chaosx_ai_probability_auditor` with evaluate/sweep/simulation/sequence/render and a same-scenario baseline compare.
6. Add bounded pagination and complete dynamic candidate state text for domain, Grand Doctrine, track, and branch selection.
7. Correct ordinary Event 027 and National Breakthroughs availability to the accepted Calm/Tier 0 contract, and implement optional cluster participation when another real member is selected.
8. Rerun focused event inspect/render/compare and doctrine inspect/render/compare after resolving `SCAN_BYTE_LIMIT`; do not substitute source review.
9. Run the required localisation auditor, spreadsheet worker, and final completion auditor. Update overview, Event Details text, achievement wording where necessary, workbook, and exports from verified implementation facts.
10. Keep Event 027 disabled for completion purposes until queue, exact mastery, empty-track, evolution, probability, and save/reload proof gates are closed.

## Final completion classification

- Finished: static report art; achievement art triplets and sprite aliases; source-level repeatable registration; source-level no-actor Event Log mapping; Event Details/evolution registration; CXT extension wiring; explicit fail-closed future adapter row.
- Partial: participant definition; adapter coverage; Grand Doctrine adoption; lifecycle hooks; settings; cluster; localisation; achievements; docs/catalog alignment; event MCP structural evidence.
- Blocked: first batch start; all normal receipt processing; empty-track branch setup; exact mastery and banked mastery; evolution pacing; required AI/probability scenarios and compare; doctrine MCP evidence; live acceptance.
- Design gaps: the accepted pagination contract has no implementation; cluster optional-member behavior has no second runtime member; dead AI strategy flags have no owner/source; receipt schema conflates batch-row and choice-receipt cardinality.

Event 027 must not be marked complete.
