# spm-convert

Script for converting Scanning Probe Microscopy (SPM) data formats.

## Installation

The following installations are required:

1. **32 bit** version of [Gwyddion](http://gwyddion.net/download.php)
2. Python 2.7
3. PyGObject
4. PyGTK
5. PyCairo

Windows installers for Python2 and the needed packages can be found
[here](https://sourceforge.net/projects/gwyddion/files/pygtk-win32/).

After installation, the Pygwy Console should be available in Gwyddion under 
_Data Process_.

If everything is set up, just run

```bash

$ python2 -m pip isntall -r requirements.txt
$ python2 -m pip install .

```

from the root directory of the project.


## Usage

After installation, the spm-convert command is available. For help, use
`spm-convert --help`.

```
Usage: spm_convert [OPTIONS] FNAME OUT_EXT

  This script converts SPM data files. If a file contains multiple
  channels, all get converted.

  FNAME is the file or folder with files to convert

  OUT-EXT is the file extension of the format to convert to

Options:
  -i, --interactive  Open interactive save dialogue for each file.
  -f, --folder       Convert all files in a folder.
  -r, --recursive    Convert all files in a folder and its subfolders.
                     Dependent on --folder.

  --help             Show this message and exit.
```


## Input File Formats

All [file formats that are supported by Gwyddion.](http://gwyddion.net/documentation/user-guide-en/file-formats.html)
can be used.
You can specify which file types are allowed for import in the `config.yml` file.


## Export File Formats

All formats, that Gwyddion can export to, can be used:

- Gwyddion native format (.gwy)
- ASCII data matrix (.txt)
- Assing AFM files (.afm)
- Encapsulated PostScript (.eps)
- Gwyddion Simple Field (.gsf)
- Igor binary waves (.ibw)
- ISO 28600:2011 SPM data transfer files (.spm)
- JPEG (.jpeg, .jpg)
- Nearly raw raster data (NRRD) files (.nrrd)
- Object File Format (.off)
- OpenEXR images (.exr)
- Polygon file format (.ply)
- Portable document format (.pdf)
- Portable Network Graphics (.png)
- Portable Pixmap (.ppm, .pnm)
- Scalable Vector Graphics (.svg)
- SPIP ASCII files (.asc)
- Stereolitography STL (.stl)
- Surf files (.sur)
- Surfstand SDF files, text (.sdf)
- TARGA (.tga, .targa)
- TIFF (.tiff, .tif)
- VTK structured grid (.vtk)
- Wavefront geometry definition (.obj)
- WebP (.webp)
- Windows or OS2 Bitmap (.bmp)
- WSxM files (.tom, .top, .stp)
- XYZ text data (.xyz)
