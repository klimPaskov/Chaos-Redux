# Vanilla 1.19 Headquarters and Regimental Support Research

## Verified current mechanics

Official Hearts of Iron IV 1.19 material introduced Army Headquarters that assign a general and staff to specific orders. Headquarters can receive dedicated support companies. Five commander abilities are unlocked by headquarters companies. The free update also introduced a separate regimental support row with twelve company types.

The July 2026 open beta notes explicitly state that regimental support did not meet balance goals. The notes increase equipment and manpower requirements, normalize support-unit penalties, add essential equipment blocks, and make battalion-adjuster effects scale with equipment and manpower status. They also note excessive stat growth and low economic requirements as the central problem.

Army Headquarters abilities use `unit_modifiers` in current 1.19 scripting. Older temporary unit-buff patterns should not be used.

## Design implications for Chaos Warfare

### Headquarters are the operational layer

The doctrine's strongest theater effects belong at Army Headquarters because they represent planning, meteorology, medical preparation, supply routing, decontamination, and biosecurity. The assigned order defines which divisions receive the effect.

### Regimental support is the division layer

Gas-mask issue, chemical reconnaissance, projector detachments, decontamination teams, and medical countermeasures belong in the regimental support row where they compete with other useful support options.

### Essential equipment is mandatory

A chemical or protective support company must lose most of its special effect when it lacks masks, payloads, vehicles, medical stores, or specialist equipment. The design must define essential-equipment blocks for every unit that grants a battalion adjuster or order-wide effect.

### Economic burden must be visible

Chemical support should never be a cheap way to add army-wide soft attack. Strong effects require:

- specialist equipment production
- payload production
- protective-equipment production
- motorisation for mobile decontamination
- headquarters support slots
- regimental support slots
- command power for order abilities
- recurring operation expenditure
- supply and fuel in the affected theater

### Stat contributions stay modest

New units should provide narrow battlefield roles and scripted operational effects. Their direct attack values should be comparable to other support choices after penalties. Agent lethality is represented through exposure, disruption, attrition, deaths, contamination, and temporary unit modifiers rather than extreme base soft attack.

## Required implementation verification

Before coding, the implementation agent must inspect the local 1.19 files and documentation for:

- Army Headquarters support-company schema
- ability unlock fields
- order targeting and scope
- `unit_modifiers`
- essential equipment blocks
- regimental support groups and slot rules
- battalion adjusters and equipment scaling
- AI template selection for headquarters and regimental support

The plan intentionally does not invent unverified engine keys. It defines gameplay behavior and leaves exact syntax to direct local documentation and vanilla precedent.
