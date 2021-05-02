story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"


#            A   B   C   D   F
# Story     +6  +5  +4  +2  +0
# Text      +5  +4  +3  +1  +0
# Role      +4  +3  +2  +1  +0
# Director  +3  +2  +1  +0  +0
# Cast/Misc +2  +1  +0  +0  +0

# 20: Perfect score
# 17 to 19: Must do
# 14 to 16: Seriously consider
# 12 to 13: On the bubble
# 11 or below: Pass

score = 0

story_scale = {"A":6, "B":5, "C":4, "D":2, "F":0}
text_scale = {"A":5, "B":4, "C":3, "D":1, "F":0}
role_scale = {"A":4, "B":3, "C":2, "D":1, "F":0}
dir_scale = {"A":3, "B":2, "C":1, "D":0, "F":0}
cast_scale = {"A":2, "B":1, "C":0, "D":0, "F":0}


if story in story_scale:
    score += story_scale[story]
if text in text_scale:
    score += text_scale[text]
if role in role_scale:
    score += role_scale[role]
if director in dir_scale:
    score += dir_scale[director]
if cast in cast_scale:
    score += cast_scale[cast]
print(score)

if score == 20:
    print("Perfect")
if score >= 17 and score <= 19:
    print("Must do")
if score >= 14 and score <= 16:
    print("Seriously consider")
if score >= 12 and score <= 13:
    print("On the bubble")
if score <= 11:
    print("Pass")