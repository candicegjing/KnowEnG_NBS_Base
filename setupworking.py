from setuptools import setup
import vcversioner


setup(name='knpackage',
    # setup_requires=['vcversioner'],
    # vcversioner={
    #       'vcs_args': ['git', '--git-dir', '%(root)s/.git',
    #            ],
    # },
      version=vcversioner.find_version().version,
      description='Knoweng for test',
      url='https://github.com/candicegjing/KnowEnG_NBS_Base',
      author='Jing Ge',
      author_email='candicegjing@gmail.com',
      license='MIT',
      packages=['knpackage'],
      zip_safe=False)