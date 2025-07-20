
import os
from shutil import which
from IPython.display import Markdown, HTML

folderpath = '/content/' if not os.path.exists('/content/pseudocode-forall') else "/content/"

nb_pseudocodePATH = folderpath+"pseudocode-forall/pseudocode"

class progress_bar():
  def __init__(self, steps=100, desc="Progress... ", update=lambda n:1, wait=1, timeout=10):
    from tqdm.notebook import tqdm
    import threading; from time import sleep;
    if timeout is None: timeout = float('inf')
    self.total_steps = total_steps
    self.prog_bar = tqdm(total=total_steps, desc=desc)
    def update_prog_bar(self=self,
      timeout = timeout,
      wait = wait):
      while self.prog_bar.n < self.total_steps or timeout <= 0:
        self.prog_bar.n = update(self.prog_bar.n)
        self.prog_bar.refresh()
        sleep(wait)
        timeout -= wait
    self.progress_thread = threading.Thread(target=update_prog_bar)
  def start(self):
    self.progress_thread.start()
  def set_progress(self, n):
    self.prog_bar.n = n
    self.prog_bar.refresh()
  def stop(self):
    self.progress_thread.join()
    self.prog_bar.close()
#print
total_steps = 1895
open("install.log", 'w').close()
pbar = progress_bar(
    steps=total_steps,
    desc="Installing pseudocode... ",
    update=lambda n: (len((file := open('install.log', 'r')).read().split('\n')), file.close())[0],
    timeout=None,
)
pbar.start()

if not which("fpc"):
  with open("setup.sh",'w') as sh:
    sh.write("""#!/bin/bash
# Echo the current directory
echo "Current directory: $(pwd)"
echo "Directory contents:"
ls -la

# Step 1: Download the Free Pascal Compiler
echo "Downloading Free Pascal Compiler..."
wget https://downloads.freepascal.org/fpc/dist/3.2.2/x86_64-linux/fpc-3.2.2.x86_64-linux.tar -O fpc.tar

# Step 2: Extract the tarball
echo "Extracting Free Pascal Compiler..."
tar -xvf fpc.tar

# Step 3: Navigate to extracted folder and install locally
cd fpc-3.2.2.x86_64-linux
echo "Installing Free Pascal Compiler locally..."
./install.sh --prefix=$HOME/fpc

# Step 4: Add FPC to PATH for current session
echo "Updating PATH..."
export PATH=$HOME/fpc/bin:$PATH
echo "FPC installed successfully. Add 'export PATH=$HOME/fpc/bin:\$PATH' to your shell profile to make it permanent."
""")
  get_ipython().system("sudo chmod +x ./setup.sh")
  get_ipython().system('''
bash setup.sh << EOF > install.log 2>&1
/usr/
n
n
EOF
rm -rf /content/fpc-3.2.2.x86_64-linux /content/fpc.tar /content/setup.sh
''')
  if which("fpc"): display(Markdown("Free Pascal successfully installed."))
else: display(Markdown("Free Pascal is already installed."))

if which(f'{nb_pseudocodePATH}'):
  get_ipython().system(f"sudo chmod +x {nb_pseudocodePATH}")
  display(Markdown(f'<span style="color:green">pseudocode successfully installed.</span>'))
  with open("install.log", 'a') as log: log.write("pseudocode successfully installed.\n")
else:
  display(HTML(f'<span style="color:red">WARNING: {nb_pseudocodePATH} not found.</span>'))

from IPython.core.magic import register_cell_magic
@register_cell_magic
def pseudocode(line, cell):
  import re
  fname = re.search(r"""\"[^\"]+\"|\'[^\']+\'|\S+""" ,line).group(0).strip("\"'") if line.strip() else "mypseudocode"
  fname = fname.strip("\"'").removesuffix('.pseudo')
  os.system(f"rm '{fname}.pas' '{fname}.o' '{fname}'")
  with open(fname+'.pseudo', 'w') as file: file.write(cell)


  direct = re.search(r'^//.*-- direct\b', cell) != None
  echoinputs = re.search(r'^//.*--echo-inputs\b', cell) != None
  command = f"{nb_pseudocodePATH if not direct else 'python pseudocode.py'} '{fname}.pseudo' "+(" --echo-inputs" if echoinputs else "")
  #print(command)
  get_ipython().system(command)
  pascode = ''
  with open(fname+'.pas', 'r') as file:
    filelns=file.read()
    totallines = len(filelns.split('\n'))
    lns = filelns.split("// end of preamble")[-1].lstrip().split('\n')
    for i, ln in enumerate(reversed(lns)):
      pascode = f'{(totallines-i): >{len(str(totallines))}} {ln if "TFPHashFilesList" not in ln else "//"}\n' + pascode
    pascode = '[previous lines truncated]...\n' + pascode.rstrip()

  debug = re.search(r'^//.*--debug\b', cell) != None
  norun = re.search(r'^//.*--no-run\b', cell) != None
  if debug:
    print("Generated Pascal Code:")
    full = re.search(r'^//.*--debug-full\b', cell) != None
    if not full: print(pascode)
    else:
      with open(fname+'.pas', 'r') as file:
        lines = file.readlines()
        linno_width = len(str(len(lines)))
        for i, line in enumerate(lines):
          #print('here', linno_width)
          print(f"{i+1: >{linno_width}} {line.strip()}")
  get_ipython().system(f"fpc '{fname}.pas' > stdout.log 2>&1")
  with open('stdout.log', 'r') as file:
    stdout = file.read().split('\n')
    if any('error' in i.lower() for i in stdout): #or 'warning' in i.lower()
      print(f"Generated Pascal Code:\n{pascode}\n" if not debug else "", f"Error Message:",*stdout, sep="\n"); return
  get_ipython().system("rm *.log *.o")
  if debug: print(f'\nRunning the program named "{fname}"...\n')
  if not norun: get_ipython().system(f"./'{fname}'")
with open("install.log", 'a') as log: log.write("Registered cell magic %%pseudocode.\n")
get_ipython().run_line_magic('alias', "pascal fpc '%l.pas' && './%l'")
from IPython.core.magic import register_cell_magic
@register_cell_magic
def pascal(line, cell):
  line = line if line.strip() else "__pascalprogram__.pas"
  with open(line, 'w') as file: file.write(cell)
  get_ipython().run_line_magic('pascal', line.removesuffix('.pas'))
with open("install.log", 'a') as log: log.write("Registered cell magic %%pascal.\n")

pbar.set_progress(total_steps)
pbar.stop()

display(Markdown("""## Welcome to Pseudocode-forAll!
### Pseudocode-forAll runs pseudocode based on the CAIE Pseudocode Guide, applicable for exams on 2025-2029.
- For smoothest coding experience, turn off syntax check by selecting **Tools>Settings>Editor>[scroll down] Code Diagnostics>None**.
- To use a cell to run pseudocode, use the magic command syntax: `%%pseudocode` or `%%pseudocode <filename>.pseudo` at the top of the cell with your code in the rest of the cell as shown in the following examples."""))

dark_mode_code = """
<div style="background-color: #1e1e1e; color: #d4d4d4; padding: 10px; border-radius: 5px; font-family: monospace;">
<pre>
<span style="color: #569cd6;">%%pseudocode</span>
<span style="color: #dcdcaa;">OUTPUT</span> <span style="color: #ce9178;">"Hello, world!"</span>
</pre>
</div>
"""

display(HTML(dark_mode_code))

display(Markdown(f"{'&nbsp;'*20}<b>OR</b>"))

dark_mode_code = """
<div style="background-color: #1e1e1e; color: #d4d4d4; padding: 10px; border-radius: 5px; font-family: monospace;">
<pre>
<span style="color: #569cd6;">%%pseudocode</span> <span style="color: #DDDDDD;">hello_program.pseudo</span>
<span style="color: #dcdcaa;">OUTPUT</span> <span style="color: #ce9178;">"Hello, world!"</span>
</pre>
</div>
"""
display(HTML(dark_mode_code))
