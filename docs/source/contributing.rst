Contribution Guidelines
=======================

Thank you for your interest in contributing to this project! Here are some guidelines to help ensure a smooth and successful contribution process. Please read them carefully before contributing. We are happy to answer any questions you may have, and to welcome you as a contributor.

1. **Fork** the project to your own GitHub account by clicking the "Fork" button in the top right corner of the repository page. This will allow you to make changes to the project without affecting the main project.

2. Create a **new branch** for your contribution. This will keep your changes separate from the main branch and make it easier to review and merge your changes. The name of your branch should be concise and descriptive. For example, if you are adding a new feature, you might call your branch "add-feature".

3. Write concise **commit messages** that describe the changes you made. Use the present tense and avoid redundant information. We try to follow the `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ specification.

4. Make sure your changes work as intended and do not introduce new bugs or problems. Write **tests** if applicable.

5. **Document** your changes by following the `numpydoc <https://numpydoc.readthedocs.io/en/latest/format.html>`_ format. This step is important to ensure that the package documentation is up-to-date and complete. If you are not sure about this step, we can help you.

6. When you are ready to submit your changes, create a **pull request** from your branch to the main branch of the original repository. Provide a clear description of your changes and why they are necessary, and we will review your contribution.

Thank you again for your interest in contributing to this project!

Making a Release
================

To make a release, please follow these steps:

1. Stage all your changes with:

   .. code-block:: bash

      git stage .

2. Commit the code to the master branch. Make sure to use a proper commit message. Use the following command:

   .. code-block:: bash

      git commit -s -m "set up pypi release"

3. Tag the code with the next version number x.x.x. Please note that version numbering needs to follow proper major, minor, micro increments. Use the following command:

   .. code-block:: bash

      git tag x.x.x

4. Push to origin with:

   .. code-block:: bash

      git push origin --tags

   This will trigger GitHub Actions which will:
   
   1. Automatically push to PyPI and PyPI test:
   
      `GitHub Actions PyPI release workflow <https://github.com/INGV/ScatCluster/actions/workflows/pypi_release.yml>`_
   
   2. Run pre-commit changes to check code quality:
   
      `GitHub Actions pre-commit workflow <https://github.com/INGV/ScatCluster/actions/workflows/pre-commit.yml>`_
   
   3. Build documentation:
   
      `GitHub Actions documentation build workflow <https://github.com/INGV/ScatCluster/actions/workflows/docs.yml>`_
