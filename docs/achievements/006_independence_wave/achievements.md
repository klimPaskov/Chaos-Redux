# Event 006 Independence Wave achievements

## Purpose

Event 006 defines sixteen achievements around sovereign survival, negotiated host relations, league governance, regional formables, package-specific histories, and `SCN-008`. Their conditions are evaluated from durable Event 006 history rather than resource rewards or periodic country scans.

The implementation is split across:

- `common/achievements/chaos_redux_achievements.txt` for achievement registration;
- `common/script_constants/006_independence_wave_achievement_constants.txt` for every numerical threshold;
- `common/scripted_triggers/006_independence_wave_achievement_triggers.txt` for final-state proofs;
- `common/scripted_effects/006_independence_wave_achievement_effects.txt` for historical ledgers and clocks;
- `common/on_actions/006_independence_wave_achievement_on_actions.txt` for narrow engine events;
- `localisation/english/006_independence_wave_achievements_l_english.yml` for final names, descriptions, and exact condition tooltips.

No daily, weekly, or monthly on-action is used. Wave initialization iterates only the frozen plan's host array. League clocks iterate only the maintained league-member array. Scenario survival iterates only the countries committed by the current scenario plan.

## Achievement coverage

| Achievement | Proof and historical disqualifiers | Runtime status |
| --- | --- | --- |
| Seal of a Sovereign Decade | One-state opening; foundational legitimacy; entrenched recognition; mature capacity; ten sovereign years; no scenario origin, subject history, or voluntary reunion | Wired |
| Sovereignty Without Strings | Entrenched recognition and formidable security; no subject history, client route, or current patron warning | Wired |
| Five Quiet Years | Recognized separation plus property and citizenship settlements; five years without a former-host war; forced recognition is excluded | Wired |
| The Tower Never Fell | Former host attacks; release reaches peace independent while retaining the anchor; a capital loss of thirty days fails the defense | Wired |
| Five Signatures at the Table | Natural formal-league founder; five members; all five charter pillars; pre-formed Common Congress excluded | Wired |
| Four Regions, One Charter | Ten members, four regions, 70 cohesion for two continuous years; formal/durable/reformed phase only; radical and scenario-preformed membership excluded | Wired |
| The Smallest Capital Saved | DM-44 rescue target remains active, independent, and uncapitulated for one year; voluntary reunion invalidates the rescuer's current proof | Wired |
| A Union Beyond Proclamation | Registered formable transaction committed; first-stage and every required initial integration objective completed | Wired for admitted formable families |
| Bolgar's Modern Heirs | Exact `CHU` / IW-043 Event 6 origin; restoration or federal route; states 249 and 256; Soviet Collapse origin excluded | Definition, route-specific proof, and writers are wired. The achievement remains unreachable while the package portrait admission gate is closed |
| The Council Between Two Rivers | Exact `ASY` / IW-058 Event 6 origin; recognition, population protection, Mesopotamian settlement, host-conflict survival, and state 676; client and Soviet Collapse origins excluded | Definition, route-specific proof, writers, and icon triplet are wired. The achievement remains unreachable while the package portrait admission gate is closed |
| Institutions Before Empire | One-state opening becomes a major before a formable, fields the professional army, and leads a successful league goal | Wired |
| The Open-Border Reckoning | Radical route triggers the radical dangerous milestone, then receives an external containment attack and survives one year; scenario-forced qualification excluded | Wired |
| The Long Roll Call | Low-intensity, non-Common-Congress `SCN-008`; after five years at least 85 percent of that plan's released countries remain active and independent | Wired |
| Three Patrons, No Master | Major aid history from three distinct patrons; no dependency history or client route; all concessions bought out | Wired |
| Five Lines, No Shots | Five DM-43 arbitrations in one leadership term; any member war, DM-51 coercion, or a completed DM-60 charter expulsion invalidates that term | Arbitration, war, coercion, and the bounded patron-client expulsion proof are wired |
| One Capital, Ten Years | Former host left with one state; settlements with all ledgered breakaways; never a subject or reconqueror; ten peaceful years, 60 percent stability, two civilian factories, and level-two capital infrastructure | Wired |

## Historical transactions

### Country and patron history

`independence_wave_refresh_country_state` records subject history, patron dependency, institutional major status, and the start of a fully negotiated former-host peace. The patron-channel transaction records a patron only when its cumulative aid reaches the centralized major-aid threshold. Buying out a concession writes proof only after the cost and influence reduction complete.

### League history

Formal proclamation marks the exact founder array. A global provenance marker excludes a scenario-preformed Common Congress, including countries that join it after scenario application, from both founding proof and cross-regional clocks. The marker is cleared on league dissolution, first network initialization, or a genuinely new natural proclamation, so it cannot permanently lock later league generations. The cross-regional clock starts only while member count, region count, cohesion, phase, and route all qualify; it is cleared on threshold loss, exit, split, dissolution, or radicalization. Leadership changes begin a fresh arbitration term. DM-43 increments that term only for the current leader, while member wars, DM-51 coercion, and completed DM-60 charter expulsions invalidate it.

### War, peace, and state control

`on_war_relation_added` identifies former-host reconquest direction, league-member wars, and non-member attacks on the qualified radical bloc. The radical survival date begins with the first qualifying external containment war, not with publication of the dangerous milestone. `on_peace` and `on_peaceconference_ended` resolve the reconquest proof. The anchor-loss grace window is seeded at reconquest declaration when the anchor is already uncontrolled, otherwise `on_state_control_changed` starts it only during an active former-host reconquest. Recovery or the qualifying peace closes the clock, while thirty or more days of loss permanently fails the defense proof.

### Scenario survival

After a successful `SCN-008` commit and type application, the launching country receives the challenge ledger only for Low intensity outside Common Congress. Each committed scenario country is counted once. Annexation and subject transitions update the bounded count through engine on-actions; no global country scan is required.

### Host-remnant proof

After all frozen country origins commit, each unique plan host is checked while its Event 6 bilateral ledger is still available. A host reduced to one state receives its exact required-settlement count. Its ten-year date begins only while it is fully at peace and restarts after any later war ends. Each breakaway contributes at most one settlement receipt. A host reconquest or subject transition is permanently disqualifying for that remnant attempt, including subject status already present when the candidate is initialized. Annexing, voluntarily reabsorbing, or subordinating one of its Event 6 breakaways also writes the host's permanent reconquest disqualifier.

### Formable integration proof

Each admitted formable family writes the two generic integration receipts only from its route-specific completion transaction. FORM03 clears stale receipts when post-charter progression begins, writes both receipts only on full confederal ratification, and clears them during progression cleanup; compromise or failed charters do not qualify.

## Assets and wiring

Achievement art uses the standard HOI4 filename convention and does not require a `.gfx` sprite registration. Each complete set consists of:

- `gfx/achievements/<achievement_id>.dds`;
- `gfx/achievements/<achievement_id>_grey.dds`;
- `gfx/achievements/<achievement_id>_not_eligible.dds`.

All sixteen achievements have all three 64 by 64 runtime DDS files and matching source and processed PNG records under `docs/assets/006_independence_wave/`. The Assyria triplet is supplied by `iw043_iw058_static_icons_2026_07_18`, is installed in `gfx/achievements/`, and has a dated parent visual approval record. Asset completion does not bypass the package portrait and origin-admission gates.

## Validation scenarios

The completion audit must cover at least:

1. one-state survival with and without a temporary subject transition;
2. negotiated recognition versus DM-28 forced recognition;
3. former-host attack, anchor loss below and above thirty days, and peace resolution;
4. natural five-founder formation versus a pre-formed Common Congress;
5. two continuous cross-regional years, including cohesion loss, split, radicalization, and reformation resets;
6. rescue survival and voluntary reunion;
7. every admitted formable family's first-stage integration receipts;
8. leadership transfer, five arbitrations, member war, DM-51 coercion, all seven factual expulsion grounds, a successful DM-60 expulsion for each ground, a DM-60 vote cancelled after commitment, DM-61 coup evidence without civil-war double counting, and DM-62 matching-mandate consumption versus an unauthorized declaration;
9. all five `SCN-008` intensities and every scenario type, confirming only Low non-Common-Congress attempts start the survival ledger;
10. host remnant settlement counting, subject disqualification, reconquest disqualification, and economic thresholds;
11. Event 5 origin collision checks, exact compile-time admission rejection, and fail-closed route-proof checks for the currently unadmitted Volga Bulgaria and Assyria packages.

## Future extensions

All seven accepted factual grounds now enter the same DM-60 expulsion target pool. The remaining league extension is the charter-governed rival-bloc transaction after expulsion; it still needs a separate generation-safe membership contract, visible actions, AI, cleanup, and achievement-scenario coverage. The two package-specific achievements remain fail-closed at country admission until their sourced portrait packages pass the current grounded-country rules.
