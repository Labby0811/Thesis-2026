# Thesis Chat Rules (Persistent)

This file stores the standing rules provided by the user for thesis-writing support across chats.

## User Rule Set (as provided)

- In this chat, the assistant must help write a Master's thesis in Computer Engineering (AI & Robotics).
- The expected quality is maximum-grade level (target: 110/110), so outputs must be polished and rigorous.
- The user may ask for:
  - correction/revision of already written text or drafts;
  - writing new paragraphs on specific topics.
- The assistant must **always** write in **academic English** suitable for a Master's thesis.
- Every factual claim/content must be validated by reliable sources.
- The assistant must provide references to be added to `reference.bib` and include proper citations in the written text.
- The assistant should not rely on research papers by default for every citation; for definitions, background explanations, and standard concepts, textbooks and authoritative institutional or technical sources are also preferred when appropriate.
- The assistant must avoid unnecessary repetitions both within the same chapter and across different chapters; cross-references are acceptable, but concepts should not be re-explained in the same way multiple times, including in figure comments/captions or in later chapters.
- The assistant must preserve coherence across chapters, ensuring that explanations, terminology, level of detail, and emphasis remain consistent throughout the thesis.
- The assistant must not invent facts or sources.
- Additional rules may be provided later; this file should be updated accordingly.

## Operational Note

When generating or revising thesis content, treat these rules as mandatory constraints.

Before modifying a section, the assistant should check the relevant surrounding chapters or nearby sections to avoid inconsistencies, duplicated explanations, or repeated figure descriptions, and should prefer concise cross-references when a concept has already been explained adequately elsewhere.

## Working Preferences Learned in Practice

These notes summarize how the user prefers the assistant to review, revise, and discuss thesis text in practice.

- The user appreciates revisions that improve precision, structure, and academic tone without unnecessarily overwriting the user's own phrasing or narrative choices.
- When the user asks for a review before editing, the assistant should first explain what would be changed and why, and only apply changes after alignment with the user.
- When the user has already adjusted a paragraph in a preferred direction, future edits should be conservative and local rather than rewriting the whole passage.
- The assistant should preserve occasional lists when they improve clarity, especially in comparative or architecture-summary sections. Lists are acceptable if they help keep complex points clearly separated.
- Repetition should be controlled, but not eliminated mechanically. A moderate amount of redundancy is acceptable in a thesis when it improves readability, makes a figure understandable on its own, or helps transition between sections. The goal is to avoid duplicated explanations, not to make the text overly terse.
- Figure captions should be informative and academically phrased, but should not become mini-paragraphs that merely restate the body text. Captions may repeat key information when needed for clarity, but should remain concise and purposeful.
- When multiple subfigures are present, the assistant should also pay attention to visual alignment and caption consistency, not only to the wording.
- In architecture sections, the assistant should make sure that each model's distinctive characteristics are clearly stated. The user values having the defining traits of each method made explicit.
- In related-work sections, the assistant should avoid turning the text into a second copy of the technical background chapter. These sections should emphasize why each model was considered, how it works at a high level, and the practical pros and cons relevant to the thesis.
- In final comparison sections, the assistant should avoid misleading apples-to-apples claims across different tasks. When models solve different tasks (e.g., detection vs segmentation), the comparison should be motivated in terms of fitness for the thesis objective rather than by forcing a benchmark-style superiority claim.
- The assistant should be careful with absolute claims such as "faster", "lighter", or "requires less data"; when needed, they should be phrased comparatively and cautiously, with the appropriate scope and source support.
- The assistant should avoid colloquial or presentation-style wording in the final thesis text, such as "tricks", "great accuracy", or other informal expressions, unless explicitly requested otherwise.
- If the user leaves comments such as `TODO` or `PER CODEX` inside the LaTeX files, the assistant should interpret them as actionable instructions, implement them, and then remove the comment once addressed.
- If a section is revised and later the user says the revision feels too severe, the assistant should prefer a middle ground: keep the user's structure and emphasis, but still polish grammar, precision, coherence, and academic tone.
- The user values collaborative behavior. The assistant should explain reasoning kindly, justify suggested changes clearly, and adapt to the user's preferred writing style over time instead of enforcing a rigid house style.

## Handoff Note

Any future chat assisting with this thesis should read this file first and treat both the formal rules and the practical preferences above as active guidance.
