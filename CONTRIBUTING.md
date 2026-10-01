# Contributing

Thank you for improving Research Cold Emailing.

## Scope

Useful contributions make the skill more accurate, portable, or easier to use without weakening its evidence and authorization boundaries. Examples include:

- clearer research-source guidance for a field with different publication norms;
- better factual-integrity or draft-review checks;
- synthetic examples that clarify an edge case;
- mail-operation guidance that remains service-independent;
- accessibility or readability improvements to the documentation.

This repository is not the place for private student profiles, real résumés, real mail exports, credentials, or collections of faculty contact information.

## Design principles

- Keep `SKILL.md` concise and route conditional detail to `references/`.
- Add instructions only when they change an agent's decision or prevent a demonstrated failure.
- Keep research, local drafting, mail-draft creation, and sending as separate permission levels.
- Prefer primary and official sources.
- Preserve uncertainty instead of filling gaps with plausible text.
- Keep all committed examples synthetic.
- Avoid binding the skill to one university, discipline, mail provider, or student.

## Before submitting a change

1. Read the complete skill and every reference affected by the change.
2. Confirm that all links from `SKILL.md` resolve.
3. Run the repository validation:

   ```bash
   python3 scripts/validate_release.py
   ```

4. Run the Codex skill validator when it is available locally:

   ```bash
   python /path/to/skill-creator/scripts/quick_validate.py research-cold-emailing
   ```

5. Search the repository for personal data, secrets, real email messages, and unfinished placeholders.
6. Test the changed path with a synthetic request.
7. Check that `agents/openai.yaml` still describes the skill accurately.

## Writing style

Use direct, imperative instructions inside the skill. Explain why only when the reason changes behavior. Avoid duplicating the same rule across files; link to the authoritative reference instead.
