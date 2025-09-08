# Erdős Institute Data Science Boot Camp

This repository contains the materials for the [Erdős Institute ](https://www.erdosinstitute.org/)Data Science Boot Camp.

## conda environment

You should set up a conda environment and run all of the notebooks with this environment. Below are minimal instructions.  You can find more detailed instructions here: [https://docs.google.com/document/d/1UsmDLnQwGjTB7eLKoccQZvLq2uWJexFcNov_CzkN2Ng/edit?tab=t.0](https://docs.google.com/document/d/1UsmDLnQwGjTB7eLKoccQZvLq2uWJexFcNov_CzkN2Ng/edit?tab=t.0)

Check to make sure you have conda by running the following in your command line interface:

    conda --version

If you don't have conda, google how to install it!

Once you have conda run:

    conda update conda

Press [y] to all of the prompts.  When you are done check the version again.  It should be version 23 or above.

Then run 

    conda env create --file=environment.yml

Press [y] to all of the prompts.  You will be downloading a lot of packages.

Once this is done:

    conda activate erdos_ds_environment

To check everything is there:

    conda list

Should show all of the packages!

If you ever need to add more packages to this environment please refer to the [conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#installing-packages).

Finally open `lectures/00_orientation/computer_setup_day/find_secret_code` and run the only cell there.  It will give you a numerical output.  Put that output in the textbox at [https://www.erdosinstitute.org/ds-boot-camp-prep](https://www.erdosinstitute.org/ds-boot-camp-prep).  If you set up the conda env correctly it will tell you that you have it set up correctly!  Please do this because us figure out who still needs assistance setting up python/jupyter/conda.

If you are using Visual Studio Code just select erdos_ds_environment as the kernel when running the notebooks.

## data

The data folder contains various data files used throughout the repository's notebooks.

### lectures

These folders contain the lecture jupyter notebooks for the boot camp. 

### problem_sessions

These folders contain the jupyter notebooks used in our problem solving sessions.  Note that problem solving sessions are **synchronous**. You can also find "prep" notebooks in this folder. Prep notebooks are for those participants wishing to have additional practice prior to the correspong problem solving session. They will remind you of some python fundamentals which will be needed to complete the problem session.  Prep notebooks are optional.

### math_hours

These folders contain supplemental expositions of the mathematics underlying some of the content from the lecture.  They are also optional.  We will discuss these notebooks during "math hour".


-------------------------
Copyright Info

All content was authored by Matthew Tyler Osborne and Steven Gubkin.

Any potential redistributors must seek and receive permission from Matthew Tyler Osborne and Steven Gubkin prior to redistribution. Redistribution of the material contained in this repository is conditional on acknowledgement of Matthew Tyler Osborne original authorship and sponsorship of the Erdős Institute. (see License.md)
