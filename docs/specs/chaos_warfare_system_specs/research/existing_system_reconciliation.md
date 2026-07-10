# Existing System Reconciliation

## Existing foundation retained

The rework keeps the following systems as authoritative rather than creating parallel copies:

- `condemnation_total` and its source buckets remain the diplomatic blame system.
- Air Cleanliness remains the global contamination system.
- The shared Deaths tracker remains the population-loss and military-loss sink.
- Existing state chemical contamination modifiers remain the common state effect layer.
- Existing outbreak states, countermeasure decisions, and biological special projects remain the biological foundation.
- Existing chemical payload cylinder equipment remains usable during migration, although the final equipment model consolidates unnecessary variants.
- Existing general abilities, combat tactics, raids, and special operations remain recognizable player actions.
- Existing weaponized-zombie content stays separate from conventional biological warfare.
- Existing condemnation tiers and sanction design remain the external consequence ladder.

## Major inconsistencies found

### Doctrine power is mostly flat stat stacking

The current grand doctrine gives chemical support companies broad attack, breakthrough, and defence bonuses. The four existing subdoctrines add many more broad unit-category modifiers. This makes the doctrine powerful even when a country has no payloads, no masks, no specialist headquarters, no weather preparation, and no willingness to accept international consequences.

The replacement design moves power into:

- unique equipment and production commitments
- headquarters support companies
- order-scoped commander abilities
- regimental support choices
- doctrine-only technologies
- delivery operations
- protective coverage
- contamination and exploitation rules
- response speed and decontamination

### Grand-doctrine milestones are empty

The current grand doctrine defines four milestone blocks without content. The redesign uses them to unlock the doctrine's operational layers in a clear sequence.

### Gas masks are research without logistics

The existing basic, improved, and advanced gas-mask technologies change tactics and passive protection. They do not create producible equipment, military issue requirements, civilian reserves, filter exhaustion, or distribution choices. The redesign turns gas masks into a visible stockpile and protective-coverage system.

### Offensive stockpiles are copy-pasted

Britain, France, Germany, and the Soviet Union start with identical large chlorine, phosgene, and mustard stocks. Italy, Japan, and the United States use other hand-entered bundles. The values do not reflect population, industry, doctrine, defensive readiness, or program identity. No comparable protective stockpile exists.

The replacement uses country profiles and formulas, then records explicit tuned starting bands for the major powers.

### Chemical aircraft do not consume payload stock

Current chemical air modules add industrial cost, ground attack, weight, and agility penalties. Continuous contamination is estimated weekly from deployed CAS and tactical bombers because the script path cannot reliably observe an exact module flying an exact mission. This can create contamination without a clear payload budget.

The redesign separates three layers:

1. Aircraft design eligibility and ordinary combat stats.
2. Reliable chemical raid and operation completion hooks that consume payloads and apply exact state results.
3. A lower-confidence continuous mission estimator that is disabled by default unless the implementation agent confirms a reliable 1.19 hook.

### Chemical tank companies are duplicated by chassis and agent

The existing system defines many light, medium, and heavy chemical tank support companies for each agent. This creates large file volume, duplicate balance blocks, poor AI selection, and difficult template management.

The replacement uses one armored delivery subunit per chassis role, then selects payload class through equipment, operation stance, or scripted profile. It avoids one subunit for every agent.

### Chaos Battalion requires incompatible equipment

The current Chaos Battalion requires multiple choking, blister, nerve, and biological payloads at the same time. It also has extremely low organisation, extreme soft attack, very low reliability, and a tiny combat width. Its equipment list makes reinforcement fragile and its stats invite abuse.

The redesigned Chaos Assault Battalion is a protected assault cadre. It requires infantry weapons, support equipment, protective crates, decontamination equipment, and specialist delivery equipment. Payload selection belongs to the attached support and current operation, not to a permanent requirement for every weapon class.

### Confirmed culpability can be discounted too aggressively

Parts of the operations branch reduce Condemnation gain. This is acceptable only for attribution uncertainty, disciplined targeting, lower civilian exposure, or reduced visible evidence. It is not acceptable to erase responsibility after confirmed mass use.

The redesign distinguishes:

- exposure caused
- evidence generated
- attribution confidence
- public Condemnation

Doctrine can reduce friendly accidents and evidence generation. It cannot reduce confirmed Condemnation below a floor determined by deaths, persistent contamination, and target status.

### Chemical suppression is entangled with genocide terminology

The current armor branch includes route names and an occupation law that overlap with the camp and genocide system. This blurs military CBRN mechanics, occupation repression, and exposed atrocity systems.

The replacement uses operational names for military doctrine. Atrocity content remains in its own crisis and discovery systems. Nerve-agent occupation use still causes deaths, resistance radicalisation, evidence, and Condemnation.

### AI is inconsistent

Some chemical tactics and abilities are disabled for normal AI while doctrine content assumes integrated use. Chemical tank support companies have no meaningful AI priority. Biological delivery tech can be disabled for AI even after a completed special project.

The redesign gives AI a full program model. It decides whether to adopt the doctrine, build protection, choose an agent class, prepare an operation, accept Condemnation risk, and stop when sanctions or supply make continued use irrational.

## Migration principle

The rework should preserve save-facing identifiers where practical, but it should not preserve bad content merely to avoid migration work. Obsolete unit variants can remain hidden for compatibility while new templates use the consolidated units. Legacy country stockpiles can be converted once through a migration effect. Documentation must state which identifiers remain compatibility aliases.
