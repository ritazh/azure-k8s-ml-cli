# azure-k8s-ml-cli
🚧 Command line tool for running ML loads in K8s on Azure

> :triangular_flag_on_post: NOTE: Currently this tool assumes you have already provisioned a K8s cluster using acs-engine on Azure

## Usage

Eventually this tool should do the following:

```
# Install
$ pip install -U azure-k8s-ml-cli

# Go into your own project directory
$ cd < ML project directory >

# Initialize azure-k8s-ml-cli for your project
$ azk8sml init < ML project directory >

# Run your project on a K8s cluster on Azure
$ azk8sml execute --gpu \
--library tensorflow \
--storageaccountname <STORAGEACCOUNTNAME> \
--storageaccountkey <STORAGEACCOUNTKEY> \
--mountpath <MOUNTPATHFORDATAFILES>	\
"python app.py"

```

## Development

To add new features or fix bugs, you can clone this repo, make modifications, then build it and test it locally before creating a PR.

```
# Get this code
$ git clone 

# Build it
$ sudo pip install --editable .

# Run it
$ azk8sml version

```

