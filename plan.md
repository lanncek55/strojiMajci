1.  **Add Task 2.4 (Trifazni transformator, vezava Yz5)**:
    -   Parse and add the text for Task 2.4.
    -   Include equations for calculating primary and secondary turns ($ N_1 $, $ N_2 $) for a three-phase Yz5 transformer, handling phase vs line voltage ($ U_{1f} = U_1 / \sqrt{3} $).
    -   Add a "Real World Use" section (e.g., zig-zag connection benefits for unbalanced loads).
    -   Create an interactive SVG diagram showing the Yz5 connection and its phasor vectors.
    -   Add a radio-button quiz about phase vs. line voltage or zigzag connection.
2.  **Add Task 2.5 (Preračun izgub, ohmske upornosti, izkoristek)**:
    -   Parse and add text for Task 2.5.
    -   Include detailed derivations of calculating phase resistance from terminal resistance in Y and D configurations ($ P_{Cu} = 1.5 \cdot I^2 \cdot R_{sp} $).
    -   Include equations for nominal loss ratio ($ \xi_n $), losses at different voltages, and finding the point of maximum efficiency ($ d\eta/dS = 0 $).
    -   Add a "Real World Use" section (e.g., designing transformers for peak efficiency at expected average load).
    -   Create an interactive SVG graph showing efficiency vs load curve ($ \eta(S) $) peaking where iron losses equal copper losses.
    -   Add a radio-button quiz about maximum efficiency or measuring resistance.
3.  **Update `gemini.md`**:
    -   Mark step 10 as complete.
4.  **Pre-commit steps**:
    -   Verify the HTML renders correctly.
    -   Run Playwright UI tests with screenshot/video verification.
    -   Clean up scratchpad files.
5.  **Submit changes**: Commit and submit the code on the same branch.
