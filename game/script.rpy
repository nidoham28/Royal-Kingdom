# ═══════════════════════════════════════════════════════════════
#  START.RPY — Project entry point
# ═══════════════════════════════════════════════════════════════
#  PURPOSE
#    • The single place where a playthrough begins.
#    • Ren'Py looks for "label start" and runs it first.
#    • Keep this file SHORT — just the initial jump.
#
#  RULES
#    • Only ONE "label start" may exist in the whole project.
#    • Never put narrative text here — send it to chapter1.rpy.
#    • If you add a prologue later, jump to it here.
# ═══════════════════════════════════════════════════════════════

label start:
    jump ch1_s1_rooftop        # → first label in chapter1.rpy




# ═══════════════════════════════════════════════════════════════
#  CHAPTER N — <chapter title>
# ═══════════════════════════════════════════════════════════════
#  LABEL NAMING:   chN_s{scene}_{location}
#  ENTRY:          jump chN_s1_<location>   (from previous chapter)
#  EXIT:           jump ch{N+1}_s1_<location>
#
#  SCENE CHECKLIST
#    [ ] scene  <bg>    with <transition>
#    [ ] play   <music> (optional)
#    [ ] show   <chars> (optional)
#    [ ]        dialogue
#    [ ] hide   <chars> before scene change
#    [ ] jump   <next label>
#
#  DO NOT
#    ✗ put "label start" here (only in start.rpy)
#    ✗ redefine characters (only in definitions.rpy)
#    ✗ reuse a label name from another file
#    ✗ put a "label" keyword inside a "#" comment
# ═══════════════════════════════════════════════════════════════