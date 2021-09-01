import numpy as np

class Evaluator:
    def __init__(self):
        self.cnt = 0
        self.x = np.arange(start=-50, stop=50, step=1)
        """
        You can initialize your model here
        """
        self.result = []

    def evaluate_one_data(self, input_source: dict, input_target: dict) -> dict:
        self.cnt = self.cnt + 0.5
        ratio = np.tan(self.cnt)
        y = self.x * ratio

        dict_ret = {
                'overall': {
                    'float_file_metric': self.cnt,
                    'curve_file_metric': {
                        'x': self.x.tolist(),
                        'y': y.tolist()
                    }
                }
        }
        self.result = self.result + [self.cnt]
        return dict_ret

    def get_result(self) -> dict:
        r = np.array(self.result)
        r_float = float(r.mean())
        self.cnt = self.cnt + 0.5
        ratio = np.tan(self.cnt)
        y = self.x * ratio
        dict_ret = {
            'overall': {
                    'float_file_metric': self.cnt,
                    'curve_file_metric': {
                        'x': self.x.tolist(),
                        'y': y.tolist()
                    }
                }
        }
        return dict_ret

