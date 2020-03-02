import os
import time

start_time = time.time()
print('Running LuaLaTeX')
os.system('lualatex -interaction nonstopmode main.tex')
print('Running LuaLaTeX a second time')
os.system('lualatex -interaction nonstopmode main.tex')
t = time.time() - start_time
print('Building finished in ' + str(round(t, 2)) + 's')