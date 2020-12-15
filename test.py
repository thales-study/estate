from modules.loadingbar import LoadingBar
import time
total = 20
bar = LoadingBar(20, 20)
bar.start()
for i in range(1, total+1):
  time.sleep(0.1)
  bar.process(i)
bar.end()