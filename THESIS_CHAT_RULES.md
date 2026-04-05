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

## Additional Persistent Preferences Learned Later

- The user usually discusses the work in Italian, but all thesis text to be written or revised must remain in academic English.
- Before modifying thesis prose, the assistant should normally:
  1. read the relevant file and nearby sections,
  2. propose what should be changed and why,
  3. wait for the user's approval,
  4. only then edit the file.
- Exception: if the user explicitly gives a direct go-ahead such as "vai", "procedi", or clearly asks for the text to be written immediately, the assistant may edit directly.
- The assistant must preserve the user's intentional `\\` line breaks in LaTeX unless the user explicitly asks to remove them.
- The assistant should not automatically download or insert external figures anymore. If figures are needed, the assistant should:
  - suggest where a figure belongs,
  - prepare the LaTeX `figure` block,
  - propose caption and label,
  - leave only the image filename as a placeholder for the user to fill.
- If content is moved from one chapter to another for structural reasons, the assistant must make sure that no important detail is lost in the process.

## Structural Decisions Already Agreed with the User

- Chapter 3 should mainly describe:
  - industrial context,
  - site setup,
  - hardware,
  - acquisition logic,
  - and only a high-level statement of how the data are later used.
- Chapter 4 should contain:
  - the actual implementation logic,
  - the pipeline details,
  - motion detection,
  - automatic labelling,
  - detector training,
  - volume estimation for Site 1,
  - anomaly detection for Site 2.
- The generic idea of a broad `Implementation` section listing libraries such as OpenCV, Open3D, Torch, and TensorBoard was considered not very useful. Instead, implementation details should be integrated into the methodological sections where they are actually used.
- A specific example of this rule is:
  - background subtraction for frame triggering belongs under `Motion Detection`;
  - background subtraction used to separate dough from the support table belongs under `Site 1: Volume Estimation`.
- The Chapter 1 section `4_Internship.tex`, especially `Pipeline summary`, should remain a true summary and should not absorb detailed implementation material that belongs to Chapter 4.

## Current State of Chapter 4

As of the latest update in this chat, Chapter 4 has already been rewritten to align with the actual implementation and repositories.

- Main file:
  - `Chapters/Chapter_4/0_chapter_4.tex`
- Motion-detection subsection file:
  - `Chapters/Chapter_4/4_opencv.tex`

The current Chapter 4 now covers:

- shared offline/online pipeline across both sites;
- motion-triggered acquisition;
- automatic labelling with Lang-SAM;
- DEIMv2 as the common detection layer;
- Site 1 volume estimation with:
  - filtered detection cache,
  - empty-table depth background modelling,
  - foreground extraction from color/depth,
  - aligned RGB-D point-cloud generation,
  - axis construction and rotational completion,
  - multiple volume estimators including rotated hull, rotated alpha shape, and depth-gap;
- Site 2 anomaly detection with:
  - loaf-crop dataset preparation,
  - automatic split and interactive review options,
  - EfficientAD training through anomalib,
  - one-class training on good samples,
  - use of a small auxiliary defect set from online images,
  - chunked inference and anomaly-score reporting.

Future assistants should not overwrite this structure casually. If the repositories change, Chapter 4 should be updated accordingly, but always by re-reading the real code and README files first.

## Repositories That Must Be Treated as Primary Sources for Chapter 4

For implementation-related writing, especially Chapter 4, the assistant should use these repositories as primary sources and read both the README files and the code:

- Main implementation repository:
  - `https://github.com/Labby0811/thesis`
- Motion-detection / acquisition repository:
  - `https://github.com/Labby0811/Kinect_acquisition`

These repositories were already used to rewrite Chapter 4, and the following bibliography entries were added for them:

- `labby_thesis_repo_2026`
- `labby_kinect_acquisition_2026`

If the user later says the repositories were updated, the assistant should re-read them before touching Chapter 4.

## Build and LaTeX Notes

- The thesis root file is `tesi.tex`.
- In this project, incremental `latexmk` runs can sometimes get confused by stale auxiliary files and produce misleading BibTeX errors such as missing `\bibdata` / `\bibstyle` or runaway `\citation` entries in `tesi.aux`.
- When this happens, the reliable workflow is:
  1. delete the generated auxiliary files (`tesi.aux`, `tesi.bbl`, `tesi.blg`, `tesi.fdb_latexmk`, `tesi.fls`, `tesi.lof`, `tesi.log`, `tesi.lot`, `tesi.out`, `tesi.toc`);
  2. rerun `latexmk -pdf -interaction=nonstopmode -file-line-error tesi.tex`.
- A clean build was successfully completed after the Chapter 4 rewrite.

## Known Remaining Issues Not Caused by Chapter 4

At the time of this handoff, the main remaining unresolved references are:

- `fig:3D_volume_rendering`
- `fig:Anomaly_map`

These occur in `Chapters/Chapter_1/3_Thesis goal.tex` and were already present independently of the Chapter 4 work.

## Handoff Note

Any future chat assisting with this thesis should read this file first and treat:

- the formal rules,
- the practical preferences,
- the structural decisions,
- the repository notes,
- and the build notes

as active guidance for continuing the work consistently with the previous chat.
