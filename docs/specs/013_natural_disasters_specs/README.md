
# Event 013 Natural Disasters planning package

This package contains the source specification and implementation prompts for reworking Event 13 Natural Disasters.

## Contents

- `specs/013_natural_disasters_spec.md` is the core design.
- `specs/013_natural_disasters_evolutions_cluster_scenario.md` expands evolutions, cluster behavior, and the Disaster Barrage scenario.
- `specs/013_natural_disasters_recovery_gui_spec.md` expands decisions, missions, scripted GUI, and animation.
- `matrices/` contains disaster family, AI, and tuning matrices.
- `prompts/` contains implementation, asset, achievement, decision, super-event, and `/goal` prompts.
- `research/` contains source notes for disaster taxonomy and design calibration.
- `subagent_handoffs/` maps provided subagents to concrete Event 13 work.
- `diagrams/` contains a sequence flow diagram.

## Important design rulings

- Event 13 has no world-end scenario.
- One Event 13 sequence creates one event log row.
- Subevents inside the sequence are delayed and do not spam the random event log.
- Cluster-triggered repeated Event 13 member slots can create multiple Event 13 rows because each member slot is a true Event 13 firing.
- Sandstorm active gameplay should route through Event 13.
- Event 46 or Earth Earthquake should become an inactive unknown placeholder, with seismic content handled by Event 13.
- The optional Evolution III super-event is non-terminal and must use research gates before final title, quote, button remark, and audio are written.

## Revision note

This package requires all disaster population losses and civilian deaths to be calculated from per-state dynamic percentages. Fixed casualty amounts and fixed per-state death totals are forbidden. Severe evolved disasters can produce multi-million deaths when they hit dense states or dense regional chains.


## V3 depth correction

This package now includes disaster specific playbooks and big disaster decision categories. The earlier generic recovery category is no longer the full design. It is only an overview and small incident hub.

New binding files:

- `specs/013_natural_disasters_external_event_boundary.md`
- `specs/013_natural_disasters_individual_disaster_playbooks.md`
- `specs/013_natural_disasters_big_disaster_decision_categories.md`
- `matrices/013_natural_disasters_big_disaster_category_matrix.md`

The implementation agent must not use existing unreworked Sandstorm, Heat Wave, Asteroid Incoming, Meteor Shower, Massive Flood, BOOM, or seismic placeholder event code as Event 13 logic. Event 13 owns its own disaster system.
