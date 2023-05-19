import os, shutil
curdir = os.path.dirname(os.path.realpath(__file__))
os.makedirs('/content/cagliostro-colab-ui/static', exist_ok=True)
timerscriptdir = '/content/cagliostro-colab-ui/extensions-builtin/nocrypt-colab-timer/javascript'
os.makedirs(timerscriptdir, exist_ok=True)
timerscriptpath = os.path.join(timerscriptdir, 'colab-timer.js')
if not os.path.exists(timerscriptpath):
    shutil.copy2(os.path.join(curdir, 'colab-timer.js'), timerscriptpath)
