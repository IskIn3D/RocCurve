import matplotlib.pyplot as plt

class RocCurve:
    def __init__(self, input_data, fit, h0_class=True):
        self.curve_points = [[0.0],[0.0]]
        data = input_data.copy()
        data.sort(key=fit, reverse=True)
        sum_p = len(list(filter(lambda x: x.target_class == h0_class, data)))
        sum_n = len(data) - sum_p
        tpr = 0.0
        fpr = 0.0
        for target in data:
            if target.target_class == h0_class:
                tpr += 1/sum_p
            else:
                fpr += 1/sum_n
            self.curve_points[0].append(fpr)
            self.curve_points[1].append(tpr)

    def __call__(self):
        plt.axis([0, 1, 0, 1])
        plt.xlabel("FPR")
        plt.ylabel("TPR")
        plt.plot(self.curve_points[0], self.curve_points[1])
        plt.show()
