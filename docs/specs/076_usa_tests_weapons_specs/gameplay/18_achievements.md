# 18 · Achievements

## Reward difficult outcomes with provable conditions

These proposed achievements use original internal IDs. Their final names, descriptions and flavour are left to the localisation writer. They should recognize a varied American development campaign, difficult survival and useful international action. None awards progress simply for a larger civilian death count.

Register them only in `common/achievements/chaos_redux_achievements.txt`, after inspecting the current unique-ID allocation and existing achievement conventions. Preserve all unrelated entries and IDs. Do not create a second Event 076 achievement registry.

Shared achievement eligibility, setup, difficulty and human-control requirements remain authoritative. Do not claim perfect console or cheat detection if the existing owner does not provide it. A condition must be demonstrated through ordinary valid gameplay and durable event or map receipts.

## Proposed set

### `chaosx_076_multi_service_research`

As the same human-controlled USA identity, complete and receive useful analysis rewards from eight distinct testing families, including at least one land, air and naval family, in at least four distinct foreign minor countries and three continents. Complete the set within four game years from its first counted success.

Only fully verified tests with an actually granted useful reward count. Repeated equipment variants within one family count once. Partial trials, canceled demands and unresolved reward claims do not count. Record family, service, country, continent, completion date and reward receipt per counted experiment.

Icon direction: a single readable military research emblem combining three service cues around a test instrument. Keep the silhouette simple at 64 × 64, without miniature written labels.

### `chaosx_076_prototype_development`

As human USA, complete a real restricted foreign nuclear prototype before mature nuclear weapons are available, receive its corresponding nuclear development benefit, and later finish the relevant mature capability through the actual research or project owner.

The prototype's pre-maturity status is frozen at commitment and checked again at impact. If mature weapons were already available before the trial, it does not satisfy the prototype achievement. The later completion must be a real technology or project milestone. An invented event-local counter or an automatically granted mature stockpile does not qualify.

Icon direction: one experimental instrument beside a restrained atomic-program symbol. Avoid a crowded explosion scene or a medal implying the civilian losses themselves are the achievement.

### `chaosx_076_repeated_victim_rebuild`

As one human-controlled minor identity, survive three completed tests across separate waves, complete the verified access and productive-district recovery objectives associated with those incidents, and remain an independent existing country for 365 days after the last required recovery completion.

Population is not restored by this objective. The conditions measure damaged infrastructure and productive capacity, alongside political survival. New tests during the final year do not reset the record of completed earlier work, but the country must still exist and remain independent when the check completes. A recovered district later destroyed again must meet its actual required objective at the award check.

Icon direction: rebuilt transport or a factory beside a damaged but standing national emblem. Use one clear central subject that remains readable at native size.

### `chaosx_076_refusal_survival`

As a human minor, refuse a valid ultimatum, receive the resulting USA-led declaration, remain independent through that conflict, and end the actual war while still controlling the demanded state. The war ending may follow a valid negotiated outcome or victory supported by ordinary game mechanics.

A proposal that was invalidated before refusal, a USA disappearance before any declaration, or an existing unrelated war does not qualify. Event 076 does not create a free scripted white peace to make this achievable. Record the refusal, actual attacker and target, war identity or equivalent native relationship, territorial demand and verified final outcome.

Icon direction: a sealed ultimatum blocked by a simple defensive emblem. No final written slogan is embedded in the icon.

### `chaosx_076_international_reconstruction`

As one human-controlled donor outside the target governments, make paid, useful contributions to completed Event 076 access-restoration objectives in three distinct victim countries across at least two continents. Each contribution must be acknowledged by the actual relief owner and materially support a completed damaged objective.

Repeatedly sending and returning the same stockpile, donating after a mission is already complete, or giving resources to an undamaged country does not qualify. The donor's own prior test damage does not count as a separate foreign recipient. The achievement can share proof with the proposed once-only international relief Chaos reduction without applying the reduction twice.

Icon direction: a clear rail-repair tool or bridge motif with a restrained international aid symbol. Avoid several tiny flags.

### `chaosx_076_containment_recovery`

As a human victim of a completed Event 076 biological or chemical test, satisfy the owning system's full containment and recovery objectives for the test-linked affected states within the country, then maintain 180 days without a new test-linked local spread event or unresolved contamination objective.

The disease or contamination owner defines actual recovery. A negative modifier expiring, a report being dismissed or an event-local timer alone does not qualify. Later deaths and spread must remain correctly recorded during the observation period. A new test or renewed linked outbreak pauses or restarts the applicable clean-period check according to the owner, without deleting previous losses.

Icon direction: a sealed affected district or protective medical emblem with a rebuilding cue, without biological diagrams or operational equipment detail.

## Persistence and fairness

Eligibility binds to the campaign and the qualifying country identity. Tag switches, releases, annexation and civil wars follow the existing achievement owner's identity rules. Do not pool several unrelated countries into one supposed survivor or donor.

Each achievement consumes authoritative test, reward, war, repair or owner-recovery receipts. UI counters can display progress, but the award check must not trust a mutable selected job, an unverified death estimate or a debug-only shortcut.

Save and reload preserve first-success dates, distinct sets and observation periods. A threshold crossing awards once. Repeated callbacks do not add new families, countries, repair completions or days. Achievements gated on an absent required owner remain unavailable with a correct reason until the dependency is implemented.

## Icon production

Each full achievement ID receives one original color master with genuine alpha. Produce the grey and not-eligible variants deterministically through the achievement pipeline. Do not independently generate three similar pictures, and do not use a generic DDS conversion command as a substitute for the locked template compositor.

The required locked inputs are `icons/achievements/template/achievement_template.png`, `achievement_template_grey.png` and `overlay.png`. Inspect the supplied skill and actual repository versions before use. The final template canvas is 64 × 64, and the exact red not-eligible overlay must remain intact.

Use `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py` with the current validated arguments. Inspect its output and use the required DDS conversion and round-trip checks. The final files sit directly under `gfx/achievements/` as `<full_id>.dds`, `<full_id>_grey.dds` and `<full_id>_not_eligible.dds`.

All six entries, their individual icon directions and proof contracts are planning proposals. No registry entry, icon triplet or achievement test has been produced or executed here.
