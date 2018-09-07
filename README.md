Automation of google ocr using python
1. Create an env for python 2, this package requires python2
```bash
conda create -n py2 python=2
source activate py2

=====================================
1. install gdcmdtools from https://github.com/tienfuc/gdcmdtools and complete the setup
2. use "convert" tool by imagemagics to convert a pdf into individual images.

#--------------------------------------------------
# after install gdcmdtools
in `google_ocr.py` config
```
    python2_path = "/Users/bi/miniconda3/envs/py2/bin/python "
    gdcmd_path = "/Users/bi/gitprojects/google-ocr-python/gdcmdtools"
```

