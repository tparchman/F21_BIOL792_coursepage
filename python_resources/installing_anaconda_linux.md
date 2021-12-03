# Quick guige to installing and getting started with Anaconda environments 

## Installing

### 1. Download linux installer (Anaconda3-2021.11-Linux-x86_64.sh)
I suggest doing this in your home directory

	$ wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh

### 2. Run the anaconda installer

	$ bash Anaconda3-2021.11-Linux-x86_64.sh

To save some time choose yes to go ahead and initiate when prompted with: "Do you wish the installer to initialize Anaconda3
by running conda init? [yes|no]"

Without further action, the conda base environment will automatically be up when you login. To change that, follow instructions that come at the end of the install output:

==> For changes to take effect, close and re-open your current shell. <==

If you'd prefer that conda's base environment not be activated on startup, 
   set the auto_activate_base parameter to false: 

	$ conda config --set auto_activate_base false

### Activate Anaconda

After installation, Anaconda needs to be activated. The .bashrc file should have what it needs after install, so now you just need to run: 

	$ source ~/.bashrc

After doing this, o verify that the install is complete and things look right:

	$ conda list
OR
	$ conda info
 
## Installing Anaconda environments and add some channels

This is done with the `conda` command. Below I am creating an environment named **py39** with **python 3.9**.

	$ conda create -n py39 python=3.9

Once you have created an environment, deactivate with:

	$ conda deactivate

or alternatively activate with:

	$ conda activate py39

## Channels
Conda channels are the locations where packages are stored, and serve as the base for managing packages. The conda command searches a set of channels. By default, packages are automatically downloaded and updated from the default channel https://repo.anaconda.com/pkgs/, but may require fee. The conda-forge channel is free for all to use, as are many others. Once you configure channels, you will need to specify them along with your conda install commands.


### Adding/configuring channels

Below, I am configuring free channels that I anticipate using regularly.

	$ conda config --add channels bioconda
	$ conda config --add channels conda-forge
	$ conda config --add channels defaults
	$ conda config --add channels r

 NOTE: need to nano .condarc
	## move conda-forge and bioconda to top of list



## Installing pyrpipe as an example

Intalling pyrpipe using bioconda channel

	$ conda install -c bioconda pyrpipe
 
Installing required packages

	$ conda install -c bioconda star
	$ conda install -c bioconda sra-tools
	$ conda install -c bioconda stringtie
	$ conda install -c bioconda trim-galore
	$ conda install -c bioconda orfipy
	$ conda install -c bioconda salmon

	