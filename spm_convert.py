from __future__ import print_function
import os
import yaml
import sys
import click

if sys.platform == "win32":
    sys.path.append(r"C:\Program Files (x86)\Gwyddion\bin")
import gwy

config_file = os.path.join(os.path.dirname(__file__), "config.yml")
with open(config_file) as f:
    config = yaml.safe_load(f)

ALLOWED_FTYPES_IN = tuple(config["allowed filetypes in"])
ALLOWED_FTYPES_OUT = (
    "gwy",
    "txt",
    "afm",
    "eps",
    "gsf",
    "ibw",
    "spm",
    "jpegjpg",
    "nrrd",
    "off",
    "exr",
    "ply",
    "pdf",
    "png",
    "ppm",
    "pnm",
    "svg",
    "asc",
    "stl",
    "sur",
    "sdf",
    "tga",
    "targa",
    "tiff",
    "tif",
    "vtk",
    "obj",
    "webp",
    "bmp",
    "tom",
    "top",
    "stp",
    "xyz",
)


def save_file(out_ext, container, filename, save_mode, out_dir=None):
    image_ids = gwy.gwy_app_data_browser_get_data_ids(container)
    name, _ = os.path.splitext(filename)

    if out_dir is not None:
        name = os.path.join(out_dir, name)

    for i in image_ids:
        gwy.gwy_app_data_browser_select_data_field(container, i)
        channel_title = (
            gwy.gwy_app_get_data_field_title(container, i)
            .strip()
            .replace(" ", "_")
        )
        out_name = "{}_{}.{}".format(
            name,
            channel_title,
            out_ext,
        )
        click.echo("{} created".format(out_name))
        gwy.gwy_file_save(container, out_name, save_mode)


def save_files(out_ext, filenames, folder, save_mode, out_dir):
    for filename in filenames:
        if filename.endswith(ALLOWED_FTYPES_IN):
            if not os.path.exists(out_dir):
                os.mkdir(out_dir)

            container = gwy.gwy_file_load(
                os.path.join(folder, filename), gwy.RUN_IMMEDIATE
            )
            gwy.gwy_app_data_browser_add(container)

            save_file(out_ext, container, filename, save_mode, out_dir)


def convert_file(filename, out_ext, save_mode):
    """Converts a file"""
    if filename.endswith(ALLOWED_FTYPES_IN):
        container = gwy.gwy_file_load(filename, gwy.RUN_IMMEDIATE)
        gwy.gwy_app_data_browser_add(container)

        save_file(out_ext, container, filename, save_mode)


def convert_folder(folder, out_ext, save_mode):
    """Converts all files in folder"""
    out_dir = os.path.join(folder, "{}_files".format(out_ext))
    filenames = os.listdir(folder)

    save_files(out_ext, filenames, folder, save_mode, out_dir)


def convert_folder_recursively(folder, out_ext, save_mode):
    """Searches recursively in folder and converts files"""
    for dirpath, _, filenames in os.walk(folder):
        out_dir = os.path.join(dirpath, "{}_files".format(out_ext))

        save_files(out_ext, filenames, dirpath, save_mode, out_dir)


@click.command()
@click.argument("fname")
@click.argument("out-ext")
@click.option(
    "--interactive",
    "-i",
    is_flag=True,
    default=False,
    help="Open interactive save dialogue for each file.",
)
@click.option(
    "--folder",
    "-f",
    is_flag=True,
    default=False,
    help="Convert all files in a folder.",
)
@click.option(
    "--recursive",
    "-r",
    is_flag=True,
    default=False,
    help=(
        "Convert all files in a folder and its subfolders. Dependent on"
        " --folder."
    ),
)
def cli(fname, out_ext, interactive, folder, recursive):
    """This script converts SPM data files.
    If a file contains multiple channels, all get converted.

    FNAME is the file or folder with files to convert\n
    OUT-EXT is the file extension of the format to convert to

    """
    save_mode = gwy.RUN_INTERACTIVE if interactive else gwy.RUN_NONINTERACTIVE

    if out_ext not in ALLOWED_FTYPES_OUT:
        click.echo("Export file type {} is not supported".format(out_ext))
        sys.exit()
    else:
        if folder and recursive:
            if os.path.isdir(fname):
                convert_folder_recursively(fname, out_ext, save_mode)
            else:
                click.echo(
                    "First argument is not a directory. For a file, unset"
                    " --folder and --recursive."
                )

        elif recursive and not folder:
            click.echo("--recursive is dependent on --folder.")

        elif folder and not recursive:
            if os.path.isdir(fname):
                convert_folder(fname, out_ext, save_mode)
            else:
                click.echo(
                    "First argument is not a directory. For a file, unset"
                    " --folder."
                )

        else:
            if os.path.isfile(fname):
                convert_file(fname, out_ext, save_mode)
            else:
                click.echo(
                    "First argument is not a file. For a folder, set the"
                    " --folder."
                )
