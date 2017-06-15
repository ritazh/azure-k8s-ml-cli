import click
from azk8sml.constants import DOCKER_IMAGES
from azk8sml.log import logger as azk8sml_logger
import os
from ruamel.yaml import YAML
import numpy

current_dir = os.path.dirname(__file__)
output_dir = "_output"
yaml = YAML()

@click.command()
@click.option('--gpu/--cpu', default=False, help='Run on a gpu instance')
@click.option('--mountpath', default='/data', help='Mount path of the input data')
@click.option('--storageaccountname', help='Name of the Azure storage account containing mounted data')
@click.option('--storageaccountkey', help='Key of the Azure storage account containing mounted data')
@click.option('--library',
              help='Machine learning library type to use [tensorflow (only this is available today), cntk, keras, etc])',
              default='tensorflow')
@click.option('--mode',
              help='Different modes',
              default='job',
              type=click.Choice(['job', 'jupyter', 'serve']))
@click.argument('command', nargs=-1)
@click.pass_context
def execute(ctx, gpu, mountpath, storageaccountname, storageaccountkey, library, mode, command):
    """
    Execute a command on azk8sml. azk8sml will use the data in the
    specified Azure storage account and run your command remotely.
    This command will generate a run id for reference.
    """
    
    azk8sml_logger.info("Running mode: {}".format(mode))
    docker_image = get_docker_image(library, gpu)

    # Secret yaml
    print("""
Generating secret yaml files...
    """)
    secret_yaml = "azurefile-secret.yaml"
    secretyaml_filepath = os.path.join(current_dir + '/../templates', secret_yaml)
    f = open(secretyaml_filepath, 'r')
    s = f.read()
    data = yaml.load(s)
    data['data']['azurestorageaccountname'] = storageaccountname
    data['data']['azurestorageaccountkey'] = storageaccountkey
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filepath = os.path.join(output_dir, secret_yaml)
    with open(output_filepath, 'w') as secretyaml_file:
        yaml.dump(data, secretyaml_file)
        print("""
Locate generated secret yaml file: {}
    """.format(output_filepath))

    # Deployment/Job/Service yaml
    if mode == 'job':
        print("""
Create yaml file training using image: `{}`
            """.format(docker_image))
        train_yaml = "train_gpu.yaml" if gpu else "train.yaml"
        trainyaml_filepath = os.path.join(current_dir + '/../templates/' + library, train_yaml)
        f = open(trainyaml_filepath, 'r')
        s = f.read()
        data = yaml.load(s)
        data['spec']['template']['spec']['containers'][0]['image'] = docker_image
        data['spec']['template']['spec']['containers'][0]['volumeMounts'][0]['mountPath'] = mountpath
        data['spec']['template']['spec']['containers'][0]['command'] = str(command[0]).split()
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_filepath = os.path.join(output_dir, train_yaml)
        with open(output_filepath, 'w') as trainyaml_file:
            yaml.default_flow_style='"'
            yaml.dump(data, trainyaml_file)
            print("""
    Locate generated training yaml file: {}
        """.format(output_filepath))
        return
    if mode in ['jupyter', 'serve']:
        

        # Print the path to jupyter notebook
        if mode == 'jupyter':
            print("""
Create yaml file for deployment for jupyter using image: `{}`
            """.format(docker_image))
            return
            

        # Print the path to serving endpoint
        if mode == 'serve':
            print("""
Create yaml file for deployment for inference using image: `{}`
            """.format(docker_image))
            return
            
def get_docker_image(library, gpu):
    gpu_cpu = "gpu" if gpu else "cpu"
    return DOCKER_IMAGES.get(gpu_cpu).get(library)
