from distutils.core import setup
setup(
  name = 'pyspikon',         # How you named your package folder (MyLib)
  packages = ['pyspikon'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='GNU GPLv3',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'PySpikeConverter converts any .llsp file into .py codes.',   # Give a short description about your library
  author = 'PyJonhAct',                   # Type in your name
  author_email = 'joaovmiziara@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['SPIKE PRIME', 'LEGO EDUCATION', 'ROBOTICS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'argparse'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3.0',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)