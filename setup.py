from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='mp_rocker',
    version='0.0.0',

    description='Personal rocker plugins',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Miguel Prada',
    author_email='miguel.prada@tecnalia.com',

    packages=['mp_rocker'],
    package_data={'mp_rocker': ['templates/*.em']},

    install_requires=[
        'rocker',
    ],

    entry_points={
        'rocker.extensions': [
            'mp_vim_dev = mp_rocker.vim_dev:VimDev',
            'mp_zsh = mp_rocker.zsh:Zsh',
        ]
    },
)

