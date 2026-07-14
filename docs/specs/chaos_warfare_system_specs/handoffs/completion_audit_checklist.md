# Completion Audit Checklist

## Doctrine

- [ ] adoption no longer grants excessive global combat bonuses
- [ ] four milestones have functional unlocks
- [ ] four tracks match the accepted spec
- [ ] mastery pacing depends on equipped participation
- [ ] doctrine-only technologies are correctly gated
- [ ] officer corps spirits are bounded and mutually exclusive where intended

## Army Headquarters

- [ ] exact 1.19 schema and vanilla precedent documented
- [ ] all planned HQ companies implemented or explicitly dispositioned
- [ ] company-gated abilities use order scope and current unit-modifier pattern
- [ ] command-power costs scale correctly
- [ ] essential equipment blocks effects when missing
- [ ] AI creates HQs and uses abilities

## Regimental support and units

- [ ] masks, recon, pioneer, projector, ammunition, armored delivery, medical, epidemiology, biosecurity, and suppression roles covered
- [ ] no agent-by-agent duplicate unit family remains active without reason
- [ ] Chaos Assault Battalion has coherent stats and equipment
- [ ] no chemical tank support is parachute-capable without verified reason
- [ ] legacy units migrate safely or remain hidden compatibility content

## Equipment and technology

- [ ] gas-mask equipment is producible
- [ ] decontamination and instrument equipment is implemented
- [ ] equipment enums updated
- [ ] payload and shell or air operation consumption works
- [ ] tabun has a complete or precursor-only role
- [ ] all techs have AI, icons, localisation, and dependencies

## Chemical operations

- [ ] all delivery calls use shared exposure
- [ ] artillery consumes shell lots
- [ ] armored delivery consumes payload
- [ ] air raids reliably contaminate selected states
- [ ] continuous air mission behavior is verified or blocked, not silently approximated
- [ ] first-use shock is defender adaptation, not a global attacker buff
- [ ] weather and protection affect outcomes
- [ ] friendly blowback works

## Biological operations

- [ ] incubation and detection work
- [ ] agent profiles differ
- [ ] spread uses targeted approved hooks
- [ ] quarantine, hospitals, antibiotics, vaccination, and border closure work
- [ ] stockpile accidents scale with safety and stock
- [ ] facilities create capture and evidence risk
- [ ] zombie systems remain separate

## Gas masks and civil defence

- [ ] country starting reserves follow profiles
- [ ] military coverage uses actual equipment
- [ ] civilian distribution consumes crates based on population
- [ ] filters and damaged masks need replacement
- [ ] emergency distribution has wastage
- [ ] masks reduce every chemical death pipeline
- [ ] occupied-population protection choices work

## Suppression and occupation

- [ ] nerve suppression is targeted and temporary
- [ ] payload and advanced protection required
- [ ] deaths, contamination, trauma, evidence, and Condemnation apply
- [ ] no genocide infrastructure is unlocked by doctrine
- [ ] later liberation can discover responsibility

## Shared consequences

- [ ] deaths use the shared tracker
- [ ] population never becomes invalid
- [ ] continuing deaths do not duplicate
- [ ] Air Cleanliness updates by contamination class
- [ ] attribution moves from hidden to confirmed without double charge
- [ ] confirmed use has a Condemnation floor
- [ ] sanctions affect practical support and imports
- [ ] retaliation and treaty context work

## AI

- [ ] AI protects before attacking
- [ ] AI has research, production, template, HQ, operation, containment, and sanction behavior
- [ ] country program profiles differ
- [ ] invalid targets and suicidal use are blocked
- [ ] minors can use defensive content

## UI and localisation

- [ ] readiness, stockpiles, protection, operations, contamination, and response are readable
- [ ] irrelevant decisions hide
- [ ] all dynamic requirements have custom tooltips
- [ ] no hidden mechanics are exposed through final text
- [ ] localisation matches repository style and encoding

## Assets

- [ ] every visible icon in the asset prompt has source, PNG, DDS, manifest, and GFX handoff
- [ ] animated assets have real source frames and static fallbacks
- [ ] no placeholder art remains
- [ ] asset types are not resized substitutes for one another

## Documentation

- [ ] accepted specs promoted to source-of-truth folder
- [ ] old docs marked superseded or updated
- [ ] mechanics guide matches implementation
- [ ] relevant event docs and catalog rows match actual changed events
- [ ] all plans have a disposition

## Validation

- [ ] ten balance scenarios recorded at weak, normal, and high-chaos conditions
- [ ] AI scenarios recorded for seven major country profiles and three minor profiles
- [ ] exact air-operation hook result documented
- [ ] no broad unapproved global pulse added
- [ ] completion auditor finds no missing accepted requirement

## Simplification report

Completion report must explicitly list every omitted, merged, unsupported, placeholder, or weaker substitute. If none exist, it must state that and provide file and audit evidence.
