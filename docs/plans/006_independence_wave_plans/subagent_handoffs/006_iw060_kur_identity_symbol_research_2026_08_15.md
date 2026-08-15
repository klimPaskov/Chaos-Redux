# IW-060 KUR identity, symbol, and vanilla-carrier provenance

Date: 2026-08-15

Status: research complete with explicit runtime blockers; no runtime asset was selected or created.

Scope: IW-060 Kurdistan (`KUR`), the 1936 anchor advertised as state 421, the current installed map split, the exact vanilla carrier, existing vanilla KUR country leaders, historical institution/symbol candidates, and Event005/Form-18 collision review.

Ownership boundary: this is a source-research handoff only. No flag, portrait, PNG, DDS, GFX, gameplay, central-admission, Join, country-history, or character file was created or edited. Portrait work remains owned by `chaosx_portrait_creator`; a final flag reconstruction would require parent approval and the normal event-assets/ImageGen route.

## Executive disposition

1. The exact vanilla 1936 owner of public anchor state 421 is `PER` (Persia), not `KUR`. Vanilla state 421 adds cores for both `PER` and `KUR`.
2. The current Chaos Redux installed map split uses state 1001 as the IW-060 dedicated Kurdistan anchor. Vanilla state 1001 is likewise owned by `PER` in 1936 and has cores for both `PER` and `KUR`.
3. The current package scripts therefore bind IW-060 to `KUR` plus state 1001, while the public research anchor and the Form-18 state-piece surface still name state 421. This is an unresolved identity/anchor-coherence collision, not a reason to rewrite the map from this research task.
4. The safest opening identity is reuse of the registered vanilla `KUR` tag, its existing leader roster, and its existing proprietary flag ladder. No new neutral pan-Kurdish flag is defensible from the sources reviewed for a 1936 opening.
5. The strongest named institution-specific symbol candidate is the flag associated with the Kingdom of Southern Kurdistan under Sheikh Mahmud Barzanji, attested for 1922–1924. It is a `needs_user_review` candidate for a route that explicitly claims Barzanji/Kingdom continuity, not a default pan-Kurdish flag.
6. Xoybûn, Ararat, and Mahabad flag reconstructions are not safe 1936 opening symbols under the project’s evidence standard. Xoybûn and Ararat lack a sufficiently defensible primary flag attestation in the reviewed sources, and Mahabad is a 1946–1947 polity.
7. Among existing vanilla KUR country leaders, Sheikh Mahmud Barzanji is the best opening-era named identity if the route is framed as a Southern Kurdistan/Barzanji continuity claim. Ihsan Nuri is a period-relevant living insurgent figure but requires source clearance and a cross-border Xoybûn/Ararat framing. Seyid Riza is better date-gated to the 1937 Dersim continuation. Qazi Muhammad is a 1946–1947 Mahabad figure and is blocked for the 1936 opening.
8. No direct Event005 Soviet Collapse reference to the `KUR` tag, KUR flag, or KUR leaders was found. The Form-18 member trigger excludes Soviet Collapse-origin countries, so Event005 origin separation is preserved.

## Required carrier and anchor evidence

### Vanilla state ownership

The installed vanilla state files contain the following 1936 history:

```text
C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/421-Kurdistan.txt
state={
 id=421
 name="STATE_421"
 history={
   owner=PER
   add_core_of=PER
   add_core_of=KUR
 }
}
```

```text
C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/1001-Kurdistan.txt
state={
 id=1001
 name="STATE_1001"
 history={
   owner=PER
   add_core_of=PER
   add_core_of=KUR
 }
}
```

State 421 has provinces `829`, `5050`, and `10774`. State 1001 has provinces `4943`, `9816`, `5098`, and `12773`, with vanilla victory points at 4943 and 5098. These are different vanilla map slices despite the shared `Kurdistan` name.

The vanilla country history at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/KUR - Kurdistan.txt` sets `capital = 800`; that capital is a separate vanilla KUR-country fact and must not be conflated with either the public 421 anchor or the current installed 1001 anchor.

### Current Chaos Redux binding

The current installed package binding at `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` records IW-060 as:

```text
IW-060,Kurdistan,KUR,automatic_pool_ready_if_not_living,ready_if_tag_not_living,fixed_anchor_compact,1001,Kurdistan,1001,Kurdistan,...,RG-NORTHERN-MESOPOTAMIA,421,Kurdistan,rebound_to_current_split,1001=PER,PER=266
```

The package implementation agrees with the current binding:

- `common/scripted_effects/006_independence_wave_packages_region_06_effects.txt:42` saves state `1001` as `liberation_candidate_anchor` for IW-060.
- `common/scripted_triggers/006_independence_wave_packages_region_06_triggers.txt:32` begins `can_plan_independence_wave_package_iw_060`; its anchor availability path resolves to state 1001.
- `common/script_constants/006_independence_wave_kurdistan_constants.txt` still describes state 421 as the accepted research anchor and separately warns that vanilla KUR’s state-800 capital is unresolved. This comment is stale relative to the current installed binding and was not edited here.

Disposition: treat state 1001 as the current runtime binding and state 421 as the public/spec research anchor until the parent makes an explicit map/formable decision. Do not silently substitute 421 for 1001 in runtime work.

## Vanilla KUR identity and flag ladder

Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/KUR - Kurdistan.txt` recruits the following country leaders:

| Vanilla token | Vanilla role/ideology surface | Research disposition |
| --- | --- | --- |
| `KUR_qazi_muhamad` | Country leader, Marxism | Real person, but Mahabad is 1946–1947; block for 1936 opening and date-gate to a later route. |
| `KUR_mahmud_barzanji` | Country leader, despotism | Best named opening-era candidate for an explicit Barzanji/Southern Kurdistan continuity route; source clearance still required. |
| `KUR_ishan_nuri` | Country leader, fascism ideology; field marshal | Period-relevant to Xoybûn/Ararat, but cross-border and source clearance required. |
| `KUR_seyid_riza` | Country leader, conservatism | Historical Dersim leadership belongs principally to 1937; block as the default 1936 opening authority and date-gate if used. |

The same history recruits `KUR_ferzende_bege_haseni` as a corps commander, not a country-leader identity. The remaining KUR named entries are advisors or high command and are outside this country-leader portrait request. Generic advisor textures and TODO large-portrait comments are not evidence for a grounded national leader.

Vanilla `common/characters/KUR.txt` uses the country-leader portrait tokens `GFX_portrait_PER_qazi_muhammad`, `GFX_portrait_Sheikh_Mahmud_Barzanji`, `GFX_portrait_kur_ihsan_nuri`, and `GFX_portrait_kur_seyid_riza`. The installed vanilla portrait definitions include generic Syrian/Arabian textures for Qazi and Sheikh Mahmud and a KUR texture for Ihsan Nuri; the Seyid Riza texture is also KUR-specific. These are proprietary Paradox assets and are not source-license evidence. Reusing the vanilla roster does not authorize copying or repackaging those textures as sourced portraits.

The installed vanilla flag ladder contains `gfx/flags/KUR.tga`, `KUR_communism.tga`, `KUR_fascism.tga`, `KUR_neutrality.tga`, `KUR_FRA.tga`, and `KUR_france_democratic.tga`, with corresponding medium and small variants, plus separate `greater_kurdistan_*` and `IRQ_kurdistan_tag_*` families. These are proprietary vanilla runtime assets and should remain authoritative unless the parent explicitly approves a new, sourced and reconstructed flag package.

The canonical review-only reference root at `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference` was inspected. Its flags contact sheet contains vanilla ladder examples but no KUR-specific reference. No canonical reference was copied into the repository.

## Historical symbol and flag candidates

| Candidate | Named institution/community | Date and role fit | Source and rights facts | Disposition |
| --- | --- | --- | --- | --- |
| Kingdom of Southern Kurdistan / Sheikh Mahmud Barzanji flag | The Kingdom of Southern Kurdistan and the Barzanji monarchy, rather than an undifferentiated pan-Kurdish identity | Attested for the 1922–1924 Barzanji kingdom; historically before the 1936 start and plausible only as continuity/revival or explicit constitutional claim | FOTW, `https://www.fotw.info/flags/krd_slvd.html`, identifies a green field with a centered red disc containing a white fly-pointing crescent and cites a 1922 oath photograph plus Ahmed Khwaja’s 1970 autobiography sketch. The FOTW page is a copyrighted design reference, not a project asset license. The related Commons historical-flag image is marked CC BY-SA 4.0, but is a modern Zheen Archive/Kurdish Wikimedians image package and should not be mistaken for the original 1922 artifact. | **Best candidate; `needs_user_review`.** Use only if the route names the Barzanji institution or an explicit Southern Kurdistan restoration claim. Do not use as an unqualified pan-Kurdish default. |
| Xoybûn reconstruction | Xoybûn, the Kurdish organization associated with the Ararat revolt | Organization active in the late 1920s and early 1930s; cross-border, not a compact 1936 state authority | `https://commons.wikimedia.org/wiki/File:Flag_of_Xoybûn_1927.jpg` is a modern 2015 reconstruction by Kurdishhistoryy, marked CC BY-SA 3.0/GFDL, with no period artifact or archive citation on the file page. `https://commons.wikimedia.org/wiki/File:Kurdish_flag_(Khoiboun).svg` is another modern reconstruction, marked CC BY-SA 4.0, also without a primary attestation. | **Blocked** as a grounded 1936 historical flag. It can be considered only as clearly labeled secondary/reconstructed route art after parent review. |
| Ararat Republic reconstruction | Claimed Republic of Ararat, 1927–1931 | Wrong as a generic 1936 state authority and historically uncertain as a flag | `https://commons.wikimedia.org/wiki/File:Flag_of_Republic_of_Ararat.svg` expressly says that no sources substantiating the alleged flag have been found. The drawing’s public-domain status applies to the modern drawing, not to historical attestation. `https://commons.wikimedia.org/wiki/File:Republic_ararat.gif` is sourced to FOTW and categorized as special or fictional, not stronger period evidence. | **Blocked** for historical use. Do not present the modern reconstruction as an attested Ararat flag. |
| Republic of Mahabad reconstruction | Republic of Mahabad | 1946–1947, ten years after the 1936 opening | `https://commons.wikimedia.org/wiki/File:Flag_of_the_Republic_of_Mahabad.svg` is a modern reconstruction marked CC0 with sources listed as RBvex/FOTW/Rûdaw. The sunburst and coat-of-arms reconstructions are later CC BY-SA/CC0 drawings, not 1936 evidence. | **Blocked for IW-060 opening.** Reserve for a date-gated 1946–1947 evolution or alternate-history route only. |
| Vanilla KUR flag ladder | Registered vanilla `KUR` country identity | Exact runtime identity, but not a freely sourced historical asset | Installed vanilla `gfx/flags/KUR*` files are Paradox-owned runtime files. | **Reuse authoritative vanilla ladder.** No replacement asset was created in this handoff. |

### Barzanji evidence details

The FOTW page attributes the green/red/white-crescent design to a 1922 photograph of the Kurdish Army oath of allegiance and to a sketch with color notes in Ahmed Khwaja’s autobiography `Cim Di` (1970). Its page caption identifies the photograph as an unknown photographer image courtesy of Rafiq Studio, reproduced through Susan Meiselas, *Kurdistan in the Shadow of History* (Random House, 1997), p. 83. This is enough to identify a named institution-specific candidate, but not enough to grant a blanket asset license or to claim the reconstruction is the uncontested flag of all Kurds.

The Commons page `https://commons.wikimedia.org/wiki/File:ئاڵای_حوکمداریی_شێخ_مەحموودی_حەفید_1.jpg` presents a 1922–1924 Barzanji flag image through the Zheen Archive Center/Kurdish Wikimedians project and marks the uploaded image CC BY-SA 4.0. It is useful as a secondary cross-check of the period design, but its modern upload and archive-package provenance must be preserved if the parent ever uses it. No file was downloaded.

## Period male-leader candidates and portrait routing

The table below separates historical role/date fit from the availability of a source image. A Commons license label applies to the particular uploaded scan or reconstruction, not automatically to the underlying photograph, photographer, archive, or a derivative HOI4 portrait.

| Vanilla token | Historical role and organization | 1936 fit | Candidate source and rights/date state | Disposition |
| --- | --- | --- | --- | --- |
| `KUR_mahmud_barzanji` | Sheikh Mahmud Barzanji, leader of the Barzanji movement and King of Southern Kurdistan in 1922–1924 | Alive in the period and the strongest named identity for an explicit Southern Kurdistan/Barzanji continuity route; not an unqualified 1936 sitting authority after the kingdom’s collapse | Commons category `https://commons.wikimedia.org/wiki/Category:Mahmud_Barzanji` includes public-domain-labelled period candidates such as `Sheikh Mahmoud as sent to exile by Englishmen to India.jpg` (1921) and `Mahmud Barzanji.jpg` (1919), with source-chain details varying by file. The Commons PD label and period date are promising, but archive/photographer provenance must be independently checked before portrait work. | **`needs_user_review`; route to `chaosx_portrait_creator` only after source-chain clearance.** Do not substitute the vanilla generic Syrian texture as a sourced portrait. |
| `KUR_ishan_nuri` | Ihsan Nuri Pasha, generalissimo associated with the Ararat revolt and Xoybûn, 1927–1930 | Alive and period-relevant, but represents a specific cross-border insurgent tradition rather than an automatic compact KUR institution | Commons `https://commons.wikimedia.org/wiki/File:Ihsan_Nuri.jpg` is marked public domain and estimated 1927–1930, but the artist/source is listed as unknown or NA. That uncertainty is material. Later group and user-made files are not substitutes for an attributed period source. | **`needs_user_review`; source clearance required before portrait routing.** Suitable only for a route that names the Xoybûn/Ararat connection. |
| `KUR_seyid_riza` | Seyid Riza, religious and political leader of the Dersim rebellion | Alive at the 1936 start, but his principal armed leadership belongs to the 1937 Dersim rebellion; this is a late-period continuation identity rather than a safe opening default | Commons category `https://commons.wikimedia.org/wiki/Category:Seyid_Riza` includes public-domain-labelled files dated before 1937 or 1937, but source chains vary and several uploads are modern derivatives. | **Blocked as default 1936 opening leader.** Consider only as a date-gated 1937 continuation after portrait-worker source verification. |
| `KUR_qazi_muhamad` | Qazi Muhammad, president of the Republic of Mahabad, 1946–1947 | Wrong era for the 1936 opening | Commons category `https://commons.wikimedia.org/wiki/Category:Qazi_Muhammad` contains public-domain-labelled 1946–1947 period images and later derivatives, but all useful identity evidence is post-1936. | **Blocked for IW-060 opening.** Reserve for a date-gated Mahabad/late-evolution branch. |

Portrait disposition is deliberately not a runtime asset handoff. No portrait source file, placeholder, PNG, DDS, contact sheet, manifest entry, or GFX entry was produced. If the parent approves a grounded identity, pass the candidate URLs and the uncertainty notes to `chaosx_portrait_creator`; do not generate or edit a real-person portrait in this worker.

## Event005 and Form-18 collision review

### Event005 Soviet Collapse

The inspected Event005 surfaces (`events/005_soviet_collapse.txt`, `common/on_actions/005_soviet_collapse_on_actions.txt`, and `common/ai_strategy/005_soviet_collapse.txt`) contain no direct `KUR` tag, KUR leader, KUR flag, or KUR portrait reference.

The Form-18 member-candidate guard in `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:512` excludes `soviet_collapse_active_origin`, `soviet_collapse_event_created_republic`, `soviet_collapse_breakaway_setup_complete`, and `liberation_origin = soviet_collapse` before accepting a member. This preserves the Event005 origin boundary. The vanilla formable compatibility adapter only suppresses shortcuts for active IW-043 CHU and IW-058 ASY countries, so it does not rewrite ordinary KUR or Event005 behavior.

Disposition: **no direct Event005/KUR collision found**. Keep the existing origin guard; no Event005 or central-admission edit is authorized by this handoff.

### Form-18 state and identity surface

The Form-18 trigger surface at `common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt:333-335` defines state 421 as the KUR member piece:

```text
independence_wave_formable_state_puzzle_form18_state_421_qualifies = {
    KUR = {
        is_independence_wave_iw058_formable_member_candidate = yes
        has_frozen_accepted_independence_wave_formable_invitation_from_root = yes
    }
}
```

The corresponding unresolved/qualifying art paths are `gfx/interface/formables/state_puzzles/006_form18_state_puzzle/states/independence_wave_form18_state_421_unresolved.dds` and `independence_wave_form18_state_421_qualifying.dds`, wired by `interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui` and `interface/chaosx_formable_state_puzzles.gfx`.

The KUR member trigger does not directly require the map state 421. It checks the candidate’s saved anchor ownership/control and the package identity, including `original_tag = KUR` plus package id `iw_060`. Therefore KUR can qualify as the Form-18 external member through the current state-1001 anchor while the visual/state piece is still named 421. State 421 itself remains vanilla `PER`-owned.

This creates a real but bounded collision:

- FORM-18 territory is the ASY root at 676 plus KUR at 421 plus CJX at 413.
- IW-060’s current installed candidate anchor is KUR at 1001.
- The Form-18 KUR piece is still labelled by state 421.
- The trigger can pass through KUR’s 1001 anchor while the UI presents 421.

Disposition: **`needs_user_review` and parent-owned blocker.** The parent must choose one explicit authority before changing runtime surfaces: retain current binding at 1001 and reconcile/relabel the Form-18 state-piece representation, or deliberately restore 421 as the IW-060 anchor after a full current-map and package audit. This research task does not choose between those options and does not patch the GUI, GFX, triggers, or map.

## Source register and evidence links

Repository sources:

- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, IW-060 row: KUR, automatic pool readiness, state-421 research anchor, compact Kurdish anchor, sourced real male period leader requirement, named-institution symbol requirement, and source IDs.
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, IW-060 row: KUR/reuse-registered-tag candidate registry.
- `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`, `RG-NORTHERN-MESOPOTAMIA`: public IDs 676 and 421, packages IW-058 and IW-060, one automatic package limit.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`, IW-060 row: current 1001 binding, `1001=PER`, `PER=266`, and 421 research-anchor trace.
- `common/ideas/006_independence_wave_kurdistan_ideas.txt:5`: vanilla KUR leaders, portraits, flag, and history remain authoritative; no new character or visual asset is created.
- `docs/specs/006_independence_wave_specs/research/006_source_register.csv`: `SRC-EVENT5-ORIGIN` repository baseline and `ETH-KURD` David McDowall, *A Modern History of the Kurds*.

External historical and asset-provenance sources:

- FOTW, `https://www.fotw.info/flags/krd_slvd.html`, “Kurdistan: Short-lived independent states,” last modified 2020-08-07 by Ian Macdonald, including the Barzanji 1922–1924 flag description and period-source citations.
- Wikimedia Commons, `https://commons.wikimedia.org/wiki/File:ئاڵای_حوکمداریی_شێخ_مەحموودی_حەفید_1.jpg`, CC BY-SA 4.0 archive-package image labelled 1922–1924; secondary cross-check only.
- Wikimedia Commons, `https://commons.wikimedia.org/wiki/File:Flag_of_Kingdom_of_Kurdistan_(1922-1924).svg`, public-domain/PD-Iraq/PD-ineligible categories for a modern reconstruction, with accuracy-dispute caveat; geometry reference only.
- Wikimedia Commons, `https://commons.wikimedia.org/wiki/File:Flag_of_Xoybûn_1927.jpg`, CC BY-SA 3.0/GFDL modern reconstruction with no primary artifact cited.
- Wikimedia Commons, `https://commons.wikimedia.org/wiki/File:Flag_of_Republic_of_Ararat.svg`, explicit no-substantiation warning for the alleged historical flag.
- Wikimedia Commons, `https://commons.wikimedia.org/wiki/File:Flag_of_the_Republic_of_Mahabad.svg`, CC0 modern reconstruction of a 1946–1947 flag, wrong era for the 1936 opening.
- Wikimedia Commons leader categories and candidate files: `https://commons.wikimedia.org/wiki/Category:Mahmud_Barzanji`, `https://commons.wikimedia.org/wiki/File:Ihsan_Nuri.jpg`, `https://commons.wikimedia.org/wiki/Category:Seyid_Riza`, and `https://commons.wikimedia.org/wiki/Category:Qazi_Muhammad`.

Required references consulted before this handoff:

- Offline Paradox wiki snapshot: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Installed vanilla documentation: `documentation/script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `loc_objects_documentation.md`, and `loc_formatter_documentation.md`.
- Relevant installed vanilla files: KUR country history, KUR characters, KUR state histories, KUR flag ladder, and leader portrait definitions.

## Asset and rights accounting

- Source files selected/downloaded: none (`N/A` by design).
- Processed PNG previews: none (`N/A` by design).
- DDS outputs: none (`N/A` by design).
- GFX edits or runtime basenames proposed: none (`N/A` by design).
- Contact sheet: not applicable because no candidate was downloaded or processed.
- Manifest entry: not created because no runtime asset reached `complete` status.
- Source hashes: not applicable because no source file was copied into the repository.
- Runtime flag/portrait status: intentionally unresolved; do not treat the absence of files as an incomplete forgotten asset.

## Exact blockers for the parent

1. A defensible, rights-clear, institution-specific Barzanji flag reference exists only as a `needs_user_review` design candidate. It cannot be promoted to a runtime flag without confirming the intended route, preserving FOTW/archive attribution, and running the normal reconstruction/asset pipeline.
2. No reviewed source establishes a neutral, pan-Kurdish 1936 flag suitable for the default IW-060 opening. Do not use modern generic tricolors, Xoybûn reconstructions, the unsubstantiated Ararat reconstruction, or the post-1936 Mahabad flag as an unqualified substitute.
3. Barzanji and Ihsan Nuri portrait candidates require independent archive/source-chain review by `chaosx_portrait_creator`. Qazi Muhammad is wrong-era for the opening, and Seyid Riza should be date-gated.
4. The current runtime anchor 1001 and Form-18 state-piece 421 disagree. Parent-owned implementation must establish one explicit authority before changing visual or trigger surfaces.
5. Vanilla Paradox flag and portrait textures are proprietary runtime references. They may establish existing carrier identity but do not clear redistribution or extraction rights for new assets.

No simplification was hidden: every missing runtime asset is intentionally omitted under the research-only scope, and every unresolved candidate is marked `needs_user_review` or blocked above.
