#!/usr/bin/env python3

import os
import sys
from pathlib import Path

#add noelpy from the singularity container to python path
sys.path.insert(1, '/noelpy')
from image_processing import noelTexturesPy, logger

if len(sys.argv) <= 3 or len(sys.argv) > 5:
    print(f'usage: {sys.argv[0]} ID T1 <T2 (optional)> OUTPUT_DIR')
    sys.exit(1)

id = sys.argv[1]
t1 = sys.argv[2]
if len(sys.argv) == 4:
    t2 = None
    output_dir = sys.argv[3]
elif len(sys.argv) == 5:
    t2 = sys.argv[3]
    output_dir = sys.argv[4]

template = '/noelpy/templates/mni_icbm152_t1_tal_nlin_sym_09a.nii.gz'
Path(output_dir).mkdir(parents=True, exist_ok=True)

noelTexturesPy(id=id, t1=t1, t2=t2, output_dir=output_dir, template=template, usen3=False).file_processor()

# Original call to noelTexturesPy
#noelTexturesPy(id=id, t1=t1, t2=t2, output_dir=output_dir, template=template, usen3=False).file_processor()

