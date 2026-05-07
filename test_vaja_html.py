with open("vaja_04.html", "r") as f:
    text = f.read()

# Make sure all the old interactive features from index or related files are properly done.
# But looking closely, vaja 4 and 5 NEVER EXISTED BEFORE IN THE REPO as html.
# There were only `1_magnetni_krogi.html`, `2_transformatorji.html`, etc.
# And `vaja_00` to `vaja_03` were created by the agent PREVIOUSLY.
# Ah! Wait!
# Let's check `git log -p -1` to see what files were there.
