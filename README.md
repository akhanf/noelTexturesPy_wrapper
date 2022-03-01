# noelTexturesPy_wrapper

Simple Singularity-based wrapper for https://github.com/NOEL-MNI/noelTexturesPy

Uses antsPy U-net brainmasking, ANTS N4, ANTS, atropos tissue segmentation

Example usage: 
```
./noelTexturesPy.sh 013 sub-013_bids/sub-P013_ses-pre_acq-FSPGR_run-02_T1w.nii.gz  sub-013_bids/sub-P013_ses-pre_acq-Cor_run-01_FLAIR.nii.gz output_texture_maps
```
