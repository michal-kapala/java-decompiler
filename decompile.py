import os

def decompile(file: str) -> int:
  """Runs Procyon decompiler - https://github.com/mstrobel/procyon/wiki/Java-Decompiler"""
  return os.system(f'java -jar decompiler.jar -jar {file} -o {file.replace(".jar", "")}')

files = os.listdir()

for file in files:
  if file.find('.jar') != -1 and file != 'decompiler.jar':
    try:
      decompile(file)
    except Exception as e:
      print(e)
      continue
