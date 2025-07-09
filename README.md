# Exploring Quantum Information

In this repository I hold my quantum explorations. For now it is mostly python work using Qiskit and QuTiP.

## Qiskit
[Qiskit](https://quantum.cloud.ibm.com/docs/en/guides) is the Quantum SDK for python made by IBM. It contains features to build and execute quantum circuits in simulation and on real hardware.

- [01_QiskitIntroExpanded](./Python/Qiskit/01_QiskitIntroExpanded.ipynb)
    - Expanded version of the Qiskit introduction tutorial found [here](https://quantum.cloud.ibm.com/docs/en/tutorials/hello-world). I included some additional context using QuTip and details on how to run the circuit locally with a Sampler or Estimator and what that means.
- [02_SimulatingLargerUsingAer](./Python/Qiskit/02_SimulatingLargerUsingAer.ipynb)
    - Another swimulation tutorial. Instead of running on real hardware in the cloud, we can use the Aer simulator to run larger systems (up to 20-25 qubits on standard hardware). The standard simulator also can't handle backends larger than 65 qubits, which Aer knows how to handle. Aer also has some other nice features like noise simulation. Again following the basic beats of the Qiskit Hello World example.
- [03_ConnectToIBMQP](./Python/Qiskit/03_ConnectToIBMQP.ipynb)
    - `WIP` Will show how to connect to IBM Quantum Cloud and run simulations on real hardware. Will be finished as soon as IBM accepts my credit card. Also includes a quick tutorial on sharing circuits between QuTip and Qiskit using QASM.
- [04_StatePreparationWithQclib](./Python/Qiskit/04_StatePreparationWithQclib.ipynb)
    - `WIP` QClib is a state preparation library built on Qiskit. Here we look at how to prepare states for use in a circuit.

#### Scripts
- [Save Backend Coupling Maps](./Python/Qiskit/coupling-maps/save-backend-coupling-maps.py)
    - Save a `.png` version of the available backend coupling maps in the `/Python/Qiskit/coupling-maps` folder.

## Cirq


## Resources

### Python
- [Scientific Computing with Python](https://github.com/jrjohansson/scientific-python-lectures)
- [Medium - Mastering Figure size units in MPL](https://labexio.medium.com/mastering-figure-size-units-in-matplotlib-9ed687ebdb31)
- [pillow Docs](https://pillow.readthedocs.io/en/stable/index.html)

### Physics
- [GHZ state - Wikipedia](https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_state)

### QuTiP
- [QuTiP Tutorials (Github)](https://github.com/qutip/qutip-tutorials)
- [QuTiP Tutorials (Docs)](https://jakelishman.github.io/qutip.github.io/tutorials.html)

### Qiskit
- [Qiskit Docs - Quantum Circuit Model](https://docs.quantum.ibm.com/api/qiskit/circuit)
- [Qiskit Docs - Primitives](https://quantum.cloud.ibm.com/docs/en/guides/primitives)
- [Qiskit Docs - Transpilation](https://quantum.cloud.ibm.com/docs/en/guides/transpile)
- [Qiskit Aer Documentation](https://qiskit.github.io/qiskit-aer/index.html)
- [Detailed example of transpilation](https://quantumcomputing.stackexchange.com/a/15453)

### PyQuill
- [PyQuill - Docs](https://pyquil-docs.rigetti.com/en/stable/)

### Pennylane
- [Pennylane - Homepage](https://pennylane.ai/)

### qclib
- [qclib - Github](https://github.com/qclib/qclib)