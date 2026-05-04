1.  **Add Task 2.6 (Kappov diagram, padec napetosti, izgube)**:
    -   Parse and add the text for Task 2.6.
    -   Include detailed MathJax equations for current, new losses at altered frequency ($f' = 60\text{Hz}$), short-circuit parameters ($u_R, u_X, u_K$), and voltage drop calculation using Kapp's diagram.
    -   Add a "Real World Use" section (e.g., using Kapp's diagram to predict voltage drops in real distribution networks).
    -   Create an interactive SVG diagram representing Kapp's triangle and the voltage drop vectors ($U_1$, $E$, $U_2'$).
    -   Add a radio-button quiz about the behavior of iron losses when frequency changes.
2.  **Add Task 2.7 (Paralelno obratovanje transformatorjev)**:
    -   Parse and add text for Task 2.7.
    -   Include detailed MathJax equations for parallel load sharing based on short-circuit voltage ($u_K$) and calculating temperature rise for non-homogenous loads.
    -   Add a "Real World Use" section (e.g., how substations balance loads using parallel transformers).
    -   Create an interactive SVG diagram showing two parallel transformers and how load distributes based on their $u_K$ settings.
    -   Add a radio-button quiz about which transformer takes more load in parallel operation.
3.  **Add Task 2.8 (Segrevanje stroja, časovna konstanta)**:
    -   Parse and add text for Task 2.8.
    -   Include detailed MathJax equations for the thermal heating curve ($\Theta(t) = \Theta_{max}(1 - e^{-t/T})$) and solving for time $t$.
    -   Add a "Real World Use" section (e.g., overloading transformers safely for short periods based on thermal inertia).
    -   Create an interactive SVG graph displaying the heating curve over time.
    -   Add a numerical quiz to calculate the time to reach a certain temperature percentage.
4.  **Update `gemini.md`**:
    -   Mark step 11 as complete.
5.  **Pre-commit steps**:
    -   Verify the HTML renders correctly.
    -   Run Playwright UI tests with screenshot/video verification.
    -   Clean up scratchpad files.
6.  **Submit changes**: Commit and submit the code on the same branch.
