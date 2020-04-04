import tensorflow as tf
import tensorflow_quantum as tfq

import pandas as pd
import cirq
# import sympy
# import numpy as np

import matplotlib.pyplot as plt
# from cirq.contrib.svg import  SVGCircuit

length = 2

qubits = [cirq.GridQubit(i, j) for i in range(length) for j in range(length)]
print(qubits, '\n\n')


circuit = cirq.Circuit(
    cirq.Z(qubits[0]),
    cirq.Y(qubits[1]),
    cirq.X(qubits[2]),
    cirq.X(qubits[3]),

    cirq.CNOT(target=qubits[1], control=qubits[0]),
    cirq.CNOT(target=qubits[3], control=qubits[2]),

    cirq.measure(qubits[0], key='q0 M'),
    cirq.measure(qubits[1], key='q1 M'),
    cirq.measure(qubits[2], key='q2 M'),

    cirq.SWAP(qubits[3], qubits[1]),
    cirq.CNOT(target=qubits[3], control=qubits[1]),

    cirq.measure(qubits[3], key='q3 M')
)

# circuit.append(cirq.measure(qubits[j]) for j in range(length+2))

print('Circuit: ')
print(circuit, '\n')

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
matrixResult = result.data

print('Results:')
print(result.data, '\n')

pd.DataFrame(matrixResult)
# print(matrixResult['(0, 0)'])
print(matrixResult.describe())


plt.hist(matrixResult)
# plt.show()