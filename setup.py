from os import environ
from time import asctime
from subprocess import Popen, PIPE
from setuptools import setup, find_packages
from os.path import exists, dirname, realpath, join

version_file = "frskyosd/version.py"


def readme():
    with open("README.md", encoding = "utf-8") as f:
        content = f.read()
    return content


def get_git_hash():

    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ["SYSTEMROOT", "PATH", "HOME"]:
            v = environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env["LANGUAGE"] = 'C'
        env["LANG"] = 'C'
        env["LC_ALL"] = 'C'
        out = Popen(cmd, stdout = PIPE, env = env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(["git", "rev-parse", "HEAD"])
        sha = out.strip().decode("ascii")
    except OSError:
        sha = "unknown"

    return sha


def get_hash():
    if exists(".git"):
        sha = get_git_hash()[:7]
    else:
        sha = "unknown"

    return sha


def write_version_py():
    content = """# GENERATED VERSION FILE
# TIME: {}
__version__ = '{}'
__gitsha__ = '{}'
version_info = ({})
"""
    sha = get_hash()
    with open("VERSION.txt", 'r') as f:
        SHORT_VERSION = f.read().strip()
    VERSION_INFO = ", ".join([x if x.isdigit() else f'"{x}"' for x in SHORT_VERSION.split('.')])

    version_file_str = content.format(asctime(), SHORT_VERSION, sha, VERSION_INFO)
    with open(version_file, 'w') as f:
        f.write(version_file_str)


def get_version():
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']

def get_requirements(filename = "requirements.txt"):
    here = dirname(realpath(__file__))
    with open(join(here, filename), 'r') as f:
        requires = [line.replace('\n', '') for line in f.readlines()]
    return requires

if __name__ == "__main__":
    write_version_py()
    setup(
        name = "frskyosd",
        version = get_version(),
        description = "Pixel-based OSD product launched by FrSky",
        author_email = "frsky@frsky-rc.com",
        url = "https://github.com/FrSkyRC/PixelOSD",
        include_package_data = True,
        long_description = readme(),
        long_description_content_type = "text/markdown",
        packages = find_packages(include = [
            "frskyosd*"
        ]),
        install_requires = get_requirements(),
        zip_safe = False
    )