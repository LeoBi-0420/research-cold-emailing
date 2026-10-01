# Quality review

Read this reference when reviewing or approving an outreach draft.

## Content-readiness checks

A draft is not `content-ready` if any answer is `no` or `unknown`:

- Is the professor's identity resolved?
- Can every research claim be traced to the cited source?
- Does the wording match what was actually reviewed?
- Are all student claims present in an approved profile or supplied evidence?
- Does the draft avoid claiming an opening or current project without evidence?
- Are `Research fit` and `Current opportunity evidence` recorded separately?
- Does the purpose sentence match the recorded opportunity evidence instead of treating research fit as proof of availability?

## Mail-readiness checks

A result is not `mail-ready` unless it is already `content-ready` and every answer below is `yes`:

- Is the recipient address explicitly supported by an authoritative source?
- Did the connected mail service resolve the intended person?
- Was the saved draft reopened after the service persisted it?
- Do the reopened subject and complete body match the approved content?
- If an attachment is required or mentioned, is the correct file visible in the reopened draft?

Never use `mail-ready` for text that exists only in the conversation or a local file.

## Ten-point quality gate

Score each dimension from 0 to 2:

### Specificity

- `0`: generic field labels or praise;
- `1`: a real source is named, but the connection remains broad;
- `2`: a concrete result, method, tension, dataset, or question is used accurately.

### Authenticity

- `0`: exaggerated, performative, or inconsistent with the student profile;
- `1`: plausible but generic;
- `2`: the reaction sounds natural and proportionate to what the student reviewed.

### Relevance

- `0`: the student evidence is unrelated or merely impressive;
- `1`: a loose connection exists;
- `2`: one verified experience or learning goal clearly connects to the research detail.

### Reply ease

- `0`: the request is unclear, demanding, or asks for several things;
- `1`: the ask is understandable but broad;
- `2`: the professor can respond briefly with availability, redirection, or a next step.

### Factual integrity

- `0`: a material claim is fabricated or contradicted;
- `1`: a material claim is weakly sourced, overstated, or ambiguous;
- `2`: every material claim is supported and carefully scoped.

Treat an implied opening as a material claim. When current opportunity evidence is `none found`, exploratory wording can pass; wording that presupposes a role cannot.

Require at least 8 out of 10 and a factual-integrity score of 2 for `content-ready`. A high total never overrides a factual-integrity failure. This score is a drafting heuristic, not a prediction of reply probability.

## Human-voice pass

After scoring, remove wording that a real student would be unlikely to say aloud. Check for:

- abstract nouns replacing clear verbs;
- several polished claims packed into one sentence;
- repeated sentence structure;
- flattery that adds no information;
- a research paragraph that sounds like an abstract;
- an experience paragraph that sounds copied from a résumé;
- an ask that sounds entitled or excessively deferential.

Preserve the student's natural level of certainty. Curiosity can be specific without pretending to have expertise.

## Review output

Return:

```text
Status: content-ready | mail-ready | revise | blocked
Score: X/10
Blocking issue, if any:
Mail readiness: verified | not requested | not assessed | blocked
Research claim checked against:
Student claim checked against:
Main revision made or needed:
```

Use `mail-ready` only after the separate mail-readiness checks pass. Otherwise use `content-ready` when the writing and evidence pass, and report mail readiness separately.
