import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 200
from PIL.PngImagePlugin import PngImageFile

import os

image_path = os.path.abspath( os.path.dirname( __file__ ) )

from qiskit_ibm_runtime.fake_provider import FakeProviderForBackendV2

# Get a list of all backend names and print them
def list_and_get_backend_names(provider):

    backends = provider.backends()
    print("Available fake backends:")
    for be in backends:
        cfg = be.configuration()
        print(f" • {be.name}: {cfg.num_qubits} qubits")

    return backends

if __name__ == "__main__":

    # Set up a fake provider to get all available backends
    provider = FakeProviderForBackendV2()
    backends = list_and_get_backend_names(provider)

    # For each available backend, draw the coupling map and export as image
    for backend in backends:
        be = provider.backend(backend.name)
        connection_map: PngImageFile = be.coupling_map.draw()
        size = connection_map.size
        px = 1/plt.rcParams['figure.dpi']
        plt.subplots(figsize=[size[0]*px, size[1]*px])
        plt.imshow(connection_map)
        plt.axis('off')
        plt.title(backend.name)
        plt.savefig(f'{image_path}/({backend.num_qubits})_{backend.name[5:]}.png', bbox_inches='tight', dpi='figure', format='png')
        plt.close()