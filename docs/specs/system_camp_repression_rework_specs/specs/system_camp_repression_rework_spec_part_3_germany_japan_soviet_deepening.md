# System Camp Repression Rework Spec, Part 3: Germany, Japan, and Soviet Deepening

This part gives the detailed design for the three deepest packages.

## Germany deepening: Auschwitz, Mengele, and the Directorate

The existing Mengele chain already has `mengele_autonomy`, `mengele_permission_level`, Auschwitz state `88`, `germany_mengele.17`, `germany_mengele.20`, `germany_mengele.22`, `sp_mengele_cloning`, and the Directorate civil war path. The rework should connect camp expansion to that spine without duplicating it.

### Core design

Auschwitz should become a layered site:

1. concentration-camp or labor-administration site;
2. extermination or radicalized atrocity site if Germany escalates;
3. experiment-linked site if Auschwitz Experiments are authorized or restricted;
4. biowarfare facility site if `germany_mengele.17` or a related facility effect places a facility there;
5. cloning unlock source if Mengele reaches the required power package.

The player should feel that Auschwitz is a shared node for labor, atrocity, experimentation, evidence, and revolt risk.

### Permission and autonomy effects

`mengele_permission_level` should modify:

- experiment-site monthly deaths;
- biological research speed;
- special project availability;
- prisoner-transfer pressure from occupied pools;
- hidden atrocity score;
- future discovery condemnation;
- coup pressure;
- Directorate starting unit scale;
- laboratory-state ideas if the coup fires.

`mengele_autonomy` should rise from:

- full authorization;
- accepting facility demands;
- transferring prisoners to experiment-linked sites;
- radicalized atrocity sites under SS control;
- silencing military review;
- allowing bypass permission;
- completing abnormal reports;
- adding biowarfare facilities under SS control.

`mengele_autonomy` should fall from:

- military review;
- closing the Auschwitz program;
- purging SS medical offices;
- refusing facility demands;
- dismantling experiment-linked camps;
- losing access to occupied prisoner-transfer pools.

### Prisoner-transfer logic

Transfers should draw from occupied Poland and other occupied/non-core state pools first. If valid Polish occupied states exist, they must be used before German core states. If no valid occupied or non-core pool exists, core-state fallback is allowed only with lower research benefit, lower Mengele gain, high stability loss, high war-support loss, and severe internal backlash.

This preserves the user's request that Auschwitz-linked experimentation should not drain German cores while occupied Poland remains available, without creating a protected-class target selector.

### Germany decisions

Working labels:

- Expand Occupied Poland Camp Administration.
- Assign Rail Capacity to Deportation Logistics.
- Transfer Prisoners to Auschwitz Experiments.
- Build SS Laboratory Annex at Auschwitz.
- Classify Eastern Records.
- Military Review of Auschwitz.
- Purge SS Medical Offices.
- Close Auschwitz Program.
- Increase Guard Allocation to SS Sites.
- Destroy Evidence Before Retreat.
- Dismantle Auschwitz Complex after Regime Change.

### Cloning project unlock

The cloning special project should become researchable when Mengele has enough power, not too early from a single click.

Unlock package:

- `mengele_permission_level` at full or bypass level;
- `mengele_autonomy` at high or critical threshold;
- at least one biowarfare facility in Auschwitz or an experiment-linked site;
- at least one active experiment-linked camp state;
- high SS archive control or low military review;
- sufficient hidden project progress from reports.

The event that unlocks `sp_mengele_cloning` should feel like the laboratory network has become a state inside the state. It should not describe the technology as proven. It should show the regime giving resources to an unstable program.

### Directorate revolt rework

The Directorate revolt should become a deeper civil-war branch.

Pressure sources:

- critical Mengele autonomy;
- three or more biowarfare facilities;
- high permission level;
- active experiment-linked sites;
- war with the Soviet Union;
- high fascist support;
- desperate war state;
- high chaos tier;
- completed or near-complete cloning project.

Pre-revolt warning states:

- SS laboratories refuse inspection.
- Camp guards answer to laboratory officers.
- transport ledgers vanish from military offices.
- biowarfare facilities report through separate command channels.
- military review decisions become expensive and risky.

When revolt fires:

- breakaway receives Auschwitz, controlled biowarfare-facility states, and experiment-linked sites where valid;
- receives Josef Mengele as leader unless the later artificial formation overthrow path replaces him;
- receives laboratory state ideas;
- receives Experimental Twin Formation and clone formations scaled by autonomy, facilities, permission, and completed project status;
- Germany receives emergency decisions to isolate labs, reclaim results, or make a temporary truce in desperate Soviet war conditions.

### Directorate after victory

If the Directorate wins, it should inherit the camp and experiment network as a corrupted state economy. It should not become a normal Germany with passive bonuses.

Core values:

- `clone_manpower_output`
- `laboratory_state_reach`
- `numbered_army_growth`
- `foreign_clone_network_strength`
- `world_threat_source_mengele`
- `internal_overwrite_pressure`

The existing Angelic World Order branch can remain the world-end path. This rework should ensure camp expansion and experimentation are part of why the Directorate exists, not a disconnected precursor.

## Japan deepening: Shiro Ishii, occupied China, and biowarfare projects

Japan needs a system that makes Shiro Ishii and the Kwantung Army matter.

### Shiro Ishii role

Shiro Ishii should be represented as a scientist, advisor, hidden authority, or event character whose influence grows from:

- Pingfang or Harbin/Pingfang-equivalent facility setup;
- prisoner-experiment decisions;
- Kwantung Army autonomy;
- successful biowarfare special projects;
- silencing army medical review;
- covering up occupation evidence;
- high chaos tier or desperate war state.

`ishii_influence` should unlock:

- stronger biowarfare research modifiers;
- Japan-specific special-project gates;
- increased evidence severity;
- higher outbreak accident risk;
- higher chance of uncontrolled spread;
- stronger tribunal severity if discovered;
- a possible post-defeat or Soviet-capture exposure chain.

### Japan-specific values

- `ishii_influence`
- `kwantung_autonomy`
- `pingfang_facility_level`
- `occupation_test_records`
- `bio_project_pressure`
- `outbreak_accident_risk`
- `chinese_resistance_pressure`
- `evidence_depth_china`
- `imperial_army_review_pressure`

### Decision families

- Establish Pingfang Research Bureau.
- Transfer Prisoners to Army Medical Research.
- Expand Occupation Test Records.
- Shield Ishii from Army Review.
- Invite Kwantung Army Medical Officers.
- Route Supplies to Epidemic Prevention.
- Destroy Pingfang Records.
- Evacuate Research Staff Before Soviet Advance.
- Submit to Army Review.
- Shut Down Prisoner Experiments.

### State pools

Use controlled Chinese and Manchurian states. Avoid Japan core states unless no occupied pool exists and Japan is desperate. The occupied pool should determine the Deaths-tab owner attribution: state owner receives population loss while Japan remains responsible for evidence and condemnation.

### Special project branch

Projects are research and risk gates.

Project working labels:

- Pingfang Records Office: unlocks first Japan-specific biowarfare research bonus and Ishii influence.
- Kwantung Medical Intelligence: allows faster special-project progress but adds high evidence and accident risk.
- Occupation Test Ledger: registers biowarfare experiment-linked sites into monthly processing.
- Epidemic Mapping Bureau: unlocks containment and defensive medicine while preserving evidence and reducing accident risk if used ethically.
- Cherry Blossom Dossier: high-chaos desperation branch using existing doomsday biowarfare framework, not a new operational recipe.

### Events

Japan should have few ordinary flavor events. Use threshold events:

- Ishii gains independent authority.
- Kwantung medical officers bypass Tokyo.
- uncontrolled outbreak in occupied territory.
- Soviet or Allied forces discover Pingfang evidence.
- Japan chooses to evacuate, destroy, or surrender records.
- postwar tribunal exposure.

## Soviet deepening: paranoia, gulags, famine, and collapse

The Soviet Union should become the most mechanically distinct package.

### Values and relationships

`paranoia_pressure` should open harsher decisions and increase AI willingness.

`nkvd_authority` should improve repression efficiency and reduce short-term opposition but raise long-term grievance.

`gulag_network_reach` should create forced-labor output and Deaths-tab movement.

`grain_extraction_burden` should feed `famine_pressure`.

`famine_pressure` should cause state damage, population loss, stability loss, recruitable population loss, and republic grievance.

`old_movement_grievance` should feed the Soviet Collapse event and republic resistance.

`union_crisis_suppression_relief` should reduce early collapse pressure but be capped at high crisis levels.

### Paranoia thresholds

Low paranoia:

- gulag background remains mostly dormant;
- no famine crisis;
- only mild forced-labor and political-prisoner decisions.

Medium paranoia:

- deportation and forced-labor quota decisions become visible;
- purge administrator decisions can reduce corruption but raise fear;
- famine pressure can begin if grain extraction is used.

High paranoia:

- harsh quota and confiscation decisions become available;
- NKVD authority rises;
- military obedience may improve briefly;
- old movement grievance and republic fear rise faster;
- famine events become possible.

Critical paranoia:

- mass deportation, famine, and administrative breakdown chains become likely;
- suppression can no longer prevent Union Unmade on its own;
- republic grievances harden;
- high risk of collapse backlash or internal reckoning.

### Famine pressure

Famine should be a failed-management chain, not a random flavor event.

Famine pressure rises from:

- grain confiscation;
- excessive gulag quotas;
- low stability;
- war devastation;
- supply disruption;
- high paranoia;
- state devastation or infrastructure damage;
- repeated administrator purges.

Famine pressure falls from:

- emergency grain relief;
- reducing forced-labor quotas;
- improving supply;
- lowering paranoia;
- accepting foreign or republican aid;
- pausing deportation actions;
- dismantling overextended camps.

Famine effects:

- visible state-population loss through Deaths;
- stability loss;
- recruitable population damage;
- infrastructure and local output damage;
- rising old movement grievance;
- stronger foreign condemnation if discovered through invasion or post-collapse records.

### Gulag labor output

Gulag output should provide:

- resource extraction;
- construction speed in remote or industrial states;
- rail/infrastructure projects;
- military construction in emergency war;
- industrial relocation support.

It should cost:

- population loss;
- low productivity after overreach;
- stability damage;
- corruption;
- guard manpower burden;
- administrator purge risk;
- famine pressure.

### Soviet Collapse bridge

During Union Crisis:

- early repression can reduce organized opposition or increase Moscow Authority;
- it can raise Military Obedience if NKVD authority is high;
- it increases Old Movement grievance and foreign grievance;
- at high crisis threat, suppression relief stops scaling;
- overuse makes post-collapse successor states more hostile;
- famine or mass deportation states should become more likely to defect or radicalize.

### Extreme escalation

Extreme escalation should be locked behind critical paranoia, extreme communist path, high chaos, or collapse desperation. It uses borderland/periphery/political-opposition state pools, not protected-class target menus. Effects are mostly negative and should push collapse, discovery, and tribunal severity.
