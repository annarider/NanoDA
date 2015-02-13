from ggplot import *
import pandas as pd
df = pd.DataFrame({"x":[1,2,3,4], "y":[1,3,4,2]})
ggplot(aes(x="x", weight="y"), df) + geom_bar()