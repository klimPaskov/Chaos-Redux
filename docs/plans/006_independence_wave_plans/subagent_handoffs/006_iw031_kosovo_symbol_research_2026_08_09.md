# IW-031 Kosovo historical symbol and flag research handoff

**Date:** 2026-08-09  
**Scope:** source-only historical flag/symbol research for Event 006 IW-031 (Kosovo), registered tag `KOS`, installed anchor state `802`.  
**Mode:** no ImageGen, source download, image processing, DDS/TGA export, `.gfx` edit, localisation edit, or gameplay edit.

## Decision

The vanilla `KOS` flag family is **not historically defensible for a 1936 opening**.  The installed files are the post-2008 Kosovo state design: blue field, gold Kosovo map, and six white stars (`KOS.tga`, `KOS_communism.tga`, `KOS_democratic.tga`, `KOS_fascism.tga`, `KOS_neutrality.tga`, with normal/medium/small ladders).  The six-star map flag was adopted by the Assembly of the Republic of Kosovo immediately after the 17 February 2008 declaration of independence, following a 2007 international design competition.  It must not be presented as an interwar Kosovo or Kingdom-of-Yugoslavia regional flag.

There is no defensible, directly attested **universal Kosovo flag for 1936** in the sources reviewed.  Kosovo was part of the Kingdom of Serbs, Croats and Slovenes (renamed Kingdom of Yugoslavia in 1929) and its constitutional status inside Yugoslavia remained unresolved throughout 1918–1941.  An Event 006 package therefore must not silently turn a later ethnic or modern state symbol into a 1936 regional state symbol.

**Recommended acceptance contract:** mark a universal IW-031 historical flag `blocked/needs_user_review` until the route identity is explicit.  If the parent accepts an explicitly Albanian-led provisional route, use a separate route/cosmetic flag, proposed runtime family `KOS_albanian_civic_1936` (normal/medium/small), reconstructed by ImageGen from the 1928 Albanian Kingdom statute:

- rectangular red field, period plain red rather than the modern Kosovo blue;
- one centered black double-headed eagle;
- no Kosovo map, six stars, red star, fasces, crown, lettering, or invented seal;
- treat the eagle as an **Albanian national/community symbol**, not a neutral or universal Kosovo emblem;
- keep minority guarantees and mixed-community governance in the route text; do not label this flag “the historical flag of all Kosovo.”

This is a historically grounded Albanian-community route, not proof of a distinct interwar Kosovo flag.  It must use a route-specific cosmetic tag and must not overwrite the existing no-suffix `KOS` base files.  If the intended opening is a neutral mixed-community administration under Yugoslavia instead, the exact attested design is the Kingdom of Yugoslavia blue–white–red horizontal tricolour (2:3); that should be labelled a Yugoslav provisional/administrative standard, not a Kosovo national flag.  Choosing between these two meanings is a parent design decision; do not generate either until it is recorded.

## Historical evidence

### Kingdom of Yugoslavia (the governing state in 1936)

- The 3 September 1931 **Constitution of the Kingdom of Yugoslavia**, Chapter I, Article 2, states: “The national standard is blue-white-red in the horizontal sense against a vertical staff.”  The text also describes the royal arms (white double-headed eagle on red shield with the Kingdom crown), but those arms are state heraldry and are not a Kosovo regional emblem.
- The constitutional text is retained in the Internet Archive capture of the contemporary translation: [Constitution of the Kingdom of Yugoslavia, Belgrade, 3 September 1931](https://web.archive.org/web/20091021145008/http://geocities.com/dagtho/yugconst19310903.html).
- The `Flag of Yugoslavia` historical summary records the plain blue/white/red tricolour as the Kingdom’s flag from 1918–1941, with official adoption of the first state flag in 1922 and the 1929 state-name change: [Flag of Yugoslavia](https://en.wikipedia.org/wiki/Flag_of_Yugoslavia).  This is secondary corroboration; the 1931 constitutional wording is the controlling design reference.

### Albanian Kingdom (the defensible Albanian-community motif)

- The **Fundamental Statute of the Kingdom of Albania**, dated 1 December 1928 and published in the *Official Gazette* on 13 December 1928, states in Article 3: “The Albanian flag is red, with a double-headed black eagle in the centre.”  This establishes the period field and principal emblem used by the Kingdom of Albania during the 1936 start date.
- Source text: [Fundamental Statute of the Kingdom of Albania, 1 December 1928](http://www.hoelseth.com/royalty/albania/albconst19281201.html) (a translated reproduction of the *Gazeta Zyrtare* text; use as design evidence, not as an image licence).
- A Commons vector reconstruction is useful for geometry comparison only: [Flag of Albania (1934–1939).svg](https://commons.wikimedia.org/wiki/File:Flag_of_Albania_(1934%E2%80%931939).svg).  Its metadata lists a 750×500, 3:2 reconstruction, public-domain/ineligible claim, and credits vectorisation from historical flag/arms references.  It is **not** an original 1934–1939 textile or archive photograph; do not treat its exact eagle drawing or palette as independently attested.  The statute’s red field and black double-headed eagle are the reliable constraints.  The reconstructed SVG uses a dark red around `#cc1100`, but the statute gives no colour standard, so ImageGen should preserve the documented red/black relationship rather than claim a legally exact hex value.
- The broader history of the Albanian flag documents the black double-headed eagle on red as an Albanian national symbol and records that Albanian flags were used by Kosovo Albanians in later periods; this supports the community-route boundary but does **not** backdate a Kosovo state flag to 1936: [Flag of Albania](https://en.wikipedia.org/wiki/Flag_of_Albania), [Flag of Kosovo — Historical flags](https://en.wikipedia.org/wiki/Flag_of_Kosovo#Historical_flags).

### Kosovo status and absence of a 1936 regional flag

- The historical background records that Kosovo entered the new Yugoslav state with Serbia in 1918, was under the Kingdom of Yugoslavia after 1929, and had unresolved constitutional status during 1918–1941: [Socialist Autonomous Province of Kosovo — Background](https://en.wikipedia.org/wiki/Socialist_Autonomous_Province_of_Kosovo#Background).
- The later provincial history explicitly notes that Kosovo did not have an official flag of its own even after post-1945 autonomy; official use followed the Serbian/Yugoslav state flags while Albanian, Serbian, and Turkish community flags represented their own constituencies: [Socialist Autonomous Province of Kosovo — Flag](https://en.wikipedia.org/wiki/Socialist_Autonomous_Province_of_Kosovo#Flag).  This is later-period evidence and must not be read as a direct 1936 law, but it reinforces the conservative conclusion that a universal Kosovo flag cannot be invented from the modern six-star design.
- No primary 1936 Kosovo flag decree, provincial statute, municipal flag register, or period Kosovo-wide emblem was found in this bounded pass.  That absence is a blocker for claiming an attested neutral Kosovo flag; it is not evidence that no Albanian, Serbian, Turkish, religious, municipal, or party banners were privately used.

## Design and source-rights matrix

| Candidate | Historical fit at 1936 | Exact documented geometry | Identity boundary | Rights/source status | Decision |
|---|---|---|---|---|---|
| Vanilla `KOS` blue/gold map/six stars | No; adopted 2008 | Blue field, gold Kosovo map, six white stars | Modern multi-ethnic Republic of Kosovo | Installed game asset; no new source needed | **Reject for 1936**; preserve existing files unless a route-specific transformation is accepted |
| Kingdom of Yugoslavia tricolour | Yes as the governing state standard | Blue/white/red, three horizontal equal bands; 2:3; plain civil/state standard | Yugoslav state/administration, not a Kosovo national flag | 1931 constitutional text; public-domain historical design facts, but no copied asset | **Conditional** neutral/mixed-community administrative route |
| Albanian Kingdom / Albanian-community civic flag | Yes as an Albanian national/community symbol in 1936 | Red field; centered black double-headed eagle; no modern Kosovo map/stars | Albanian-led route only; not a universal Kosovo identity | 1928 statute text; Commons SVG is PD/ineligible reconstruction, not an original source image | **Recommended route-specific contract** if parent explicitly chooses Albanian provisional identity |

## Institutional emblem and leader boundary

No authentic interwar Kosovo-wide institutional emblem was established in this pass.  The Yugoslav royal arms and Albanian double-headed eagle are state/national symbols, not a sourced “Kosovo provisional council” badge.  Do not create a non-person council seal from them or use a generated emblem to stand in for a grounded institution.  The package’s required real male political identity/leader sourcing remains a separate portrait task; this symbol handoff does not authorize a replacement leader, council portrait, or advisor card.

## Parent wiring and ImageGen handoff

1. Keep the installed vanilla `KOS` normal/medium/small ladders unchanged while the package is unresolved.
2. Do not add a default flag override merely because the `KOS` tag participates in Event 006.
3. If the parent accepts the Albanian-community contract, register a route-specific cosmetic tag and ask the generated-art worker to create **one clean flat orthographic ImageGen master** constrained to the 1928 statute (red field, centered black double-headed eagle).  ImageGen output must be a flat flag graphic, never waving cloth, a pole, a scene, a painting, a map, or an invented heraldic seal.  Produce the normal 82×52, medium 41×26, and small 10×7 TGA ladder only after the parent records the route decision and the generated master is visually compared against the cited design reference.
4. If the parent accepts the neutral administrative contract, use a separate route/cosmetic tag with the 1931 Yugoslav tricolour and describe it as a Yugoslav provisional administration.  Do not call it “the historical flag of Kosovo.”
5. No source PNG, processed preview, DDS/TGA, contact sheet, manifest row, or `.gfx` handoff was created here because this was research-only and the universal route is blocked.

## Uncertainty and blockers

- The 1928 Albanian statute fixes the principal colours and symbol but does not provide a modern colour standard, exact eagle feather geometry, or a flag ratio.  The 3:2 dimensions and detailed eagle in the Commons SVG are a later vector reconstruction; treat them as a visual aid, not primary attestation.
- The 1931 Yugoslav constitutional wording fixes the national standard but not every local administrative/banner practice in Kosovo.  It is safe as a state flag, not as proof of a Kosovo regional identity.
- No source found in this pass proves a Kosovo-wide flag used by all communities in 1936.  A single universal Event 006 Kosovo flag remains **blocked** pending explicit route semantics and community review.
