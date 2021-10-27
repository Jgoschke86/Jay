
import re

fs = "apple banana artichoke cherry date enchilada appetizer"

print(re.findall(r'\ba.{3}',fs,re.IGNORECASE))
