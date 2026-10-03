# Research Cold Emailing

An open-source Codex skill for researching university faculty and writing concise, evidence-backed student outreach emails.

It is designed for the difficult part of cold outreach: finding a real intellectual connection without inventing familiarity, overstating the student's background, or pretending an old publication is a current opening.

## Install (macOS/Linux)

You need [Codex](https://developers.openai.com/codex) and Git. Copy this **entire block** into a terminal; it downloads the public repository, installs the nested skill folder, and displays the installed `SKILL.md` path:

```bash
git clone --depth 1 https://github.com/LeoBi-0420/research-cold-emailing.git
cd research-cold-emailing
mkdir -p ~/.codex/skills
cp -R research-cold-emailing ~/.codex/skills/
ls ~/.codex/skills/research-cold-emailing/SKILL.md
```

The last line should display a path ending in `research-cold-emailing/SKILL.md`. If it does not, the installation did not finish. Restart Codex if the skill is not available in your current session. This first-time block assumes you are in a directory that does not already contain a folder named `research-cold-emailing`.

The repository and skill folder have the same name: the skill is the **inner** `research-cold-emailing/` folder, which directly contains `SKILL.md`. The repository also contains examples, tests, and release checks; those do not need to be installed.

## First use

Make a private copy of the [student profile example](research-cold-emailing/references/student-profile.example.md), outside the cloned repository:

```bash
mkdir -p ~/.codex/research-cold-emailing
cp -n \
  ~/.codex/skills/research-cold-emailing/references/student-profile.example.md \
  ~/.codex/research-cold-emailing/student-profile.md
```

Open `~/.codex/research-cold-emailing/student-profile.md` in your editor. Fill in only facts you have checked and want used in outreach. `cp -n` will not overwrite an existing profile. Keep your completed profile, résumé, transcript, phone number, personal email, mail export, API key, and outreach history out of public repositories.

Then ask Codex:

```text
Use $research-cold-emailing to research Professor Jane Doe and draft a first-contact email. Use my verified profile at ~/.codex/research-cold-emailing/student-profile.md. Return the research brief, sources, draft, and quality score. Do not create or send mail.
```

Replace the professor name with a real person. You can also supply their official faculty page. If you have not filled in a profile yet, give Codex your verified background in the request; the skill must ask for missing facts instead of inventing them. Research and text drafting do not require a mail connection. Creating drafts in a mail account or sending requires an available mail tool and a separate, explicit instruction.

## What it does

- resolves a professor's identity and official contact information;
- finds primary research sources and labels how current they are;
- extracts one email-sized result, method, tension, dataset, or question;
- connects that detail to a verified student experience or learning goal;
- drafts or reviews first-contact and follow-up emails;
- scores drafts for specificity, authenticity, relevance, reply ease, and factual integrity;
- supports bounded batch preparation without lowering the evidence standard;
- separates research, text drafting, mail-draft creation, and sending into distinct permission levels.

It does **not** discover private contact information, infer email addresses, promise that a professor is recruiting, bypass authentication, or send mail merely because a draft was requested.

## Why this skill exists

Most outreach templates optimize sentence structure. The harder problems happen earlier:

1. Is this the right professor?
2. Is the research detail accurate and current?
3. Did the student actually review enough material to say this?
4. Is the claimed connection supported by the student's background?
5. Is the request small and easy to answer?

This skill makes those questions part of the workflow instead of treating them as optional polish.

## Research fit is not opportunity evidence

The skill records two independent judgments:

```text
Research fit: strong
Current opportunity evidence: none found
```

`Research fit` determines whether the student has a specific, honest reason to contact the professor. `Current opportunity evidence` determines whether the email may refer to a known opening or invitation.

No public evidence of an opening does not prohibit contact. It changes the language from an assertion to an exploratory question. Sending more well-researched inquiries may reveal opportunities that were never posted, but volume never upgrades the evidence recorded for an individual professor.

## More ways to use it

Review an existing draft:

```text
Use $research-cold-emailing to review this email for factual support, specificity, authenticity, and reply ease. Show unsupported claims and rewrite only what needs changing. Do not send anything.
```

Prepare a bounded batch:

```text
Use $research-cold-emailing to research up to 10 professors from this official department directory. Create local research briefs and text drafts only. Skip anyone whose identity, official email, or research evidence cannot be verified, and report the reason.
```

Mail-account actions require a connected mail tool and an explicit instruction. A research or drafting request never authorizes creating mail drafts or sending.

The package keeps the method in `SKILL.md` and task-specific material under `references/`. The public skill contains the method; the private profile contains the student's identity, evidence, preferences, and constraints.

## How the workflow is organized

```text
student profile + official faculty source
                  ↓
          identity resolution
                  ↓
       evidence record and currentness
                  ↓
     one research idea + one student link
                  ↓
              text draft
                  ↓
       quality and factual-integrity gate
                  ↓
     optional mail draft → reopen → verify
                  ↓
      optional bounded, authorized sending
```

## Evidence levels

The skill changes its wording based on what was actually reviewed:

- a full paper can support discussion of a result, method, design choice, or limitation;
- an abstract can support only what the abstract states;
- a project page can support the stated project scope;
- a faculty profile can support an established research area, not a current project;
- a secondary source is normally a path to stronger evidence, not the final basis for personalization.

If the evidence is weak, the correct output is a modest draft or a blocker—not invented depth.

## How the email is written

The full paragraph-by-paragraph method is in the [email drafting guide](research-cold-emailing/references/writing-rules.md). In brief, every first-contact email answers:

1. Who is the student, and why are they writing?
2. What specific result, method, tension, dataset, or question prompted this contact?
3. Why did that detail genuinely interest the student?
4. What one verified experience gives the student a starting point?
5. What small response is being requested?

The guide includes subject lines, salutations, five research-angle patterns, weak-versus-strong examples, preparation language, follow-up instructions, attachment wording, and a final drafting checklist. See the [complete synthetic first-contact example](research-cold-emailing/references/example-first-contact.md) for the evidence-to-email transformation.

## Quality standard

Every `content-ready` draft must pass blocking factual checks and score at least 8 out of 10 across:

- specificity;
- authenticity;
- relevance;
- reply ease;
- factual integrity.

Factual integrity must receive 2 out of 2. A polished email with an unsupported claim does not pass.

`Mail-ready` is a separate status. It applies only after the saved draft has been reopened in the connected mail service and the recipient, subject, complete body, and required attachments have been verified. A local text draft can be `content-ready`, but never `mail-ready`.

## Repository layout

```text
research-cold-emailing/
├── agents/
│   └── openai.yaml
├── references/
│   ├── batch-workflow.md
│   ├── example-first-contact.md
│   ├── operating-mode.md
│   ├── quality-review.md
│   ├── research-method.md
│   ├── student-profile.example.md
│   └── writing-rules.md
└── SKILL.md

examples/
├── review-output.synthetic.md
└── student-profile.synthetic.md

evals/
└── behavior-cases.md

scripts/
└── validate_release.py
```

## Privacy and safety

- Keep student profiles and attachments outside the public repository.
- Use only publicly available faculty sources unless the user provides other authorized material.
- Never infer an email address from an institutional pattern.
- Never claim a professor is accepting students without current evidence.
- Check Drafts and Sent Items before first-contact mail actions.
- Reopen every saved mail draft and verify recipient, subject, body, and required attachments.
- Stop for authentication challenges, ambiguous recipients, missing attachments, changed content, or unclear sending scope.

## Limitations

- Public sources can be stale, incomplete, or inconsistent.
- A strong research fit does not imply an available position.
- The skill cannot guarantee replies.
- Mail-draft creation and sending depend on the connected tools and account permissions in the user's environment.
- The quality gate improves consistency but does not replace the student's final judgment.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a change. Keep examples synthetic and never include personal data or real unsent outreach.

Run `python3 scripts/validate_release.py` before publishing or opening a pull request. The included GitHub Actions workflow runs the same check on pushes and pull requests.

## License

MIT. See [LICENSE](LICENSE).
