import click
from azk8sml.constants import DOCKER_IMAGES
from azk8sml.log import logger as azk8sml_logger
import os
from ruamel.yaml import YAML

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

    if mode == 'job':
        print("""
Create yaml file for deployment for training using image: `{}`
            """.format(docker_image))
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
