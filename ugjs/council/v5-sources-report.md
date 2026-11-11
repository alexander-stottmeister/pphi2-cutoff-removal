# Rounds V5, V5b and V5c: sources and integration of the free-field appendix (11 November 2026)

One agent (general-purpose, model claude-opus-5-5) that had written none of the audited text, read-only. It checked every quotation and every statement about a source in the repair against pages it rendered itself, the dossier images, the builds of both versions, the label numbers, the cross-references and the consistency of what the record says about itself. It then re-checked the orchestrator's fixes twice (V5b, V5c). It did not see the edits made after V5c (ten lines of the proof of Lemma E.7; the round names in the title-page notice and the blank line before that notice). Three reports, in the order returned.

Returned by the agent as messages, not as files. Saved here on 11 November 2026 by the orchestrator from the session transcript, before the commit of the repair. The text is verbatim except that paths under the home directory and under the session's temporary folder are replaced: `<scratch>/` is that temporary folder, which is not kept (the files `phase5/...` and the diffs named in the reports were the orchestrator's working copies there), and paths inside this repository are written relative to its root. The line numbers of each report refer to the working tree as it was when that report was written; the times are those of the transcript, in UTC. Findings and dispositions: `part_i/README.md`, "Free-field appendix (2026-11-11)".

---

## V5 (returned 2026-11-11 11:19 UTC)

I found nothing CRITICAL. Every quotation I checked against the rendered page is exact, and the build, the label numbers and the dated history all check out. There are two MAJOR findings, both statements about the record, and nine MINOR ones. I worked read-only; my scratch files are under <scratch>/.

## 1. Findings (most serious first)

**M1. MAJOR: status restored before the repair is audited; the gate record disagrees.**
- Where: `part_i/main.tex`, title-page notice "The free-field layer (11 November 2026)", ll. 137–150.
- Text: "With this addition the status sentence of 7 November 2026 above stands."
- What the record says: `part_i/README.md` (Status review, l. 535, not modified in the working tree) says "Standing until the repair is audited: Theorem 12.2 is proved conditional on the standard definitions of π₀ and H₀ and on the three properties behind F4, F6 and F7 …". AGENTS.md rule 3.10 treats a repair as a new claim that needs its own audit.
- As written, `main.tex` restores the status unconditionally while its gate record still says conditional.
- Correction: make the sentence conditional on the audit of Appendix E, or update README.md once that audit has passed.

**M2. MAJOR: Appendix E's statement of its external inputs is incomplete.**
- Where: Appendix E (`app:freefield`), opening paragraph, l. 7892f.
- Text: "Its external inputs are the printed statements of \cite{SimonBook} listed in Assumption~\ref{A:cutoff}, items (e) and (f) … Everything else is proved here."
- What the appendix actually uses besides (e)–(f):
  - A1(a), the Wick recursion, in Lemma E.4(iii);
  - A1(c), Γ_n, in Definition E.3 and Lemma E.4;
  - A1(d) and (W.1) in Proposition E.5 (T), (P), (D);
  - A1(g) in Lemma E.7.
- A1's own Used-in line (l. ~788) says "Appendix E (items (a), (c)–(g))", so the two passages contradict each other.
- The intro notice (l. 145, "listed in … items (e)–(f)") is not exclusive and can stay.
- Correction: replace "items (e) and (f)" in the opening paragraph with "items (a), (c)–(f)", and keep the sentence that (g) enters only Lemma E.7.

**m1. MINOR: the claim that Ω₀ is now introduced where it is first used is false.**
- Where: Appendix B, new entry, l. 3417.
- Text: "$\varphi_0$ and $\Om_0$ are introduced where they are first used".
- Ω₀ is still used first at l. 360 (introduction, §1.4: "$\psi_T=e^{-TH(g)}\Om_0$"). It is defined only at l. 451 (§2.1, "$\Om_0:=1$").
- F2 of the report named this use (old l. 346).
- Correction: add a forward reference at l. 360, or weaken the claim.

**m2. MINOR: the same symbol carries two meanings.**
- Where: A1 (e), l. 698–699, and the Scope, l. 764.
- Manuscript: `\HH`=`\mathcal H`, so `\HH_C` (the real one-particle space of A1, l. 634) prints exactly like Simon's `\mathcal H_C`, the complexification.
- Item (e) quotes "$\mathcal F_n(\mathcal H)=\mathcal H_C\otimes_s\cdots$", and the Scope then sets "$\mathcal H=\HH_C$". Under that substitution the printed $\mathcal H_C$ would denote the real space, not its complexification.
- Appendix E avoids the clash by writing $\mathcal K_m$, $\mathcal K_m^{\C}$.
- Correction: write the substitution as $\mathcal H=\mathcal K_{m_0}$, or add a one-line warning.

**m3. MINOR: one statement about where items (e) and (f) are printed is slightly too broad.**
- Where: A1 Scope, ll. 763–764.
- Text: "items (e) and (f) are printed for an arbitrary real Hilbert space".
- Item (f) includes Theorem II.17 ((II.46)–(II.48), Simon pp. 78–79). That theorem is printed for the specific space F_{m₀}, not an arbitrary one. The same sentence then treats (II.48) separately, so nothing downstream is wrong.
- Correction: "items (e) and (I.40)–(I.41) of (f)".

**m4. MINOR: a source convention the isometry rests on is not cited.**
- Where: A1 Scope, ll. 772–774.
- Claim: "f↦μ^{-1/2}f̂ carries F_{m₀} isometrically onto L²_r".
- This holds only because Simon normalises the Fourier transform with (2π)^{-n/2} "throughout these notes". That convention is printed on p. 27 (PDF 49, which I rendered and read); I checked it matches Appendix E's convention.
- p. 27 is not cited and not in the dossier. There is an image `simon-secondq-047` = p. 25, but no image of p. 27.
- Correction: cite p. 27 (and add the image).

**m5. MINOR: the dictionary sentence omits the sign of the translation.**
- Where: A1 Scope, l. 777.
- Text: "carries … their translation unitaries to $1,\varphi_0,\pi_0,H_0$ and $U_a$".
- Lemma E.7(a)(4) and A7 say that 𝔇 carries U(−a) to U_a, not U(a). The sentence leaves the sign out.
- Correction: "their translation unitaries U(−a) to U_a".

**m6. MINOR: Corollary 12.3 is named as an affected proof, but it does not use that property and is left out of the repair.**
- Where: Appendix B, new entry (iii), l. 3404.
- Claim: τ_a(𝔄(O))=𝔄(O+a) "was used in the proofs of Theorem MAIN(4), Corollary canonical and Theorem dichotomy".
- Corollary 12.3's proof (read in full) uses only (T), for A∈𝔄(O), and the identification "σ_{a'} … (our τ_{εa'})" with GJ3's translations. It does not use τ_a(𝔄(O))=𝔄(O+a). This follows the auditor's F6 ("Cor. 12.3, l. 2917").
- The repair sentence of the same entry ("… the proofs of Theorems MAIN(4) and dichotomy refer to it") omits the corollary, and the corollary has no reference to Appendix E or Lemma E.7(a)(4).
- Correction: either drop the corollary from (iii), or say that it uses only τ_a=Ad U_a and its identification with GJ3's σ, and add a reference.

**m7. MINOR: "each finding re-read at the source" overstates.**
- Where: Appendix B, new entry, l. 3394.
- `part_i/README.md` l. 535 records that F5's judgment on how the V identity was justified, and the auditor's statement about §§9–10, are "the auditor's alone", i.e. not re-read.
- Correction: "each finding re-read at the source except two judgments of F5 (README)".

**m8. MINOR: the source attribution in Lemma E.7(b)'s proof hides a sign convention.**
- Where: Lemma E.7(b) proof, l. 8496–8497.
- Text: "By Assumption~\ref{A:cutoff}(f) (the source's Example 3 …), $-T$ generates a contraction semigroup".
- Simon p. 32 prints "the closure of dΓ(A) generates a contraction semigroup" in his convention, e^{-t dΓ(A)}, (I.41). "−T generates" is the Hille–Yosida convention. The conclusion (T+1 onto) is unaffected.
- Correction: "the closure T of dΓ(μ) generates, in the source's convention e^{-tT}, a contraction semigroup".

**m9. MINOR: completeness of provenance and [sic] notes.**
- (a) External residue, l. 3449: lists the pages read for Appendix E as "\cite{GJ2}, pp. 364–365". A1's Sources line (l. ~744) gives "pp. 364–365, 398", and the A1 Dossier includes `gj2-cutoff-independence-38` (p. 398). So p. 398 is missing at l. 3449.
- (b) A6 Scope, l. 1011: the [sic] for ">" covers "g(y)=λ for |x−y|>|t|". The same page prints ">" a second time in the next clause, "if g(y)=λ for |x+α−y|>|t|". It is not used, but it is unreported.

## 2. Checked and found correct

Every quotation below was compared symbol for symbol against a page I rendered at 150 dpi from `refs/`. The offsets hold: Simon PDF page = printed + 22; GJ2 PDF page = printed − 360.

**Simon p. 23**
- "$\mathcal F_n(\mathcal H)=\mathcal H_C\otimes_s\cdots\otimes_s\mathcal H_C$ (n times)" (I.28b).
- "$\mathcal F(\mathcal H)=\bigoplus_{n=0}^\infty\mathcal F_n(\mathcal H)$" (I.28c).
- "Let $\mathcal F_F(\mathcal H)$ be the incompleted direct sum of the $\mathcal F_n$".
- "Given f∈H and ψ∈F_n(H), we define A*(f)ψ=√(n+1) S_{n+1}(f⊗ψ) (I.29a) where S_{n+1} is the symmetrization operator".
- The real-H setting, and "f∈H, not H_C" (supports Appendix E's remark that A*(f) is defined for f∈K only).

**Simon p. 24**
- (I.29b) "A(f)=A*(f)*↾F_F(H)".
- (I.29c) "φ(f)=1/√2(A*(f)+A(f))".
- "the φ(f) are essentially self-adjoint on F_F(H)".
- "the vector (1,0,…,0,…)∈F(H)".
- Theorem I.11 (a), (b), (c), exact.
- Remark 1: "We also drop "D" treating it as an identity", which supports "drop[s] `D' treating it as an identity" and "uses Γ, Γ_n for F, F_n".

**Simon p. 31**
- "(not necessarily bounded) operator", "on H (with domain D(A))".
- "D_n(A)⊂Γ_n(H)", "(incomplete tensor product)".
- (I.40), exact; the definition is on this page.

**Simon p. 32**
- Example 3, exact; the ellipsis replaces "(and, in fact, on each L^p(Q_H,dμ); p<∞)", which hides nothing relevant.
- (I.41).
- "In particular, this holds if A is a positive self-adjoint operator on H".

**Simon pp. 78–79**
- Theorem II.17: "the Hilbert space of all real distributions on R whose Fourier transforms are functions with the property that the norm[:]" (II.46) "is finite".
- μ=(−Δ+m₀²)^{1/2} is (II.47a) (the text says "(II.47)", acceptable).
- H₀=dΓ(μ) (II.48) is on p. 79.

**GJ2 p. 364**
- "The Fock space F is the Hilbert space completion of the symmetric tensor algebra over L₂(R)".
- Ω₀={1,0,0,⋯} (1.2.3).
- (1.2.5), (1.2.6).
- a(k) (unnumbered, on p. 364), exact.

**GJ2 p. 365**
- 𝔖, "the set 𝔖 of vectors ψ in F with ψ_n=0 for large n and ψ_n∈S(R^n) for all n" (fraktur S, as printed).
- (1.2.7), (1.2.10), (1.2.11), exact.

**GJ2 p. 398**
- (3.6.2), exact.
- "U(−α)H(g)U(+α)=H(g′), where g′(x)=g(x−α)", exact.
- "from the definition (1.2.11)" where φ(x) is (1.2.10): the [sic] is correct.
- "g(y)=λ for |x−y|>|t|", exact.

**GJ2 p. 397**
- The unchanged A6 quotations, all exact.
- "distance less than |σ|" (3.5.1), exact.
- The ">"-for-"<" [sic] is justified by (3.5.1).

**Expositions p. 42** (`gjexp-056`): Theorem 4.1.2, "let g ≡ 1 on B_t", exact.

**Dictionary consistency.** U_a=U(−a) agrees with (3.6.2) under j(τ_a f)=e^{−iak}jf. A7's identity transfers to U_aK(g)U_a^*=K(τ_a g).

**A8(viii) "imports a Euclidean scaling only".** Supported by GJS p. 590 (`gjs-scaling-07`): "a unitary scaling transformation on L²(S′(R²),dΦ)". A8(viii) itself (l. 1306) reads "space-time dilation of [GJS, p. 590]".

**Bibliography**
- `SimonBook`: title, Princeton University Press, Princeton 1974 (title page, PDF 5, rendered).
- `GJ2`: title, Ann. of Math. 91 (1970) 362–401 (JSTOR cover, PDF 1, rendered).
- `GJExp`: Birkhäuser, Boston, 1985 (PDF 2, text layer only; not rendered).

**Dossier**
- All names in the Dossier lines of A1, A6 and A7 exist in `audit_2026/evidence/`.
- The six Simon images are byte-identical (sha256) to my 150-dpi renders: `simon-fock-045` = p. 23, `-046` = p. 24, `simon-dgamma-053` = p. 31, `-054` = p. 32, `simon-freefield-100` = p. 78, `-101` = p. 79.
- Viewed: `gj2-fock-04` = p. 364, `gj2-fields-05` = p. 365, `gj2-cutoff-independence-38` = p. 398.
- `gj2-locality-37` = p. 397 (byte-identical to my render).
- `gjexp-056` = Expositions p. 42.
- The eight new images are dated 11 Nov 2026 11:08 (mtime).

**History**
- `main.tex` is identical at 231b8ea, f213cc8 and HEAD (`git diff` empty), so the whole diff is today's work.
- 231b8ea is dated 7 Nov 2026 23:23 +0100.
- V4f report: F1, F4, F6, F7 are MAJOR and F2, F3, F5, F8, F9, F10 are MINOR. That is 4 MAJOR and 6 MINOR, mapping to the entry's (i)–(iv) and its six MINOR repairs.
- "All four gaps older than the integration": confirmed in `git show 910959d:part_i/main.tex`. There π₀ (l. 379) and H₀ (l. 395) are used undefined, σ_s appears at l. 1100–1108, τ_{−a}A at l. 2439, and θ: W(f,h)→W(−f,−h) at l. 2444.
- The 9-November page reads are recorded in README l. 535 (GJ2 pp. 365, 398; Simon p. 24).
- "No statement of a theorem changed": a script comparison of all theorem, proposition, lemma, corollary, auxlemma, hypothesis, definition and remark environments by label, f213cc8 against the working tree, finds changes only in A1, A6, A7 (assumptions) and Remark 3.3, plus the seven new E-labels. No theorem, lemma or proposition statement changed. A6(i) and A7's opening did change, but they are assumptions, not theorems.

**Structure**
- Every assumption keeps its Sources, Scope, Used-in and Dossier lines, with two pre-existing exceptions that this diff does not touch: A3 (`A:stability`) has "Source." and A8 (`A:gjs`) has no Sources line.
- A1's Used-in names Appendix E.
- Date: `\date{11 November 2026}`, the comment above it, and epoch 1794355200 = Wed 11 Nov 2026 00:00:00 UTC (`date -u -r`) all agree.

**Cross-references.** Every `\ref` and `\eqref` in the added lines resolves to the object the sentence means, including Lemma N.19 (`aux:notation-kernel`), (W.1) (`eq:wickpairing`), Proposition E.5(D), Remark E.6, Lemma E.4(ii)/(iv)/(v), Lemma E.7(a)/(b), and §§2–14 (`sec:setting`–`sec:discussion`). "§2.6" does not occur in `main.tex`; it occurs only in README.md.

**Searches.** I grepped `W(f,h)`, `Weyl`, `\sigma_s`, `dictionary`, `Fock`, `U_a`, `\Theta`, "no other external", "used without" and "reading". No remaining passage contradicts the new text. The remaining hits are historical parentheses, or Part II's lattice Weyl unitaries (ll. 3225, 3231), which are a different object.

**Unrelated changes.** None. Every hunk is in the list you gave, except two that are also explained:
- the 7-November Appendix B entry reworded (F8);
- the External residue sentence (part of the Appendix B change).

The only other change is whitespace in the 𝔄(O) display.

## 3. Build and labels

**Working tree**
- Three passes in a temporary copy, `SOURCE_DATE_EPOCH=1794355200 FORCE_SOURCE_DATE=1`.
- `^!` 0, Overfull 0, undefined 0.
- 123 pages.
- sha256 d3266e57…f734, byte-identical to `part_i/main.pdf`; the `.aux` is identical to `part_i/main.aux` (`cmp`).
- The `pdftotext | /usr/bin/grep -nE '\?\?|TODO|Hmm|wait,'` check prints nothing.

**f213cc8**
- Same build, epoch 1794009600.
- 0 / 0 / 0.
- 110 pages.
- sha256 f1962e11…b41e, identical to the committed f213cc8 `main.pdf`.

**Labels.** There are 230 labels at f213cc8 and 238 now; none of the 230 changed its number. The new labels are:

| label | number | page |
|---|---|---|
| `app:freefield` | E | 114 |
| `lem:ff-onepart` | E.1 | 114 |
| `lem:ff-gamma` | E.2 | 115 |
| `def:ff-objects` | E.3 | 116 |
| `lem:ff-transport` | E.4 | 117 |
| `prop:ff-symmetries` | E.5 | 118 |
| `rem:ff-A7` | E.6 | 121 |
| `lem:ff-sources` | E.7 | 121 |

## 4. Not checked

- The mathematics of Appendix E and of the rewritten proofs (the other auditor's remit), beyond the convention points in m4, m5 and m8.
- GJ2's own definition of H(g) (p. 363; the text layer is garbled and I did not render it), so "printed for its (φ⁴)₂ Hamiltonian" is checked only against the paper's title and p. 364.
- The Expositions title page as an image (`gjexp-cover-001.png` shows only a logo); I used the text layer of PDF page 2.
- GJ1 §III, `gj1-locality-06`, `gjexp-054/055` and `gj2-local-algebra-40` (unchanged dossier entries; existence checked only).
- `part_i/README.md`, the companion and the KB, beyond the README lines cited above.

---

## V5b, re-check of the fixes (11:36 UTC)

Re-audit of the free-field repair, round V5b (read-only, nothing in the repository touched)

Ten of my eleven findings are closed and one (m7) is partly closed. No quotation in the new text deviates from the page. There are three new findings, all MINOR, plus a list of diff changes that your brief does not explain.

I compared `phase5/main.v1-audited.tex` with my own copy of the version I audited: they are byte-identical. I worked from my own `diff -u` of that file against `part_i/main.tex`, which is 747 lines, the same length as `v1-to-v3.diff`.

## 1. Status of my findings

- **M1: closed, on the condition you name.**
  - The title notice now says: "The repair was audited on 11 November 2026 by two agents that had written none of it, and their findings were applied and re-checked (rounds V5 and V5b; `part_i/README.md`). With this addition the status sentence of 7 November 2026 above stands."
  - It is accurate provided two things hold. First, README.md records V5 and V5b and drops its sentence "Standing until the repair is audited …" (l. 535, still present now). Second, whatever you apply after this report (for example N1–N3 below) is either re-checked or does not touch statements. Otherwise "re-checked" would be false for those edits.
- **M2: closed.**
  - Appendix E's opening (now ll. 7972–7981) lists items (a), (c), (d), (e), (f), says what item (g) is for, cites Theorem I.6 for the realisation, and names Lemma N.19.
  - The new Conventions sentence says that A1 (a)–(g) and Lemma N.19 hold for every mass.
  - Introduction (l. ~441) now says "from the printed statements listed in Assumption A1". The title notice (l. 145) says "listed in Assumption A1 (its items (e)–(f) are new)". Neither is exclusive any more.
- **m1: closed.**
  - l. 362: "$\psi_T=e^{-TH(g)}\Om_0$, with $\Om_0\equiv1$ the constant function of $Q$-space (§2.1)".
  - The Appendix B entry now reads "introduced at the start of §2.1, and Ω₀ also at its first occurrence, in the introduction", which is accurate.
- **m2: closed.**
  - A1's paragraph says "its $\mathcal H_C$ is not the space $\HH_C$ of this assumption, which is real and takes the place of the source's $\mathcal H$".
  - The Scope repeats the warning and points to $\mathcal K_m$, $\mathcal K_m^{\C}$.
- **m3: closed.**
  - The Scope says "item (e) and the statements (I.40), (I.41) of item (f) are printed for an arbitrary real Hilbert space", and "(II.48) is printed for the space $F_{m_0}$ only".
- **m4: closed.**
  - The quotation of Simon p. 27 is exact (see section 3).
  - `simon-fourier-049.png` is byte-identical (sha256 3c769bc0…) to my 150-dpi render of PDF page 49, which is printed p. 27.
  - p. 27 is now in A1's Sources line and Dossier line.
- **m5: closed.** The text now reads "their translation unitary $U(-a)$ to $U_a$".
- **m6: closed.**
  - Item (iii) is reworded. The three results "use them as such", meaning the translations as automorphisms. τ_a(𝔄(O))=𝔄(O+a) is now attributed only to the proofs of Theorems 12.2(4) and 13.2, which is correct.
  - Corollary 12.3's proof now reads "our $\tau_{\epsilon a'}=\mathrm{Ad}\,U_{\epsilon a'}$ of Proposition E.5(T)".
  - The identification with GJ3's σ_{a'} is still not referred to Lemma E.7; that is acceptable, since it is a reading of GJ3.
- **m7: partly closed.**
  - The entry now exempts only "the auditor's judgment on how the identity for $V$ in Remark 3.3 had been justified".
  - `part_i/README.md` l. 535 names a second item that was not re-read: "its statement that §§9–10 use the net only through Proposition 2.7, the Locality paragraph and A6(iii)".
  - Correction: name both exemptions, or reconcile the README in the same commit.
- **m8: closed.**
  - The proof now says "$T$ generates a contraction semigroup in the source's convention, $e^{-tT}$; so, by the Hille–Yosida theorem, $T+1$ maps $D(T)$ onto $L^2(d\phi_0)$". This matches (I.41) on p. 32.
  - Hille–Yosida, like Stone's theorem, is standard textbook functional analysis, not a source import.
- **m9: closed.**
  - The External residue now lists Simon pp. 23–24, 27, 31–32, 78–79; GJ2 pp. 364–365, 398; and GJ1 p. 1948.
  - A6's Scope reports both printed ">" on GJ2 p. 398 ("$|x-y|>|t|$" and "$|x+\alpha-y|>|t|$"); I checked both against the page.

## 2. New findings

**N1. MINOR: a reading is presented as printed.**
- Where: proof of Lemma E.4(iii), l. ~8264.
- Text: "By the recursion of Assumption A1(a), read as the source prints it, for formal variables with $\partial/\partial g_i$ the formal partial derivative, …".
- Simon p. 12 (PDF 34, rendered) prints "∂/∂f_i :f_1^{n_1}…f_k^{n_k}: = n_i :f_1^{n_1}…f_i^{n_i−1}…f_k^{n_k}:". The word "formal" does not appear and the source does not say what ∂/∂f_i means.
- Correction: "read, as the source does not specify, with $\partial/\partial g_i$ the formal partial derivative of a polynomial".

**N2. MINOR: the symbol $m_1$ now carries two values; the conflict existed before the repair but is now explicit.**
- l. 1501: in the working coordinates, "$m_1>0$ … denote the printed constants".
- Remark 3.3(5), l. ~1675: "the gap of the original model is $m_1:=s\,m_{1,*}$".
- Remark 3.3(1), l. ~1658: "In the original coordinates the rate is this function [$\Psi_{m_{1,*}}(s\,d)$]; it is not the function $\Psi_\gamma$ formed with the gap $\gamma=s\,m_{1,*}$ of item (5)".
- Meanwhile the introduction's statement of the result (ll. 231–233) and Theorem 12.2(1) write "$\le\Psi_{m_1}(d)$", where $\Psi_{m_1}:=\Psi_\gamma|_{\gamma=m_1}$ (l. 2905), without naming the coordinates.
- Read under the convention of l. 1498 ("we may, and from now on do, assume … $m_0=M_*$"), Theorem 12.2 is consistent. But read with the $m_1$ of Remark 3.3(5), the introduction's displayed rate is the one Remark 3.3(1) says it is not.
- f213cc8 already had "rate becomes $\Psi_{m_{1,*}}(s\,d)$ … gap $m_1:=s\,m_{1,*}$", so the repair did not create this.
- Correction: give the original model's gap a separate symbol, or add "(in the working coordinates, Remark 3.3)" at ll. 231–233 and in Theorem 12.2(1).

**N3. MINOR: GJ1's fields are covered by no stated reading.**
- Where: A6 Scope, l. ~1036.
- Item (i) is now quoted from GJ1 p. 1948 for its algebra 𝔄(O) "generated by the spectral projections of all the fields φ(f) and π(f), supp f⊂O".
- The Scope records as a reading only that GJ2's p. 397 fields are its (1.2.10)–(1.2.11). Nothing says that GJ1's Fock-space fields are the same objects, which is what carrying item (i) "through the same unitary" requires.
- Correction: extend the reading sentence to GJ1's φ(f), π(f) of p. 1948.

**Not on your list: changes the brief does not explain.** The Remark 3.3 comment attributes them to "audit round V5, findings F-A to F-C", the other auditor's round:
- Remark 3.3 rewritten, now ll. 1600–1690: the transport of each conclusion (1)–(5), the intertwining relation for α, and the identities for E(g) and H(g).
- Lemma 2.8: the added domain argument for Θ commuting with K(g).
- Remark E.6: the domain sentences for $U_a$ and Θ.
- (W.1): now "for real $f_1,\dots,f_n$".
- Proposition E.5, both proofs: "$\mathcal S(\R)$" becomes "$\mathcal S_\R(\R)$".
- Lemma E.1(ii): the closure of μ and the complex extension; Lemma E.1(iii): the complex extension.
- Definition E.3(a): the parenthesis distinguishing $N$ from $N_I$ (§2.3).
- Conventions: the note on Appendix D's Fourier normalisation.
- A6(i): rephrased, with "(stated as this inclusion since 11 November 2026)".
- A7 Scope: "Theorems 12.2 and 13.2" becomes "§12 and §13".
- A1 Scope: the sentences on the mass and on the realisation.

I checked the references and source statements in these, not their mathematics. Nothing else is in the diff.

## 3. Checked and found correct

Every page below I rendered from `refs/` and read myself.

- **GJ1, PDF page 4 = printed p. 1948.** All three quotations are exact:
  - "we infer that $e^{iH_0t}\mathfrak A(O)e^{-iH_0t}\subset\mathfrak A(O_t)$, (3.4) where $O_t$ is the region $O$ expanded by $t$";
  - "an open region of space";
  - "the von Neumann algebra of operators generated by the spectral projections of all the fields φ(f) and π(f), supp f⊂O".
  - Section III begins on that page, which supports "§III, p. 1948".
- **`gj1-propagation-04.png`:** viewed; it shows printed p. 1948, with the journal's running number 176.
- **GJ1 bibliography entry:** checked against the first page (PDF 1, rendered): "A λφ⁴ Quantum Field Theory without Cutoffs. I", Physical Review, Volume 176, Number 5, 1968, first page 1945. The last page, 1951, comes from the text layer of PDF page 7 only.
- **Simon p. 27 (PDF 49):** "(Here and throughout these notes, we normalize the Fourier transform by $\hat F(t_1,\dots,t_n)=(2\pi)^{-n/2}\int e^{-i\Sigma t_ix_i}F(x_1,\dots,x_n)d^nx$". The quotation and the display are exact.
- **Simon p. 78 (PDF 100):** "(μ is then the closure of the operator defined on S)" is printed directly after (II.47c). The locator "(II.47)" is acceptable.
- **GJ2 p. 365:** "the bilinear forms φ(f) and π(g) define operators whose closures on 𝔇(N^{1/2}) are self-adjoint" is exact. $N$ is the source's (1.2.4) on p. 364: "(Nψ)_n=nψ_n".
- **GJ2 p. 398:** "|x+α−y|>|t|" is exact.
- **Lemma N.19's proof:** it uses $\hat p_t(k)=e^{-tk^2}$ and $(2\pi)^{-1}\int|\hat f|^2$, that is, the non-unitary Fourier transform, as Appendix E's new Conventions note says.
- **Dossier names:** every name in the Dossier lines of A1, A6 and A7 exists in `audit_2026/evidence/`, including the new `simon-fourier-049` and `gj1-propagation-04`.
- **Renamed symbols:** Appendix E (ll. 7960–8632) contains no stray old mass symbol (no `_M`, `\mathcal K_M`, `(M)`, `=sM` or `M,\lambda`) and no old `J`; the only remaining `M` there is the commutant $\mathcal M$. In Remark 3.3, $M$ is only the moment constant, and the remark uses $m=m_0$, $m'=M_*$ as Proposition E.5(D) requires.
- **References in the added lines:** each resolves to the object the sentence means, including Proposition 2.6 = `prop:smoothing` ("$\Om_g\in D(V(h))$ …"), Proposition 12.1 = `prop:spectral`, §2.3 = `subsec:freeze` (which lists $N_I$), §12 = `sec:ground`, §13 = `sec:dichotomy`, Remark E.6, Lemma N.19 and (W.1).
- **Contradiction search:** "Fock", "Weyl", "dictionary", "W(f,h)", "Ω₀" and the "(e)–(f)" wording show no conflict with the new text, apart from N2.

## 4. Build and labels

- **Working tree, three passes** in a temporary copy (`SOURCE_DATE_EPOCH=1794355200 FORCE_SOURCE_DATE=1`):
  - errors 0, Overfull 0, undefined 0;
  - 124 pages;
  - sha256 4a119900…1c62, byte-identical to `part_i/main.pdf`; the `.aux` is identical to `part_i/main.aux`;
  - the `??|TODO|Hmm|wait,` grep prints nothing.
- **Labels:** 238 now against 230 at f213cc8 (my earlier build). All 230 keep their numbers, and none of the 238 labels of the version I audited changed number.
- **New labels:**

| label | number | page |
|---|---|---|
| `app:freefield` | E | 114 |
| `lem:ff-onepart` | E.1 | 114 |
| `lem:ff-gamma` | E.2 | 116 |
| `def:ff-objects` | E.3 | 117 |
| `lem:ff-transport` | E.4 | 117 |
| `prop:ff-symmetries` | E.5 | 119 |
| `rem:ff-A7` | E.6 | 121 |
| `lem:ff-sources` | E.7 | 121 |

## 5. Not checked

- The mathematics of the V5-driven rewrites: Remark 3.3 (1)–(5), the domain arguments in Lemma 2.8 and Remark E.6, the core argument in Lemma E.1(ii), and the graph-norm argument in Lemma E.7(a)(2).
- `part_i/README.md` as it will stand after your update.
- GJ2's own definition of H(g).
- The Expositions title page as an image.
- GJ1 pages other than 1, 4 and 7 (text layer only for 7).

---

## V5c, check of the last edits (11:38 UTC)

V5c result: N1, N2, N3 and m7 are all closed, the build of the final file is clean, and I have one optional MINOR remark. I read the 115-line diff myself and changed nothing in the repository. `main.v3-rechecked.tex` is byte-identical to the file I re-checked in V5b.

**Status of the four points**
- **N1, closed.** Lemma E.4(iii) now reads "read with $\partial/\partial g_i$ the formal partial derivative of a polynomial in formal variables (the source does not say how the derivative is meant)". This matches Simon p. 12, which prints ∂/∂f_i without saying how it is meant.
- **N2, closed.**
  - Remark 3.3(5) now says "the gap of the original model is $s\,m_{1,*}$, the number called $m_1$ at the end of the proof of Proposition 3.2". That proof does end with "thus the rate in the original coordinates is $m_1:=sm_{1,*}>0$".
  - The new closing sentence of Remark 3.3 and the new sentence after "See Theorem 12.2." in the introduction both state that $\Psi_{m_1}$ and $m_1$ are meant in the working coordinates of §2.6 (`subsec:weak`).
  - The statement of Theorem 12.2 is unchanged.
- **N3, closed.** A6's Scope now says: "That the fields and the Fock space of \cite{GJ1} are those of \cite[(1.2.1)--(1.2.11)]{GJ2}, and that its test functions are real, is a reading of the source". GJ2 pp. 364–365 do carry (1.2.1)–(1.2.11).
- **m7, closed.** The Appendix B entry now names both items that were not re-read. The wording matches `part_i/README.md` l. 535, and §§9–10 is `sec:filter`–`sec:lppl`.

**Build of the final file** (three passes in a temporary copy, `SOURCE_DATE_EPOCH=1794355200 FORCE_SOURCE_DATE=1`)
- Errors 0, Overfull 0, undefined references 0.
- 125 pages.
- sha256 89f3f4f2915d04963e29b52ce7ba3fc79ae28c004b1c5cfce25e2be69c431e77, byte-identical to `part_i/main.pdf`.
- The `??|TODO|Hmm|wait,` grep prints nothing.

**Labels**
- There are 238 labels now and 230 at f213cc8. Every f213cc8 label keeps its number.
- All 238 labels have the same numbers as in the V5b version, and there are no new labels. Only page numbers moved, for example Appendix E now starts on p. 115.

**References in the 115 lines** all point where the sentence means:
- §2.6 = `subsec:weak` ("Standing weak-coupling assumption")
- Remark 3.3 = `rem:wlog`
- Proposition 3.2 = `prop:scaling`
- Proposition 2.6 = `prop:smoothing`
- Proposition 2.7 = `prop:propagation`
- §§9–10 = `sec:filter`–`sec:lppl`
- §2.1 (the Locality paragraph) = `subsec:model`
- A6(iii) = `A:patch`
- Theorem 12.2 = `thm:MAIN`
- Lemma E.2(iii) = `lem:ff-gamma`

**One optional MINOR remark**
- The symbol $m_1$ still has two values in the record:
  - the end of the proof of Proposition 3.2 defines "$m_1:=sm_{1,*}$" (original coordinates);
  - l. 1501, the introduction and Theorem 12.2 use $m_1=m_{1,*}$ (working coordinates, $s=1$).
- Each passage now says which value it means, and the closing sentence of Remark 3.3 reconciles the two, so nothing is wrong or ambiguous in context.
- If you want to remove the overloading entirely, write $s\,m_{1,*}$ in place of "$m_1:=$" at the end of Proposition 3.2's proof.

**Status sentence and gate record**
- The title-page notice (rounds V5, V5b, V5c) is accurate, provided the same commit updates `part_i/README.md` as you describe. That means naming the three rounds and marking "Standing until the repair is audited" as superseded. I have not seen that README version.

**Not checked:** the mathematics of the new continuity argument in the proof of Lemma E.7(a)(2), apart from the constant $\sqrt2$, which follows from the two bounds stated just before it. That argument is the other auditor's remit.
