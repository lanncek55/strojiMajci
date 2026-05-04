1.  **Extract `ES_AV - Vaja 01.pdf` text**: Done.
2.  **Add Task Vaja 01 (Magnetilni tok dušilke navite na toroidno jedro)**:
    -   Create `vaja_01.html` using the template layout.
    -   Parse and add the text from `vaja_01.txt`.
    -   Include all MathJax equations for integrating Faraday's law to get $E = 4.44 \cdot f \cdot N \cdot B \cdot S$, and calculating the magnetizing current $I_\mu$ using Ampere's law.
    -   Add a "Real World Use" section (e.g. why transformers and motors use iron cores instead of air cores - directly related to the massive difference in required current demonstrated in the task).
    -   Create an interactive SVG diagram: A dynamic B-H curve where the user can pick the operating point (voltage/frequency) and it calculates the necessary magnetizing current for an iron core vs an air core. Show a small visual of the toroid coil.
    -   Add a radio-button quiz about the factor 4.44 (form factor of sine wave) or the consequence of removing the iron core.
3.  **Update `gemini.md`**:
    -   Mark Korak 17 as complete.
4.  **Pre-commit steps**:
    -   Verify HTML rendering.
    -   Run Playwright UI tests with screenshot/video verification.
    -   Clean up scratchpads.
5.  **Submit changes**: Commit and submit the code on a new branch.
