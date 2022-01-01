set zone=arttest

set color=green
blender --background %zone%_base.blend --python generate.py -- %color%
copy %zone%_%color%.blend %zone%.blend
blender --background %zone%.blend --python C:\src\eqgzoneImporter\bin\convert.py
eqgzi import %zone%
mkdir out\%color%\
copy out\* out\%color%\

set color=blue
blender --background %zone%_base.blend --python generate.py -- %color%
copy %zone%_%color%.blend %zone%.blend
blender --background %zone%.blend --python C:\src\eqgzoneImporter\bin\convert.py
eqgzi import %zone%
mkdir out\%color%\
copy out\* out\%color%\

set color=pink
blender --background %zone%_base.blend --python generate.py -- %color%
copy %zone%_%color%.blend %zone%.blend
blender --background %zone%.blend --python C:\src\eqgzoneImporter\bin\convert.py
eqgzi import %zone%
mkdir out\%color%\
copy out\* out\%color%\

set color=black
blender --background %zone%_base.blend --python generate.py -- %color%
copy %zone%_%color%.blend %zone%.blend
blender --background %zone%.blend --python C:\src\eqgzoneImporter\bin\convert.py
eqgzi import %zone%
mkdir out\%color%\
copy out\* out\%color%\