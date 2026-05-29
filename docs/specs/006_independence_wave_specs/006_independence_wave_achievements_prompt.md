# Achievement Prompt: Event 6 Independence Wave

Use the achievement implementation pattern already used by Chaos Redux. Implement achievements with strict conditions, disqualifiers, icon directions, and tracking flags. Do not create achievements that unlock simply because the event fired.

## Shared tracking notes

Track:

- release origin
- patron acceptance
- patron leverage threshold
- coalition foundation
- league formation
- peaceful border resolution
- hostile border war
- historical-return package created
- local-polity package created
- strange-state reveal
- Event 005 separation check for shared tags
- debug or bypass disqualifiers

## cr_independence_without_patron

- Title: Independence Without a Master
- Player-facing description direction: As any Independence Wave country, become fully recognized without accepting a patron cabinet, foreign puppet status, or emergency occupation.
- Difficulty: Hard
- Visibility: Visible
- Disqualifiers: puppet shortcuts, debug firing, event disabled bypasses, wrong release origin.
- Icon direction: small flag held between two large shadows.

## cr_five_small_flags

- Title: Five Small Flags
- Player-facing description direction: Have five Independence Wave countries alive, mutually guaranteeing each other, and not in a major-led faction.
- Difficulty: Hard
- Visibility: Visible
- Disqualifiers: debug firing, wrong release origin, major-led faction shortcut.
- Icon direction: five small flags around a shield.

## cr_charter_not_chains

- Title: A Charter, Not Chains
- Player-facing description direction: Form the League of New States while every founding member keeps autonomy above puppet level.
- Difficulty: Very hard
- Visibility: Visible
- Disqualifiers: patron puppet status, debug firing, wrong release origin.
- Icon direction: signed charter breaking a chain.

## cr_suppression_failed

- Title: The Cost of Silence
- Player-facing description direction: As a host country, suppress the first independence movement, then lose two later breakaways because stability and legitimacy collapsed.
- Difficulty: Medium
- Visibility: Visible
- Disqualifiers: debug firing or scripted test bypass.
- Icon direction: sealed petition under a cracked baton.

## cr_old_name_modern_state

- Title: Old Name, Modern State
- Player-facing description direction: As a historical-return country released by Independence Wave, complete the modern compromise route without becoming a puppet or starting a border war.
- Difficulty: Hard
- Visibility: Hidden until a historical-return package exists.
- Disqualifiers: wrong release origin, Event 005 release path, patron puppet status, offensive border war.
- Icon direction: old seal stamped onto a modern constitution.

## cr_volga_without_collapse

- Title: The River Remembers Differently
- Player-facing description direction: As Volga Bulgaria released by Independence Wave, complete the Volga historical-return overlay without using the Soviet Collapse route.
- Difficulty: Very hard
- Visibility: Hidden.
- Disqualifiers: released by Event 005, Event 005 focus tree active, debug spawn, puppet shortcut.
- Icon direction: river map with a restored seal and a broken dependency chain.

## cr_land_congress_recognized

- Title: The Land Congress Speaks
- Player-facing description direction: As a local-polity or indigenous authority released by Independence Wave, gain full recognition while keeping patron leverage low.
- Difficulty: Hard
- Visibility: Hidden until local-polity packages are implemented.
- Disqualifiers: puppet route, wrong release origin, debug spawn.
- Icon direction: council circle around a small flag.

## cr_partition_week_survived

- Title: Week of a Hundred Petitions
- Player-facing description direction: Survive a high-chaos Independence Wave that releases at least eight countries while keeping your original capital and avoiding puppet status.
- Difficulty: Very hard
- Visibility: Hidden until Evo IV or higher.
- Disqualifiers: debug firing, tag switched by console, world-end cleanup bypass.
- Icon direction: map room covered in small pins.

## cr_impossible_state_recognized

- Title: Recognition of the Impossible
- Player-facing description direction: As an impossible-state package from Independence Wave, force at least one ordinary major to recognize you or sign a containment treaty.
- Difficulty: Extreme
- Visibility: Hidden.
- Disqualifiers: wrong release origin, debug spawn, recognition granted by testing event.
- Icon direction: formal diplomatic seal over an inhuman shadow.

## Expanded achievement design

Achievements should test mastery of the event's systems, not the mere fact that countries were released. Every achievement should check the Event 006 release origin where the player is using a breakaway. Shared tags from Event 005 must not satisfy Event 006 achievements. Soviet republic style tags released by Event 006 can satisfy Event 006 achievements only through Event 006 routes, not through Soviet Collapse trees, missions, or formables.

### Shared disqualifiers

All achievements should fail or remain locked when:

- the event was debug-fired through a testing bypass
- the target country lacks the Independence Wave origin when the condition requires it
- the player uses a scripted shortcut that skips the dossier, crisis, or release process
- a cleanup event grants the result without the intended route
- an achievement path depends on a disabled evolution
- the country was created by Event 005 or another event and only later received an Event 006 idea by mistake

### Required tracking flags

| Flag or variable | Scope | Purpose |
| --- | --- | --- |
| `chaosx_iw_achievement_valid_origin` | country | confirms Event 006 origin |
| `chaosx_iw_no_patron_accepted` | country | tracks patron-free route |
| `chaosx_iw_patron_accepted` | country | disqualifies no-master achievements |
| `chaosx_iw_puppet_status_ever` | country | detects puppet shortcuts |
| `chaosx_iw_founded_league` | country or global | league founder |
| `chaosx_iw_league_member_count` | global or faction | count of qualifying members |
| `chaosx_iw_mutual_guarantee_network` | global or faction | Five Small Flags |
| `chaosx_iw_host_suppressed_first` | host | suppression failure setup |
| `chaosx_iw_later_breakaways_lost_by_host` | host | Cost of Silence progress |
| `chaosx_iw_peaceful_border_resolution` | country | peaceful border achievement |
| `chaosx_iw_host_kept_capital` | host | host survival achievement |
| `chaosx_iw_historical_return_package` | country | old-name achievement path |
| `chaosx_iw_local_polity_package` | country | local-polity achievement path |
| `chaosx_iw_strange_package` | country | impossible-state path |
| `chaosx_iw_event005_collision_checked` | country | shared-tag origin guard |

### Achievement catalog

| ID | Title | Player role | Difficulty | Core test |
| --- | --- | --- | --- | --- |
| `cr_independence_without_patron` | Independence Without a Master | breakaway | hard | recognition without patron control |
| `cr_five_small_flags` | Five Small Flags | any or breakaway | hard | five mutual guarantees outside major faction |
| `cr_charter_not_chains` | A Charter, Not Chains | breakaway or league founder | very hard | league formed without founding puppets |
| `cr_suppression_failed` | The Cost of Silence | host | medium | suppress first, lose later waves |
| `cr_old_name_modern_state` | Old Name, Modern State | historical-return | hard | modern compromise route without puppet or border war |
| `cr_capital_still_answers` | The Capital Still Answers | host | medium | survive a severe wave with capital retained |
| `cr_no_country_erased` | Every Seal Survives | host or observer | hard | resolve a high-chaos mass wave where every host survives |
| `cr_brokers_exposed` | The Broker Leaves by Night | breakaway | medium | escape patron leverage after nearly becoming a client |
| `cr_partition_without_war` | Lines Without Guns | host or breakaway | hard | settle three border disputes peacefully |
| `cr_first_old_name` | Wake the Archive | historical-return | medium | create first old-name state through Event 006 |
| `cr_local_land_congress` | Land Congress | local-polity | hard | win recognition through local-polity route without major patron |
| `cr_railway_country` | The Timetable Has a Flag | railway package | medium | survive as railway sovereignty and secure rail hubs |
| `cr_not_the_collapse` | Not That Collapse | shared tag | hard | as shared tag such as Volga Bulgaria, prove Event 006 origin and complete Independence Wave route |
| `cr_league_war_victory` | The Charter Held | league | very hard | league defeats a major or patron coalition |
| `cr_impossible_recognition` | Recognition of the Impossible | strange package | very hard | strange state gains recognition from another Event 006 country |
| `cr_human_renunciation` | No Appeal to Mankind | anti-mankind | extreme | complete anti-mankind route with enough power to matter |

### Detailed achievement specs

#### `cr_capital_still_answers`

**Description direction:** As a host, survive an Independence Wave that takes at least four states while retaining your capital.

**Conditions:**

- player is host
- Event 006 wave resolves against player or player-observed host
- host loses at least four states in the wave
- host remains alive
- host still owns original protected capital state
- no debug bypass

**Why it exists:**

This rewards the absolute host-survival rule as active gameplay. It tells the player that losing land is not the same as deletion.

**Icon direction:**

Capital building behind a torn map.

#### `cr_no_country_erased`

**Description direction:** During a high-chaos Independence Wave that releases at least eight countries, ensure that every affected host survives the wave.

**Conditions:**

- Evo IV or Evo V active
- actual release count at least eight
- at least two hosts affected
- every host that lost land keeps at least one state
- no candidate was allowed to bypass the survival floor
- player controls a host, a league leader, or an observer country with decisions that helped settlements

**Icon direction:**

Many small flags around several surviving capital stars.

#### `cr_brokers_exposed`

**Description direction:** As an Independence Wave country, reach high patron leverage, expose foreign brokers, and become fully recognized without becoming a puppet.

**Conditions:**

- Event 006 origin
- patron leverage crosses danger threshold
- player completes anti-patron route decision or focus
- country avoids puppet status
- recognition achieved
- no patron cabinet accepted as final route

**Icon direction:**

Torn contract under lamp.

#### `cr_partition_without_war`

**Description direction:** Resolve three Independence Wave border disputes through arbitration, protected transfers, or treaty settlement without starting a border war.

**Conditions:**

- three disputes tied to Event 006 candidates
- each resolved by peaceful decision, observer mission, league arbitration, or host treaty
- no war goal fired from those disputes
- no hidden event grants free territory without cost

**Icon direction:**

Survey chain over map with white flags.

#### `cr_first_old_name`

**Description direction:** Be the first campaign country created by Independence Wave as a historical-return package.

**Conditions:**

- country has historical-return package type
- origin is Event 006
- first global old-name flag not yet set before release
- player controls the package or its host at release
- no Event 005 origin

**Icon direction:**

Old seal stamped onto a modern passport.

#### `cr_local_land_congress`

**Description direction:** As a local-polity Independence Wave country, gain recognition through land congress decisions without accepting a major patron.

**Conditions:**

- local-polity package type
- completes land congress or equivalent route
- gains recognition
- no major patron puppet status
- at least one community defense or land testimony mission completed

**Icon direction:**

Council seat and field boundary marker.

#### `cr_railway_country`

**Description direction:** As a railway sovereignty created by Independence Wave, control your release-state rail hub and two connected supply nodes for a set period.

**Conditions:**

- railway package type
- origin is Event 006
- controls capital state rail hub
- controls or allies with two connected supply nodes
- survives timed mission
- no puppet shortcut

**Icon direction:**

Locomotive front with small flag.

#### `cr_not_the_collapse`

**Description direction:** As a shared tag that can also appear through another event, complete an Independence Wave route without using the other event's content.

**Conditions:**

- country tag is marked shared by package file
- origin is Event 006
- Event 005 origin flag is absent
- Event 005 tree or mission flag is absent
- complete Independence Wave first sovereignty congress or package overlay finisher
- Volga Bulgaria should be one valid example if implemented

**Icon direction:**

Two file folders, one stamped Event 006.

#### `cr_league_war_victory`

**Description direction:** As the League of New States, win a defensive or recognition war against a major power or patron coalition.

**Conditions:**

- league exists
- at least four Event 006 members
- enemy is major or patron coalition leader
- war goal tied to recognition, member defense, or anti-patron defense
- peace conference or scripted outcome confirms victory
- founding members do not become puppets during the war

**Icon direction:**

Small charter over crossed rifles.

#### `cr_impossible_recognition`

**Description direction:** As a strange Independence Wave state, gain formal recognition from another Independence Wave country.

**Conditions:**

- strange package type
- origin is Event 006
- another Event 006 country completes recognition decision or focus toward it
- not forced by debug
- no world-end shortcut

**Icon direction:**

A blank face on a passport stamp.

#### `cr_human_renunciation`

**Description direction:** As an anti-mankind Independence Wave country, complete the doctrine route and make another strange state cooperate with you.

**Conditions:**

- origin is Event 006
- anti-mankind route locked
- controls a minimum state or victory point threshold
- completes doctrine finisher
- at least one strange-state cooperation link
- no normal democratic restoration after lock

**Icon direction:**

State seal over an erased human outline.

### Hidden achievement reveal rules

- Historical-return achievements should reveal after the first historical-return package appears.
- Local-polity achievements should reveal after a local-polity package appears or when the player controls one.
- Strange achievements should reveal only after a strange package appears.
- Shared-tag achievement should reveal when a shared tag is released by Event 006.
- Host-survival achievements can be visible because they teach the rule.

### Achievement validation

Before implementation completion, verify:

1. every achievement checks origin where relevant
2. no achievement can be earned by Event 005 Volga Bulgaria through Event 006 achievement logic
3. no Soviet republic style tag can earn Event 006 achievements through Event 005 trees, missions, or formables
3. debug and bypass flags disqualify routes
4. hidden achievements reveal through sensible flags
5. icon names exist in the asset prompt
6. docs and catalog list the same IDs
7. route completion flags are persistent enough to survive tag switches, capitulation, and reload
8. achievements do not reward passive waiting without a decision, route, war, or survival challenge

## Added formable and GUI achievements

## cr_charter_becomes_state

- Title: The Charter Becomes a State
- Player-facing description direction: As an Independence Wave country, complete a major Event 006 formation route after founding or joining the League of New States, without becoming a puppet.
- Difficulty: Very hard
- Visibility: Hidden until a formation route is revealed.
- Disqualifiers: wrong release origin, wrong formation origin, puppet shortcut, debug firing, direct tag switch bypass.
- Tracking notes: require `chaosx_release_origin_independence_wave`, `chaosx_formation_origin_independence_wave`, League participation or congress support, and no puppet status at unlock.
- Icon direction: a small charter seal unfolding into a flag.

## cr_the_ledger_votes_back

- Title: The Ledger Votes Back
- Player-facing description direction: Use the New States Congress or Formation Ledger to complete a formation, block patron domination, or win a League vote while at least three Event 006 countries remain independent.
- Difficulty: Hard
- Visibility: Visible.
- Disqualifiers: wrong release origin, GUI bypass debug helper, major-led faction shortcut.
- Tracking notes: track GUI or decision-equivalent action path so AI-compatible decisions can also satisfy the achievement when played by a human tag.
- Icon direction: glowing ledger page with three stamps.

## cr_no_more_flags_needed

- Title: No More Flags Needed
- Player-facing description direction: Reach an improvement-loop closure state for Event 006 in a campaign path by resolving all active wave crises, keeping every host alive, and having no unresolved breakaway wars or patron puppet disputes.
- Difficulty: Very hard
- Visibility: Hidden.
- Disqualifiers: debug firing, world-end bypass, host deleted by non-Event 006 cleanup during an active wave.
- Tracking notes: this is a gameplay achievement, not a development achievement. It should represent a clean political settlement in-game, not an implementation report.
- Icon direction: folded flags in a calm map room.
