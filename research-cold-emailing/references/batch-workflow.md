# Batch workflow

Read this reference for multiple professors, scheduled preparation, or unattended research and drafting.

## Batch contract

Before starting, establish:

- the institution, department, or explicit source list;
- the maximum number of professors to process;
- inclusion and exclusion rules;
- the student profile and approved claims;
- the requested output: research briefs, local drafts, mail drafts, or sending;
- attachment rules;
- stopping conditions.

If sending is requested, the authorization requirements in [operating-mode.md](operating-mode.md) still apply.

## Process each professor independently

For every record:

1. resolve identity and official contact information;
2. check existing local records, Drafts, and Sent Items when mail access is in scope;
3. build the evidence record;
4. record `Research fit` and `Current opportunity evidence` independently;
5. select one research detail and one student connection;
6. match the opportunity wording to the evidence level;
7. draft and apply the quality gate;
8. save the result or record the exact skip reason.

Continue past an isolated research or drafting failure unless the failure indicates a batch-wide problem, such as the wrong institution, wrong account, missing profile, expired login, or unclear authorization.

## Do not trade quality for volume

- Use reasonable request pacing and respect site access restrictions. Do not bypass access controls or repeatedly retry a blocked source.
- Do not reuse the same research paragraph across professors.
- Do not treat different papers with similar keywords as interchangeable.
- Do not use a generic email merely because a source is unavailable.
- Do not infer email addresses to increase completion count.
- Do not convert research fit into an implied opening to increase response volume.
- Do not report an item as complete until its requested artifact exists and passes verification.

## Statuses

Use explicit, observable statuses:

- `researched`: evidence record complete;
- `drafted`: text draft complete and quality gate passed;
- `mail draft verified`: reopened mail draft passed recipient, subject, body, and attachment checks;
- `sent`: the mail service visibly confirmed sending and the message appears in Sent Items;
- `skipped`: not processed, with a reason;
- `blocked`: batch-wide issue prevents safe continuation.

Do not use a more advanced status based on intention or an intermediate screen.

## Batch report

Report at minimum:

```text
Scope:
Requested maximum:
Researched:
Drafted:
Mail drafts verified:
Sent:
Skipped:
Blocked:
Per-person status and source:
Per-person research fit:
Per-person current opportunity evidence:
Unresolved issues:
```

For unattended work, leave the batch in the safest completed state permitted by the instruction. Research and local drafts are preferable to unverified mail actions.
