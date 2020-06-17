from matplotlib import pyplot as plt, patches
import numpy as np

def draw(testInputs, computedTestOutputs, realTestOutputs):
    fig = plt.figure(dpi=150,figsize=(7,5))
    ax = fig.add_subplot(111,projection='3d')
    testInputsGDP = []
    testInputsFreedom = []
    for inp in testInputs:
        testInputsGDP.append(inp[0])
        testInputsFreedom.append(inp[1])

    points=[[testInputsGDP[0], testInputsFreedom[0], computedTestOutputs[0]],
            [testInputsGDP[1], testInputsFreedom[1], computedTestOutputs[1]],
            [testInputsGDP[2], testInputsFreedom[2], computedTestOutputs[2]]]
    p0, p1, p2 = points
    x0, y0, z0 = p0
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    ux, uy, uz = [x1 - x0, y1 - y0, z1 - z0]
    vx, vy, vz = [x2 - x0, y2 - y0, z2 - z0]
    u_cross_v = [uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx]
    point = np.array(p0)
    normal = np.array(u_cross_v)
    d = -point.dot(normal)
    xx, yy = np.meshgrid(range(2), range(2))
    z = (-normal[0] * xx - normal[1] * yy-d) * 1. / normal[2]
    ax.plot_surface(xx, yy, z, alpha=0.7, color="red", edgecolor='red')

    # plot the test output data
    ax.scatter(testInputsGDP, testInputsFreedom,realTestOutputs,marker='o', s=50, c="blue")
    ax.set_xlabel('GDP')
    ax.set_ylabel('freedom')
    ax.set_zlabel('happiness')
    plt.title('Computed test outputs and real test outputs')
    plt.show()