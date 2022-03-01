# noelTexturesPy_wrapper

Simple Singularity-based wrapper for https://github.com/NOEL-MNI/noelTexturesPy

Uses antsPy U-net brainmasking, ANTS N4, ANTS, atropos tissue segmentation

Example usage: 
```
git clone https://github.com/akhanf/noelTexturesPy_wrapper
./noelTexturesPy_wrapper/noelTexturesPy.sh 013 sub-013_bids/sub-P013_ses-pre_acq-FSPGR_run-02_T1w.nii.gz  sub-013_bids/sub-P013_ses-pre_acq-Cor_run-01_FLAIR.nii.gz output_texture_maps
```


## Khanlab deployment:
If using graham (and neuroglia-helpers with khanlab cfg), checkout the `graham` branch first:
```
git clone https://github.com/akhanf/noelTexturesPy_wrapper
cd noelTexturesPy_wrapper
git checkout graham
```

There is also a `CBS` branch for the CBS server (though the `master` branch should work already, it avoids downloading the container again)
