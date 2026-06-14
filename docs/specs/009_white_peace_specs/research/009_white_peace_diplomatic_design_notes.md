# Event 009 — Diplomatic Design Notes

## White peace vocabulary

The core settlement fantasy is a status-quo peace: no conquest, no indemnity, no public victory. The related diplomatic phrase **status quo ante bellum** means the state existing before the war. Merriam-Webster defines it as “the state existing before the war,” and general treaty usage contrasts it with settlements that keep conquered positions.

Sources used for vocabulary grounding:

- Merriam-Webster, “Status quo ante bellum,” https://www.merriam-webster.com/dictionary/status%20quo%20ante%20bellum
- Wikipedia, “Status quo ante bellum,” https://en.wikipedia.org/wiki/Status_quo_ante_bellum

The mod should use the vocabulary as flavor, not as legal simulation. The event effect is simply a no-gain, no-loss white peace between selected HOI4 participants.

## Design anchors

Good event language should lean on:

- consular notes;
- armistice circulars;
- neutral telegraph offices;
- staff orders;
- unchanged border posts;
- absence of flags being raised;
- exhausted governments not admitting exhaustion;
- newspapers trying to report a peace with no victor.

The event should not sound like an idealist peace movement. It is an administrative act that stops fighting because the war has become useless, unsafe, or too small to justify continued chaos.

## Why the event should be restrained

A chaos mod needs conflict pressure. A peace event can be valuable, but only if it solves clutter instead of protecting countries from the consequences of war. This is why the spec uses:

- low ordinary weight;
- dynamic war-pressure cap;
- repeatable recovery and decay;
- higher-stage selection penalties;
- candidate safety gates;
- direct Chaos reduction caps;
- pair memory to prevent loops.

## Settlement image motifs

Best visual motifs:

- a typed note on a crowded desk;
- a telegraph operator at night;
- two exhausted border officers exchanging papers;
- a dim neutral consulate corridor;
- a military radio room receiving a ceasefire order;
- abandoned artillery crews waiting by silent guns.

Avoid grand treaty halls, smiling diplomats, flags of specific real treaties, or triumphal crowds.
